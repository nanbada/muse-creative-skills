#!/usr/bin/env python3
"""Token-cheap social sourcing: X single tweets via FxTwitter API, Reddit via Arctic Shift API.
Plain HTTPS + stdlib only. No browser, no API keys.

Usage:
  social_fetch.py x <x.com status URL>              # fetch one tweet as JSON
  social_fetch.py xtext <x.com status URL>           # print tweet text only
  social_fetch.py reddit <subreddit> <query> [limit] # search reddit posts
  social_fetch.py redditself <subreddit> <query> [limit]  # include post bodies
"""
import json, os, random, re, sys, time, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"}

# ---- Backoff state machine (pattern from radhikagk/instagram-ai-agent) ----
# Persistent per-host cooldown: on repeated failures we stop hammering the host
# and exit early until backoff_until. Cooldown escalates 1h, 2h, 3h, ...
BACKOFF_FILE = os.path.expanduser("~/.cache/social-sourcing/backoff.json")

def _load_backoff():
    try:
        with open(BACKOFF_FILE) as f:
            return json.load(f)
    except (FileNotFoundError, ValueError):
        return {}

def _save_backoff(state):
    os.makedirs(os.path.dirname(BACKOFF_FILE), exist_ok=True)
    with open(BACKOFF_FILE, "w") as f:
        json.dump(state, f)

def _host_key(url):
    return re.sub(r"^https?://", "", url).split("/")[0]

def check_backoff(url):
    """Exit early if this host is in cooldown. Returns state dict otherwise."""
    state = _load_backoff()
    entry = state.get(_host_key(url), {})
    until = entry.get("backoff_until", 0)
    if until > time.time():
        mins = int((until - time.time()) / 60)
        sys.exit(f"backoff active for {_host_key(url)}: {mins} min remaining "
                 f"(reason={entry.get('reason')}, fails={entry.get('fails', 0)}). "
                 f"Wait it out instead of retrying.")
    return state

def record_success(url, state):
    key = _host_key(url)
    if key in state:
        del state[key]
        _save_backoff(state)

def record_failure(url, state, reason):
    key = _host_key(url)
    entry = state.get(key, {})
    fails = entry.get("fails", 0) + 1
    hours = fails  # escalating: 1h, 2h, 3h, ...
    entry.update({"fails": fails, "reason": reason,
                  "backoff_until": time.time() + hours * 3600})
    state[key] = entry
    _save_backoff(state)
    print(f"backoff entered for {key}: {hours}h (consecutive fails={fails}, reason={reason})",
          file=sys.stderr)

def fetch_raw(url, timeout=25):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode("utf-8", "replace"))

def get(url, timeout=25):
    state = check_backoff(url)
    try:
        data = fetch_raw(url, timeout)
    except Exception as e:
        record_failure(url, state, f"{type(e).__name__}: {e}")
        raise
    record_success(url, state)
    return data

def fetch_tweet(url):
    m = re.search(r"(?:x\.com|twitter\.com)/([A-Za-z0-9_]+)/status/(\d+)", url)
    if not m:
        sys.exit("not an x.com status URL")
    handle, sid = m.group(1), m.group(2)
    data = get(f"https://api.fxtwitter.com/{handle}/status/{sid}")
    if data.get("code") != 200:
        sys.exit(f"fxtwitter error: {data.get('message')}")
    return data["tweet"]

def cmd_x(url, text_only=False):
    t = fetch_tweet(url)
    a = t.get("author", {})
    if text_only:
        print(f"@{a.get('screen_name')} ({t.get('created_at','')}):")
        print(t.get("text", ""))
        print(f"likes={t.get('likes')} RT={t.get('retweets')} replies={t.get('replies')} | {t.get('url')}")
    else:
        print(json.dumps(t, ensure_ascii=False, indent=1))

def cmd_reddit(subreddit, query, limit=10, bodies=False):
    from urllib.parse import quote
    url = (f"https://arctic-shift.photon-reddit.com/api/posts/search"
           f"?subreddit={quote(subreddit)}&query={quote(query)}&limit={limit}&sort=desc")
    state = check_backoff(url)
    data, last_err = None, None
    for attempt in range(4):
        try:
            data = fetch_raw(url, timeout=30)
            break
        except Exception as e:
            last_err = e
            time.sleep(10 * (attempt + 1) + random.uniform(0, 5))  # linear + jitter
    if data is None:
        record_failure(url, state, f"{type(last_err).__name__}: {last_err}")
        sys.exit(f"arctic shift failed after retries: {last_err} "
                 f"(backoff entered — wait it out instead of retrying)")
    record_success(url, state)
    posts = data.get("data") or []
    for p in posts:
        print(f"- {p.get('title')}")
        print(f"  r/{p.get('subreddit')} | u/{p.get('author')} | score={p.get('score')} | comments={p.get('num_comments')} | {p.get('created_utc')}")
        print(f"  https://www.reddit.com{p.get('permalink')}")
        if bodies and p.get("selftext"):
            print("  " + p["selftext"][:600].replace("\n", " "))
        print()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    cmd = sys.argv[1]
    if cmd == "x":
        cmd_x(sys.argv[2])
    elif cmd == "xtext":
        cmd_x(sys.argv[2], text_only=True)
    elif cmd == "reddit":
        cmd_reddit(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 10)
    elif cmd == "redditself":
        cmd_reddit(sys.argv[2], sys.argv[3], int(sys.argv[4]) if len(sys.argv) > 4 else 10, bodies=True)
    else:
        sys.exit(__doc__)

#!/usr/bin/env python3
# Tavily Web Search - cross-platform (Windows / macOS / Linux)

import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request


API_URL = "https://api.tavily.com/search"
MAX_RESULTS = 5


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def print_usage():
    print("Usage: search.py <query> [--format text|json] [--max-results N] [--no-answer]", file=sys.stderr)
    print("", file=sys.stderr)
    print("Environment:", file=sys.stderr)
    print("  TAVILY_API_KEY   required  Tavily API key (get one at https://tavily.com/)", file=sys.stderr)


def parse_args(argv):
    query_parts = []
    fmt = "text"
    max_results = MAX_RESULTS
    include_answer = True

    it = iter(argv[1:])
    for token in it:
        if token in ("-h", "--help"):
            print_usage()
            sys.exit(0)
        elif token == "--format":
            try:
                fmt = next(it)
            except StopIteration:
                eprint("Error: --format requires a value (text|json)")
                sys.exit(1)
            if fmt not in ("text", "json"):
                eprint(f"Error: invalid --format '{fmt}' (expected text|json)")
                sys.exit(1)
        elif token == "--max-results":
            try:
                max_results = int(next(it))
            except (StopIteration, ValueError):
                eprint("Error: --max-results requires an integer")
                sys.exit(1)
        elif token == "--no-answer":
            include_answer = False
        elif token.startswith("--"):
            eprint(f"Error: unknown option '{token}'")
            print_usage()
            sys.exit(1)
        else:
            query_parts.append(token)

    query = " ".join(query_parts).strip()
    if not query:
        print_usage()
        sys.exit(1)

    return query, fmt, max_results, include_answer


def tavily_search(query, api_key, max_results, include_answer):
    payload = {
        "query": query,
        "max_results": max_results,
        "include_answer": include_answer,
    }
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        API_URL,
        data=data,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body)
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        eprint(f"HTTP {e.code} {e.reason}: {body}")
        raise SystemExit(2)
    except urllib.error.URLError as e:
        eprint(f"Network error: {e.reason}")
        raise SystemExit(3)


def render_text(result):
    lines = [f"Query: {result.get('query', '')}"]
    answer = result.get("answer")
    if answer:
        lines.append("")
        lines.append("📝 Answer:")
        lines.append(answer)
    lines.append("")
    lines.append("🔗 Sources:")
    for r in result.get("results", [])[:MAX_RESULTS]:
        title = r.get("title") or "No title"
        url = r.get("url") or ""
        content = (r.get("content") or "").strip()
        lines.append(f"  - {title}")
        lines.append(f"    {url}")
        if content:
            snippet = content if len(content) <= 240 else content[:240] + "…"
            lines.append(f"    {snippet}")
    print("\n".join(lines))


def main():
    query, fmt, max_results, include_answer = parse_args(sys.argv)

    api_key = os.environ.get("TAVILY_API_KEY", "").strip()
    if not api_key:
        eprint("Error: TAVILY_API_KEY not set.")
        eprint("Get one at https://tavily.com/ and set it in your environment:")
        eprint("  PowerShell : $env:TAVILY_API_KEY = 'tvly-...'")
        eprint("  cmd        : set TAVILY_API_KEY=tvly-...")
        eprint("  bash/shell : export TAVILY_API_KEY='tvly-...'")
        sys.exit(1)

    print(f"Searching: {query}", file=sys.stderr)
    data = tavily_search(query, api_key, max_results, include_answer)

    if fmt == "json":
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        render_text(data)


if __name__ == "__main__":
    main()

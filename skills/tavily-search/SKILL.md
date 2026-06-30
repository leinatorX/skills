---
name: tavily-search
description: Tavily AI search API - Optimized search for AI agents. Use when searching the web for current information, news, facts, or any task requiring real-time data. Cross-platform: works on Windows, macOS, and Linux.
---

# Tavily Search

Web search optimized for AI agents using the Tavily API. Pure-Python implementation, no shell dependencies — runs the same on Windows (cmd / PowerShell / Git Bash), macOS, and Linux.

## Requirements

- Python 3.7+
- `TAVILY_API_KEY` environment variable

## Usage

```bash
python scripts/search.py "your search query"
```

## Options

| Flag | Description |
|------|-------------|
| `--format text` *(default)* | Human-readable output (answer + sources) |
| `--format json` | Raw JSON response |
| `--max-results N` | Override the default of 5 results |
| `--no-answer` | Skip the AI-generated answer, only return sources |
| `-h`, `--help` | Show usage |

## Environment

Pick the right form for your shell:

```powershell
# PowerShell
$env:TAVILY_API_KEY = "your-api-key"
```

```cmd
:: cmd.exe
set TAVILY_API_KEY=your-api-key
```

```bash
# bash / zsh / Git Bash
export TAVILY_API_KEY="your-api-key"
```

Get an API key at: https://tavily.com/

## Examples

```bash
# Basic search (human-readable output)
python scripts/search.py "Claude AI latest features"

# Get raw JSON for programmatic use
python scripts/search.py "latest AI news" --format json

# Tune result count
python scripts/search.py "Python async best practices" --max-results 10

# Sources only, skip the synthesized answer
python scripts/search.py "Rust 1.80 release notes" --no-answer
```

The script returns search results optimized for AI context: a synthesized `answer` plus up to N `sources` (title, URL, snippet).

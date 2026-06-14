# OOP: Pattern Matching with re
# Pattern: encapsulate compiled regex patterns inside a class
# Concepts: re.compile, search, findall, sub, groups, named groups

import re
from dataclasses import dataclass


# ── 1. Simple PatternMatcher ──────────────────────────────────────────────────
# Compile once, reuse many times — faster than re.search(pattern, ...) each call

class PatternMatcher:
    """Encapsulates a compiled regex. Compile once, match many."""

    def __init__(self, pattern: str, flags: int = 0):
        self._pattern = re.compile(pattern, flags)

    def match(self, text: str) -> bool:
        return bool(self._pattern.search(text))

    def find_first(self, text: str) -> str | None:
        m = self._pattern.search(text)
        return m.group() if m else None

    def find_all(self, text: str) -> list[str]:
        return self._pattern.findall(text)

    def replace(self, text: str, replacement: str) -> str:
        return self._pattern.sub(replacement, text)

    def __repr__(self) -> str:
        return f"PatternMatcher(pattern={self._pattern.pattern!r})"


# ── 2. HTTPLogParser ──────────────────────────────────────────────────────────
# Real-world: parse Apache/Nginx access log lines into structured data
# Pattern uses named groups → m.group('name') instead of m.group(1)

@dataclass
class LogEntry:
    ip:       str
    method:   str
    endpoint: str
    status:   int
    size:     int


class HTTPLogParser:
    """
    Parses HTTP access log lines into LogEntry objects.
    Format: <ip> - - [date] "METHOD /path HTTP/1.x" status size
    """

    _PATTERN = re.compile(
        r'(?P<ip>\d+\.\d+\.\d+\.\d+)'       # IP address
        r'.*?"'
        r'(?P<method>\w+) '                   # HTTP method
        r'(?P<endpoint>\S+) HTTP/\S+"'        # endpoint
        r' (?P<status>\d{3})'                 # status code
        r' (?P<size>\d+)'                     # response size
    )

    def parse(self, line: str) -> LogEntry | None:
        m = self._PATTERN.search(line)
        if not m:
            return None
        return LogEntry(
            ip=m.group('ip'),
            method=m.group('method'),
            endpoint=m.group('endpoint'),
            status=int(m.group('status')),
            size=int(m.group('size')),
        )

    def parse_many(self, lines: list[str]) -> list[LogEntry]:
        return [e for line in lines if (e := self.parse(line))]

    def filter_by_status(self, lines: list[str], status: int) -> list[LogEntry]:
        return [e for e in self.parse_many(lines) if e.status == status]


# ── 3. TextCleaner ───────────────────────────────────────────────────────────
# Demonstrates re.sub chains and flags (IGNORECASE, MULTILINE)

class TextCleaner:
    """Applies a pipeline of regex substitutions to clean text."""

    def __init__(self):
        self._steps: list[tuple[re.Pattern, str]] = []

    def add_rule(self, pattern: str, replacement: str, flags: int = 0) -> "TextCleaner":
        self._steps.append((re.compile(pattern, flags), replacement))
        return self     # fluent interface — chain calls

    def clean(self, text: str) -> str:
        for pattern, replacement in self._steps:
            text = pattern.sub(replacement, text)
        return text.strip()


# ── Quick Reference ───────────────────────────────────────────────────────────
# re.search(p, s)      → first match anywhere       returns Match or None
# re.match(p, s)       → match only at start        returns Match or None
# re.findall(p, s)     → list of all matches        returns list[str]
# re.finditer(p, s)    → iterator of Match objects
# re.sub(p, r, s)      → replace all matches
# re.split(p, s)       → split string by pattern
# re.compile(p, flags) → compiled Pattern object
#
# Match object methods:
# m.group()   / m.group(0)    → full match
# m.group(1)                  → first capture group
# m.group('name')             → named group
# m.groups()                  → tuple of all groups
# m.start() / m.end()         → match position
#
# Common patterns:
# r'\d+'        digits
# r'\w+'        word chars (letters, digits, _)
# r'\s+'        whitespace
# r'[a-zA-Z]+'  letters only
# r'^\d{4}-\d{2}-\d{2}$'  date YYYY-MM-DD (anchored)
# r'(?P<name>\w+)'         named capture group


if __name__ == "__main__":
    # ── PatternMatcher ────────────────────────────────────────────────────────
    email = PatternMatcher(r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}')
    print(email.match("contact me at user@example.com please"))  # True
    print(email.find_first("send to alice@work.org"))            # alice@work.org
    print(email.find_all("a@b.com and c@d.org"))                 # ['a@b.com', 'c@d.org']

    digits = PatternMatcher(r'\d+')
    print(digits.replace("abc 123 def 456", "NUM"))              # abc NUM def NUM

    print()

    # ── HTTPLogParser ─────────────────────────────────────────────────────────
    logs = [
        '192.168.1.1 - - [01/Jan/2025] "GET /home HTTP/1.1" 200 1024',
        '10.0.0.5 - - [01/Jan/2025] "POST /login HTTP/1.1" 401 256',
        '172.16.0.2 - - [01/Jan/2025] "GET /api/data HTTP/1.1" 200 4096',
        'INVALID LINE — no match here',
    ]

    parser = HTTPLogParser()
    entries = parser.parse_many(logs)
    for e in entries:
        print(e)

    print("\n401 errors:")
    for e in parser.filter_by_status(logs, 401):
        print(e)

    print()

    # ── TextCleaner ───────────────────────────────────────────────────────────
    cleaner = (
        TextCleaner()
        .add_rule(r'<[^>]+>', '')                  # strip HTML tags
        .add_rule(r'\s+', ' ')                     # collapse whitespace
        .add_rule(r'http\S+', '[URL]')             # redact URLs
        .add_rule(r'[^\w\s\[\]]', '', re.ASCII)    # remove punctuation
    )

    raw = "  <b>Hello</b>   world!  Visit http://example.com for more.  "
    print(cleaner.clean(raw))                      # Hello world Visit [URL] for more

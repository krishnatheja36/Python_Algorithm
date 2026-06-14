# OOP: Log Processing with re
# Pattern: wrap re.search / findall / sub / finditer inside focused classes
# Concepts: numbered groups vs named groups, re.findall, re.finditer, re.sub,
#           re.IGNORECASE, Counter, defaultdict, histogram

import re
from collections import Counter, defaultdict


# ── 1. HTTPLogParser ──────────────────────────────────────────────────────────
# Mirrors the CK interview task: parse log lines → dicts using numbered groups
# Format: <ip> - - [date] "METHOD /path HTTP/x" status bytes

class HTTPLogParser:
    """
    Parses HTTP access log lines into dicts.
    Uses numbered capture groups — contrast with named groups in oop5.
    """

    _PATTERN = re.compile(
        r'(\d+\.\d+\.\d+\.\d+)'    # group 1: IP
        r'.*?"'
        r'(\w+) '                   # group 2: method
        r'(\S+) HTTP[^"]*"'         # group 3: endpoint
        r' (\d{3})'                 # group 4: status
        r' (\d+)'                   # group 5: bytes
    )

    def parse(self, line: str) -> dict | None:
        m = self._PATTERN.search(line)
        if not m:
            return None
        ip, method, endpoint, status, size = m.groups()
        return {
            'ip':       ip,
            'method':   method,
            'endpoint': endpoint,
            'status':   int(status),
            'bytes':    int(size),
        }

    def parse_many(self, lines: list[str]) -> list[dict]:
        return [d for line in lines if (d := self.parse(line))]


# ── 2. LogAnalyzer ────────────────────────────────────────────────────────────
# Status histogram + top-N endpoints — exactly the CK interview tasks, in OOP

class LogAnalyzer:
    """Produces histograms and rankings from parsed log dicts."""

    def __init__(self, records: list[dict]):
        self._records = records

    def status_histogram(self) -> None:
        counts = Counter(r['status'] for r in self._records)
        print("Status Code Histogram:")
        for status, count in sorted(counts.items()):
            print(f"  {status} | {'#' * count} ({count})")

    def top_endpoints(self, n: int = 5) -> list[tuple[str, int]]:
        return Counter(r['endpoint'] for r in self._records).most_common(n)

    def requests_by_ip(self) -> dict[str, int]:
        tally: dict[str, int] = defaultdict(int)
        for r in self._records:
            tally[r['ip']] += 1
        return dict(sorted(tally.items(), key=lambda x: x[1], reverse=True))

    def filter_by_status(self, status: int) -> list[dict]:
        return [r for r in self._records if r['status'] == status]


# ── 3. LogRedactor ────────────────────────────────────────────────────────────
# re.sub with strings and callables — mask sensitive data before storing logs

class LogRedactor:
    """
    Masks sensitive values in raw log lines using re.sub.
    sub(pattern, replacement, string) — replacement can be a string or callable.
    """

    # compiled once as class attrs
    _IP      = re.compile(r'\d{1,3}(?:\.\d{1,3}){3}')
    _EMAIL   = re.compile(r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}')
    _TOKEN   = re.compile(r'(?i)token[=:]\s*\S+')   # re.IGNORECASE via (?i)
    _CARD    = re.compile(r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b')

    def redact(self, line: str) -> str:
        line = self._IP.sub('[IP]', line)
        line = self._EMAIL.sub('[EMAIL]', line)
        line = self._TOKEN.sub('token=[REDACTED]', line)
        line = self._CARD.sub('[CARD]', line)
        return line

    def redact_many(self, lines: list[str]) -> list[str]:
        return [self.redact(line) for line in lines]


# ── 4. LogScanner ─────────────────────────────────────────────────────────────
# re.findall → list of strings
# re.finditer → iterator of Match objects (use when you need .start()/.end())

class LogScanner:
    """
    Scans raw log text for patterns using findall and finditer.
    findall  → returns list[str]           — just the matches
    finditer → returns Iterator[Match]     — full match objects with position
    """

    _ERROR_CODE = re.compile(r'E\d{4}', re.IGNORECASE)  # E1234 style codes
    _URL        = re.compile(r'https?://\S+')
    _DURATION   = re.compile(r'(\d+)ms')                # capture the number only

    def find_error_codes(self, text: str) -> list[str]:
        return self._ERROR_CODE.findall(text)            # ['E1001', 'E4023', ...]

    def find_urls(self, text: str) -> list[str]:
        return self._URL.findall(text)

    def find_durations_ms(self, text: str) -> list[int]:
        return [int(n) for n in self._DURATION.findall(text)]

    def locate_error_codes(self, text: str) -> list[tuple[str, int, int]]:
        """finditer: returns (match, start, end) — useful when position matters."""
        return [
            (m.group(), m.start(), m.end())
            for m in self._ERROR_CODE.finditer(text)
        ]


# ── Quick Reference ───────────────────────────────────────────────────────────
# re.search(p, s)       → first match anywhere            Match | None
# re.match(p, s)        → match only at start             Match | None
# re.findall(p, s)      → all matches                     list[str]
# re.finditer(p, s)     → all matches as Match objects    Iterator[Match]
# re.sub(p, r, s)       → replace all matches             str
# re.compile(p, flags)  → compiled Pattern
#
# Numbered groups:  m.group(1), m.group(2), ...  m.groups() → tuple
# Named groups:     (?P<name>...)  →  m.group('name')
#
# Inline flags (no re.compile needed):
# (?i) = re.IGNORECASE      (?m) = re.MULTILINE     (?s) = re.DOTALL
# (?:...) = non-capturing group  (matches but not in m.groups())


if __name__ == "__main__":
    logs = [
        '192.168.1.1 - - [10/May/2026] "GET /api/score HTTP/1.1" 200 1234',
        '192.168.1.2 - - [10/May/2026] "POST /api/login HTTP/1.1" 401 567',
        '192.168.1.1 - - [10/May/2026] "GET /api/score HTTP/1.1" 200 890',
        '192.168.1.3 - - [10/May/2026] "GET /api/offers HTTP/1.1" 500 234',
        '192.168.1.2 - - [10/May/2026] "GET /api/score HTTP/1.1" 200 456',
        'MALFORMED — no match here',
    ]

    # ── Parse + Analyze ───────────────────────────────────────────────────────
    parser  = HTTPLogParser()
    records = parser.parse_many(logs)
    print(f"Parsed {len(records)} of {len(logs)} lines\n")

    analyzer = LogAnalyzer(records)
    analyzer.status_histogram()

    print(f"\nTop 3 endpoints:")
    for endpoint, count in analyzer.top_endpoints(3):
        print(f"  {endpoint:25} {count} requests")

    print(f"\nRequests by IP:")
    for ip, count in analyzer.requests_by_ip().items():
        print(f"  {ip:15} {count}")

    print(f"\n401 errors:")
    for r in analyzer.filter_by_status(401):
        print(" ", r)

    print()

    # ── Redact ────────────────────────────────────────────────────────────────
    sensitive = [
        "User alice@example.com logged in from 192.168.1.5",
        "Auth failed: token=abc123secret for 10.0.0.1",
        "Payment card 4111 1111 1111 1111 submitted",
    ]
    redactor = LogRedactor()
    print("Redacted lines:")
    for line in redactor.redact_many(sensitive):
        print(" ", line)

    print()

    # ── Scan ─────────────────────────────────────────────────────────────────
    error_log = (
        "Pipeline failed E1042 at step 3 (12ms). "
        "Retry triggered E1042 again. See https://docs.internal/e1042 (45ms)."
    )
    scanner = LogScanner()
    print("Error codes   :", scanner.find_error_codes(error_log))
    print("URLs          :", scanner.find_urls(error_log))
    print("Durations (ms):", scanner.find_durations_ms(error_log))
    print("Positions     :", scanner.locate_error_codes(error_log))

"""
Subdomain Visit Count — Karat / LeetCode 811 | Arrays & Hashing

Pattern: Counter — accumulate clicks across all suffix subdomains.
  Split each entry into count + domain. Split the domain by "." to get all
  subdomains (suffixes). Add the click count to each suffix in a Counter.
  Return each subdomain with its total count.

Time:  O(n * d) — n entries, d = max subdomain depth
Space: O(n * d) — counter of all unique subdomains
"""
import collections


def subdomain_visit_count(cpdomains):
    ans = collections.Counter()
    for domain in cpdomains:
        count, domain = domain.split()
        count = int(count)
        frags = domain.split('.')
        for i in range(len(frags)):
            ans[".".join(frags[i:])] += count

    return [f"{ct} {dom}" for dom, ct in ans.items()]


if __name__ == "__main__":
    inp = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(subdomain_visit_count(inp))
    # ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]

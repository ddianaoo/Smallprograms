ispalindrome = lambda s: sum(s.count(c) % for c in set(s)) < 2

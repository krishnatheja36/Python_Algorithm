"""
Find Error Action — Karat | Arrays & Hashing

Pattern: Hash Map + String Pattern Matching
  Group all actions per user into a defaultdict(list). For each user,
  join their action sequence into a string and check if the error_action
  substring appears in it. Return users whose joined sequence contains
  the error pattern.

Time:  O(n * e) — n action records, e = length of error_action
Space: O(n)     — action sequences per user
"""
from collections import defaultdict


def find_error_action(action_user, error_action):
    user_actions = defaultdict(list)
    for action, user in action_user:
        user_actions[user].append(action)

    return [user for user, actions in user_actions.items()
            if error_action in "".join(actions)]


if __name__ == "__main__":
    action_user = [
        ["A","1"], ["B","1"], ["B","2"], ["C","1"], ["C","2"],
        ["C","3"], ["A","2"], ["A","3"], ["A","2"], ["B","2"], ["C","2"],
    ]
    error_action = "ABC"
    print(find_error_action(action_user, error_action))   # users whose actions contain "ABC"

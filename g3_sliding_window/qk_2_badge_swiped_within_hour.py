"""
Badge Swiped Within One Hour — Karat | Sliding Window

Pattern: Sliding Window on sorted timestamps per person
  Group swipe times by name. For each person, sort their times.
  Slide a window: if times[i+2] - times[i] <= 100 (in HHMM format, 100 = 1 hour),
  all three swipes are within one hour — flag that person.

  Note: time comparison uses HHMM as an integer. The "within 1 hour" check
  is times[i+2] - times[i] <= 100 (not 60) because the format is HHMM.

Time:  O(n log n) — sorting per person dominates
Space: O(n)       — grouped swipe times
"""
from collections import defaultdict


def badge_swiped_within_hour(key_names, key_times):
    swipes = defaultdict(list)
    for name, time in zip(key_names, key_times):
        hhmm = int(time[:2] + time[3:5])   # "HH:MM" → integer HHMM
        swipes[name].append(hhmm)

    result = {}
    for name, times in swipes.items():
        times.sort()
        for i in range(len(times) - 2):
            if times[i + 2] - times[i] <= 100:
                result[name] = [f"{t // 100:02d}:{t % 100:02d}" for t in times]
                break
    return result


if __name__ == "__main__":
    names = ["daniel","daniel","daniel","luis","luis","luis","luis"]
    times = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
    print(badge_swiped_within_hour(names, times))
    # {'daniel': ['10:00', '10:40', '11:00']}

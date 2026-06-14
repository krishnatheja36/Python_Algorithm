"""
Student Course Overlap — Karat | Arrays & Hashing + Combinations

Pattern: Hash Map + Combinations
  Build a map of course → [student_ids]. Then for every pair of students,
  check which courses they share by scanning the course map.
  itertools.combinations generates all student pairs without repetition.

Time:  O(c * s²) — c courses, s students; each pair checked against all courses
Space: O(c * s)  — course → students map
"""
from collections import defaultdict
from itertools import combinations


def student_course_overlap(student_course_pairs):
    course_to_students = defaultdict(list)
    students = set()

    for sid, course in student_course_pairs:
        students.add(sid)
        course_to_students[course].append(sid)

    result = {}
    for a, b in sorted(map(sorted, combinations(students, 2))):
        pair = (a, b)
        shared = [course for course, sids in course_to_students.items()
                  if a in sids and b in sids]
        result[pair] = shared

    return result


if __name__ == "__main__":
    pairs = [
        ["58", "Software Design"], ["58", "Linear Algebra"],
        ["94", "Art History"],     ["94", "Operating Systems"],
        ["17", "Software Design"], ["58", "Mechanics"],
        ["58", "Economics"],       ["17", "Linear Algebra"],
        ["17", "Political Science"], ["94", "Economics"],
        ["25", "Economics"],
    ]
    for k, v in student_course_overlap(pairs).items():
        if v:
            print(f"{k}: {v}")

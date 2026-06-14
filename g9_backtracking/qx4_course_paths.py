"""
Course Paths — Custom Graph Problem | Backtracking / DFS

Logic:
    Build a directed graph from course dependency pairs. Find all root courses
    (no incoming edges) and all leaf courses (no outgoing edges). Run a DFS from
    each root, collecting the full path when a leaf is reached. Returns all
    linear paths from root to leaf in the curriculum graph.

Time:  O(V + E + P) — V nodes, E edges, P total length of all paths
Space: O(V + E) — adjacency list and parent map; O(depth) for the DFS stack
"""

# Question: PYTHON Students may decide to take different "tracks" or sequences of courses in the Computer Science curriculum. 
# There may be more than one track that includes the same course, but each student follows a single linear track from a "root" node to a "leaf" node. 
# In the graph below, their path always moves left to right. 
# Return all possible paths in the curriculum

from collections import defaultdict, deque

class Solution:
    def course_paths(self, course_pairs):
        children = defaultdict(list)
        parents = defaultdict(list)
        all_courses = set()

        for src, dst in course_pairs:
            children[src].append(dst)
            parents[dst].append(src)
            all_courses.update([src, dst])

        
        # print("Parents -")
        # for key, value in parents.items(): print("\t{} : {}".format(key, value))
        # print("Children -")
        # for key, value in children.items(): print("\t{} : {}".format(key, value))

        # Find root courses
        roots = [course for course in all_courses if course not in parents]
        # print("\nRoots : {}\n".format(roots))

        # DFS to find all linear paths
        def dfs(course, path):
            path.append(course)
            if not children[course]:
                paths.append(path)
            else:
                for next_course in children[course]:
                    dfs(next_course, path.copy())
            path.pop()
            

        paths = []
        for root in roots:
            dfs(root, [])

        return paths



if __name__ == '__main__':
    S = Solution()

    all_courses = [
        ["Logic","COBOL"],
        ["Data Structures","Algorithms"],
        ["Creative Writing","Data Structures"],
        ["Algorithms","COBOL"],
        ["Intro to Computer Science","Data Structures"],
        ["Logic","Compilers"],
        ["Data Structures","Logic"],
        ["Creative Writing","System Administration"],
        ["Databases","System Administration"],
        ["Creative Writing","Databases"]
    ]
    print("All the possible paths -")
    for path in S.course_paths(all_courses): print("\t{}".format(path))
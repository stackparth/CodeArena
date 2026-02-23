"""Append 10 Advanced DSA questions (20000 pts each) to questions.py"""
import pprint

with open('app/questions.py', 'r', encoding='utf-8') as f:
    content = f.read()
qs = eval(content.split('=', 1)[1].strip())

advanced = [
    {
        'id': 101, 'difficulty': 'Advanced', 'points': 20000,
        'title': 'LRU Cache',
        'description': (
            "You're designing a web browser's cache system. It should store the most recently used pages "
            "and evict the least recently used one when full.\n\n"
            "Implement an LRU Cache class with `get(key)` and `put(key, value)` methods. "
            "Both should run in O(1) time.\n\n"
            "For this problem, implement a function `lru_cache_test(capacity, operations, args)` that:\n"
            "- Creates an LRU Cache with given capacity\n"
            "- Executes operations ('get' or 'put') with corresponding args\n"
            "- Returns a list of results (get returns value or -1, put returns None)\n\n"
            "🎯 Real-Life Use: Browser caching, database query caching, CDN systems.\n\n"
            "Example Test Case:\n"
            "Input: `lru_cache_test(2, ['put','put','get','put','get','put','get','get','get'], [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]])`\n"
            "Expected Output: `[None, None, 1, None, -1, None, -1, 3, 4]`"
        ),
        'starter': (
            "def lru_cache_test(capacity, operations, args):\n"
            "    # Implement an LRU Cache and process operations\n"
            "    pass"
        ),
        'tests': [{'input': "lru_cache_test(2, ['put','put','get','put','get','put','get','get','get'], [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]])",
                    'expected': [None, None, 1, None, -1, None, -1, 3, 4]}],
        'hint': 'Use an OrderedDict or combine a HashMap with a Doubly Linked List for O(1) get/put.',
        'tags': ['data-structures', 'design', 'advanced']
    },
    {
        'id': 102, 'difficulty': 'Advanced', 'points': 20000,
        'title': 'Serialize & Deserialize Binary Tree',
        'description': (
            "You're building a cloud save system for a game. The game's skill tree (a binary tree) needs to be "
            "saved as a string and later reconstructed exactly.\n\n"
            "Implement `serialize(root)` to convert a tree (given as nested lists `[val, left, right]` or None) "
            "to a string, and `deserialize(data)` to convert it back.\n\n"
            "For this problem, implement `serde_test(tree)` that serializes then deserializes and returns the result.\n\n"
            "🎯 Real-Life Use: Saving/loading game states, database storage of tree structures.\n\n"
            "Example Test Case:\n"
            "Input: `serde_test([1, [2, None, None], [3, [4, None, None], [5, None, None]]])`\n"
            "Expected Output: `[1, [2, None, None], [3, [4, None, None], [5, None, None]]]`"
        ),
        'starter': (
            "def serde_test(tree):\n"
            "    # Serialize tree to string, then deserialize back\n"
            "    pass"
        ),
        'tests': [{'input': "serde_test([1, [2, None, None], [3, [4, None, None], [5, None, None]]])",
                    'expected': [1, [2, None, None], [3, [4, None, None], [5, None, None]]]}],
        'hint': 'Use preorder traversal with a delimiter. Use a queue/iterator for deserialization.',
        'tags': ['trees', 'design', 'advanced']
    },
    {
        'id': 103, 'difficulty': 'Advanced', 'points': 20000,
        'title': 'Median of Two Sorted Arrays',
        'description': (
            "Two hospitals merge their patient age records (both sorted). You need to find the median age "
            "across all patients efficiently without merging the full lists.\n\n"
            "Write `find_median(nums1, nums2)` that returns the median of two sorted arrays.\n"
            "The overall run time complexity should be O(log(min(m,n))).\n\n"
            "🎯 Real-Life Use: Merging sorted datasets in distributed databases.\n\n"
            "Example Test Case:\n"
            "Input: `find_median([1, 3], [2])`\n"
            "Expected Output: `2.0`"
        ),
        'starter': "def find_median(nums1, nums2):\n    pass",
        'tests': [{'input': 'find_median([1, 3], [2])', 'expected': 2.0}],
        'hint': 'Use binary search on the shorter array. Partition both arrays so left halves have the smaller elements.',
        'tags': ['binary-search', 'arrays', 'advanced']
    },
    {
        'id': 104, 'difficulty': 'Advanced', 'points': 20000,
        'title': 'Minimum Window Substring',
        'description': (
            "A DNA researcher needs to find the shortest segment of a genome that contains all required markers.\n\n"
            "Given strings `s` and `t`, find the minimum window substring of `s` that contains all characters of `t` "
            "(including duplicates). Return empty string if no such window exists.\n\n"
            "🎯 Real-Life Use: Genome sequencing, text search engines.\n\n"
            "Example Test Case:\n"
            "Input: `min_window('ADOBECODEBANC', 'ABC')`\n"
            "Expected Output: `BANC`"
        ),
        'starter': "def min_window(s, t):\n    pass",
        'tests': [{'input': "min_window('ADOBECODEBANC', 'ABC')", 'expected': 'BANC'}],
        'hint': 'Use sliding window with two pointers. Expand right to include, shrink left to minimize.',
        'tags': ['sliding-window', 'strings', 'advanced']
    },
    {
        'id': 105, 'difficulty': 'Advanced', 'points': 20000,
        'title': 'Longest Increasing Subsequence Length',
        'description': (
            "A stock analyst tracks daily closing prices and wants to find the longest period where prices were "
            "strictly increasing (not necessarily consecutive days).\n\n"
            "Given an array `nums`, return the length of the longest strictly increasing subsequence.\n"
            "Aim for O(n log n) complexity.\n\n"
            "🎯 Real-Life Use: Stock trend analysis, patience sorting.\n\n"
            "Example Test Case:\n"
            "Input: `lis_length([10, 9, 2, 5, 3, 7, 101, 18])`\n"
            "Expected Output: `4`"
        ),
        'starter': "def lis_length(nums):\n    pass",
        'tests': [{'input': 'lis_length([10, 9, 2, 5, 3, 7, 101, 18])', 'expected': 4}],
        'hint': 'Use a "tails" array with binary search. For each num, replace the first tail >= num, or append if larger than all.',
        'tags': ['dp', 'binary-search', 'advanced']
    },
    {
        'id': 106, 'difficulty': 'Advanced', 'points': 20000,
        'title': 'Word Search II (Trie + Backtracking)',
        'description': (
            "You're building a word puzzle game (like Boggle). Given a 2D board of letters and a list of words, "
            "find all words that can be formed by connecting adjacent cells (horizontal/vertical, no reuse).\n\n"
            "Return a sorted list of found words.\n\n"
            "🎯 Real-Life Use: Word puzzle solvers, autocomplete on keyboards.\n\n"
            "Example Test Case:\n"
            "Input: `sorted(find_words([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], ['oath','pea','eat','rain']))`\n"
            "Expected Output: `['eat', 'oath']`"
        ),
        'starter': "def find_words(board, words):\n    pass",
        'tests': [{'input': "sorted(find_words([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], ['oath','pea','eat','rain']))",
                    'expected': ['eat', 'oath']}],
        'hint': 'Build a Trie from the word list. DFS/backtrack on the board while walking the Trie to prune early.',
        'tags': ['trie', 'backtracking', 'advanced']
    },
    {
        'id': 107, 'difficulty': 'Advanced', 'points': 20000,
        'title': 'Dijkstra Shortest Path',
        'description': (
            "A delivery app needs to find the shortest route between warehouses in a city. The city map is a "
            "weighted graph.\n\n"
            "Given `n` nodes (0 to n-1), a list of edges `[u, v, weight]`, and a `start` node, return a list of "
            "shortest distances from start to each node. Use -1 for unreachable nodes.\n\n"
            "🎯 Real-Life Use: Google Maps routing, network packet routing.\n\n"
            "Example Test Case:\n"
            "Input: `dijkstra(4, [[0,1,1],[0,2,4],[1,2,2],[1,3,6],[2,3,3]], 0)`\n"
            "Expected Output: `[0, 1, 3, 6]`"
        ),
        'starter': "def dijkstra(n, edges, start):\n    pass",
        'tests': [{'input': 'dijkstra(4, [[0,1,1],[0,2,4],[1,2,2],[1,3,6],[2,3,3]], 0)',
                    'expected': [0, 1, 3, 6]}],
        'hint': 'Use a min-heap (heapq). Push (distance, node), always process the smallest distance first. Skip if already visited.',
        'tags': ['graphs', 'heap', 'advanced']
    },
    {
        'id': 108, 'difficulty': 'Advanced', 'points': 20000,
        'title': 'Topological Sort (Course Schedule)',
        'description': (
            "A university needs to determine a valid order to offer courses, given that some courses have prerequisites.\n\n"
            "Given `n` courses (0 to n-1) and a list of prerequisites `[course, prereq]`, return a valid ordering. "
            "If impossible (circular dependency), return an empty list.\n\n"
            "🎯 Real-Life Use: Course planning, build systems (make/gradle), task scheduling.\n\n"
            "Example Test Case:\n"
            "Input: `topo_sort(4, [[1,0],[2,0],[3,1],[3,2]])`\n"
            "Expected Output: `[0, 1, 2, 3]`"
        ),
        'starter': "def topo_sort(n, prerequisites):\n    pass",
        'tests': [{'input': 'topo_sort(4, [[1,0],[2,0],[3,1],[3,2]])', 'expected': [0, 1, 2, 3]}],
        'hint': "Use Kahn's algorithm (BFS with in-degree tracking) or DFS with visited states.",
        'tags': ['graphs', 'topological-sort', 'advanced']
    },
    {
        'id': 109, 'difficulty': 'Advanced', 'points': 20000,
        'title': 'Knapsack 0/1',
        'description': (
            "A thief breaks into a store and has a backpack with limited capacity. Each item has a weight and value. "
            "They can either take or leave each item (no splitting). Maximize total value.\n\n"
            "Given `capacity`, list of `weights`, and list of `values`, return the maximum value achievable.\n\n"
            "🎯 Real-Life Use: Resource allocation, investment portfolio optimization, cargo loading.\n\n"
            "Example Test Case:\n"
            "Input: `knapsack(7, [1, 3, 4, 5], [1, 4, 5, 7])`\n"
            "Expected Output: `9`"
        ),
        'starter': "def knapsack(capacity, weights, values):\n    pass",
        'tests': [{'input': 'knapsack(7, [1, 3, 4, 5], [1, 4, 5, 7])', 'expected': 9}],
        'hint': 'Use 2D DP: dp[i][w] = max value using first i items with capacity w. Optimize to 1D if you want.',
        'tags': ['dp', 'advanced']
    },
    {
        'id': 110, 'difficulty': 'Advanced', 'points': 20000,
        'title': 'Detect Cycle in Directed Graph',
        'description': (
            "A CI/CD pipeline has tasks that depend on each other. Before running, you need to detect if there's "
            "a circular dependency which would cause an infinite loop.\n\n"
            "Given `n` nodes and a list of directed edges `[from, to]`, return True if the graph contains a cycle.\n\n"
            "🎯 Real-Life Use: Deadlock detection, dependency resolution, compiler analysis.\n\n"
            "Example Test Case:\n"
            "Input: `has_cycle(4, [[0,1],[1,2],[2,3]])`\n"
            "Expected Output: `False`"
        ),
        'starter': "def has_cycle(n, edges):\n    pass",
        'tests': [{'input': 'has_cycle(4, [[0,1],[1,2],[2,3]])', 'expected': False}],
        'hint': 'Use DFS with 3 colors: white (unvisited), gray (in-progress), black (done). A gray→gray edge means cycle.',
        'tags': ['graphs', 'dfs', 'advanced']
    },
]

qs.extend(advanced)

with open('app/questions.py', 'w', encoding='utf-8') as f:
    f.write('QUESTIONS = ')
    pp = pprint.PrettyPrinter(indent=2, width=120, stream=f)
    pp.pprint(qs)
    f.write('\n')

print(f"✅ Added {len(advanced)} Advanced questions. Total: {len(qs)} questions.")

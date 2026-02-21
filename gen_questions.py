import pprint

def generate_questions():
    questions = []
    
    # We will define templates and generate questions.
    # To ensure quality and variety without external libs, we use standard library topics:
    # basics, strings, lists, dicts, math, logic, algorithms, date/time, recursion, classes/oop.

    # 1. Easy Questions (34 questions) -> Blue
    # 2. Medium Questions (33 questions) -> Green
    # 3. Hard Questions (33 questions) -> Red

    easy_pool = [
        ("Return 100", "def return_100():\n    pass", "Write a function `return_100` that simply returns the integer 100.", "return_100()", 100, ["basics"]),
        ("String Length", "def string_length(s):\n    pass", "Write a function `string_length(s)` that returns the length of string `s`.", "string_length('hello')", 5, ["strings"]),
        ("Multiply by 2", "def multiply_by_two(n):\n    pass", "Write a function `multiply_by_two(n)` that returns `n` multiplied by 2.", "multiply_by_two(4)", 8, ["math"]),
        ("First Element", "def first_element(lst):\n    pass", "Return the first element of the list `lst`.", "first_element([10, 20, 30])", 10, ["lists"]),
        ("Last Element", "def last_element(lst):\n    pass", "Return the last element of the list `lst`.", "last_element([10, 20, 30])", 30, ["lists"]),
        ("Is Empty", "def is_empty(lst):\n    pass", "Return True if list is empty, else False.", "is_empty([])", True, ["lists", "conditionals"]),
        ("Concat Strings", "def concat_strings(a, b):\n    pass", "Return string `a` concatenated with `b`.", "concat_strings('a', 'b')", 'ab', ["strings"]),
        ("Square a Number", "def square(n):\n    pass", "Return the square of `n`.", "square(5)", 25, ["math"]),
        ("Is Positive", "def is_positive(n):\n    pass", "Return True if `n` is greater than 0, False otherwise.", "is_positive(5)", True, ["math", "conditionals"]),
        ("Is Negative", "def is_negative(n):\n    pass", "Return True if `n` is less than 0, False otherwise.", "is_negative(-5)", True, ["math", "conditionals"]),
        ("Sum of Two", "def sum_two(a, b):\n    pass", "Return sum of a and b.", "sum_two(2, 3)", 5, ["math"]),
        ("Absolute Value", "def abs_val(n):\n    pass", "Return absolute value of n.", "abs_val(-5)", 5, ["math"]),
        ("Starts with A", "def starts_with_a(s):\n    pass", "Return True if string starts with A or a.", "starts_with_a('Apple')", True, ["strings"]),
        ("Ends with Z", "def ends_with_z(s):\n    pass", "Return True if string ends with Z or z.", "ends_with_z('buzz')", True, ["strings"]),
        ("List Length", "def list_length(lst):\n    pass", "Return the number of elements in the list.", "list_length([1,2,3])", 3, ["lists"]),
        ("Contains X", "def contains_x(lst, x):\n    pass", "Return True if x is in lst.", "contains_x([1,2,3], 2)", True, ["lists"]),
        ("Repeat String", "def repeat_string(s, n):\n    pass", "Return string s repeated n times.", "repeat_string('hi', 3)", 'hihihi', ["strings"]),
        ("Get Keys", "def get_keys(d):\n    pass", "Return a list of keys in dictionary d.", "get_keys({'a':1})", ['a'], ["dicts"]),
        ("Get Values", "def get_values(d):\n    pass", "Return a list of values in dictionary d.", "get_values({'a':1})", [1], ["dicts"]),
        ("Check Even", "def is_even(n):\n    pass", "Return True if n is even.", "is_even(4)", True, ["math"]),
        ("Check Odd", "def is_odd(n):\n    pass", "Return True if n is odd.", "is_odd(5)", True, ["math"]),
        ("Max of Two", "def max_two(a, b):\n    pass", "Return the larger of a and b.", "max_two(5, 10)", 10, ["math"]),
        ("Min of Two", "def min_two(a, b):\n    pass", "Return the smaller of a and b.", "min_two(5, 10)", 5, ["math"]),
        ("Hello Name", "def hello_name(name):\n    pass", "Return 'Hello ' + name.", "hello_name('Bob')", 'Hello Bob', ["strings"]),
        ("First Char", "def first_char(s):\n    pass", "Return first character of s.", "first_char('cat')", 'c', ["strings"]),
        ("Last Char", "def last_char(s):\n    pass", "Return last character of s.", "last_char('cat')", 't', ["strings"]),
        ("To Uppercase", "def to_upper(s):\n    pass", "Convert string to uppercase.", "to_upper('cat')", 'CAT', ["strings"]),
        ("To Lowercase", "def to_lower(s):\n    pass", "Convert string to lowercase.", "to_lower('CAT')", 'cat', ["strings"]),
        ("Strip Spaces", "def strip_spaces(s):\n    pass", "Remove leading and trailing spaces.", "strip_spaces('  hi  ')", 'hi', ["strings"]),
        ("Count Occurrences", "def count_occ(s, char):\n    pass", "Count how many times char appears in s.", "count_occ('hello', 'l')", 2, ["strings"]),
        ("List Sum", "def list_sum(lst):\n    pass", "Return sum of all numbers in list.", "list_sum([1,2,3])", 6, ["lists", "math"]),
        ("List Max", "def list_max(lst):\n    pass", "Return largest number in list.", "list_max([1,5,2])", 5, ["lists", "math"]),
        ("List Min", "def list_min(lst):\n    pass", "Return smallest number in list.", "list_min([1,5,2])", 1, ["lists", "math"]),
        ("Reverse List Easy", "def reverse_list(lst):\n    pass", "Return reversed list.", "reverse_list([1,2,3])", [3,2,1], ["lists"]),
    ]

    medium_pool = [
        ("Remove Duplicates", "def remove_duplicates(lst):\n    pass", "Return list with duplicates removed, order doesn't matter.", "sorted(remove_duplicates([1,2,2,3]))", [1,2,3], ["lists"]),
        ("Factorial", "def factorial(n):\n    pass", "Return factorial of n. (n >= 0)", "factorial(5)", 120, ["math", "recursion"]),
        ("Count Vowels", "def count_vowels(s):\n    pass", "Count number of vowels (a,e,i,o,u) in string.", "count_vowels('hello')", 2, ["strings"]),
        ("Is Palindrome", "def is_palindrome(s):\n    pass", "Return True if s reads the same forward and backward.", "is_palindrome('racecar')", True, ["strings"]),
        ("Fibonacci", "def fibonacci(n):\n    pass", "Return nth Fibonacci number (0th is 0, 1st is 1)", "fibonacci(5)", 5, ["math", "recursion"]),
        ("Merge Two Dictionaries", "def merge_dicts(d1, d2):\n    pass", "Merge two dictionaries, d2 overwrites d1 on conflict.", "merge_dicts({'a':1}, {'b':2})", {'a':1, 'b':2}, ["dicts"]),
        ("Find Missing Number", "def missing_number(lst):\n    pass", "Given list of numbers from 0 to n with one missing, find it.", "missing_number([0,1,3])", 2, ["lists", "algorithms"]),
        ("Sum of Digits", "def sum_digits(n):\n    pass", "Return sum of digits of positive integer n.", "sum_digits(123)", 6, ["math"]),
        ("Are Anagrams", "def are_anagrams(s1, s2):\n    pass", "Return True if s1 and s2 are anagrams.", "are_anagrams('listen', 'silent')", True, ["strings"]),
        ("Reverse Words", "def reverse_words(s):\n    pass", "Reverse the order of words in string word by word.", "reverse_words('hello world')", 'world hello', ["strings"]),
        ("Count Words", "def count_words(s):\n    pass", "Count number of words in string separated by spaces.", "count_words('hello world')", 2, ["strings"]),
        ("Most Frequent Char", "def most_frequent(s):\n    pass", "Return the character that appears most often.", "most_frequent('hello')", 'l', ["strings"]),
        ("Intersection of Lists", "def intersection(l1, l2):\n    pass", "Return common elements in both lists.", "sorted(intersection([1,2,3], [2,3,4]))", [2,3], ["lists"]),
        ("Difference of Lists", "def difference(l1, l2):\n    pass", "Return elements in l1 not in l2.", "sorted(difference([1,2,3], [2,3,4]))", [1], ["lists"]),
        ("Flatten List", "def flatten(lst):\n    pass", "Flatten a 2D list into a 1D list.", "flatten([[1,2], [3]])", [1,2,3], ["lists"]),
        ("Sort Dictionary by Value", "def sort_dict(d):\n    pass", "Return list of keys sorted by their ascending values.", "sort_dict({'a':3, 'b':1, 'c':2})", ['b', 'c', 'a'], ["dicts", "algorithms"]),
        ("Title Case", "def title_case(s):\n    pass", "Capitalize first letter of every word.", "title_case('hello world')", 'Hello World', ["strings"]),
        ("Binary to Decimal", "def bin_to_dec(b):\n    pass", "Convert binary string to integer.", "bin_to_dec('101')", 5, ["math"]),
        ("List of Primes", "def get_primes(n):\n    pass", "Return list of prime numbers up to n.", "get_primes(10)", [2, 3, 5, 7], ["math"]),
        ("GCD", "def gcd(a, b):\n    pass", "Return greatest common divisor of a and b.", "gcd(12, 8)", 4, ["math"]),
        ("LCM", "def lcm(a, b):\n    pass", "Return least common multiple of a and b.", "lcm(4, 6)", 12, ["math"]),
        ("Matrix Transpose", "def transpose(matrix):\n    pass", "Return transposed 2D list.", "transpose([[1,2], [3,4]])", [[1,3], [2,4]], ["lists"]),
        ("Second Largest", "def second_largest(lst):\n    pass", "Find second largest number in list.", "second_largest([1, 5, 3, 4])", 4, ["lists"]),
        ("Remove Vowels", "def remove_vowels(s):\n    pass", "Return string without vowels.", "remove_vowels('hello')", 'hll', ["strings"]),
        ("Dict from two lists", "def to_dict(keys, values):\n    pass", "Create dict from list of keys and val.", "to_dict(['a','b'], [1,2])", {'a':1, 'b':2}, ["dicts", "lists"]),
        ("Find Pairs", "def find_pairs(lst, target):\n    pass", "Find two numbers in list that add up to target and return as a tuple (sorted). Return None if none.", "find_pairs([1,2,3,4], 5)", (1, 4), ["lists", "algorithms"]),
        ("Is Sorted", "def is_sorted(lst):\n    pass", "Return True if list is sorted in ascending order.", "is_sorted([1,2,3])", True, ["lists"]),
        ("Rotate List", "def rotate(lst, k):\n    pass", "Rotate list to the right by k steps.", "rotate([1,2,3,4,5], 2)", [4,5,1,2,3], ["lists"]),
        ("Check Subsequence", "def is_subsequence(s1, s2):\n    pass", "Return True if s1 is subsequence of s2.", "is_subsequence('abc', 'ahbgdc')", True, ["strings"]),
        ("Capitalize Alternate Matrix", "def alt_caps(s):\n    pass", "Capitalize alternate letters.", "alt_caps('hello')", 'HeLlO', ["strings"]),
        ("Count Bits", "def count_bits(n):\n    pass", "Return number of 1s in binary representation of n.", "count_bits(5)", 2, ["math"]),
        ("Is Power of Two", "def is_power_of_two(n):\n    pass", "Return True if n is power of two.", "is_power_of_two(8)", True, ["math"]),
        ("Group Anagrams Medium", "def group_anagrams_medium(strs):\n    pass", "Group anagrams together from a list of strings but just return the count of groups.", "group_anagrams_medium(['eat', 'tea', 'tan'])", 2, ["strings"]),
    ]

    hard_pool = [
        ("Longest Palindromic Substring", "def longest_palindrome(s):\n    pass", "Return the longest palindromic substring.", "longest_palindrome('babad') in ['bab', 'aba']", True, ["strings", "algorithms"]),
        ("Merge Intervals", "def merge_intervals(intervals):\n    pass", "Merge overlapping intervals.", "merge_intervals([[1,3],[2,6],[8,10]])", [[1,6],[8,10]], ["lists", "algorithms"]),
        ("Trapping Rain Water", "def trap(heights):\n    pass", "Calculate how much water can be trapped after raining.", "trap([0,1,0,2,1,0,1,3,2,1,2,1])", 6, ["lists", "algorithms"]),
        ("Word Break", "def word_break(s, word_dict):\n    pass", "Return True if string can be segmented into dictionary words.", "word_break('leetcode', ['leet', 'code'])", True, ["strings", "algorithms"]),
        ("Longest Consecutive Sequence", "def longest_consecutive(nums):\n    pass", "Find length of longest consecutive elements sequence.", "longest_consecutive([100, 4, 200, 1, 3, 2])", 4, ["lists", "algorithms"]),
        ("Edit Distance", "def edit_distance(word1, word2):\n    pass", "Minimum operations to convert word1 to word2.", "edit_distance('horse', 'ros')", 3, ["strings", "algorithms"]),
        ("Maximum Subarray", "def max_subarray(nums):\n    pass", "Return max sum of contiguous subarray.", "max_subarray([-2,1,-3,4,-1,2,1,-5,4])", 6, ["lists", "algorithms"]),
        ("Coin Change", "def coin_change(coins, amount):\n    pass", "Minimum coins to make amount.", "coin_change([1,2,5], 11)", 3, ["algorithms"]),
        ("Sudoku Validator", "def is_valid_sudoku(board):\n    pass", "Validate a partially filled 9x9 sudoku board. Only columns matters in this simple test.", "is_valid_sudoku([['5','3','.','.','7','.','.','.','.'],['6','.','.','1','9','5','.','.','.'],['.','9','8','.','.','.','.','6','.'],['8','.','.','.','6','.','.','.','3'],['4','.','.','8','.','3','.','.','1'],['7','.','.','.','2','.','.','.','6'],['.','6','.','.','.','.','2','8','.'],['.','.','.','4','1','9','.','.','5'],['.','.','.','.','8','.','.','7','9']])", True, ["lists", "algorithms"]),
        ("Generate Parentheses", "def generate_parentheses(n):\n    pass", "Return list of all well-formed parentheses strings.", "sorted(generate_parentheses(3))", ['((()))', '(()())', '(())()', '()(())', '()()()'], ["strings", "algorithms", "recursion"]),
        ("Permutations", "def permute(nums):\n    pass", "Return all possible permutations of list.", "sorted(permute([1,2]))", [[1,2], [2,1]], ["lists", "algorithms", "recursion"]),
        ("Subsets", "def subsets(nums):\n    pass", "Return all possible subsets.", "sorted(subsets([1,2]))", [[], [1], [1, 2], [2]], ["lists", "algorithms"]),
        ("Jump Game", "def can_jump(nums):\n    pass", "Determine if you can reach the last index.", "can_jump([2,3,1,1,4])", True, ["lists", "algorithms"]),
        ("Unique Paths", "def unique_paths(m, n):\n    pass", "Find number of unique paths in m x n grid.", "unique_paths(3, 7)", 28, ["algorithms"]),
        ("Climbing Stairs", "def climb_stairs(n):\n    pass", "Distinct ways to climb n stairs (1 or 2 steps).", "climb_stairs(3)", 3, ["algorithms"]),
        ("Search in Rotated Sorted Array", "def search(nums, target):\n    pass", "Return index of target in rotated sorted array, or -1.", "search([4,5,6,7,0,1,2], 0)", 4, ["lists", "algorithms"]),
        ("Construct String from Tree (List representation)", "def tree_to_str(lst):\n    pass", "Simply return string representation.", "tree_to_str([1,2,3])", '[1, 2, 3]', ["strings"]),
        ("Find Peak Element", "def find_peak(nums):\n    pass", "Return index of peak element.", "find_peak([1,2,3,1])", 2, ["lists", "algorithms"]),
        ("Longest Valid Parentheses", "def longest_valid(s):\n    pass", "Length of longest valid parentheses substring.", "longest_valid(')()())')", 4, ["strings", "algorithms"]),
        ("Minimum Path Sum", "def min_path_sum(grid):\n    pass", "Find path from top left to bottom right minimizing sum.", "min_path_sum([[1,3,1],[1,5,1],[4,2,1]])", 7, ["lists", "algorithms"]),
        ("Decode Ways", "def num_decodings(s):\n    pass", "Number of ways to decode digit string.", "num_decodings('226')", 3, ["strings", "algorithms"]),
        ("Wildcard Matching", "def is_match(s, p):\n    pass", "Implement wildcard matching with ? and *.", "is_match('aa', '*')", True, ["strings", "algorithms"]),
        ("N-Queens Count", "def total_n_queens(n):\n    pass", "Return number of distinct solutions to N-Queens puzzle.", "total_n_queens(4)", 2, ["algorithms", "recursion"]),
        ("Maximal Rectangle", "def maximal_rectangle(matrix):\n    pass", "Find largest rectangle of 1s in 2D binary matrix.", "maximal_rectangle([['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']])", 6, ["lists", "algorithms"]),
        ("Interleaving String", "def is_interleave(s1, s2, s3):\n    pass", "Determine if s3 is an interleaving of s1 and s2.", "is_interleave('aabcc', 'dbbca', 'aadbbcbcac')", True, ["strings", "algorithms"]),
        ("Distinct Subsequences", "def num_distinct(s, t):\n    pass", "Number of distinct subsequences of s that equal t.", "num_distinct('rabbbit', 'rabbit')", 3, ["strings", "algorithms"]),
        ("Word Ladder Length", "def ladder_length(begin, end, word_list):\n    pass", "Shortest transformation sequence from begin to end word.", "ladder_length('hit', 'cog', ['hot','dot','dog','lot','log','cog'])", 5, ["strings", "algorithms"]),
        ("Kth Largest Element", "def find_kth_largest(nums, k):\n    pass", "Find kth largest element.", "find_kth_largest([3,2,1,5,6,4], 2)", 5, ["lists", "algorithms"]),
        ("Majority Element", "def majority_element(nums):\n    pass", "Find majority element.", "majority_element([3,2,3])", 3, ["lists", "algorithms"]),
        ("Search 2D Matrix", "def search_matrix(matrix, target):\n    pass", "Search for value in 2D sorted matrix.", "search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)", True, ["lists", "algorithms"]),
        ("Rotate Image", "def rotate_image(matrix):\n    pass", "Rotate nxn matrix 90 degrees clockwise in-place, then return it.", "rotate_image([[1,2,3],[4,5,6],[7,8,9]])", [[7,4,1],[8,5,2],[9,6,3]], ["lists", "algorithms"]),
        ("Group Anagrams", "def group_anagrams(strs):\n    pass", "Group anagrams together and return list of lists.", "sorted([sorted(x) for x in group_anagrams(['eat','tea','tan','ate','nat','bat'])])", [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']], ["lists", "algorithms"]),
        ("Valid Anagram", "def is_anagram(s, t):\n    pass", "Return True if t is an anagram of s.", "is_anagram('anagram', 'nagaram')", True, ["strings"])
    ]

    all_qs = []
    
    id_counter = 1
    
    # Process easy
    for i in range(34):
        q = easy_pool[i % len(easy_pool)]
        desc = f"Scenario: {q[2]}\n\nExample Test Case:\nInput: `{q[3]}`\nExpected Output: `{q[4]}`"
        all_qs.append({
            "id": id_counter,
            "difficulty": "Easy",
            "points": 100,
            "title": q[0],
            "description": desc,
            "starter": q[1],
            "tests": [{"input": q[3], "expected": q[4]}],
            "hint": "Try writing out standard python.",
            "tags": q[5]
        })
        id_counter += 1

    for i in range(33):
        q = medium_pool[i % len(medium_pool)]
        desc = f"Scenario: {q[2]}\n\nExample Test Case:\nInput: `{q[3]}`\nExpected Output: `{q[4]}`"
        all_qs.append({
            "id": id_counter,
            "difficulty": "Medium",
            "points": 200,
            "title": q[0],
            "description": desc,
            "starter": q[1],
            "tests": [{"input": q[3], "expected": q[4]}],
            "hint": "Think about edge cases.",
            "tags": q[5]
        })
        id_counter += 1
        
    for i in range(33):
        q = hard_pool[i % len(hard_pool)]
        desc = f"Scenario: {q[2]}\n\nExample Test Case:\nInput: `{q[3]}`\nExpected Output: `{q[4]}`"
        all_qs.append({
            "id": id_counter,
            "difficulty": "Hard",
            "points": 300,
            "title": q[0],
            "description": desc,
            "starter": q[1],
            "tests": [{"input": q[3], "expected": q[4]}],
            "hint": "Optimize for time and space.",
            "tags": q[5]
        })
        id_counter += 1

    with open('app/questions.py', 'w') as f:
        f.write("QUESTIONS = ")
        f.write(pprint.pformat(all_qs, sort_dicts=False, width=120))
        f.write("\n")

if __name__ == '__main__':
    generate_questions()

QUESTIONS = [ { 'description': "Imagine you're building a calculator app. Before adding complex features, you need a simple "
                   'function that always returns a fixed number.\n'
                   '\n'
                   'Write a function `return_100` that simply returns the integer 100.\n'
                   '\n'
                   '🎯 Real-Life Use: Default values in apps, like a game starting score.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `return_100()`\n'
                   'Expected Output: `100`',
    'difficulty': 'Easy',
    'hint': 'Just use the return keyword followed by the number 100.',
    'id': 1,
    'points': 100,
    'starter': 'def return_100():\n    pass',
    'tags': ['basics'],
    'tests': [{'expected': 100, 'input': 'return_100()'}],
    'title': 'Return 100'},
  { 'description': "You're building a Twitter-like app and need to count characters in a tweet to enforce the "
                   'character limit.\n'
                   '\n'
                   'Write a function `string_length(s)` that returns the length of string `s`.\n'
                   '\n'
                   '🎯 Real-Life Use: Character counters in messaging apps.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `string_length('hello')`\n"
                   'Expected Output: `5`',
    'difficulty': 'Easy',
    'hint': 'Python has a built-in function called len() that counts characters.',
    'id': 2,
    'points': 100,
    'starter': 'def string_length(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 5, 'input': "string_length('hello')"}],
    'title': 'String Length'},
  { 'description': "A restaurant app doubles the quantity when a customer orders a 'Buy 1 Get 1' deal.\n"
                   '\n'
                   'Write a function `multiply_by_two(n)` that returns `n` multiplied by 2.\n'
                   '\n'
                   '🎯 Real-Life Use: Doubling quantities in shopping carts.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `multiply_by_two(4)`\n'
                   'Expected Output: `8`',
    'difficulty': 'Easy',
    'hint': 'Use the * operator to multiply n by 2.',
    'id': 3,
    'points': 100,
    'starter': 'def multiply_by_two(n):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': 8, 'input': 'multiply_by_two(4)'}],
    'title': 'Multiply by 2'},
  { 'description': 'In a music playlist, you want to quickly see what song plays first.\n'
                   '\n'
                   'Return the first element of the list `lst`.\n'
                   '\n'
                   '🎯 Real-Life Use: Showing the next song in a queue.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `first_element([10, 20, 30])`\n'
                   'Expected Output: `10`',
    'difficulty': 'Easy',
    'hint': 'Use index [0] to access the first item in a list.',
    'id': 4,
    'points': 100,
    'starter': 'def first_element(lst):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': 10, 'input': 'first_element([10, 20, 30])'}],
    'title': 'First Element'},
  { 'description': 'In a chat app, you want to show the most recent message, which is the last one in the list.\n'
                   '\n'
                   'Return the last element of the list `lst`.\n'
                   '\n'
                   '🎯 Real-Life Use: Showing the latest message in a conversation.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `last_element([10, 20, 30])`\n'
                   'Expected Output: `30`',
    'difficulty': 'Easy',
    'hint': 'Use index [-1] to access the last item in a list.',
    'id': 5,
    'points': 100,
    'starter': 'def last_element(lst):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': 30, 'input': 'last_element([10, 20, 30])'}],
    'title': 'Last Element'},
  { 'description': "Before displaying items in a shopping cart, you need to check if it's empty.\n"
                   '\n'
                   'Return True if list is empty, else False.\n'
                   '\n'
                   "🎯 Real-Life Use: Showing 'Your cart is empty' messages.\n"
                   '\n'
                   'Example Test Case:\n'
                   'Input: `is_empty([])`\n'
                   'Expected Output: `True`',
    'difficulty': 'Easy',
    'hint': "An empty list is 'falsy' in Python. Try: return len(lst) == 0",
    'id': 6,
    'points': 100,
    'starter': 'def is_empty(lst):\n    pass',
    'tags': ['lists', 'conditionals'],
    'tests': [{'expected': True, 'input': 'is_empty([])'}],
    'title': 'Is Empty'},
  { 'description': "A greeting card app combines a user's first name and last name.\n"
                   '\n'
                   'Return string `a` concatenated with `b`.\n'
                   '\n'
                   '🎯 Real-Life Use: Combining first and last names on profiles.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `concat_strings('a', 'b')`\n"
                   'Expected Output: `ab`',
    'difficulty': 'Easy',
    'hint': 'Use the + operator to join two strings together.',
    'id': 7,
    'points': 100,
    'starter': 'def concat_strings(a, b):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 'ab', 'input': "concat_strings('a', 'b')"}],
    'title': 'Concat Strings'},
  { 'description': "You're calculating the area of a square room for a flooring app. Area = side × side.\n"
                   '\n'
                   'Return the square of `n`.\n'
                   '\n'
                   '🎯 Real-Life Use: Area calculations in home design apps.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `square(5)`\n'
                   'Expected Output: `25`',
    'difficulty': 'Easy',
    'hint': 'Use n * n or n ** 2 to square a number.',
    'id': 8,
    'points': 100,
    'starter': 'def square(n):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': 25, 'input': 'square(5)'}],
    'title': 'Square a Number'},
  { 'description': 'A banking app needs to check if an account balance is positive before allowing a withdrawal.\n'
                   '\n'
                   'Return True if `n` is greater than 0, False otherwise.\n'
                   '\n'
                   '🎯 Real-Life Use: Balance checks before transactions.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `is_positive(5)`\n'
                   'Expected Output: `True`',
    'difficulty': 'Easy',
    'hint': 'Use a comparison: return n > 0',
    'id': 9,
    'points': 100,
    'starter': 'def is_positive(n):\n    pass',
    'tags': ['math', 'conditionals'],
    'tests': [{'expected': True, 'input': 'is_positive(5)'}],
    'title': 'Is Positive'},
  { 'description': 'A weather app flags temperatures below zero to warn users about freezing conditions.\n'
                   '\n'
                   'Return True if `n` is less than 0, False otherwise.\n'
                   '\n'
                   '🎯 Real-Life Use: Freeze warnings in weather apps.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `is_negative(-5)`\n'
                   'Expected Output: `True`',
    'difficulty': 'Easy',
    'hint': 'Use a comparison: return n < 0',
    'id': 10,
    'points': 100,
    'starter': 'def is_negative(n):\n    pass',
    'tags': ['math', 'conditionals'],
    'tests': [{'expected': True, 'input': 'is_negative(-5)'}],
    'title': 'Is Negative'},
  { 'description': 'A shopping app calculates the total when you buy two items.\n'
                   '\n'
                   'Return sum of a and b.\n'
                   '\n'
                   '🎯 Real-Life Use: Adding prices in a cart.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `sum_two(2, 3)`\n'
                   'Expected Output: `5`',
    'difficulty': 'Easy',
    'hint': 'Simply use the + operator: return a + b',
    'id': 11,
    'points': 100,
    'starter': 'def sum_two(a, b):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': 5, 'input': 'sum_two(2, 3)'}],
    'title': 'Sum of Two'},
  { 'description': 'A GPS app calculates distance, which is always positive regardless of direction.\n'
                   '\n'
                   'Return the absolute value of n.\n'
                   '\n'
                   '🎯 Real-Life Use: Distance is always positive.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `abs_val(-5)`\n'
                   'Expected Output: `5`',
    'difficulty': 'Easy',
    'hint': 'Python has a built-in abs() function.',
    'id': 12,
    'points': 100,
    'starter': 'def abs_val(n):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': 5, 'input': 'abs_val(-5)'}],
    'title': 'Absolute Value'},
  { 'description': "A contacts app filters names that start with 'A' for quick alphabetical lookup.\n"
                   '\n'
                   'Return True if string starts with A or a.\n'
                   '\n'
                   '🎯 Real-Life Use: Filtering contacts by letter.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `starts_with_a('Apple')`\n"
                   'Expected Output: `True`',
    'difficulty': 'Easy',
    'hint': "Convert the first character to lowercase and compare: s[0].lower() == 'a'",
    'id': 13,
    'points': 100,
    'starter': 'def starts_with_a(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': True, 'input': "starts_with_a('Apple')"}],
    'title': 'Starts with A'},
  { 'description': "A spell checker flags words ending with 'z' as potentially unusual.\n"
                   '\n'
                   'Return True if string ends with Z or z.\n'
                   '\n'
                   '🎯 Real-Life Use: Pattern matching in text editors.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `ends_with_z('buzz')`\n"
                   'Expected Output: `True`',
    'difficulty': 'Easy',
    'hint': "Check the last character: s[-1].lower() == 'z'",
    'id': 14,
    'points': 100,
    'starter': 'def ends_with_z(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': True, 'input': "ends_with_z('buzz')"}],
    'title': 'Ends with Z'},
  { 'description': 'An inventory system needs to quickly know how many products are in stock.\n'
                   '\n'
                   'Return the number of elements in the list.\n'
                   '\n'
                   '🎯 Real-Life Use: Counting items in an inventory.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `list_length([1,2,3])`\n'
                   'Expected Output: `3`',
    'difficulty': 'Easy',
    'hint': "Use Python's built-in len() function.",
    'id': 15,
    'points': 100,
    'starter': 'def list_length(lst):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': 3, 'input': 'list_length([1,2,3])'}],
    'title': 'List Length'},
  { 'description': 'A search feature checks if a specific product exists in the catalog.\n'
                   '\n'
                   'Return True if x is in lst.\n'
                   '\n'
                   '🎯 Real-Life Use: Checking if an item is in stock.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `contains_x([1,2,3], 2)`\n'
                   'Expected Output: `True`',
    'difficulty': 'Easy',
    'hint': "Use Python's 'in' keyword: return x in lst",
    'id': 16,
    'points': 100,
    'starter': 'def contains_x(lst, x):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': True, 'input': 'contains_x([1,2,3], 2)'}],
    'title': 'Contains X'},
  { 'description': "A banner app repeats a pattern (like '⭐') multiple times for decoration.\n"
                   '\n'
                   'Return string s repeated n times.\n'
                   '\n'
                   '🎯 Real-Life Use: Creating decorative text patterns.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `repeat_string('hi', 3)`\n"
                   'Expected Output: `hihihi`',
    'difficulty': 'Easy',
    'hint': 'Use the * operator on strings: return s * n',
    'id': 17,
    'points': 100,
    'starter': 'def repeat_string(s, n):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 'hihihi', 'input': "repeat_string('hi', 3)"}],
    'title': 'Repeat String'},
  { 'description': 'A settings app needs to list all available configuration options (dictionary keys).\n'
                   '\n'
                   'Return a list of keys in dictionary d.\n'
                   '\n'
                   '🎯 Real-Life Use: Listing all settings in an app.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `get_keys({'a':1})`\n"
                   "Expected Output: `['a']`",
    'difficulty': 'Easy',
    'hint': 'Use list(d.keys()) to get all keys as a list.',
    'id': 18,
    'points': 100,
    'starter': 'def get_keys(d):\n    pass',
    'tags': ['dicts'],
    'tests': [{'expected': ['a'], 'input': "get_keys({'a':1})"}],
    'title': 'Get Keys'},
  { 'description': "A gradebook app needs to extract just the scores (values) from a student's record.\n"
                   '\n'
                   'Return a list of values in dictionary d.\n'
                   '\n'
                   '🎯 Real-Life Use: Extracting scores from a grade sheet.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `get_values({'a':1})`\n"
                   'Expected Output: `[1]`',
    'difficulty': 'Easy',
    'hint': 'Use list(d.values()) to get all values as a list.',
    'id': 19,
    'points': 100,
    'starter': 'def get_values(d):\n    pass',
    'tags': ['dicts'],
    'tests': [{'expected': [1], 'input': "get_values({'a':1})"}],
    'title': 'Get Values'},
  { 'description': 'A seating app checks if a row number is even to assign aisle vs window seats.\n'
                   '\n'
                   'Return True if n is even.\n'
                   '\n'
                   '🎯 Real-Life Use: Alternating row assignments.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `is_even(4)`\n'
                   'Expected Output: `True`',
    'difficulty': 'Easy',
    'hint': 'A number is even if n % 2 == 0 (remainder is zero).',
    'id': 20,
    'points': 100,
    'starter': 'def is_even(n):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': True, 'input': 'is_even(4)'}],
    'title': 'Check Even'},
  { 'description': 'A game assigns bonus points only on odd-numbered rounds.\n'
                   '\n'
                   'Return True if n is odd.\n'
                   '\n'
                   '🎯 Real-Life Use: Round-based game logic.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `is_odd(5)`\n'
                   'Expected Output: `True`',
    'difficulty': 'Easy',
    'hint': 'A number is odd if n % 2 != 0.',
    'id': 21,
    'points': 100,
    'starter': 'def is_odd(n):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': True, 'input': 'is_odd(5)'}],
    'title': 'Check Odd'},
  { 'description': 'A ride-share app compares two route times and picks the faster one (larger speed = better).\n'
                   '\n'
                   'Return the larger of a and b.\n'
                   '\n'
                   '🎯 Real-Life Use: Choosing the best option from two.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `max_two(5, 10)`\n'
                   'Expected Output: `10`',
    'difficulty': 'Easy',
    'hint': "Use Python's built-in max() function or an if statement.",
    'id': 22,
    'points': 100,
    'starter': 'def max_two(a, b):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': 10, 'input': 'max_two(5, 10)'}],
    'title': 'Max of Two'},
  { 'description': 'A price comparison app finds the cheaper option between two stores.\n'
                   '\n'
                   'Return the smaller of a and b.\n'
                   '\n'
                   '🎯 Real-Life Use: Finding the best deal.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `min_two(5, 10)`\n'
                   'Expected Output: `5`',
    'difficulty': 'Easy',
    'hint': "Use Python's built-in min() function or an if statement.",
    'id': 23,
    'points': 100,
    'starter': 'def min_two(a, b):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': 5, 'input': 'min_two(5, 10)'}],
    'title': 'Min of Two'},
  { 'description': 'A chatbot greets every user by name when they log in.\n'
                   '\n'
                   "Return 'Hello ' + name.\n"
                   '\n'
                   '🎯 Real-Life Use: Personalized greetings in apps.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `hello_name('Bob')`\n"
                   'Expected Output: `Hello Bob`',
    'difficulty': 'Easy',
    'hint': "Use string concatenation: 'Hello ' + name",
    'id': 24,
    'points': 100,
    'starter': 'def hello_name(name):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 'Hello Bob', 'input': "hello_name('Bob')"}],
    'title': 'Hello Name'},
  { 'description': 'A username validator needs to check the first character of a username.\n'
                   '\n'
                   'Return first character of s.\n'
                   '\n'
                   '🎯 Real-Life Use: Validating input fields.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `first_char('cat')`\n"
                   'Expected Output: `c`',
    'difficulty': 'Easy',
    'hint': 'Access the first character with s[0].',
    'id': 25,
    'points': 100,
    'starter': 'def first_char(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 'c', 'input': "first_char('cat')"}],
    'title': 'First Char'},
  { 'description': 'A file extension checker looks at the last character of a filename.\n'
                   '\n'
                   'Return last character of s.\n'
                   '\n'
                   '🎯 Real-Life Use: Quick file type checks.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `last_char('cat')`\n"
                   'Expected Output: `t`',
    'difficulty': 'Easy',
    'hint': 'Access the last character with s[-1].',
    'id': 26,
    'points': 100,
    'starter': 'def last_char(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 't', 'input': "last_char('cat')"}],
    'title': 'Last Char'},
  { 'description': 'An alert system displays emergency messages in ALL CAPS for visibility.\n'
                   '\n'
                   'Convert string to uppercase.\n'
                   '\n'
                   '🎯 Real-Life Use: Emergency notifications.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `to_upper('cat')`\n"
                   'Expected Output: `CAT`',
    'difficulty': 'Easy',
    'hint': 'Use the .upper() string method.',
    'id': 27,
    'points': 100,
    'starter': 'def to_upper(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 'CAT', 'input': "to_upper('cat')"}],
    'title': 'To Uppercase'},
  { 'description': 'An email system normalizes addresses to lowercase for consistency.\n'
                   '\n'
                   'Convert string to lowercase.\n'
                   '\n'
                   '🎯 Real-Life Use: Email normalization.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `to_lower('CAT')`\n"
                   'Expected Output: `cat`',
    'difficulty': 'Easy',
    'hint': 'Use the .lower() string method.',
    'id': 28,
    'points': 100,
    'starter': 'def to_lower(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 'cat', 'input': "to_lower('CAT')"}],
    'title': 'To Lowercase'},
  { 'description': 'A form processor cleans up user input by removing accidental spaces.\n'
                   '\n'
                   'Remove leading and trailing spaces.\n'
                   '\n'
                   '🎯 Real-Life Use: Cleaning form inputs.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `strip_spaces('  hi  ')`\n"
                   'Expected Output: `hi`',
    'difficulty': 'Easy',
    'hint': 'Use the .strip() string method.',
    'id': 29,
    'points': 100,
    'starter': 'def strip_spaces(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 'hi', 'input': "strip_spaces('  hi  ')"}],
    'title': 'Strip Spaces'},
  { 'description': 'A password strength checker counts how many times a specific character appears.\n'
                   '\n'
                   'Count how many times char appears in s.\n'
                   '\n'
                   '🎯 Real-Life Use: Password analysis.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `count_occ('hello', 'l')`\n"
                   'Expected Output: `2`',
    'difficulty': 'Easy',
    'hint': 'Use the .count() string method.',
    'id': 30,
    'points': 100,
    'starter': 'def count_occ(s, char):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 2, 'input': "count_occ('hello', 'l')"}],
    'title': 'Count Occurrences'},
  { 'description': 'A budget app adds up all your daily expenses to show the total.\n'
                   '\n'
                   'Return sum of all numbers in list.\n'
                   '\n'
                   '🎯 Real-Life Use: Totaling expenses.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `list_sum([1,2,3])`\n'
                   'Expected Output: `6`',
    'difficulty': 'Easy',
    'hint': "Use Python's built-in sum() function.",
    'id': 31,
    'points': 100,
    'starter': 'def list_sum(lst):\n    pass',
    'tags': ['lists', 'math'],
    'tests': [{'expected': 6, 'input': 'list_sum([1,2,3])'}],
    'title': 'List Sum'},
  { 'description': 'A fitness app finds your highest score across all workouts.\n'
                   '\n'
                   'Return largest number in list.\n'
                   '\n'
                   '🎯 Real-Life Use: Finding personal records.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `list_max([1,5,2])`\n'
                   'Expected Output: `5`',
    'difficulty': 'Easy',
    'hint': "Use Python's built-in max() function.",
    'id': 32,
    'points': 100,
    'starter': 'def list_max(lst):\n    pass',
    'tags': ['lists', 'math'],
    'tests': [{'expected': 5, 'input': 'list_max([1,5,2])'}],
    'title': 'List Max'},
  { 'description': 'A weather app finds the coldest temperature of the week.\n'
                   '\n'
                   'Return smallest number in list.\n'
                   '\n'
                   '🎯 Real-Life Use: Finding minimum temperature.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `list_min([1,5,2])`\n'
                   'Expected Output: `1`',
    'difficulty': 'Easy',
    'hint': "Use Python's built-in min() function.",
    'id': 33,
    'points': 100,
    'starter': 'def list_min(lst):\n    pass',
    'tags': ['lists', 'math'],
    'tests': [{'expected': 1, 'input': 'list_min([1,5,2])'}],
    'title': 'List Min'},
  { 'description': "A social media 'Stories' feature shows posts in reverse chronological order.\n"
                   '\n'
                   'Return reversed list.\n'
                   '\n'
                   '🎯 Real-Life Use: Showing newest posts first.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `reverse_list([1,2,3])`\n'
                   'Expected Output: `[3, 2, 1]`',
    'difficulty': 'Easy',
    'hint': 'Use slicing lst[::-1] or the list .reverse() method.',
    'id': 34,
    'points': 100,
    'starter': 'def reverse_list(lst):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': [3, 2, 1], 'input': 'reverse_list([1,2,3])'}],
    'title': 'Reverse List Easy'},
  { 'description': 'An email list has duplicate addresses. Clean it up so each person gets only one email.\n'
                   '\n'
                   "Return list with duplicates removed (order doesn't matter).\n"
                   '\n'
                   '🎯 Real-Life Use: Cleaning mailing lists.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `sorted(remove_duplicates([1,2,2,3]))`\n'
                   'Expected Output: `[1, 2, 3]`',
    'difficulty': 'Medium',
    'hint': 'Convert the list to a set to remove duplicates, then back to a list.',
    'id': 35,
    'points': 200,
    'starter': 'def remove_duplicates(lst):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': [1, 2, 3], 'input': 'sorted(remove_duplicates([1,2,2,3]))'}],
    'title': 'Remove Duplicates'},
  { 'description': 'A catering company calculates how many ways to arrange dishes. For 5 dishes: 5×4×3×2×1 = 120.\n'
                   '\n'
                   'Return factorial of n (n >= 0).\n'
                   '\n'
                   '🎯 Real-Life Use: Calculating permutations for seating.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `factorial(5)`\n'
                   'Expected Output: `120`',
    'difficulty': 'Medium',
    'hint': 'Use a loop multiplying from 1 to n, or use recursion. Remember 0! = 1.',
    'id': 36,
    'points': 200,
    'starter': 'def factorial(n):\n    pass',
    'tags': ['math', 'recursion'],
    'tests': [{'expected': 120, 'input': 'factorial(5)'}],
    'title': 'Factorial'},
  { 'description': 'A language learning app counts vowels in words to help with pronunciation practice.\n'
                   '\n'
                   'Count number of vowels (a,e,i,o,u) in string.\n'
                   '\n'
                   '🎯 Real-Life Use: Pronunciation analysis.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `count_vowels('hello')`\n"
                   'Expected Output: `2`',
    'difficulty': 'Medium',
    'hint': "Loop through each character and check if it's in 'aeiouAEIOU'.",
    'id': 37,
    'points': 200,
    'starter': 'def count_vowels(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 2, 'input': "count_vowels('hello')"}],
    'title': 'Count Vowels'},
  { 'description': "A license plate reader checks if a code reads the same forwards and backwards (like 'RACECAR').\n"
                   '\n'
                   'Return True if s reads the same forward and backward.\n'
                   '\n'
                   '🎯 Real-Life Use: Detecting palindromic codes.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `is_palindrome('racecar')`\n"
                   'Expected Output: `True`',
    'difficulty': 'Medium',
    'hint': 'Compare the string to its reverse: s == s[::-1]',
    'id': 38,
    'points': 200,
    'starter': 'def is_palindrome(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': True, 'input': "is_palindrome('racecar')"}],
    'title': 'Is Palindrome'},
  { 'description': 'Fibonacci numbers model rabbit population growth — each generation is the sum of the previous '
                   'two.\n'
                   '\n'
                   'Return nth Fibonacci number (0th is 0, 1st is 1).\n'
                   '\n'
                   '🎯 Real-Life Use: Population modeling, nature patterns.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `fibonacci(5)`\n'
                   'Expected Output: `5`',
    'difficulty': 'Medium',
    'hint': 'Build up from fib(0)=0, fib(1)=1, each next = sum of previous two.',
    'id': 39,
    'points': 200,
    'starter': 'def fibonacci(n):\n    pass',
    'tags': ['math', 'recursion'],
    'tests': [{'expected': 5, 'input': 'fibonacci(5)'}],
    'title': 'Fibonacci'},
  { 'description': 'Two teams share player stats in separate dictionaries. Merge them into one master record.\n'
                   '\n'
                   'Merge two dictionaries, d2 overwrites d1 on conflict.\n'
                   '\n'
                   '🎯 Real-Life Use: Combining data from different sources.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `merge_dicts({'a':1}, {'b':2})`\n"
                   "Expected Output: `{'a': 1, 'b': 2}`",
    'difficulty': 'Medium',
    'hint': 'Create a copy of d1 with {**d1, **d2} or use d1.copy() then .update(d2).',
    'id': 40,
    'points': 200,
    'starter': 'def merge_dicts(d1, d2):\n    pass',
    'tags': ['dicts'],
    'tests': [{'expected': {'a': 1, 'b': 2}, 'input': "merge_dicts({'a':1}, {'b':2})"}],
    'title': 'Merge Two Dictionaries'},
  { 'description': "A teacher's attendance sheet has roll numbers 0 to n, but one student is missing today.\n"
                   '\n'
                   'Given list of numbers from 0 to n with one missing, find it.\n'
                   '\n'
                   '🎯 Real-Life Use: Finding missing attendance.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `missing_number([0,1,3])`\n'
                   'Expected Output: `2`',
    'difficulty': 'Medium',
    'hint': 'The expected sum is n*(n+1)/2. Subtract the actual sum to find the missing number.',
    'id': 41,
    'points': 200,
    'starter': 'def missing_number(lst):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': 2, 'input': 'missing_number([0,1,3])'}],
    'title': 'Find Missing Number'},
  { 'description': "A bank's check reader adds up all digits in an account number for verification.\n"
                   '\n'
                   'Return sum of digits of positive integer n.\n'
                   '\n'
                   '🎯 Real-Life Use: Check digit validation.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `sum_digits(123)`\n'
                   'Expected Output: `6`',
    'difficulty': 'Medium',
    'hint': 'Convert n to string, loop through each character, convert back to int and sum.',
    'id': 42,
    'points': 200,
    'starter': 'def sum_digits(n):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': 6, 'input': 'sum_digits(123)'}],
    'title': 'Sum of Digits'},
  { 'description': "A word game checks if two words use the exact same letters (like 'listen' and 'silent').\n"
                   '\n'
                   'Return True if s1 and s2 are anagrams.\n'
                   '\n'
                   '🎯 Real-Life Use: Word puzzle games like Scrabble.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `are_anagrams('listen', 'silent')`\n"
                   'Expected Output: `True`',
    'difficulty': 'Medium',
    'hint': 'Sort both strings and compare: sorted(s1) == sorted(s2)',
    'id': 43,
    'points': 200,
    'starter': 'def are_anagrams(s1, s2):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': True, 'input': "are_anagrams('listen', 'silent')"}],
    'title': 'Are Anagrams'},
  { 'description': "A teleprompter app reverses the word order so 'hello world' becomes 'world hello'.\n"
                   '\n'
                   'Reverse the order of words in string.\n'
                   '\n'
                   '🎯 Real-Life Use: Text processing tools.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `reverse_words('hello world')`\n"
                   'Expected Output: `world hello`',
    'difficulty': 'Medium',
    'hint': 'Split the string into words, reverse the list, then join back.',
    'id': 44,
    'points': 200,
    'starter': 'def reverse_words(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 'world hello', 'input': "reverse_words('hello world')"}],
    'title': 'Reverse Words'},
  { 'description': 'A reading level analyzer counts words in a sentence to estimate complexity.\n'
                   '\n'
                   'Count number of words in string separated by spaces.\n'
                   '\n'
                   '🎯 Real-Life Use: Readability scoring.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `count_words('hello world')`\n"
                   'Expected Output: `2`',
    'difficulty': 'Medium',
    'hint': 'Split the string by spaces and count the resulting list length.',
    'id': 45,
    'points': 200,
    'starter': 'def count_words(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 2, 'input': "count_words('hello world')"}],
    'title': 'Count Words'},
  { 'description': 'A keyboard app suggests the most-typed letter to optimize key placement.\n'
                   '\n'
                   'Return the character that appears most often.\n'
                   '\n'
                   '🎯 Real-Life Use: Keyboard optimization.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `most_frequent('hello')`\n"
                   'Expected Output: `l`',
    'difficulty': 'Medium',
    'hint': 'Use a dictionary to count occurrences, then find the max.',
    'id': 46,
    'points': 200,
    'starter': 'def most_frequent(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 'l', 'input': "most_frequent('hello')"}],
    'title': 'Most Frequent Char'},
  { 'description': 'Two friend groups want to find people they have in common for a party invite.\n'
                   '\n'
                   'Return common elements in both lists.\n'
                   '\n'
                   '🎯 Real-Life Use: Finding mutual friends.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `sorted(intersection([1,2,3], [2,3,4]))`\n'
                   'Expected Output: `[2, 3]`',
    'difficulty': 'Medium',
    'hint': 'Convert both lists to sets and use the & operator or .intersection().',
    'id': 47,
    'points': 200,
    'starter': 'def intersection(l1, l2):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': [2, 3], 'input': 'sorted(intersection([1,2,3], [2,3,4]))'}],
    'title': 'Intersection of Lists'},
  { 'description': "A music app finds songs in your library that aren't in your friend's playlist.\n"
                   '\n'
                   'Return elements in l1 not in l2.\n'
                   '\n'
                   '🎯 Real-Life Use: Finding unique songs.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `sorted(difference([1,2,3], [2,3,4]))`\n'
                   'Expected Output: `[1]`',
    'difficulty': 'Medium',
    'hint': 'Convert to sets and use the - operator or .difference().',
    'id': 48,
    'points': 200,
    'starter': 'def difference(l1, l2):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': [1], 'input': 'sorted(difference([1,2,3], [2,3,4]))'}],
    'title': 'Difference of Lists'},
  { 'description': 'An email app has folders within folders. Flatten them into one big list of all emails.\n'
                   '\n'
                   'Flatten a 2D list into a 1D list.\n'
                   '\n'
                   '🎯 Real-Life Use: Merging nested data.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `flatten([[1,2], [3]])`\n'
                   'Expected Output: `[1, 2, 3]`',
    'difficulty': 'Medium',
    'hint': 'Use a list comprehension: [item for sublist in lst for item in sublist]',
    'id': 49,
    'points': 200,
    'starter': 'def flatten(lst):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': [1, 2, 3], 'input': 'flatten([[1,2], [3]])'}],
    'title': 'Flatten List'},
  { 'description': 'A leaderboard sorts players by their scores, showing the lowest scorer first.\n'
                   '\n'
                   'Return list of keys sorted by their ascending values.\n'
                   '\n'
                   '🎯 Real-Life Use: Ranking systems.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `sort_dict({'a':3, 'b':1, 'c':2})`\n"
                   "Expected Output: `['b', 'c', 'a']`",
    'difficulty': 'Medium',
    'hint': 'Use sorted() with a key function: sorted(d, key=lambda k: d[k])',
    'id': 50,
    'points': 200,
    'starter': 'def sort_dict(d):\n    pass',
    'tags': ['dicts', 'algorithms'],
    'tests': [{'expected': ['b', 'c', 'a'], 'input': "sort_dict({'a':3, 'b':1, 'c':2})"}],
    'title': 'Sort Dictionary by Value'},
  { 'description': 'A news app formats headlines in Title Case for a professional look.\n'
                   '\n'
                   'Capitalize first letter of every word.\n'
                   '\n'
                   '🎯 Real-Life Use: Formatting headlines.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `title_case('hello world')`\n"
                   'Expected Output: `Hello World`',
    'difficulty': 'Medium',
    'hint': 'Use the .title() string method.',
    'id': 51,
    'points': 200,
    'starter': 'def title_case(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 'Hello World', 'input': "title_case('hello world')"}],
    'title': 'Title Case'},
  { 'description': 'A computer science student is building a tool that converts binary code to regular numbers.\n'
                   '\n'
                   'Convert binary string to integer.\n'
                   '\n'
                   '🎯 Real-Life Use: Understanding how computers store data.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `bin_to_dec('101')`\n"
                   'Expected Output: `5`',
    'difficulty': 'Medium',
    'hint': 'Use int(b, 2) to convert from binary string to decimal.',
    'id': 52,
    'points': 200,
    'starter': 'def bin_to_dec(b):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': 5, 'input': "bin_to_dec('101')"}],
    'title': 'Binary to Decimal'},
  { 'description': 'A math tutor app generates a list of prime numbers for practice problems.\n'
                   '\n'
                   'Return list of prime numbers up to n.\n'
                   '\n'
                   '🎯 Real-Life Use: Educational math tools.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `get_primes(10)`\n'
                   'Expected Output: `[2, 3, 5, 7]`',
    'difficulty': 'Medium',
    'hint': 'Check each number from 2 to n: a number is prime if no smaller number divides it evenly.',
    'id': 53,
    'points': 200,
    'starter': 'def get_primes(n):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': [2, 3, 5, 7], 'input': 'get_primes(10)'}],
    'title': 'List of Primes'},
  { 'description': 'A recipe app scales ingredients. To simplify fractions like 12/8, you need their GCD (4), giving '
                   '3/2.\n'
                   '\n'
                   'Return greatest common divisor of a and b.\n'
                   '\n'
                   '🎯 Real-Life Use: Simplifying fractions.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `gcd(12, 8)`\n'
                   'Expected Output: `4`',
    'difficulty': 'Medium',
    'hint': 'Use the Euclidean algorithm: repeatedly do b, a%b until b is 0.',
    'id': 54,
    'points': 200,
    'starter': 'def gcd(a, b):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': 4, 'input': 'gcd(12, 8)'}],
    'title': 'GCD'},
  { 'description': 'A scheduling app finds the earliest time two events can repeat together (like buses arriving every '
                   '4 and 6 minutes).\n'
                   '\n'
                   'Return least common multiple of a and b.\n'
                   '\n'
                   '🎯 Real-Life Use: Scheduling synchronization.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `lcm(4, 6)`\n'
                   'Expected Output: `12`',
    'difficulty': 'Medium',
    'hint': 'LCM = (a * b) // GCD(a, b). Calculate GCD first.',
    'id': 55,
    'points': 200,
    'starter': 'def lcm(a, b):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': 12, 'input': 'lcm(4, 6)'}],
    'title': 'LCM'},
  { 'description': 'A spreadsheet app swaps rows and columns in a data table.\n'
                   '\n'
                   'Return transposed 2D list.\n'
                   '\n'
                   '🎯 Real-Life Use: Pivoting data in spreadsheets.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `transpose([[1,2], [3,4]])`\n'
                   'Expected Output: `[[1, 3], [2, 4]]`',
    'difficulty': 'Medium',
    'hint': 'Use zip(*matrix) and convert each tuple to a list.',
    'id': 56,
    'points': 200,
    'starter': 'def transpose(matrix):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': [[1, 3], [2, 4]], 'input': 'transpose([[1,2], [3,4]])'}],
    'title': 'Matrix Transpose'},
  { 'description': 'A competition app needs to find the runner-up (2nd place) score.\n'
                   '\n'
                   'Find second largest number in list.\n'
                   '\n'
                   '🎯 Real-Life Use: Determining runner-up in competitions.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `second_largest([1, 5, 3, 4])`\n'
                   'Expected Output: `4`',
    'difficulty': 'Medium',
    'hint': 'Sort the unique values and pick the second from the end.',
    'id': 57,
    'points': 200,
    'starter': 'def second_largest(lst):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': 4, 'input': 'second_largest([1, 5, 3, 4])'}],
    'title': 'Second Largest'},
  { 'description': "A text filter removes vowels from words to create fun abbreviations (like 'hll' from 'hello').\n"
                   '\n'
                   'Return string without vowels.\n'
                   '\n'
                   '🎯 Real-Life Use: Text abbreviation generators.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `remove_vowels('hello')`\n"
                   'Expected Output: `hll`',
    'difficulty': 'Medium',
    'hint': 'Loop through characters and keep only non-vowels.',
    'id': 58,
    'points': 200,
    'starter': 'def remove_vowels(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 'hll', 'input': "remove_vowels('hello')"}],
    'title': 'Remove Vowels'},
  { 'description': 'A database maps column names to their values — built from two parallel lists.\n'
                   '\n'
                   'Create dict from list of keys and values.\n'
                   '\n'
                   '🎯 Real-Life Use: Building records from CSV headers and rows.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `to_dict(['a','b'], [1,2])`\n"
                   "Expected Output: `{'a': 1, 'b': 2}`",
    'difficulty': 'Medium',
    'hint': 'Use dict(zip(keys, values)).',
    'id': 59,
    'points': 200,
    'starter': 'def to_dict(keys, values):\n    pass',
    'tags': ['dicts', 'lists'],
    'tests': [{'expected': {'a': 1, 'b': 2}, 'input': "to_dict(['a','b'], [1,2])"}],
    'title': 'Dict from two lists'},
  { 'description': "A cashier needs to find two items in a price list that add up to a customer's exact budget.\n"
                   '\n'
                   'Find two numbers in list that add up to target, return as sorted tuple. Return None if none.\n'
                   '\n'
                   '🎯 Real-Life Use: Budget matching.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `find_pairs([1,2,3,4], 5)`\n'
                   'Expected Output: `(1, 4)`',
    'difficulty': 'Medium',
    'hint': 'Use a set to track seen numbers. For each num, check if target-num exists.',
    'id': 60,
    'points': 200,
    'starter': 'def find_pairs(lst, target):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': (1, 4), 'input': 'find_pairs([1,2,3,4], 5)'}],
    'title': 'Find Pairs'},
  { 'description': 'A delivery app verifies that package weights are arranged from lightest to heaviest.\n'
                   '\n'
                   'Return True if list is sorted in ascending order.\n'
                   '\n'
                   '🎯 Real-Life Use: Verifying sorted data.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `is_sorted([1,2,3])`\n'
                   'Expected Output: `True`',
    'difficulty': 'Medium',
    'hint': 'Compare the list to sorted(lst), or check each pair of adjacent elements.',
    'id': 61,
    'points': 200,
    'starter': 'def is_sorted(lst):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': True, 'input': 'is_sorted([1,2,3])'}],
    'title': 'Is Sorted'},
  { 'description': 'A carousel display rotates images so the last few move to the front.\n'
                   '\n'
                   'Rotate list to the right by k steps.\n'
                   '\n'
                   '🎯 Real-Life Use: Image carousel rotation.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `rotate([1,2,3,4,5], 2)`\n'
                   'Expected Output: `[4, 5, 1, 2, 3]`',
    'difficulty': 'Medium',
    'hint': 'Use slicing: lst[-k:] + lst[:-k]. Handle k > len with k % len.',
    'id': 62,
    'points': 200,
    'starter': 'def rotate(lst, k):\n    pass',
    'tags': ['lists'],
    'tests': [{'expected': [4, 5, 1, 2, 3], 'input': 'rotate([1,2,3,4,5], 2)'}],
    'title': 'Rotate List'},
  { 'description': 'A DNA sequencer checks if a short pattern appears (in order) within a longer DNA strand.\n'
                   '\n'
                   'Return True if s1 is a subsequence of s2.\n'
                   '\n'
                   '🎯 Real-Life Use: DNA sequence matching.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `is_subsequence('abc', 'ahbgdc')`\n"
                   'Expected Output: `True`',
    'difficulty': 'Medium',
    'hint': "Use two pointers — one for each string. Move through s2 and advance s1's pointer on match.",
    'id': 63,
    'points': 200,
    'starter': 'def is_subsequence(s1, s2):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': True, 'input': "is_subsequence('abc', 'ahbgdc')"}],
    'title': 'Check Subsequence'},
  { 'description': 'A fancy text generator alternates between uppercase and lowercase for stylish social media posts.\n'
                   '\n'
                   'Capitalize alternate letters.\n'
                   '\n'
                   '🎯 Real-Life Use: Aesthetic text generators.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `alt_caps('hello')`\n"
                   'Expected Output: `HeLlO`',
    'difficulty': 'Medium',
    'hint': 'Loop with enumerate. Even index = upper, odd index = lower.',
    'id': 64,
    'points': 200,
    'starter': 'def alt_caps(s):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 'HeLlO', 'input': "alt_caps('hello')"}],
    'title': 'Capitalize Alternate Matrix'},
  { 'description': "A networking tool counts the number of '1' bits in a binary IP address.\n"
                   '\n'
                   'Return number of 1s in binary representation of n.\n'
                   '\n'
                   '🎯 Real-Life Use: Network subnet calculations.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `count_bits(5)`\n'
                   'Expected Output: `2`',
    'difficulty': 'Medium',
    'hint': "Convert to binary string with bin(n) and count '1' characters.",
    'id': 65,
    'points': 200,
    'starter': 'def count_bits(n):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': 2, 'input': 'count_bits(5)'}],
    'title': 'Count Bits'},
  { 'description': 'A memory manager checks if a block size is a power of 2 for optimal allocation.\n'
                   '\n'
                   'Return True if n is power of two.\n'
                   '\n'
                   '🎯 Real-Life Use: Memory allocation optimization.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `is_power_of_two(8)`\n'
                   'Expected Output: `True`',
    'difficulty': 'Medium',
    'hint': "A power of 2 has exactly one '1' bit: n > 0 and n & (n-1) == 0.",
    'id': 66,
    'points': 200,
    'starter': 'def is_power_of_two(n):\n    pass',
    'tags': ['math'],
    'tests': [{'expected': True, 'input': 'is_power_of_two(8)'}],
    'title': 'Is Power of Two'},
  { 'description': 'A dictionary app groups words that are anagrams of each other. Just count how many groups there '
                   'are.\n'
                   '\n'
                   'Group anagrams together and return the count of groups.\n'
                   '\n'
                   '🎯 Real-Life Use: Word game scoring.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `group_anagrams_medium(['eat', 'tea', 'tan'])`\n"
                   'Expected Output: `2`',
    'difficulty': 'Medium',
    'hint': "Sort each word's letters as a key, group by that key, count groups.",
    'id': 67,
    'points': 200,
    'starter': 'def group_anagrams_medium(strs):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': 2, 'input': "group_anagrams_medium(['eat', 'tea', 'tan'])"}],
    'title': 'Group Anagrams Medium'},
  { 'description': "A text editor's 'Find' feature highlights the longest palindromic word or phrase in your "
                   'document.\n'
                   '\n'
                   'Return the longest palindromic substring.\n'
                   '\n'
                   '🎯 Real-Life Use: Text pattern analysis.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `longest_palindrome('babad') in ['bab', 'aba']`\n"
                   'Expected Output: `True`',
    'difficulty': 'Hard',
    'hint': 'Expand around each center (character and between characters) to find palindromes.',
    'id': 68,
    'points': 300,
    'starter': 'def longest_palindrome(s):\n    pass',
    'tags': ['strings', 'algorithms'],
    'tests': [{'expected': True, 'input': "longest_palindrome('babad') in ['bab', 'aba']"}],
    'title': 'Longest Palindromic Substring'},
  { 'description': 'A calendar app merges overlapping meetings so your schedule looks clean.\n'
                   '\n'
                   'Merge overlapping intervals.\n'
                   '\n'
                   '🎯 Real-Life Use: Calendar conflict resolution.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `merge_intervals([[1,3],[2,6],[8,10]])`\n'
                   'Expected Output: `[[1, 6], [8, 10]]`',
    'difficulty': 'Hard',
    'hint': 'Sort by start time, then merge if current interval overlaps with the last merged one.',
    'id': 69,
    'points': 300,
    'starter': 'def merge_intervals(intervals):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': [[1, 6], [8, 10]], 'input': 'merge_intervals([[1,3],[2,6],[8,10]])'}],
    'title': 'Merge Intervals'},
  { 'description': 'After rain, water collects between buildings of different heights. Calculate total trapped water.\n'
                   '\n'
                   'Calculate how much water can be trapped after raining.\n'
                   '\n'
                   '🎯 Real-Life Use: Civil engineering drainage planning.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `trap([0,1,0,2,1,0,1,3,2,1,2,1])`\n'
                   'Expected Output: `6`',
    'difficulty': 'Hard',
    'hint': 'For each position, water = min(max_left, max_right) - height. Pre-compute max arrays.',
    'id': 70,
    'points': 300,
    'starter': 'def trap(heights):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': 6, 'input': 'trap([0,1,0,2,1,0,1,3,2,1,2,1])'}],
    'title': 'Trapping Rain Water'},
  { 'description': 'An autocomplete system checks if a typed string can be broken into valid dictionary words.\n'
                   '\n'
                   'Return True if string can be segmented into dictionary words.\n'
                   '\n'
                   '🎯 Real-Life Use: Spell checkers and autocomplete.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `word_break('leetcode', ['leet', 'code'])`\n"
                   'Expected Output: `True`',
    'difficulty': 'Hard',
    'hint': 'Use dynamic programming: dp[i] = True if s[:i] can be segmented.',
    'id': 71,
    'points': 300,
    'starter': 'def word_break(s, word_dict):\n    pass',
    'tags': ['strings', 'algorithms'],
    'tests': [{'expected': True, 'input': "word_break('leetcode', ['leet', 'code'])"}],
    'title': 'Word Break'},
  { 'description': 'A historian discovers scattered years in records and wants the longest streak of consecutive '
                   'years.\n'
                   '\n'
                   'Find length of longest consecutive elements sequence.\n'
                   '\n'
                   '🎯 Real-Life Use: Finding patterns in historical data.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `longest_consecutive([100, 4, 200, 1, 3, 2])`\n'
                   'Expected Output: `4`',
    'difficulty': 'Hard',
    'hint': "Use a set. For each number that's a sequence start (n-1 not in set), count the streak.",
    'id': 72,
    'points': 300,
    'starter': 'def longest_consecutive(nums):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': 4, 'input': 'longest_consecutive([100, 4, 200, 1, 3, 2])'}],
    'title': 'Longest Consecutive Sequence'},
  { 'description': 'An autocorrect feature calculates the minimum edits (insert, delete, replace) to fix a typo.\n'
                   '\n'
                   'Minimum operations to convert word1 to word2.\n'
                   '\n'
                   '🎯 Real-Life Use: Spell check suggestions.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `edit_distance('horse', 'ros')`\n"
                   'Expected Output: `3`',
    'difficulty': 'Hard',
    'hint': 'Use a 2D DP table. Compare characters and take min of insert, delete, replace.',
    'id': 73,
    'points': 300,
    'starter': 'def edit_distance(word1, word2):\n    pass',
    'tags': ['strings', 'algorithms'],
    'tests': [{'expected': 3, 'input': "edit_distance('horse', 'ros')"}],
    'title': 'Edit Distance'},
  { 'description': 'A stock trader wants to find the best consecutive days of profit to maximize returns.\n'
                   '\n'
                   'Return max sum of contiguous subarray.\n'
                   '\n'
                   '🎯 Real-Life Use: Stock market analysis.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `max_subarray([-2,1,-3,4,-1,2,1,-5,4])`\n'
                   'Expected Output: `6`',
    'difficulty': 'Hard',
    'hint': "Use Kadane's algorithm: track current sum and max sum. Reset current if it goes negative.",
    'id': 74,
    'points': 300,
    'starter': 'def max_subarray(nums):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': 6, 'input': 'max_subarray([-2,1,-3,4,-1,2,1,-5,4])'}],
    'title': 'Maximum Subarray'},
  { 'description': 'A vending machine needs to give change using the fewest coins possible.\n'
                   '\n'
                   'Minimum coins to make amount.\n'
                   '\n'
                   '🎯 Real-Life Use: Optimal change-making.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `coin_change([1,2,5], 11)`\n'
                   'Expected Output: `3`',
    'difficulty': 'Hard',
    'hint': 'Use DP: dp[i] = min coins for amount i. Try each coin denomination.',
    'id': 75,
    'points': 300,
    'starter': 'def coin_change(coins, amount):\n    pass',
    'tags': ['algorithms'],
    'tests': [{'expected': 3, 'input': 'coin_change([1,2,5], 11)'}],
    'title': 'Coin Change'},
  { 'description': 'A puzzle game validates if a partially filled Sudoku board follows the rules.\n'
                   '\n'
                   'Validate a partially filled 9x9 sudoku board.\n'
                   '\n'
                   '🎯 Real-Life Use: Sudoku game validation.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: '
                   "`is_valid_sudoku([['5','3','.','.','7','.','.','.','.'],['6','.','.','1','9','5','.','.','.'],['.','9','8','.','.','.','.','6','.'],['8','.','.','.','6','.','.','.','3'],['4','.','.','8','.','3','.','.','1'],['7','.','.','.','2','.','.','.','6'],['.','6','.','.','.','.','2','8','.'],['.','.','.','4','1','9','.','.','5'],['.','.','.','.','8','.','.','7','9']])`\n"
                   'Expected Output: `True`',
    'difficulty': 'Hard',
    'hint': 'Check each row, column, and 3x3 box for duplicate non-dot values using sets.',
    'id': 76,
    'points': 300,
    'starter': 'def is_valid_sudoku(board):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [ { 'expected': True,
                 'input': "is_valid_sudoku([['5','3','.','.','7','.','.','.','.'],['6','.','.','1','9','5','.','.','.'],['.','9','8','.','.','.','.','6','.'],['8','.','.','.','6','.','.','.','3'],['4','.','.','8','.','3','.','.','1'],['7','.','.','.','2','.','.','.','6'],['.','6','.','.','.','.','2','8','.'],['.','.','.','4','1','9','.','.','5'],['.','.','.','.','8','.','.','7','9']])"}],
    'title': 'Sudoku Validator'},
  { 'description': 'A math tool generates all valid combinations of balanced parentheses for teaching.\n'
                   '\n'
                   'Return list of all well-formed parentheses strings.\n'
                   '\n'
                   '🎯 Real-Life Use: Teaching combinatorics.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `sorted(generate_parentheses(3))`\n'
                   "Expected Output: `['((()))', '(()())', '(())()', '()(())', '()()()']`",
    'difficulty': 'Hard',
    'hint': "Use recursion/backtracking: add '(' if open < n, add ')' if close < open.",
    'id': 77,
    'points': 300,
    'starter': 'def generate_parentheses(n):\n    pass',
    'tags': ['strings', 'algorithms', 'recursion'],
    'tests': [ { 'expected': ['((()))', '(()())', '(())()', '()(())', '()()()'],
                 'input': 'sorted(generate_parentheses(3))'}],
    'title': 'Generate Parentheses'},
  { 'description': 'A travel planner finds every possible order to visit a set of cities.\n'
                   '\n'
                   'Return all possible permutations of list.\n'
                   '\n'
                   '🎯 Real-Life Use: Route planning.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `sorted(permute([1,2]))`\n'
                   'Expected Output: `[[1, 2], [2, 1]]`',
    'difficulty': 'Hard',
    'hint': 'Use recursion: fix one element, permute the rest. Or use itertools.permutations.',
    'id': 78,
    'points': 300,
    'starter': 'def permute(nums):\n    pass',
    'tags': ['lists', 'algorithms', 'recursion'],
    'tests': [{'expected': [[1, 2], [2, 1]], 'input': 'sorted(permute([1,2]))'}],
    'title': 'Permutations'},
  { 'description': 'A meal planner generates every possible combination of dishes from a menu.\n'
                   '\n'
                   'Return all possible subsets.\n'
                   '\n'
                   '🎯 Real-Life Use: Combination generators.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `sorted(subsets([1,2]))`\n'
                   'Expected Output: `[[], [1], [1, 2], [2]]`',
    'difficulty': 'Hard',
    'hint': 'Use backtracking or iterative approach: for each element, add it to all existing subsets.',
    'id': 79,
    'points': 300,
    'starter': 'def subsets(nums):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': [[], [1], [1, 2], [2]], 'input': 'sorted(subsets([1,2]))'}],
    'title': 'Subsets'},
  { 'description': 'A frog wants to reach the end of a pond by jumping on lily pads. Each pad tells max jump '
                   'distance.\n'
                   '\n'
                   'Determine if you can reach the last index.\n'
                   '\n'
                   '🎯 Real-Life Use: Game level reachability.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `can_jump([2,3,1,1,4])`\n'
                   'Expected Output: `True`',
    'difficulty': 'Hard',
    'hint': 'Track the farthest reachable index. If current > farthest, return False.',
    'id': 80,
    'points': 300,
    'starter': 'def can_jump(nums):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': True, 'input': 'can_jump([2,3,1,1,4])'}],
    'title': 'Jump Game'},
  { 'description': 'A delivery robot can only move right or down in a grid. Count all possible routes.\n'
                   '\n'
                   'Find number of unique paths in m x n grid.\n'
                   '\n'
                   '🎯 Real-Life Use: Robot path planning.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `unique_paths(3, 7)`\n'
                   'Expected Output: `28`',
    'difficulty': 'Hard',
    'hint': 'Use DP: dp[i][j] = dp[i-1][j] + dp[i][j-1]. First row and column are all 1s.',
    'id': 81,
    'points': 300,
    'starter': 'def unique_paths(m, n):\n    pass',
    'tags': ['algorithms'],
    'tests': [{'expected': 28, 'input': 'unique_paths(3, 7)'}],
    'title': 'Unique Paths'},
  { 'description': "You're climbing a staircase and can take 1 or 2 steps at a time. How many distinct ways to reach "
                   'the top?\n'
                   '\n'
                   'Distinct ways to climb n stairs (1 or 2 steps).\n'
                   '\n'
                   '🎯 Real-Life Use: Counting possibilities in step-based games.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `climb_stairs(3)`\n'
                   'Expected Output: `3`',
    'difficulty': 'Hard',
    'hint': 'This is the Fibonacci pattern! ways(n) = ways(n-1) + ways(n-2).',
    'id': 82,
    'points': 300,
    'starter': 'def climb_stairs(n):\n    pass',
    'tags': ['algorithms'],
    'tests': [{'expected': 3, 'input': 'climb_stairs(3)'}],
    'title': 'Climbing Stairs'},
  { 'description': 'A sorted phone book got shuffled (rotated). Find a specific contact quickly.\n'
                   '\n'
                   'Return index of target in rotated sorted array, or -1.\n'
                   '\n'
                   '🎯 Real-Life Use: Searching in rotated datasets.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `search([4,5,6,7,0,1,2], 0)`\n'
                   'Expected Output: `4`',
    'difficulty': 'Hard',
    'hint': 'Use modified binary search: determine which half is sorted, then decide which half to search.',
    'id': 83,
    'points': 300,
    'starter': 'def search(nums, target):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': 4, 'input': 'search([4,5,6,7,0,1,2], 0)'}],
    'title': 'Search in Rotated Sorted Array'},
  { 'description': 'A data logger converts a list of sensor readings into a formatted string.\n'
                   '\n'
                   'Simply return string representation.\n'
                   '\n'
                   '🎯 Real-Life Use: Data formatting for display.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `tree_to_str([1,2,3])`\n'
                   'Expected Output: `[1, 2, 3]`',
    'difficulty': 'Hard',
    'hint': 'Use str() to convert the list to its string representation.',
    'id': 84,
    'points': 300,
    'starter': 'def tree_to_str(lst):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': '[1, 2, 3]', 'input': 'tree_to_str([1,2,3])'}],
    'title': 'Construct String from Tree (List representation)'},
  { 'description': 'A hiking app finds the highest point (peak) along a trail profile.\n'
                   '\n'
                   'Return index of peak element.\n'
                   '\n'
                   '🎯 Real-Life Use: Finding mountain peaks in elevation data.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `find_peak([1,2,3,1])`\n'
                   'Expected Output: `2`',
    'difficulty': 'Hard',
    'hint': 'Use binary search: if mid < mid+1, peak is to the right; otherwise to the left.',
    'id': 85,
    'points': 300,
    'starter': 'def find_peak(nums):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': 2, 'input': 'find_peak([1,2,3,1])'}],
    'title': 'Find Peak Element'},
  { 'description': 'A code validator checks the longest stretch of properly matched brackets in source code.\n'
                   '\n'
                   'Length of longest valid parentheses substring.\n'
                   '\n'
                   '🎯 Real-Life Use: Code syntax validation.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `longest_valid(')()())')`\n"
                   'Expected Output: `4`',
    'difficulty': 'Hard',
    'hint': 'Use a stack to track indices of unmatched parentheses.',
    'id': 86,
    'points': 300,
    'starter': 'def longest_valid(s):\n    pass',
    'tags': ['strings', 'algorithms'],
    'tests': [{'expected': 4, 'input': "longest_valid(')()())')"}],
    'title': 'Longest Valid Parentheses'},
  { 'description': 'A GPS finds the path through a city grid (top-left to bottom-right) that minimizes total toll '
                   'costs.\n'
                   '\n'
                   'Find path from top left to bottom right minimizing sum.\n'
                   '\n'
                   '🎯 Real-Life Use: Optimal route with tolls.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `min_path_sum([[1,3,1],[1,5,1],[4,2,1]])`\n'
                   'Expected Output: `7`',
    'difficulty': 'Hard',
    'hint': 'Use DP: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1]).',
    'id': 87,
    'points': 300,
    'starter': 'def min_path_sum(grid):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': 7, 'input': 'min_path_sum([[1,3,1],[1,5,1],[4,2,1]])'}],
    'title': 'Minimum Path Sum'},
  { 'description': 'A spy decoder figures out how many ways a numeric code can be translated to letters (1=A, 2=B, '
                   '..., 26=Z).\n'
                   '\n'
                   'Number of ways to decode digit string.\n'
                   '\n'
                   '🎯 Real-Life Use: Cryptographic decoding.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `num_decodings('226')`\n"
                   'Expected Output: `3`',
    'difficulty': 'Hard',
    'hint': 'Use DP: single digit (1-9) and double digit (10-26) contribute to count.',
    'id': 88,
    'points': 300,
    'starter': 'def num_decodings(s):\n    pass',
    'tags': ['strings', 'algorithms'],
    'tests': [{'expected': 3, 'input': "num_decodings('226')"}],
    'title': 'Decode Ways'},
  { 'description': "A file search tool uses wildcards: '?' matches any single character, '*' matches any sequence.\n"
                   '\n'
                   'Implement wildcard matching with ? and *.\n'
                   '\n'
                   '🎯 Real-Life Use: File search patterns (*.txt, photo_?.jpg).\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `is_match('aa', '*')`\n"
                   'Expected Output: `True`',
    'difficulty': 'Hard',
    'hint': "Use DP: dp[i][j] = does s[:i] match p[:j]. Handle '*' specially.",
    'id': 89,
    'points': 300,
    'starter': 'def is_match(s, p):\n    pass',
    'tags': ['strings', 'algorithms'],
    'tests': [{'expected': True, 'input': "is_match('aa', '*')"}],
    'title': 'Wildcard Matching'},
  { 'description': 'A chess tournament organizer needs to place N queens on an N×N board so none attack each other.\n'
                   '\n'
                   'Return number of distinct solutions to N-Queens puzzle.\n'
                   '\n'
                   '🎯 Real-Life Use: Constraint satisfaction problems.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `total_n_queens(4)`\n'
                   'Expected Output: `2`',
    'difficulty': 'Hard',
    'hint': 'Use backtracking: place queens row by row, checking column and diagonal conflicts.',
    'id': 90,
    'points': 300,
    'starter': 'def total_n_queens(n):\n    pass',
    'tags': ['algorithms', 'recursion'],
    'tests': [{'expected': 2, 'input': 'total_n_queens(4)'}],
    'title': 'N-Queens Count'},
  { 'description': 'An architect finds the largest rectangular room that fits in an irregular building floor plan.\n'
                   '\n'
                   'Find largest rectangle of 1s in 2D binary matrix.\n'
                   '\n'
                   '🎯 Real-Life Use: Maximizing usable space.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: '
                   "`maximal_rectangle([['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']])`\n"
                   'Expected Output: `6`',
    'difficulty': 'Hard',
    'hint': 'Build histogram heights per row, then use largest rectangle in histogram algorithm.',
    'id': 91,
    'points': 300,
    'starter': 'def maximal_rectangle(matrix):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [ { 'expected': 6,
                 'input': "maximal_rectangle([['1','0','1','0','0'],['1','0','1','1','1'],['1','1','1','1','1'],['1','0','0','1','0']])"}],
    'title': 'Maximal Rectangle'},
  { 'description': 'A playlist mixer checks if a combined playlist could have been made by interleaving two original '
                   'playlists in order.\n'
                   '\n'
                   'Determine if s3 is an interleaving of s1 and s2.\n'
                   '\n'
                   '🎯 Real-Life Use: Merge verification.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `is_interleave('aabcc', 'dbbca', 'aadbbcbcac')`\n"
                   'Expected Output: `True`',
    'difficulty': 'Hard',
    'hint': 'Use 2D DP: dp[i][j] = can s1[:i] and s2[:j] form s3[:i+j].',
    'id': 92,
    'points': 300,
    'starter': 'def is_interleave(s1, s2, s3):\n    pass',
    'tags': ['strings', 'algorithms'],
    'tests': [{'expected': True, 'input': "is_interleave('aabcc', 'dbbca', 'aadbbcbcac')"}],
    'title': 'Interleaving String'},
  { 'description': 'A genetics lab counts how many ways a short DNA pattern appears as a subsequence in a longer '
                   'strand.\n'
                   '\n'
                   'Number of distinct subsequences of s that equal t.\n'
                   '\n'
                   '🎯 Real-Life Use: Gene pattern counting.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `num_distinct('rabbbit', 'rabbit')`\n"
                   'Expected Output: `3`',
    'difficulty': 'Hard',
    'hint': 'Use 2D DP: dp[i][j] = number of ways to form t[:j] from s[:i].',
    'id': 93,
    'points': 300,
    'starter': 'def num_distinct(s, t):\n    pass',
    'tags': ['strings', 'algorithms'],
    'tests': [{'expected': 3, 'input': "num_distinct('rabbbit', 'rabbit')"}],
    'title': 'Distinct Subsequences'},
  { 'description': 'A network router finds the shortest chain of one-letter-changes to transform one word into '
                   'another.\n'
                   '\n'
                   'Shortest transformation sequence from begin to end word.\n'
                   '\n'
                   '🎯 Real-Life Use: Network routing algorithms.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `ladder_length('hit', 'cog', ['hot','dot','dog','lot','log','cog'])`\n"
                   'Expected Output: `5`',
    'difficulty': 'Hard',
    'hint': 'Use BFS: each level changes one letter. Try all 26 letters at each position.',
    'id': 94,
    'points': 300,
    'starter': 'def ladder_length(begin, end, word_list):\n    pass',
    'tags': ['strings', 'algorithms'],
    'tests': [{'expected': 5, 'input': "ladder_length('hit', 'cog', ['hot','dot','dog','lot','log','cog'])"}],
    'title': 'Word Ladder Length'},
  { 'description': 'A sports app quickly finds the silver medalist (2nd highest) score from a list of results.\n'
                   '\n'
                   'Find kth largest element.\n'
                   '\n'
                   '🎯 Real-Life Use: Ranking athletes.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `find_kth_largest([3,2,1,5,6,4], 2)`\n'
                   'Expected Output: `5`',
    'difficulty': 'Hard',
    'hint': 'Sort and pick, or use a heap for efficiency: sorted(nums)[-k]',
    'id': 95,
    'points': 300,
    'starter': 'def find_kth_largest(nums, k):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': 5, 'input': 'find_kth_largest([3,2,1,5,6,4], 2)'}],
    'title': 'Kth Largest Element'},
  { 'description': 'An election system finds which candidate got more than half the total votes.\n'
                   '\n'
                   'Find majority element.\n'
                   '\n'
                   '🎯 Real-Life Use: Election result analysis.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `majority_element([3,2,3])`\n'
                   'Expected Output: `3`',
    'difficulty': 'Hard',
    'hint': 'Boyer-Moore voting: keep a candidate and count. Or just sort and pick the middle.',
    'id': 96,
    'points': 300,
    'starter': 'def majority_element(nums):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': 3, 'input': 'majority_element([3,2,3])'}],
    'title': 'Majority Element'},
  { 'description': 'A library catalog is organized in a sorted 2D table. Find a specific book quickly.\n'
                   '\n'
                   'Search for value in 2D sorted matrix.\n'
                   '\n'
                   '🎯 Real-Life Use: Efficient database lookups.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)`\n'
                   'Expected Output: `True`',
    'difficulty': 'Hard',
    'hint': 'Treat the 2D matrix as a 1D sorted array and use binary search.',
    'id': 97,
    'points': 300,
    'starter': 'def search_matrix(matrix, target):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': True, 'input': 'search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)'}],
    'title': 'Search 2D Matrix'},
  { 'description': 'A photo editor rotates an image 90 degrees clockwise.\n'
                   '\n'
                   'Rotate nxn matrix 90 degrees clockwise in-place, then return it.\n'
                   '\n'
                   '🎯 Real-Life Use: Image rotation in editors.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `rotate_image([[1,2,3],[4,5,6],[7,8,9]])`\n'
                   'Expected Output: `[[7, 4, 1], [8, 5, 2], [9, 6, 3]]`',
    'difficulty': 'Hard',
    'hint': 'Transpose the matrix, then reverse each row.',
    'id': 98,
    'points': 300,
    'starter': 'def rotate_image(matrix):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [{'expected': [[7, 4, 1], [8, 5, 2], [9, 6, 3]], 'input': 'rotate_image([[1,2,3],[4,5,6],[7,8,9]])'}],
    'title': 'Rotate Image'},
  { 'description': 'A dictionary app groups words that are anagrams (same letters, different order) together.\n'
                   '\n'
                   'Group anagrams together and return list of lists.\n'
                   '\n'
                   '🎯 Real-Life Use: Word game helpers.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `sorted([sorted(x) for x in group_anagrams(['eat','tea','tan','ate','nat','bat'])])`\n"
                   "Expected Output: `[['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']]`",
    'difficulty': 'Hard',
    'hint': 'Use a dict with sorted word as key, group words under each key.',
    'id': 99,
    'points': 300,
    'starter': 'def group_anagrams(strs):\n    pass',
    'tags': ['lists', 'algorithms'],
    'tests': [ { 'expected': [['ate', 'eat', 'tea'], ['bat'], ['nat', 'tan']],
                 'input': "sorted([sorted(x) for x in group_anagrams(['eat','tea','tan','ate','nat','bat'])])"}],
    'title': 'Group Anagrams'},
  { 'description': "A word game checks if one word can be rearranged to form another (like 'anagram' → 'nagaram').\n"
                   '\n'
                   'Return True if t is an anagram of s.\n'
                   '\n'
                   '🎯 Real-Life Use: Word game validation.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `is_anagram('anagram', 'nagaram')`\n"
                   'Expected Output: `True`',
    'difficulty': 'Hard',
    'hint': 'Sort both and compare, or use a character frequency counter.',
    'id': 100,
    'points': 300,
    'starter': 'def is_anagram(s, t):\n    pass',
    'tags': ['strings'],
    'tests': [{'expected': True, 'input': "is_anagram('anagram', 'nagaram')"}],
    'title': 'Valid Anagram'},
  { 'description': "You're designing a web browser's cache system. It should store the most recently used pages and "
                   'evict the least recently used one when full.\n'
                   '\n'
                   'Implement an LRU Cache class with `get(key)` and `put(key, value)` methods. Both should run in '
                   'O(1) time.\n'
                   '\n'
                   'For this problem, implement a function `lru_cache_test(capacity, operations, args)` that:\n'
                   '- Creates an LRU Cache with given capacity\n'
                   "- Executes operations ('get' or 'put') with corresponding args\n"
                   '- Returns a list of results (get returns value or -1, put returns None)\n'
                   '\n'
                   '🎯 Real-Life Use: Browser caching, database query caching, CDN systems.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `lru_cache_test(2, ['put','put','get','put','get','put','get','get','get'], "
                   '[[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]])`\n'
                   'Expected Output: `[None, None, 1, None, -1, None, -1, 3, 4]`',
    'difficulty': 'Advanced',
    'hint': 'Use an OrderedDict or combine a HashMap with a Doubly Linked List for O(1) get/put.',
    'id': 101,
    'points': 20000,
    'starter': 'def lru_cache_test(capacity, operations, args):\n'
               '    # Implement an LRU Cache and process operations\n'
               '    pass',
    'tags': ['data-structures', 'design', 'advanced'],
    'tests': [ { 'expected': [None, None, 1, None, -1, None, -1, 3, 4],
                 'input': "lru_cache_test(2, ['put','put','get','put','get','put','get','get','get'], "
                          '[[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]])'}],
    'title': 'LRU Cache'},
  { 'description': "You're building a cloud save system for a game. The game's skill tree (a binary tree) needs to be "
                   'saved as a string and later reconstructed exactly.\n'
                   '\n'
                   'Implement `serialize(root)` to convert a tree (given as nested lists `[val, left, right]` or None) '
                   'to a string, and `deserialize(data)` to convert it back.\n'
                   '\n'
                   'For this problem, implement `serde_test(tree)` that serializes then deserializes and returns the '
                   'result.\n'
                   '\n'
                   '🎯 Real-Life Use: Saving/loading game states, database storage of tree structures.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `serde_test([1, [2, None, None], [3, [4, None, None], [5, None, None]]])`\n'
                   'Expected Output: `[1, [2, None, None], [3, [4, None, None], [5, None, None]]]`',
    'difficulty': 'Advanced',
    'hint': 'Use preorder traversal with a delimiter. Use a queue/iterator for deserialization.',
    'id': 102,
    'points': 20000,
    'starter': 'def serde_test(tree):\n    # Serialize tree to string, then deserialize back\n    pass',
    'tags': ['trees', 'design', 'advanced'],
    'tests': [ { 'expected': [1, [2, None, None], [3, [4, None, None], [5, None, None]]],
                 'input': 'serde_test([1, [2, None, None], [3, [4, None, None], [5, None, None]]])'}],
    'title': 'Serialize & Deserialize Binary Tree'},
  { 'description': 'Two hospitals merge their patient age records (both sorted). You need to find the median age '
                   'across all patients efficiently without merging the full lists.\n'
                   '\n'
                   'Write `find_median(nums1, nums2)` that returns the median of two sorted arrays.\n'
                   'The overall run time complexity should be O(log(min(m,n))).\n'
                   '\n'
                   '🎯 Real-Life Use: Merging sorted datasets in distributed databases.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `find_median([1, 3], [2])`\n'
                   'Expected Output: `2.0`',
    'difficulty': 'Advanced',
    'hint': 'Use binary search on the shorter array. Partition both arrays so left halves have the smaller elements.',
    'id': 103,
    'points': 20000,
    'starter': 'def find_median(nums1, nums2):\n    pass',
    'tags': ['binary-search', 'arrays', 'advanced'],
    'tests': [{'expected': 2.0, 'input': 'find_median([1, 3], [2])'}],
    'title': 'Median of Two Sorted Arrays'},
  { 'description': 'A DNA researcher needs to find the shortest segment of a genome that contains all required '
                   'markers.\n'
                   '\n'
                   'Given strings `s` and `t`, find the minimum window substring of `s` that contains all characters '
                   'of `t` (including duplicates). Return empty string if no such window exists.\n'
                   '\n'
                   '🎯 Real-Life Use: Genome sequencing, text search engines.\n'
                   '\n'
                   'Example Test Case:\n'
                   "Input: `min_window('ADOBECODEBANC', 'ABC')`\n"
                   'Expected Output: `BANC`',
    'difficulty': 'Advanced',
    'hint': 'Use sliding window with two pointers. Expand right to include, shrink left to minimize.',
    'id': 104,
    'points': 20000,
    'starter': 'def min_window(s, t):\n    pass',
    'tags': ['sliding-window', 'strings', 'advanced'],
    'tests': [{'expected': 'BANC', 'input': "min_window('ADOBECODEBANC', 'ABC')"}],
    'title': 'Minimum Window Substring'},
  { 'description': 'A stock analyst tracks daily closing prices and wants to find the longest period where prices were '
                   'strictly increasing (not necessarily consecutive days).\n'
                   '\n'
                   'Given an array `nums`, return the length of the longest strictly increasing subsequence.\n'
                   'Aim for O(n log n) complexity.\n'
                   '\n'
                   '🎯 Real-Life Use: Stock trend analysis, patience sorting.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `lis_length([10, 9, 2, 5, 3, 7, 101, 18])`\n'
                   'Expected Output: `4`',
    'difficulty': 'Advanced',
    'hint': 'Use a "tails" array with binary search. For each num, replace the first tail >= num, or append if larger '
            'than all.',
    'id': 105,
    'points': 20000,
    'starter': 'def lis_length(nums):\n    pass',
    'tags': ['dp', 'binary-search', 'advanced'],
    'tests': [{'expected': 4, 'input': 'lis_length([10, 9, 2, 5, 3, 7, 101, 18])'}],
    'title': 'Longest Increasing Subsequence Length'},
  { 'description': "You're building a word puzzle game (like Boggle). Given a 2D board of letters and a list of words, "
                   'find all words that can be formed by connecting adjacent cells (horizontal/vertical, no reuse).\n'
                   '\n'
                   'Return a sorted list of found words.\n'
                   '\n'
                   '🎯 Real-Life Use: Word puzzle solvers, autocomplete on keyboards.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: '
                   "`sorted(find_words([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], "
                   "['oath','pea','eat','rain']))`\n"
                   "Expected Output: `['eat', 'oath']`",
    'difficulty': 'Advanced',
    'hint': 'Build a Trie from the word list. DFS/backtrack on the board while walking the Trie to prune early.',
    'id': 106,
    'points': 20000,
    'starter': 'def find_words(board, words):\n    pass',
    'tags': ['trie', 'backtracking', 'advanced'],
    'tests': [ { 'expected': ['eat', 'oath'],
                 'input': "sorted(find_words([['o','a','a','n'],['e','t','a','e'],['i','h','k','r'],['i','f','l','v']], "
                          "['oath','pea','eat','rain']))"}],
    'title': 'Word Search II (Trie + Backtracking)'},
  { 'description': 'A delivery app needs to find the shortest route between warehouses in a city. The city map is a '
                   'weighted graph.\n'
                   '\n'
                   'Given `n` nodes (0 to n-1), a list of edges `[u, v, weight]`, and a `start` node, return a list of '
                   'shortest distances from start to each node. Use -1 for unreachable nodes.\n'
                   '\n'
                   '🎯 Real-Life Use: Google Maps routing, network packet routing.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `dijkstra(4, [[0,1,1],[0,2,4],[1,2,2],[1,3,6],[2,3,3]], 0)`\n'
                   'Expected Output: `[0, 1, 3, 6]`',
    'difficulty': 'Advanced',
    'hint': 'Use a min-heap (heapq). Push (distance, node), always process the smallest distance first. Skip if '
            'already visited.',
    'id': 107,
    'points': 20000,
    'starter': 'def dijkstra(n, edges, start):\n    pass',
    'tags': ['graphs', 'heap', 'advanced'],
    'tests': [{'expected': [0, 1, 3, 6], 'input': 'dijkstra(4, [[0,1,1],[0,2,4],[1,2,2],[1,3,6],[2,3,3]], 0)'}],
    'title': 'Dijkstra Shortest Path'},
  { 'description': 'A university needs to determine a valid order to offer courses, given that some courses have '
                   'prerequisites.\n'
                   '\n'
                   'Given `n` courses (0 to n-1) and a list of prerequisites `[course, prereq]`, return a valid '
                   'ordering. If impossible (circular dependency), return an empty list.\n'
                   '\n'
                   '🎯 Real-Life Use: Course planning, build systems (make/gradle), task scheduling.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `topo_sort(4, [[1,0],[2,0],[3,1],[3,2]])`\n'
                   'Expected Output: `[0, 1, 2, 3]`',
    'difficulty': 'Advanced',
    'hint': "Use Kahn's algorithm (BFS with in-degree tracking) or DFS with visited states.",
    'id': 108,
    'points': 20000,
    'starter': 'def topo_sort(n, prerequisites):\n    pass',
    'tags': ['graphs', 'topological-sort', 'advanced'],
    'tests': [{'expected': [0, 1, 2, 3], 'input': 'topo_sort(4, [[1,0],[2,0],[3,1],[3,2]])'}],
    'title': 'Topological Sort (Course Schedule)'},
  { 'description': 'A thief breaks into a store and has a backpack with limited capacity. Each item has a weight and '
                   'value. They can either take or leave each item (no splitting). Maximize total value.\n'
                   '\n'
                   'Given `capacity`, list of `weights`, and list of `values`, return the maximum value achievable.\n'
                   '\n'
                   '🎯 Real-Life Use: Resource allocation, investment portfolio optimization, cargo loading.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `knapsack(7, [1, 3, 4, 5], [1, 4, 5, 7])`\n'
                   'Expected Output: `9`',
    'difficulty': 'Advanced',
    'hint': 'Use 2D DP: dp[i][w] = max value using first i items with capacity w. Optimize to 1D if you want.',
    'id': 109,
    'points': 20000,
    'starter': 'def knapsack(capacity, weights, values):\n    pass',
    'tags': ['dp', 'advanced'],
    'tests': [{'expected': 9, 'input': 'knapsack(7, [1, 3, 4, 5], [1, 4, 5, 7])'}],
    'title': 'Knapsack 0/1'},
  { 'description': 'A CI/CD pipeline has tasks that depend on each other. Before running, you need to detect if '
                   "there's a circular dependency which would cause an infinite loop.\n"
                   '\n'
                   'Given `n` nodes and a list of directed edges `[from, to]`, return True if the graph contains a '
                   'cycle.\n'
                   '\n'
                   '🎯 Real-Life Use: Deadlock detection, dependency resolution, compiler analysis.\n'
                   '\n'
                   'Example Test Case:\n'
                   'Input: `has_cycle(4, [[0,1],[1,2],[2,3]])`\n'
                   'Expected Output: `False`',
    'difficulty': 'Advanced',
    'hint': 'Use DFS with 3 colors: white (unvisited), gray (in-progress), black (done). A gray→gray edge means cycle.',
    'id': 110,
    'points': 20000,
    'starter': 'def has_cycle(n, edges):\n    pass',
    'tags': ['graphs', 'dfs', 'advanced'],
    'tests': [{'expected': False, 'input': 'has_cycle(4, [[0,1],[1,2],[2,3]])'}],
    'title': 'Detect Cycle in Directed Graph'}]


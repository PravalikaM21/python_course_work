# my_programs.py → contains all 10 functions.
# main.py → contains the menu-driven interface.

# my_programs.py

def rotations_of_each_other():
    print(" Program: Check if Two Strings are Rotations of Each Other")
    print(""" 
def is_rotation(s1, s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)
""")
    print("Test Case 1: is_rotation('abcd', 'cdab') → True")
    print("Test Case 2: is_rotation('abcd', 'acbd') → False")
    print("Explanation: By doubling s1 and checking if s2 exists inside, we confirm rotation.")


def most_frequent_word():
    print(" Program: Find the Most Frequent Word in a Sentence")
    print(""" 
def most_frequent(sentence):
    words = sentence.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return max(freq, key=freq.get)
""")
    print(" Test Case 1: most_frequent('apple banana apple orange apple banana') → 'apple'")
    print(" Test Case 2: most_frequent('cat dog dog cat cat') → 'cat'")
    print(" Explanation: Uses dictionary to count words and finds the maximum frequency.")


def title_case_manual():
    print(" Program: Convert String to Title Case without using .title()")
    print(""" 
def to_title_case(s):
    return ' '.join(word[0].upper() + word[1:].lower() for word in s.split())
""")
    print(" Test Case 1: to_title_case('hello world') → 'Hello World'")
    print(" Test Case 2: to_title_case('PYTHON programming') → 'Python Programming'")
    print(" Explanation: Splits string into words, capitalizes first letter, lowercases rest.")


def lcm_gcd_manual():
    print(" Program: Find LCM and GCD of Two Numbers (without built-ins)")
    print(""" 
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
""")
    print(" Test Case 1: gcd(12, 18) → 6, lcm(12, 18) → 36")
    print(" Test Case 2: gcd(7, 5) → 1, lcm(7, 5) → 35")
    print(" Explanation: GCD via Euclidean algorithm; LCM = (a*b)//gcd.")


def find_duplicates():
    print(" Program: Find Duplicates in a List without using set()")
    print(""" 
def find_duplicates(lst):
    dup = []
    for i in range(len(lst)):
        if lst[i] in lst[:i] and lst[i] not in dup:
            dup.append(lst[i])
    return dup
""")
    print(" Test Case 1: find_duplicates([1,2,3,2,4,3]) → [2, 3]")
    print(" Test Case 2: find_duplicates([5,5,5,6]) → [5]")
    print(" Explanation: Checks if an element appeared before and adds it once to duplicates.")


def print_n_to_1():
    print(" Program: Print Numbers from N to 1 using Recursion")
    print(""" 
def print_reverse(n):
    if n > 0:
        print(n, end=' ')
        print_reverse(n-1)
""")
    print(" Test Case 1: print_reverse(5) → 5 4 3 2 1")
    print(" Test Case 2: print_reverse(3) → 3 2 1")
    print(" Explanation: Recursively prints number then calls function with n-1.")


def substrings_recursion():
    print(" Program: Generate All Substrings of a String using Recursion")
    print(""" 
def substrings(s, i=0, j=0):
    if i == len(s):
        return
    elif j == len(s):
        substrings(s, i+1, i+1)
    else:
        print(s[i:j+1])
        substrings(s, i, j+1)
""")
    print(" Test Case 1: substrings('abc') → a, ab, abc, b, bc, c")
    print(" Test Case 2: substrings('ab') → a, ab, b")
    print(" Explanation: Uses recursion with indices to generate substrings.")


def top2_frequent():
    print(" Program: Find Top 2 Most Frequent Elements in a List")
    print(""" 
def top2(lst):
    freq = {}
    for x in lst:
        freq[x] = freq.get(x, 0) + 1
    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [item[0] for item in sorted_items[:2]]
""")
    print(" Test Case 1: top2([1,1,2,2,2,3,3,3,3]) → [3, 2]")
    print(" Test Case 2: top2(['a','b','a','c','b','a']) → ['a','b']")
    print(" Explanation: Uses dictionary frequency count and sorts by value.")


def symmetric_matrix():
    print(" Program: Check if a Matrix is Symmetric")
    print(""" 
def is_symmetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True
""")
    print(" Test Case 1: [[1,2,3],[2,4,5],[3,5,6]] → True")
    print(" Test Case 2: [[1,0],[2,1]] → False")
    print(" Explanation: A matrix is symmetric if A[i][j] == A[j][i].")


def count_vowels_consonants():
    print(" Program: Count Number of Vowels and Consonants in a String")
    print(""" 
def count_vc(s):
    vowels = 'aeiouAEIOU'
    v = c = 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                c += 1
    return v, c
""")
    print(" Test Case 1: count_vc('hello') → (2,3)")
    print(" Test Case 2: count_vc('AEIOUxyz') → (5,3)")
    print(" Explanation: Iterates through characters, checks vowels, else counts consonants.")


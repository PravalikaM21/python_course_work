#--: Quiz Game :--
'''
Objective:
You have learned how to create a quiz game using Python, loops, conditionals, and functions. 
Now it's time to create your own Interview Prep Quiz App.

Assignment Instructions:
Prepare 10 Unique Advanced Python Interview Questions
Each question must have:
A question string
Four options (a, b, c, d)
One correct answer
Build Your Own Quiz Game
Use the provided template (you can modify it).
Use functions, loops, and conditions only.
No GUI needed / console/terminal-based quiz is expected.
Expected Output:
🧪 Welcome to the Python Quiz Game - Advanced Edition!'''

def welcome():
    print("🧪 Welcome to the Python Quiz Game - Advanced Edition!")
    print("Answer each question by typing a/b/c/d\n")

def ask_question(question, options, correct_option):
    print(question)
    for key, value in options.items():
        print(f"{key}) {value}")
    answer = input("Your answer (a/b/c/d): ").strip().lower()
    if answer == correct_option:
        print("✅ Correct!\n")
        return True
    else:
        print(f"❌ Wrong! The correct answer is '{correct_option}'\n")
        return False

def start_quiz():
    score = 0
    questions = [
        {
            "question": "1. What will be the output of the following code?\n"
                        "def outer():\n"
                        "    x = \"outer\"\n"
                        "    def inner():\n"
                        "        nonlocal x\n"
                        "        x = \"inner\"\n"
                        "        print(x)\n"
                        "    inner()\n"
                        "    print(x)\n"
                        "outer()",
            "options": {
                "a": "inner, outer",
                "b": "outer, outer",
                "c": "inner, inner",
                "d": "inner, inner, outer"
            },
            "answer": "c"
        },
        {
            "question": "2. What exactly does the `del` keyword delete in Python?",
            "options": {
                "a": "The variable and its object",
                "b": "The reference to the object",
                "c": "The memory of the object",
                "d": "Both reference and object always"
            },
            "answer": "b"
        },
        {
            "question": "3. What are 'soft keywords' introduced in Python 3.10+?",
            "options": {
                "a": "Keywords reserved only in special contexts",
                "b": "Deprecated keywords",
                "c": "New data types",
                "d": "Comments written in a specific way"
            },
            "answer": "a"
        },
        {
            "question": "4. What happens if you assign a value to `None` in Python 2.7?",
            "options": {
                "a": "It raises an error",
                "b": "It's allowed and rebinds `None`",
                "c": "None becomes a class",
                "d": "Nothing happens"
            },
            "answer": "b"
        },
        {
            "question": "5. What is the main difference between `yield` and `return`?",
            "options": {
                "a": "`yield` stops the function permanently",
                "b": "`return` creates a generator",
                "c": "`yield` pauses the function and saves state",
                "d": "`return` is slower than `yield`"
            },
            "answer": "c"
        },
        {
            "question": "6. Which of the following is NOT a Python token type?",
            "options": {
                "a": "Identifier",
                "b": "Keyword",
                "c": "Loop",
                "d": "Literal"
            },
            "answer": "c"
        },
        {
            "question": "7. Can all Python token types appear in one line of code? Which is a valid example?",
            "options": {
                "a": "if x == 1: print(\"Yes\")",
                "b": "x = 5",
                "c": "print(5 + 3)",
                "d": "while True: pass"
            },
            "answer": "a"
        },
        {
            "question": "8. In Python tokenization, what are `:` and `,` considered as?",
            "options": {
                "a": "Identifiers",
                "b": "Literals",
                "c": "Operators",
                "d": "Delimiters"
            },
            "answer": "d"
        },
        {
            "question": "9. Python is...",
            "options": {
                "a": "Weakly and statically typed",
                "b": "Strongly and dynamically typed",
                "c": "Weakly and dynamically typed",
                "d": "Strongly and statically typed"
            },
            "answer": "b"
        },
        {
            "question": "10. Why can tuples be used as dictionary keys but lists cannot?",
            "options": {
                "a": "Tuples are smaller than lists",
                "b": "Tuples are always numeric",
                "c": "Tuples are immutable and hashable",
                "d": "Lists are stored differently"
            },
            "answer": "c"
        }
    ]

    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    print(f"🎯 Your Final Score: {score}/10")
    if score == 10:
        print("🎉 Perfect score! You're a Python pro!")
    elif score >= 7:
        print("✅ Great job! Keep practicing!")
    else:
        print("📘 Review some concepts and try again.")

# Run the quiz
welcome()
start_quiz()




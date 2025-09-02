"""
Assignment 8: Intelligent Daily Journal Management System
"""

import os
import re

# Simple sentiment word lists
positive_words = ["happy", "good", "great", "love", "enjoy", "excellent"]
negative_words = ["sad", "bad", "angry", "hate", "worst", "poor"]

JOURNAL_DIR = "journals"
os.makedirs(JOURNAL_DIR, exist_ok=True)


def normalize_filename(name: str) -> str | None:
    """Trim, ensure .txt extension and sanitize filename (no folders)."""
    if not name:
        return None
    name = name.strip()
    if not name.lower().endswith(".txt"):
        name += ".txt"
    # Prevent path traversal; keep only base name
    return os.path.basename(name)


def list_journals() -> list:
    """Return sorted list of .txt files in journal dir."""
    return sorted([f for f in os.listdir(JOURNAL_DIR) if f.endswith(".txt")])


def read_journal(filename: str) -> str | None:
    fn = normalize_filename(filename)
    if not fn:
        return None
    path = os.path.join(JOURNAL_DIR, fn)
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        return None


def write_journal(filename: str, content: str) -> bool:
    fn = normalize_filename(filename)
    if not fn:
        return False
    path = os.path.join(JOURNAL_DIR, fn)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(content)
    return True


def analyze_content(content: str) -> dict:
    """
    Return dict:
      { 'sentiment': 'Positive'|'Negative'|'Neutral',
        'pos_matches': [...], 'neg_matches': [...] }
    """
    if not content:
        return {"sentiment": "Neutral", "pos_matches": [], "neg_matches": []}

    pos_pattern = r"\b(" + "|".join(map(re.escape, positive_words)) + r")\b"
    neg_pattern = r"\b(" + "|".join(map(re.escape, negative_words)) + r")\b"

    pos_matches = re.findall(pos_pattern, content, flags=re.IGNORECASE)
    neg_matches = re.findall(neg_pattern, content, flags=re.IGNORECASE)

    if len(pos_matches) > len(neg_matches):
        sentiment = "Positive"
    elif len(neg_matches) > len(pos_matches):
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {"sentiment": sentiment, "pos_matches": pos_matches, "neg_matches": neg_matches}


def create_journal():
    name = input("Enter filename (with or without .txt): ").strip()
    fn = normalize_filename(name)
    if not fn:
        print("Invalid filename.")
        return
    full_path = os.path.join(JOURNAL_DIR, fn)
    if os.path.exists(full_path):
        ans = input(f"'{fn}' exists — overwrite? (y/N): ").strip().lower()
        if ans != "y":
            print("Cancelled.")
            return

    print("Enter your journal content. Press Enter when done.")
    content = input("> ")
    if write_journal(fn, content):
        print(f"✅ Saved '{fn}'")
    else:
        print("Error saving file.")


def modify_journal():
    journals = list_journals()
    if not journals:
        print("No journals available.")
        return

    print("Available journals:")
    for i, j in enumerate(journals, 1):
        print(f"{i}. {j}")

    try:
        choice = int(input("Select journal number to modify: ").strip())
        if choice < 1 or choice > len(journals):
            print("Invalid selection.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    selected = journals[choice - 1]
    old = read_journal(selected) or ""
    print("Old Content:\n" + ("(empty)\n" if not old else old + "\n"))
    new_content = input("Enter new content (this will overwrite):\n> ")
    write_journal(selected, new_content)
    print(f"✅ '{selected}' updated.")


def analyze_journals():
    journals = list_journals()
    if not journals:
        print("No journals available.")
        return

    print("Available journals:")
    for i, j in enumerate(journals, 1):
        print(f"{i}. {j}")

    choice = input("Enter journal number to analyze or 'all': ").strip().lower()
    if choice == "all":
        for j in journals:
            content = read_journal(j) or ""
            r = analyze_content(content)
            print(f"\n--- {j} ---")
            print("Sentiment:", r["sentiment"])
            print("Positive words found:", r["pos_matches"])
            print("Negative words found:", r["neg_matches"])
    else:
        try:
            idx = int(choice) - 1
            if idx < 0 or idx >= len(journals):
                print("Invalid selection.")
                return
        except ValueError:
            print("Enter a number or 'all'.")
            return
        filename = journals[idx]
        content = read_journal(filename) or ""
        r = analyze_content(content)
        print(f"\n--- Analysis of {filename} ---")
        print("Sentiment:", r["sentiment"])
        print("Positive words found:", r["pos_matches"])
        print("Negative words found:", r["neg_matches"])


def main():
    while True:
        print("\n--- Daily Journal Management System ---")
        print("1. Create New Journal")
        print("2. Modify Journal")
        print("3. Analyze Journals")
        print("4. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            create_journal()
        elif choice == "2":
            modify_journal()
        elif choice == "3":
            analyze_journals()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()

'''=::Office Chat Data Analysis::=
Python Project using functions, loops, strings, lists, sets, and dictionaries
Problem Statement:
------------------
In this project, you will analyze Office Team Chat messages. The program uses functions, loops, and Python data types (like strings, lists, sets, and dictionaries) to provide insights such as who talked the most, what was discussed, who mentioned whom, and more.

Input Format:
-------------
Ask the user:
Enter the number of messages:
Accept chat messages one by one in the format:
Name: message
Show a menu to let the user choose analysis options.

#sample chatting:
Pravalika: Good morning team!
Teju: Morning Pravalika!
Kiran: Have we submitted the report?
Uday: Not yet, I’m working on it.
Shailu: Let me know if you need help.
Pravalika: Teju, please review the report once it's ready.
Teju: Sure, I will check it.
Kiran: The deadline is by 5 PM today.
Uday: I will finish it before that.
Shailu: Great! Let's aim to send it early.

'''
def get_chat():
    n = int(input("Enter the number of messages: "))
    chat = []
    for _ in range(n):
        chat.append(input())
    return chat

def count_total_messages(chat):
    print("Total messages:", len(chat))

def unique_members(chat):
    members = {msg.split(":")[0].strip() for msg in chat if ":" in msg}
    print("Unique team members in the chat:", members)

def total_words(chat):
    word_count = sum(len(msg.split(":")[1].split()) for msg in chat if ":" in msg)
    print("Total words in the chat:", word_count)

def average_words_per_message(chat):
    total = sum(len(msg.split(":")[1].split()) for msg in chat if ":" in msg)
    avg = total / len(chat) if chat else 0
    print("Average words per message:", round(avg, 2))

def longest_message(chat):
    longest = max(chat, key=len)
    print("Longest message:", longest)

def most_active_user(chat):
    from collections import Counter
    names = [msg.split(":")[0].strip() for msg in chat if ":" in msg]
    count = Counter(names)
    name, msgs = count.most_common(1)[0]
    print(f"Most active user: {name} ({msgs} messages)")

def user_message_count(chat):
    name = input("Enter team member name: ").strip()
    count = sum(1 for msg in chat if msg.startswith(name + ":"))
    print(f"Messages sent by {name}: {count}")

def most_frequent_word_by_user(chat):
    from collections import Counter
    name = input("Enter team member name: ").strip()
    words = []
    for msg in chat:
        if msg.startswith(name + ":"):
            words += msg.split(":")[1].strip().lower().split()
    if words:
        common = Counter(words).most_common(1)[0]
        print(f'Most frequent word used by {name}: "{common[0]}"')
    else:
        print(f"No messages found for {name}.")

def first_last_message_by_user(chat):
    name = input("Enter team member name: ").strip()
    user_msgs = [msg for msg in chat if msg.startswith(name + ":")]
    if user_msgs:
        print("First message by", name + ":", user_msgs[0])
        print("Last message by", name + ":", user_msgs[-1])
    else:
        print(f"No messages from {name}.")

def check_user_present(chat):
    name = input("Enter name to check: ").strip()
    found = any(msg.startswith(name + ":") for msg in chat)
    if found:
        print(f"User '{name}' is present in the chat.")
    else:
        print(f"User '{name}' not found in the chat.")

def common_words(chat):
    from collections import Counter
    words = []
    for msg in chat:
        if ":" in msg:
            words += msg.split(":")[1].lower().split()
    common = [word for word, freq in Counter(words).items() if freq > 1]
    print("Common repeated words:", set(common))

def user_with_longest_avg(chat):
    from collections import defaultdict
    data = defaultdict(list)
    for msg in chat:
        if ":" in msg:
            name, text = msg.split(":", 1)
            data[name.strip()].append(len(text.strip().split()))
    avg_lengths = {user: sum(lengths)/len(lengths) for user, lengths in data.items()}
    if avg_lengths:
        best = max(avg_lengths, key=avg_lengths.get)
        print(f"User with longest average message: {best} (avg {round(avg_lengths[best], 2)} words)")

def count_mentions(chat):
    name = input("Enter the name to check mentions: ").lower()
    count = sum(1 for msg in chat if name in msg.lower().split(":")[1])
    print(f"Messages mentioning '{name}': {count}")

def remove_duplicates(chat):
    unique = list(set(chat))
    print(f"Unique messages count: {len(unique)}")
    for msg in unique:
        print(msg)

def sort_messages(chat):
    for msg in sorted(chat):
        print(msg)

def extract_questions(chat):
    questions = [msg for msg in chat if "?" in msg]
    print("Questions asked in the chat:")
    for q in questions:
        print(q)

def reply_ratio(chat):
    name1 = input("From: ").strip()
    name2 = input("To: ").strip()
    count = 0
    for i in range(1, len(chat)):
        if chat[i].startswith(name1 + ":") and chat[i-1].startswith(name2 + ":"):
            count += 1
    print(f"Reply ratio from {name1} to {name2}: {count} replies")

def check_deleted(chat):
    count = sum(1 for msg in chat if "This message was deleted" in msg)
    print("Deleted messages found:", count)

# Menu
def show_menu():
    print("\nChoose an analysis option:")
    print("1. Count total number of messages")
    print("2. Identify unique team members")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message sent")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Most frequent word by a specific user")
    print("9. First and last message by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("12. User with longest average message")
    print("13. Count mentions of a specific user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract all questions")
    print("17. Calculate reply ratio between two users")
    print("18. Check for deleted messages")
    print("0. Exit")

# Main program
chat_data = get_chat()
show_menu()
while True:
    choice = input("Enter your choice: ")
    
    if choice == '1': count_total_messages(chat_data)
    elif choice == '2': unique_members(chat_data)
    elif choice == '3': total_words(chat_data)
    elif choice == '4': average_words_per_message(chat_data)
    elif choice == '5': longest_message(chat_data)
    elif choice == '6': most_active_user(chat_data)
    elif choice == '7': user_message_count(chat_data)
    elif choice == '8': most_frequent_word_by_user(chat_data)
    elif choice == '9': first_last_message_by_user(chat_data)
    elif choice == '10': check_user_present(chat_data)
    elif choice == '11': common_words(chat_data)
    elif choice == '12': user_with_longest_avg(chat_data)
    elif choice == '13': count_mentions(chat_data)
    elif choice == '14': remove_duplicates(chat_data)
    elif choice == '15': sort_messages(chat_data)
    elif choice == '16': extract_questions(chat_data)
    elif choice == '17': reply_ratio(chat_data)
    elif choice == '18': check_deleted(chat_data)
    elif choice == '0':
        print("Exiting... Thank you!")
        break
    else:
        print("Invalid choice. Try again.")

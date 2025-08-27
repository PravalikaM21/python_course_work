# main.py
import my_programs as mp

def menu():
    while True:
        print("\n------ FUNCTION MENU ------")
        print("1. Check if two strings are rotations of each other")
        print("2. Find the most frequent word in a sentence")
        print("3. Convert a string to title case without using .title()")
        print("4. Find LCM and GCD of two numbers without built-in functions")
        print("5. Find duplicates in a list without using set()")
        print("6. Print numbers from N to 1 using recursion")
        print("7. Generate all substrings of a string using recursion")
        print("8. Find top 2 most frequent elements in a list")
        print("9. Check if a matrix is symmetric")
        print("10. Count number of vowels and consonants in a string")
        print("0. Exit")
        print("----------------------------")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            mp.rotations_of_each_other()
        elif choice == "2":
            mp.most_frequent_word()
        elif choice == "3":
            mp.title_case_manual()
        elif choice == "4":
            mp.lcm_gcd_manual()
        elif choice == "5":
            mp.find_duplicates()
        elif choice == "6":
            mp.print_n_to_1()
        elif choice == "7":
            mp.substrings_recursion()
        elif choice == "8":
            mp.top2_frequent()
        elif choice == "9":
            mp.symmetric_matrix()
        elif choice == "10":
            mp.count_vowels_consonants()
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    menu()

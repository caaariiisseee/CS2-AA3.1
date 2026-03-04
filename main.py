# 8-Camia
# Alexis D. Littaua, Carisse Aiasha P. Lugo, Lemuel V. Poquiz
# AA 3.1

# import the json function
import json

try:
    # READING from the file
    filename = "questions.json"
    with open(filename, 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)

    # Print an introduction
    print("Hello! Welcome to Stay In or Go Out : MBTI Tester")
    print("\nMenu:")

    print("1. What is an MBTI? \n2. What does this program do?"
          "\n3. What is my MBTI? \n4. Exit")
    answer = int(input("\nWhat is your choice? : "))

    while answer != 4:

        if answer == 1:
            print("\nMyers-Briggs Type Indicator (MBTI) is a test where people get grouped into 16 personality types"
                  " based on their tendency or what they choose to do in certain situations.\nThese personality types are"
                  " a combination of : Extroversion, Introversion, Sensing, Intuition, Feeling, Thinking, Prospecting, "
                  "Judging.\nThis program was created to inform users about their MBTI and habits they usually do and their "
                  "personality after answering a set of questions.")
            print()
            print("-" * 100)
            print("\nWhat else do you want to do? \n1. What is an MBTI? \n2. What does this program do?"
                  "\n3. What is my MBTI? \n4. Exit")
            answer = int(input("\nWhat is your choice? : "))

        if answer == 2:
            print("\nThis program not only gives you your MBTI, but it also provides you with what you usually do and your "
                  "personality!\nThis program is very simple and you don't need to learn every single textbook definitions"
                  " as the questions would ask about what you experience.")
            print()
            print("-" * 100)
            print("\nWhat else do you want to do? \n1. What is an MBTI? \n2. What does this program do?"
                  "\n3. What is my MBTI? \n4. Exit")
            answer = int(input("\nWhat is your choice? : "))

        # To keep track of answers !

        introvert = 0
        extrovert = 0
        sensing = 0
        intuition = 0
        feeling = 0
        thinking = 0
        prospecting = 0
        judging = 0

        if answer == 3:
            print("-" * 100)
            print("\nWelcome to CLA’s MBTI checker! This program would not use your personal information against you :")
            for i in data:
                for j in i:
                    print(f"\n{j}")
                    choice = input("What is your choice? (a/b) : ")
                    if i == 0:
                        if choice == "a":
                            extrovert = extrovert + 1
                            print(f"{extrovert} to the extrovert side")
                        elif choice == "b":
                            introvert = introvert + 1
                            print("+1 to the introvert side")

            print()
            print("-" * 100)
            print("\nWhat else do you want to do? \n1. What is an MBTI? \n2. What does this program do?"
                  "\n3. What is my MBTI? \n4. Exit")
            answer = int(input("\nWhat is your choice? : "))


        else:
            print("\nPlease  input a valid choice!")
            print()
            print("-" * 100)
            print("\nWhat else do you want to do? \n1. What is an MBTI? \n2. What does this program do?"
                  "\n3. What is my MBTI? \n4. Exit")
            answer = int(input("\nWhat is your choice? : "))

    print("Thank you for using MBTI Tester :)")

except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")


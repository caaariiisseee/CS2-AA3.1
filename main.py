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
          "\n3. What is my MBTI? \n4. End")
    answer = int(input("\nWhat is your choice? : "))
    print("-" * 100)

    while answer != 4:

        if answer == 1:
            print("Myers-Briggs Type Indicator (MBTI) is a test where people get grouped into 16 personality types"
                  " based on their tendency or what they choose to do in certain situations.\nThese personality types are"
                  " a combination of : Extroversion, Introversion, Sensing, Intuition, Feeling, Thinking, Prospecting, "
                  "Judging.\nThis program was created to inform users about their MBTI and habits they usually do and their "
                  "personality after answering a set of questions.")

            print("1. What is an MBTI? \n2. What does this program do?"
                  "\n3. What is my MBTI? \n4. End")
            answer = int(input("\nWhat is your choice? : "))

        elif answer == 2:
            print("This program not only gives you your MBTI, but it also provides you with what you usually do and your "
                  "personality!\nThis program is very simple and you don't need to learn every single textbook definitions"
                  " as the questions would ask about what you experience.")

            print("1. What is an MBTI? \n2. What does this program do?"
                  "\n3. What is my MBTI? \n4. End")
            answer = int(input("\nWhat is your choice? : "))

        elif answer == 3:
            for question in data:


        else:
            print("Please  input a valid choice!")
            print("1. What is an MBTI? \n2. What does this program do?"
                  "\n3. What is my MBTI? \n4. End")
            answer = int(input("\nWhat is your choice? : "))


except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")


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

    # Print an introduction and menu
    print("Hello! Welcome to Stay In or Go Out : MBTI Tester")
    print("\nMenu:")

    print("1. What is an MBTI? \n2. What does this program do?"
          "\n3. What is my MBTI? \n4. End")
    answer = int(input("\nWhat is your choice? : "))

    # while loop to ensure all the inputs are valid
    while answer != 4:

        # prints the information about MBTIs
        if answer == 1:
            print("\nMyers-Briggs Type Indicator (MBTI) is a test where people get grouped into 16 personality types"
                  " based on their tendency or what they choose to do in certain situations.\nThese personality types are"
                  " a combination of : Extroversion, Introversion, Sensing, Intuition, Feeling, Thinking, Prospecting, "
                  "Judging.\nThis program was created to inform users about their MBTI and habits they usually do and their "
                  "personality after answering a set of questions.")
            print()
            print("-" * 100)
            print("1. What is an MBTI? \n2. What does this program do?"
                  "\n3. What is my MBTI? \n4. End")
            answer = int(input("\nWhat is your choice? : "))

        # prints the goals of the program
        if answer == 2:
            print("\nThis program not only gives you your MBTI, but it also provides you with what you usually do and your "
                  "personality!\nThis program is very simple and you don't need to learn every single textbook definitions"
                  " as the questions would ask about what you experience.")
            print()
            print("-" * 100)
            print("\n1. What is an MBTI? \n2. What does this program do?"
                  "\n3. What is my MBTI? \n4. End")
            answer = int(input("\nWhat is your choice? : "))

        # initializing the MBTI components
        introvert = 0
        extrovert = 0
        sensing = 0
        intuition = 0
        feeling = 0
        thinking = 0
        prospecting = 0
        judging = 0

        # the actual questions that present the tracker of each answer
        if answer == 3:
            print("-" * 100)
            print("\nWelcome to CLA's MBTI checker! This program will not use your personal information against you :)")
            for i in data:
                for j in i:
                    print(j)
                    choice = input("Agree (a) or Disagree (b)? : ")
                    print("-" * 100)
                    if data.index(i) == 0:
                        if choice == "a":
                            introvert += 1
                            print(f"+1 to the introvert side! "
                                  f"\nIntrovert : {introvert}"
                                  f"\nExtrovert : {extrovert}"
                                  f"\nJudging : {judging}"
                                  f"\nProspecting : {prospecting}"
                                  f"\nThinking : {thinking}"
                                  f"\nFeeling : {feeling}")
                            print("-" * 100)

                        if choice == "b":
                            extrovert += 1
                            print(f"+1 to the extrovert side! "
                                  f"\nIntrovert : {introvert}"
                                  f"\nExtrovert : {extrovert}"
                                  f"\nJudging : {judging}"
                                  f"\nProspecting : {prospecting}"
                                  f"\nThinking : {thinking}"
                                  f"\nFeeling : {feeling}")
                            print("-" * 100)

                    if data.index(i) == 1:
                        if choice == "a":
                            judging += 1
                            print(f"+1 to the judging side! "
                                  f"\nIntrovert : {introvert}"
                                  f"\nExtrovert : {extrovert}"
                                  f"\nJudging : {judging}"
                                  f"\nProspecting : {prospecting}"
                                  f"\nThinking : {thinking}"
                                  f"\nFeeling : {feeling}")
                            print("-" * 100)

                        if choice == "b":
                            prospecting += 1
                            print(f"+1 to the prospecting side! "
                                  f"\nIntrovert : {introvert}"
                                  f"\nExtrovert : {extrovert}"
                                  f"\nJudging : {judging}"
                                  f"\nProspecting : {prospecting}"
                                  f"\nThinking : {thinking}"
                                  f"\nFeeling : {feeling}")
                            print("-" * 100)

                    if data.index(i) == 2:
                        if choice == "a":
                            sensing += 1
                            print(f"+1 to the sensing side! "
                                  f"\nIntrovert : {introvert}"
                                  f"\nExtrovert : {extrovert}"
                                  f"\nJudging : {judging}"
                                  f"\nProspecting : {prospecting}"
                                  f"\nThinking : {thinking}"
                                  f"\nFeeling : {feeling}")
                            print("-" * 100)

                        if choice == "b":
                            intuition += 1
                            print(f"+1 to the intuition side! "
                                  f"\nIntrovert : {introvert}"
                                  f"\nExtrovert : {extrovert}"
                                  f"\nJudging : {judging}"
                                  f"\nProspecting : {prospecting}"
                                  f"\nThinking : {thinking}"
                                  f"\nFeeling : {feeling}")
                            print("-" * 100)

                    if data.index(i) == 3:
                        if choice == "a":
                            thinking += 1
                            print(f"+1 to the thinking side! "
                                  f"\nIntrovert : {introvert}"
                                  f"\nExtrovert : {extrovert}"
                                  f"\nJudging : {judging}"
                                  f"\nProspecting : {prospecting}"
                                  f"\nThinking : {thinking}"
                                  f"\nFeeling : {feeling}")
                            print("-" * 100)

                        if choice == "b":
                            feeling += 1
                            print(f"+1 to the feeling side! "
                                  f"\nIntrovert : {introvert}"
                                  f"\nExtrovert : {extrovert}"
                                  f"\nJudging : {judging}"
                                  f"\nProspecting : {prospecting}"
                                  f"\nThinking : {thinking}"
                                  f"\nFeeling : {feeling}")
                            print("-" * 100)

        else:
            print("Please  input a valid choice!")
            print("1. What is an MBTI? \n2. What does this program do?"
                  "\n3. What is my MBTI? \n4. End")
            answer = int(input("\nWhat is your choice? : "))


except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")


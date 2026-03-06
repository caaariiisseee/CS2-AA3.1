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

                        # adds to the introvert side
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

                        # adds to the extrovert side
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

                        # adds to the judging side
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

                        # adds to the prospecting side
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

                        # adds to the sensing side
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

                        # adds to the intuition side
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

                        # adds to the thinking side
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

                        # adds to the feeling side
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

            # prints out the result of MBTI
            print("Thank you for answering our MBTI checker! Here are your results: ")

            # introversion or extroversion
            print("\nfor the introvert and extrovert side: ")
            if introvert > extrovert:
                print("You are leaning toward the introvert side."
                      "\n- You tend to focus on individual activities."
                      "\n- You get described as 'shy'")
                mbti_one = "I"
            if extrovert > introvert:
                print("You are leaning toward the extrovert side."
                      "\n- You include yourself in social gatherings."
                      "\n- You get described as 'friendly'")
                mbti_one = "E"

            # sensing or intuition
            print("\nfor the sensing and intuition side: ")
            if sensing > intuition:
                print("You are leaning toward the sensing side."
                        "\n- You focus on details."
                        "\n- You get described as 'attentive'")
                mbti_two = "S"
            if intuition > sensing:
                print("You are leaning toward the intuition side."
                        "\n- You think reality is just as important as imaginations."
                        "\n- You get described as 'imaginative'")
                mbti_two = "N"

            # thinking or feeling
            print("\nfor the thinking and feeling side: ")
            if thinking > feeling:
                print("You are leaning toward the thinking side."
                        "\n- You leave personal feelings out the conversation."
                        "\n- You get described as 'honest'")
                mbti_three = "T"
            if feeling > thinking:
                print("You are leaning toward the feeling side."
                        "\n- You think about the feelings of others before making decisions."
                        "\n- You get described as 'thoughtful'")
                mbti_three = "F"
            # judging or prospecting
            print("\nfor the judging and prospecting side: ")
            if judging > prospecting:
                print("You are leaning toward the judging side."
                      "\n- You are very structured."
                      "\n- You get described as 'prepared'")
                mbti_four = "J"
            if prospecting > judging:
                print("You are leaning toward the prospecting side."
                      "\n- You are very flexible."
                      "\n- You get described as 'laid back'")
                mbti_four = "P"


            print("\nFinal MBTI: ")
            print(f"{mbti_one}{mbti_two}{mbti_three}{mbti_four}")

        # tells the user to put a valid input
        else:
            print("Please  input a valid choice!")
            print("1. What is an MBTI? \n2. What does this program do?"
                  "\n3. What is my MBTI? \n4. End")
            answer = int(input("\nWhat is your choice? : "))

# error control
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")


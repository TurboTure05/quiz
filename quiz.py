questions = [
    {
        "question": "What is the capital of Portugal?",
        "options": ["A: Lissabon", "B: London", "C: Berlin", "D: Madrid"],
        "answer": "A"
    },
    {
        "question": "What is the capital of Skyrim?",
        "options": ["A: Whiterun", "B: Solitude", "C: Berlin", "D: Windhelm"],
        "answer": "B"
    },
    {
        "question": "How many bits is 1 byte?",
        "options": ["A: 4", "B: 8", "C: 16", "D: 1"],
        "answer": "B"
    },
    {
        "question": "What year did Brazil abolish slavery?",
        "options": ["A: 1888", "B: 1795", "C: 1902", "D: 2020"],
        "answer": "A"
    },
    {
        "question": "What is my hometown called?",
        "options": ["A: Sandviken", "B: Stockholm", "C: Gävle", "D: Uppsala"],
        "answer": "C"
    },
    {
        "question": "What is the second highest mountain in the world?",
        "options": ["A: Everest", "B: Kebenekaise", "C: Lhotse", "D: K2"],
        "answer": "D"
    },
    {
        "question": "What is the name of the imperial fleets biggest ship in star wars?",
        "options": ["A: The Destroyer", "B: The Vengeance", "C: Justice", "D: The Executor"],
        "answer": "D"
    },
    {
        "question": "What movie has won the most awards?",
        "options": ["A: LOTR: Return of The King", "B: Ronja Rövardotter", "C: Snow White", "D: Casablanca"],
        "answer": "A"
    },
    {
        "question": "When was microsoft started?",
        "options": ["A: 1999", "B: 1975", "C: 1974", "D: 1983"],
        "answer": "B"
    },
        {
            "question": "Who is Swedens statsminister",
            "options": ["A: Olof Palme", "B: Stefan Löfven", "C: Sean Banan", "D: Ulf Kristersson"],
            "answer": "D"
        },
    ]
    # This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")

run_quiz(questions)
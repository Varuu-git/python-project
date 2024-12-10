# Simple Quiz App

def run_quiz():
    # Quiz questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. Paris", "C. Madrid", "D. Rome"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Venus", "C. Mars", "D. Jupiter"],
            "answer": "C"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
            "answer": "D"
        }
    ]

    # Variables to track the score
    score = 0

    print("Welcome to the Quiz!\n")

    # Loop through the questions
    for idx, q in enumerate(questions):
        print(f"Question {idx + 1}: {q['question']}")
        for option in q['options']:
            print(option)
        
        # Get user input
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        # Check the answer
        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")

    # Display the final score
    print(f"Quiz complete! Your final score is {score}/{len(questions)}.")

# Run the quiz app
if __name__ == "__main__":
    run_quiz()

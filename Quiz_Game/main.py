print("Welcome to my Quiz game")

#things i need, a database of question and answers

#dictionary with key value pairs. the dictionary will hold the question and answers
question_bank = [
    {"text": "What is the primarry purbose of the break statement in python?","answer": "C"}
    {"text":"How do you comment a single-line in Python?", "answer": "C"}
    {"text":" What does the len() function do in Python?", "answer": "A"}
    {"text":"Which of the following is a correct way to open a file named example.txt for reading in Python?", "answer": "A"}
    {"text": "What is the purpose of break Statement in a loop", "answer":"C"}
    {"text":"Which of the following data types is mutable in python", "answer": "C"}
]
#for the options part there are multiple ways to solve/code this
#in this example i will use lists and sublists

options=[
          ["A. To declare a variable", "B. To create a loop", "C. To perform conditional execution", "D. To define a function"]
          ["A. // comment", "B. /* comment */", "C.  # comment", "D. -- comment"]
          ["A. Returns the length of a list or string", "B. Converts a string to lowercase", "C. . Rounds a floating-point number", "D. Creates an Empty List"]
          ["A. file = open("example.txt", "r")", "B. file = read("example.txt")", "C. file = open("example.txt", "w")","D. file = read_file("example.txt")"]
          ["A. to exit the program", "B. to skip the current iteration and move to the next", "C. to terminate the loop prematurely", "D. to start a new loop"]
          ["A. Tuple", "B. Strings", "C. List", "Dictionary"]
]

#check_answer function
score = 0
def check_answer(user_guess, correct_answer):
    if user_guess == correct_answer:
        return True
    else:
        return False
#for question in question_bank: this loop is incorrect because you can't print out a dict
for question_num in range(len(question_bank)): #output will be int 0, 1, 2, 3,4
    print("****************")
    print(question_bank[question_num["text"]])#provide the key of the part you want to print
    for i in options[question_num]:
        print(i)
        
        #ask the user for input
        guess = input("Enter your answer(A/B/C/D): ").upper()
        
        #check answer
        is_correct=check_answer(guess, question_bank[question_num]["answer"])
        if is_correct:
            print("Correct Answer")
            score += 1
        else:
            print("Incorrect answer")
            print(f"The correct answer is {question_bank[question_num]['answer']}")
        print(f"Your correct score is {score}/{question_num+1 }")    
print(f"Your final score is {score}")
print(f"Your score is {(score/len(question_bank))*100}&")
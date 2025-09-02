# rubab zahra, hanzalah abedeen, jawad mustafa, zainab fatima, minahil manzoor
# QUIZZ GAME

# FIRSTLY, we have used tuple for storing the questions 
# tuple is immutable data will be stored safely in it

questions = ("What is the national language of Pakistan?: ",  
             "Who was the first Prime Minister of Pakistan?: ",  
             "Which city is known as the City of Lights in Pakistan?: ",  
             "What is the highest military award of Pakistan?: ",  
             "Which is the largest province of Pakistan by area?: ",  
             "When did Pakistan win the Cricket World Cup?: ",  
             "What is the name of Pakistan's national poet?: ",  
             "Which river is the longest in Pakistan?: ",  
             "What is the name of Pakistan's national anthem?: ",  
             "When did Pakistan become a nuclear power?: ")  

# options is another tuple.
# Each element is another tuple containing four possible answers (A, B, C, D).
# These options correspond to the respective question in the questions tuple.

options = (("A. Urdu", "B. English", "C. Punjabi", "D. Sindhi"),  
           ("A. Liaquat Ali Khan", "B. Ayub Khan", "C. Zulfikar Ali Bhutto", "D. Muhammad Ali Jinnah"),  
           ("A. Karachi", "B. Lahore", "C. Islamabad", "D. Peshawar"),  
           ("A. Nishan-e-Haider", "B. Sitara-e-Imtiaz", "C. Tamgha-e-Shujaat", "D. Hilal-e-Jurat"),  
           ("A. Punjab", "B. Balochistan", "C. Sindh", "D. Khyber Pakhtunkhwa"),  
           ("A. 1987", "B. 1992", "C. 1999", "D. 2003"),  
           ("A. Faiz Ahmed Faiz", "B. Allama Iqbal", "C. Mirza Ghalib", "D. Ahmed Faraz"),  
           ("A. Indus", "B. Chenab", "C. Ravi", "D. Jhelum"),  
           ("A. Qaumi Tarana", "B. Pak Sarzamin", "C. Milli Naghma", "D. Watan Hamara"),  
           ("A. 1974", "B. 1998", "C. 2000", "D. 2005"))  

# answers is a tuple containing the correct answers for each question.
# Each element corresponds to the correct option for the question at the same position in the questions tuple.

answers = ("A", "A", "A", "A", "B", "B", "B", "A", "A", "B")  

# guesses: An empty list to store the user's answers as they play the quiz
# list is mutable we can make changes to it as per our requirement

guesses = []  

# score: An integer variable to keep track of the number of correct answers
score = 0  

# question_num: Another integer variable to track the current question number in the loop.

question_num = 0  

# for loop: Used to iterate through each question in the questions tuple.
# question will take the value of one question at a time during each loop cycle.

for question in questions:  
    print("----------------------")  
    print(question) 

    # Nested loop: Another loop iterates through options[question_num], which retrieves the options for the current question. Each option is printed.

    for option in options[question_num]:      
        print(option)  

    # input(): This function waits for the user to type something and press Enter.
    # "Enter (A, B, C, D): " is the message shown to the user.
    # .upper(): Ensures the input is converted to uppercase (e.g., 'a' becomes 'A') for consistency.

    guess = input("Enter (A, B, C, D): ").upper()  

    # append(): Adds the user's answer (guess) to the guesses list.

    guesses.append(guess)  

    # Condition: if guess == answers[question_num] checks if the user's guess matches the correct answer for the current question.
    # Correct answer:
    # score += 1 increases the score by 1.
    # "CORRECT!" is printed

    if guess == answers[question_num]:  
        score += 1  
        print("CORRECT!")  

    # Incorrect answer:
    # "INCORRECT!" is printed.
    # The correct answer is displayed using an f-string: f"{answers[question_num]} is the correct answer".

    else:  
        print("INCORRECT!")  
        print(f"{answers[question_num]} is the correct answer")  

    # question_num is incremented by 1 to move to the next question in the next loop cycle.
    question_num += 1  

    # nested loop ends

print("----------------------")  
print("       RESULTS        ")  
print("----------------------")  

# print("answers: ", end=""): Displays the label "answers" without starting a new line (because of end="").
# for answer in answers: iterates through each correct answer and prints it on the same line.

print("answers: ", end="")  
for answer in answers:  
    print(answer, end=" ")  
print()  

# Similar to the answers, the guesses made by the user are printed on the same line.

print("guesses: ", end="")  
for guess in guesses:  
    print(guess, end=" ")  
print()  

# score / len(questions): Divides the number of correct answers (score) by the total number of questions.
# * 100: Converts the result to a percentage.
# int(): Converts the percentage to an integer (removes decimals).

score = int(score / len(questions) * 100)  

# The final score is displayed using an f-string: f"Your score is: {score}%".
print(f"Your score is: {score}%")  

print()
print("THANK YOU FOR PLAYING THE GAME:)!")

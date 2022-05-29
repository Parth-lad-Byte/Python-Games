"""Task : Create a Quiz Game: Step : 1 : Create a Skeliton for the whole quiz : this means creating all the functions
then fill all the info in side the function

"""


# creating a function called new_game : to start of the game
def new_game():
    guesses = []  # list called guesses which is empty for now
    correct_guesses = 0  # start off the game wit 0 correct guesses
    question_num = 1  # starting off the question at question 1

    for key in questions:  # for loop for displaying all the questions and nicknaming it to key
        print("---------------")  # prints --------- to separate question
        print(key)  # prints all the question
        for i in options[
            question_num - 1]:  # nested for loop ( loop in side loop) : with index of the question - 1 :aka starting
            # at 0
            print(i)  # nicknaming options to i
        guess = input("Enter (A,B,C, or D): ")  # asks for user input to ask to pick a b c d
        guess = guess.upper()  # takes the user input and makes it upper case, so no matter what is user type it's
        # always will change it to upper
        guesses.append(guess)  # appending the user inputted guess in to the guess list

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1  # increment each time question by 1
    display_score(correct_guesses, guesses)  # # displays the scores bases on guesses


# ---------------------- # comments to separate
def check_answer(answer, guess):  # creating a function called check_answer to check the user inputted answers
    if answer == guess:  # if statement for if the answer is equal to the guess
        print("CORRECT")  # then print Correct
        return 1  # gives 1 point of answer is correct
    else:  # else statement for if the answer does not equal to the guess
        print("INCORRECT")  # prints Incorrect
        return 0  # gives no point of it's wrong


# ----------------------
def display_score(correct_guesses, guesses):  # creating a function called display_score to show the scores
    print("---------------------")
    print("RESULTS")  # prints the result on  the guesses
    print("---------------------")

    print("Answers: ", end=" ")  # prints the actual answers
    for i in questions:  # for loop for questions
        print(questions.get(i), end=" ")  # get questions and prints the actual correct answers
    print()

    print("Guesses: ", end=" ")  # prints the user guessed answers
    for i in guesses:  # for loop for quesses
        print(i, end=" ")  # get guesses and prints the user guessed ans
    print()

    # calculating the score  bases on correct guesses by length of the score ( which is 4) times 100 : eg (4/4)*100 =
    # 100%
    score = int((correct_guesses / len(questions)) * 100)
    print("Your score is " + str(
        score) + "%")  # prints your score is : "the score " with string and % ( percentage symbol)


# ------------------------

def play_again():  # creating a function called play_again : if the user would like to play again or not

    response = input(
        "Do you want to play again?: (yes or no): ")  # asks user for if they wish to play again and allows user to
    # input : yes or no
    response = response.upper()  # changes user input to upper case

    if response == "YES":  # if statement for : if user response == ( means response is equals ) YES
        return True  # returns boolean ( True ) if repose equals YES
    else:  # else statement ( if returns no)
        return False  # if no then return False


# ----------------------

# Disctionary named question : which consists of Question and the right answer linked to that question
questions = {
    "Who crated Python?:": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?:": "C",
    "Is the Earth round?:": "A"
}
# 2D list option : which consists of multiple choice answers and letter assigned to it
options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2002", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A.True", "B. False", "C. sometimes", "D. What's Earth?"]]

new_game()  # calling new_game function to began new game

while play_again():  # while statement : if response is YES : They wish to play again
    new_game()  # calls the new game function : restarts the game

print("Bye, Felicia")  # else if user say no : they don't wan't to play the exits while loop and prints this

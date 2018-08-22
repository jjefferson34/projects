survey1 = {


}

survey2 = {

}

#questions1 = ["What is your favorite animal?", "How old are you?", "What career path interests you the most?", "Do you consider lobsters human?", "What is your family history?", "What is your political affiliaton?", "Do you believe in the supernatural?", "What is your religious denomination?", "What video games do you normally play?"]#
print("Welcome to the Survey!")
print("Let's start with some questions, shall we?")

answer = input("What is your favorite animal?: ")
survey1['animal'] = answer

answer = input("How old are you?: ")
survey1['age'] = answer

answer = input("What career path interests you the most?: ")
survey1['career'] = answer

answer = input("Do you consider lobsters human?: ")
survey1['lobsters'] = answer

answer = input("What is your family history?: ")
survey1['history'] = answer

answer = input("What is your political affiliaton?: ")
survey1['political'] = answer

answer = input("Do you believe in the supernatural?: ")
survey1['supernatural'] = answer

answer = input("What is your religious denomination?: ")
survey1['religious'] = answer

answer = input("What video games do you normally play?: ")
survey1['games'] = answer

print(survey1)

print("Thank you for completing our survey!")
print("Please contact this number if you have any questions!")
print("1-800-CRIPPLING-DEPRESSION")

answer = input("Would you like to take another survey?: ")
if answer == ("yes"):
    print("Welcome to Survey #2!")
#add more questions#







else:
    print("You will pay for your insolence!")

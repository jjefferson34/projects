


def introduction():
    print("Greetings!")
    print("I am Zaxor! Ask me anything you like, or just talk to me!")

def main():
    introduction()
    while True:
        answer = input("(Say something!) ")
        process_input(answer)

def process_input(answer):
    if (answer == "Hello there!"):
        occupation()
    if (answer == "What are your thoughts on spirituality or God?"):
        spirituality()
    if (answer == "Can you sing?"):
        sing()
    if (answer == "Can you go heck off?"):
        say_default()

def occupation():
    print("I am Zaxor, Destroyer of Galalxies!")
def say_default():
    print("...Huh... Can you ask me something else...?")
def spirituality():
    print("Hmm... I don't really belive in a higher power, besides me of course!")
def sing():
    print("My singing is very bad! Sounds like cats giving birth...")


# NO TOUCHY! Setup code that runs the main() function.
if __name__ == "__main__":
  main()

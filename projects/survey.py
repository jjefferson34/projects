import json #using json#
list = []
questions = ["What is your pet's name? ", "What is your age? ", "What is your favorite animal? ", "What career path interests you the most? ", "Do you consider lobsters human? ", "What is your family history? ", "What is your political affiliaton? ", "Do you believe in the supernatural? ", "What is your religious denomination? ", "What video games do you normally play? "]
keys = ['name', 'age', 'animal', 'career', 'lobsters', 'history', 'political', 'supernatural', 'religious', 'games']

while True:
    responses = {}
    for i in range(len(questions)):
        answer = input(questions[i])
        responses[keys[i]] = answer
    list.append(responses)
    again = input("Would you like to retake the survey? ")
    if again == "nope":
        break
    elif again == "yes":
        continue
#print(list)

#using json objects#
file = open("allanswers.json", "r")
olddata = json.load(file)
list.extend(olddata)
file.close()

listToJSON = json.dumps(list)
file = open("allanswers.json", "w")
file.write(listToJSON)
file.close()

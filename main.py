import random #importing the random library

#variables:
something=2
anything="Hello world"
#a list:
food = ["pizza","pasta","cannelloni","sushi"]
dinner=random.choice(food)
print (dinner)


#a function:
def choices():
  choicesList=["rock","paper","scissors"]
  player_choice=input("Enter a choice (rock-paper-scissors):") 
  opponent_choice= random.choice(choicesList)
  #dictionary of choices:
  choicesDic={"Player":player_choice,"Opponent":opponent_choice}
  return choicesDic

def greeting():
  return "Hi!"

#calling a function:
greeting()

response=greeting() ## response will be a variable
print(response) #prints out to the console

choicesVar=choices()
print(choicesVar)

color="Red"
#dictionary: key+value
dict={"Name": "beau","colour":color}

print(anything)
print(something)
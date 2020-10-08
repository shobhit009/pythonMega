import json

# get_close_matches module compares a entered word with another word and generates a score of similarity value
from difflib import get_close_matches

data = json.load(open("data.json"))

# Method to show definition of entered keyword
def showDefinition(inp):
    inp = inp.lower()
    if inp in data:
        return data[inp]
    elif inp.upper() in data:
        return data[inp.upper()]
    elif inp.title() in data:
        return data[inp.title()]
    elif len(get_close_matches(inp,data.keys())) > 0:
        yn = input("Did you mean %s? Enter 'y' for yes else 'n':" %get_close_matches(inp, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(inp, data.keys())[0]]
        elif yn.lower() == "n":
            return "Please check the word"
        else:
            return "We ddidn't understand the word"        

    else:            
        return "Keyword doesn't exist"              

# asking for user input
user_input = input("Enter Keyword: ")
output = showDefinition(user_input)

#checking if output is of list type and thenn printing each element in the list
if (type(output) == list):
    for items in output:
        print (items)
else:
    print (output)        




   
import json #to read json file 
import difflib # difference library for comparing different possible values and in this case possible case of matching the words. 
from difflib import get_close_matches #it is method that deals with the close up values and is an algorithm to find possible match with cutoff limiter.


data = json.load(open("data.json")) #loading json file

def search(word): #method to do work
   
    if word in data: #searching key inside dictonary and displaying its value if found or else showing error message
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well 
        return data[word.title()]
    elif word.upper() in data: #in case user enters ACRYMNSlike USA or NATO
        return data[word.upper()]
    elif get_close_matches(word,data.keys())!=[]: #get_close_matches(word,data.keys(),cutoff=0.8) != [] or len(get_close_matches(word,data.keys())) > 0 can be used to check condition there should be recomended matches to execute 
        choice = input("Did you mean %s instead?\nEnter Y for YES and N for NO.: " %get_close_matches(word,data.keys())[0].lower())
        if choice == 'y':
            return data[get_close_matches(word,data.keys())[0]]
        elif choice =='n':
            return "The word doesnot exist. Double check.."
        else:
            return "Matches not Found!!"
    else:
        return ( "The word doesnot exist. Double check...")
        


    

    

def start():
    word = input("Enter word to search: ") #user input
    result = search(word.lower()) # lower() converting into lower case as all of our data is in lowercase which will match whether user   input uppor or lower case word
    if type(result) == list:
        i=1
        for  item in result:
            print(str(i)+". "+ item)
            i+=1
    else:
        print(result)

    choice = input("\n\nDo you want to Search Again?\nEnter Y for YES and N for NO.: " ).lower()
    if choice == 'y':
        start()
    elif choice =='n':
        print("\n\nThank you...\n Quiting...")
        exit(0)
    else:
        print("ERROR YOU TYPED OUT OF OPTION.\nEXITING!!!...")
    
start()

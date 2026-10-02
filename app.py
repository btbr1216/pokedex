import json
## Open the JSON file of pokemon data
pokedexfile = open("./pokedex.json", encoding="utf8")
itemsfile = open("./types.json", encoding="utf8")
movesfile = open("./types.json", encoding="utf8")
typesfile = open("./types.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
pokedex = json.load(pokedexfile)
items = json.load(itemsfile)
moves = json.load(movesfile)
types = json.load(typesfile)

languageanswers = [
    {
        "English": "Would you like to change your language? English, Chinese, Japanese.",
        "Chinese": "你想換語言嗎? English, Chinese, Japanese.",
        "Japanese": "言語を変えたいですか? English, Chinese, Japanese."
    },
    {
        "English": "Successfully changed language!",
        "Chinese": "語言已成功更改!",
        "Japanese": "言語を変更しました!"
    }, 
    {
        "English": "Cannot change language to the same one", 
        "Chinese": "無法把語言改成一樣的",
        "Japanese": "同じ言語には変更できません"
    }
]

language = "English"

while True:
    answer = input(languageanswers[0][language]) # 0
    if answer == "English":
        if language != "English":
            language = "English"
            print(languageanswers[1][language]) # 1
        else:
            print(languageanswers[2][language]) # 2
    elif answer == "Chinese":
        if language != "Chinese":
            language = "Chinese"
            print(languageanswers[1][language]) # 1
        else:
            print(languageanswers[2][language]) # 2
    elif answer == "Japanese":
        if language != "Japanese":
            language = "Japanese"
            print(languageanswers[1][language]) # 1
        else:
            print(languageanswers[2][language]) # 2
        

for i, v in enumerate(pokedex):
    print()



# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

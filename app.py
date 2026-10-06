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

language = "english"

def languagefunction(gottenlanguage):


    languageanswers = [
    {
        "english": "Would you like to change your language? english, chinese, japanese, french.",
        "chinese": "你想換語言嗎? english, chinese, japanese, french.",
        "japanese": "言語を変えたいですか? english, chinese, japanese, french.",
        "french": "Voulez-vous changer votre langue? english, chinese, japanese, french."
    },
    {
        "english": "Successfully changed language!",
        "chinese": "語言已成功更改!",
        "japanese": "言語を変更しました!",
        "french": "Langue changée avec succès!"
    }, 
    {
        "english": "Cannot change language to the same one", 
        "chinese": "無法把語言改成一樣的",
        "japanese": "同じ言語には変更できません",
        "french": "Impossible de changer la langue pour la même"
    }
    ]


    answer = input(languageanswers[0][gottenlanguage]) # 0
    if answer == "english":
        if gottenlanguage != "english":
            gottenlanguage = "english"
            print(languageanswers[1][gottenlanguage]) # 1
        else:
            print(languageanswers[2][gottenlanguage]) # 2
    elif answer == "chinese":
        if gottenlanguage != "chinese":
            gottenlanguage = "chinese"
            print(languageanswers[1][gottenlanguage]) # 1
        else:
            print(languageanswers[2][gottenlanguage]) # 2
    elif answer == "japanese":
        if gottenlanguage != "japanese":
            gottenlanguage = "japanese"
            print(languageanswers[1][gottenlanguage]) # 1
        else:
            print(languageanswers[2][gottenlanguage]) # 2
    elif answer == "french":
        if gottenlanguage != "french":
            gottenlanguage = "french"
            print(languageanswers[1][gottenlanguage]) # 1
        else:
            print(languageanswers[2][gottenlanguage]) # 2
    return gottenlanguage

language = languagefunction(language)



# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.


# for _, v in enumerate(pokedex):
#     print(v["name"][language])


# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user


# typetolookfor = input("Input type of pokemon you want to look for")
# for _, v in enumerate(pokedex):
#     for _, v2 in enumerate(v["type"]):
#         if v2 == typetolookfor:
#             print(v["name"][language])


#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 



userinput = input("Input pokemon to find")
timestorun = len(userinput)

currentlist = []

for i in range(timestorun):

    if i == 0:
        for _, v in enumerate(pokedex):
            if v[1][language][i] == userinput[i]:
                currentlist.append(v[1][language])
        continue

    newlist = []    
    
    for _, v in enumerate(currentlist):
        if v[1][language][i] == userinput[i]:
            newlist.append(v[1][language])

    currentlist = newlist

for _, v in enumerate(currentlist):
    print(v)

#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
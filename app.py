import json
## Open the JSON file of pokemon data
pokedexfile = open("./pokedex.json", encoding="utf8")
itemsfile = open("./items.json", encoding="utf8")
movesfile = open("./moves.json", encoding="utf8")
typesfile = open("./types.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
pokedex = json.load(pokedexfile)
items = json.load(itemsfile)
moves = json.load(movesfile)
types = json.load(typesfile)

language = "english"

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
    },
    {
        "english": "Input type of pokemon you want to look for",
        "chinese": "輸入你想查找的寶可夢類型",
        "japanese": "探したいポケモンのタイプを入力して",
        "french": "Saisis le type de Pokémon que tu veux chercher"
    },
    {
        "english": "Input pokemon to find",
        "chinese": "輸入寶可夢來搜尋",
        "japanese": "見つけたいポケモンを入力して",
        "french": "Entrez le Pokémon à trouver"
    },
    {
        "english": "No pokemon found with matching name.",
        "chinese": "找不到名稱相符的寶可夢。",
        "japanese": "一致する名前のポケモンが見つかりませんでした。",
        "french": "Aucun Pokémon trouvé avec ce nom."
    },
    {
        "english": "Input pokemon to find out which moves they can learn",
        "chinese": "輸入寶可夢來看看它們可以學哪些招式",
        "japanese": "ポケモンを入力して、覚えられる技を調べよう",
        "french": "Saisis un Pokémon pour savoir quels mouvements il peut apprendre"
    },
    {
        "english": "Moves that your pokemon can learn:",
        "chinese": "你的寶可夢可以學會的招式",
        "japanese": "あなたのポケモンが覚えられる技:",
        "french": "Coups que ton Pokémon peut apprendre:"
    },
    {
        "english": "Cannot find pokemon.",
        "chinese": "找不到寶可夢。",
        "japanese": "ポケモンが見つからない。",
        "french": "Impossible de trouver de Pokémon."
    }

]
def languagefunction(gottenlanguage):

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


# for v in pokedex:
#     print(v["name"][language])


# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user


# typetolookfor = input(languageanswers[3][language])
# for _, v in enumerate(pokedex):
#     for _, v2 in enumerate(v["type"]):
#         if v2 == typetolookfor:
#             print(v["name"][language])


#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 



userinput = input(languageanswers[4][language])
timestorun = len(userinput)

currentlist = []

for i in range(timestorun):

    if i == 0:
        for _, v in enumerate(pokedex):
            if v["name"][language][i] == userinput[i]:
                currentlist.append(v["name"][language])
        continue

    newlist = []    
    
    for _, v in enumerate(currentlist):
        if v[i] == userinput[i]:
            newlist.append(v)

    currentlist = newlist
    if len(currentlist) == 0:
        break

for _, v in enumerate(currentlist):
    print(v)

if len(currentlist) == 0:
    print(languageanswers[5][language])



#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!

# pokemontocheckmovesfor = input(languageanswers[6][language])
# typeofthepokemon = 0

# for _, v in enumerate(pokedex):
#     if v["name"][language] == pokemontocheckmovesfor:
#         typeofthepokemon = v["type"]

# listofmoves = []

# if typeofthepokemon != 0:
#     for _, v in enumerate(moves):
#         for _, v2 in enumerate(typeofthepokemon):
#             if v["type"] == v2:
#                 listofmoves.append(v["ename"])

#     print(languageanswers[7][language])
#     for _, v in enumerate(listofmoves):
#         print(v)

# else:
#     print(languageanswers[8][language])
import random
#character name input
characters_names=[]
print("Welcome to the character generator!")
print("let's name the adventures")
for i in range(1,6):
    name=input("character {}:".format(i))
    characters_names.append(name)
#list of characters types
characters_type=["Warrior","Wizard","Potato"]
team=[]
for name in characters_names:
    characters_type=random.choice(characters_type)
    health=random.randint(5,10)*3 if characters_type=="potato" else random.randint(5,10)
    
    strength=random.randint(5,10)*3 if characters_type=="Warrior" else random.randint(5,10)
    magic=random.randint(5,10)*3 if characters_type=="potato" else random.randint(5,10) 
    character = {"name": name, "type": characters_type, "health": health, "strength": strength, "magic": magic}
    team.append(character)

print("\n***YOUR CHARACTERS ARE COMPLETE*****")
for character in team:
    print("\n{} est un(e) {} !".format(character["name"], character["type"]))
    print("Health : {}".format(character["health"]))
    print("Strength: {}".format(character["strength"]))
    print("Magic : {}".format(character["magic"]))

    print("\nHappy adventuring!")
import random


def generate_character(name):
    health = random.randint(1, 10)
    strength = random.randint(1, 10)
    magic = random.randint(1, 10)

    role = random.choice(["Warrior", "Wizard", "Potato"])
    if role == "Warrior":
        strength *= 3
    elif role == "Wizard":
        magic *= 3
    elif role == "Potato":
        health *= 3

    return {"name": name, "role": role, "health": health, "strength": strength, "magic": magic}


def display_character(character):
    print(f'"{character["name"]}" is a {character["role"]}!\n'
          f'\tStrength: {character["strength"]}\n'
          f'\tMagic: {character["magic"]}\n'
          f'\tHealth: {character["health"]}')


# enter 5 names
characters = []
for i in range(5):
    name = input(f"Character {i + 1}: Enter a name: ")
    character = generate_character(name)
    characters.append(character)

# characters info
print("*** YOUR CHARACTERS ARE COMPLETE ***")
for character in characters:
    display_character(character)

print("\nHappy adventuring!")

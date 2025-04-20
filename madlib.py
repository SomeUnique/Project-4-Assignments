print("Welcome to the Mad Libs Game!")
print("Fill in the blanks below to create your story.\n")

name = input("Enter a name: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb ending in -ing: ")
food = input("Enter a type of food: ")

story = f"""
One day, {name} went to {place}. 
It was a very {adjective} day. 
Suddenly, a {animal} appeared and started {verb} all around!
Luckily, {name} had some {food} and offered it to the {animal}.
They became best friends and lived happily ever after.
"""

print("\nHere's your story!")
print(story)

from random import choice

print("We are going to hear a story about a dragon!")
name = input("What is the name of the dragon? ")
size = input("Is your dragon big or small? ")
age = input("What is the age of the dragon? ")

if int(age) > 1000:
    description = "an old"
else:
    description = "a young"
    
print("Excellent.  The dragon is called " + name)
print("Excellent.  The dragon's size is " + size)
print("Excellent.  The dragon's age is " + age)
print("Excellent.  The dragon is an " + description + " dragon.")
print("")
print("")

things = ["goblins", "cakes", "chocolate", "rocks", "trees"]
friends = ["brady", "rachel", "candace", "carol"]
actions = ["kiss", "throw", "steal", "drink"]
places = ["downtown Dallas", "G-Town", "Westwood", "Barbados"]

thing = choice(things)
friend = choice(friends)
action = choice(actions)
place = choice(places)
story = "Once upon a time, there was a dragon called " + name + ". The dragon was a very " + description + " creature, and it was very " + size + ". It liked nothing better than to " +  action + " " + thing + ". Sadly, the dragon was so great at this that it ran out of " + thing + " to " + action + " in " + place + ". The dragon became very bored. Luckily the dragon had a friend called " + friend + ". " + friend + " knew where the dragon could find lots of " + thing + " and the two of them travelled far away from " + place + " and found a land filled with lots of lovely " + thing + " to " + action + ". " + name + " and " + friend + " lived happily ever, with all the " + thing + " they wanted."

print(story)
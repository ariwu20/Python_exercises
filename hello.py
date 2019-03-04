import random 
text = open("harrypotter.txt").readlines() # the name of the file, relative to where the script is

for line in text:
    line = line.strip()
    words = line.split(" ")
    words = [word for word in words if len(word) > 5]   # all the words that have 5 or more characters in them
    words = [word for word in words if word.startswith("t")]
    new_line = " ".join(words)
    print(new_line)
    

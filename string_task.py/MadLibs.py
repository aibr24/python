#Mad-Libs Task



Number = input("Choose a Number.:  ")
Noun = input("Choose a plural Noun.: ")
Name = input("Choose a Name.: ")
Scream = input("Pick a sentence.: ")
Verb = input("Pick a Verb.: ")

madlib = "It was %s o'clock when I heard a knock on the door. I opened the door and there was a box full of %ss with a note saying from Mr. %s. Just as I closed the door I heard a scream'%s!'. I froze in place and all I could do was %s." % (Number, Noun, Name.capitalize(), Scream.upper(), Verb)

print(madlib)

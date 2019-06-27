'''create a list of skills----------
----------creata an empty dictionary called cv, will hold all of input info---------
            ask user for name age experience and add to dictionary with key'''


import time

skills = ["Athletic", "MSoffice", "Team-Player", "Healer", "Pick-Pocket", "Python"]
cv = {}


print("Welcome to Cripco Cuz application center.")
cv["name"] = input("What is your street name?: ")
cv["age"] = input("How old are you?: ")
cv["experience"] = input("How long have you been in these streets?: ")




def printcv(cv):
	for val in cv:
		info = cv[val]
		print (info)

printcv(cv)

time.sleep(.5)
print("please pick a skill from the given options that would define you best")
time.sleep(.5)

def choose_skill1(skills):
	for number,letter in enumerate((skills),1):
		print(number, letter)
	cv["skill"] = input("Enter the corresponding number...: ")
	if cv["skill"] == "1":
		cv["skill"] = skills[0]
		return cv["skill"]
	elif cv["skill"] == "2":
		cv["skill"] = skills[1]
		return cv["skill"]
	elif cv["skill"] == "3":
		cv["skill"] = skills[2]
		return cv["skill"]
	elif cv["skill"] == "4":
		cv["skill"] = skills[3]
		return cv["skill"]
	elif cv["skill"] == "5":
		cv["skill"] = skills[4]
		return cv["skill"]
	elif cv["skill"] == "6":
		cv["skill"] = skills[5]
		return cv["skill"]
	else:
		print("Please Enter A Number Between 1 & 6:")
		return choose_skill1(skills)

def choose_skill2(skills):
	sk2 = input("Please choose another skill or N if none...:")
	if sk2 == "1":
		cv["skill2"] = skills[0]
		return cv["skill2"]
	elif sk2 == "2":
		cv["skill2"] = skills[1]
		return cv["skill2"]
	elif sk2 == "3":
		cv["skill2"] = skills[2]
		return cv["skill2"]
	elif sk2 == "4":
		cv["skill2"] = skills[3]
		return cv["skill2"]
	elif sk2 == "5":
		cv["skill2"] = skills[4]
		return cv["skill2"]
	elif sk2 == "6":
		cv["skill2"] = skills[5]
		return cv["skill2"]
	elif sk2  == "N" or "n":
		cv["skill2"] = "nul"
		return cv["skill2"]
	else:
		print("Please Enter A Number Between 1 & 6:")
		return choose_skill2(skills)

def acpt(cv):
	if cv["age"] >= "12" and (cv["skill"] == "Athletic") == True:
		return True
	elif cv["age"] >= "12" and (cv["skill2"] == "Athletic") == True:
		return True
	else:
		return False
choose_skill1(skills)
choose_skill2(skills)
acpt(cv)
if acpt(cv) is True:
	print("WELCOME TO THE GANG ")
else:
	print("NAH FAM.")



# I TRIED LOOKING FOR A WAY TO MAKE BOTH SKILL ONE AND TWO TO BE IN THE SAME KEY I COULDNT FIND IT #
#### PLEASE TELL ME IF THE FINAL RESULT ISNT WHAT IM SUPPOSED TO HAVE , CUZ I THINK I MIGHT HAVE MISUNDERSTOOD ####
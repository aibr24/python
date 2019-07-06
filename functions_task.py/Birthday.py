#check birth funct (year,month,day)
#returns F if in the future, Return T if past
###
#clac age funct (year,month,day)
#calcs age and prints it
#no return
# ask user for dates, use check birht funct,if T use calc age funct
#if F print no
##
#
from datetime import datetime, date

today = date.today()
ty = today.year
tm = today.month
td = today.day
print(today.year)
def check_birthdate(year,month,day,ty,tm,td):
	if ty>=year:
		return True
	elif ty<year:
		return False
	elif day <= td:
		return True
	elif month < tm:
		return True
	elif month > tm:
		return False 
	else:
		return False


def calculate_age(year,month,day,tm,ty,td):
	age = "You Are " + str(ty - year) +" years, " + str(abs(tm - month)) + " months, " + str(abs(td - day)) + " days old!"
	print(age)




year = int(input("Enter The Year You Were Born In: "))
month = int(input("Enter Yout Month of Birth: "))
day = int(input("Enter The Day You Were Born: "))

if check_birthdate(year,month,day,ty,tm,td) == True:
	print(calculate_age(year,month,day,tm,ty,td))
else:
	print("you are from the future!")



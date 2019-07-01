print("Welcome To HRSystems")
import time

class Employee(object):
	Emp = []

	def __init__(self, personName,personAge, EmpSalary, EmpDate):
		self.name = personName
		self.age = personAge
		self.salary = EmpSalary
		self.employment_year = EmpDate
		self.empyr = abs(EmpDate - 2019)

	def __str__(self):
		return "[name: "+ self.name +', age: '+str(self.age)+', working years: ' + str(self.empyr) + ', Salary: '+str(self.salary) +']\n'
	def __repr__(self):
		return "name: "+ self.name +', age: '+str(self.age)+', working years: ' + str(self.empyr) + ', Salary: '+str(self.salary)+ '\n'

class Manager(Employee):
	MNG = []
	#empdata = "[name: "+ self.name +', age: '+str(self.age)+', working years: ' + str(self.empyr) + ', Salary: '+str(self.salary) +', Bonus: '+(str(self.MGbonus)) +"]"

	def __init__(self, personName,personAge, EmpSalary, EmpDate, bonusP):
		Employee.__init__(self, personName,personAge, EmpSalary, EmpDate)
		self.bonusP = bonusP
		self.MGbonus = self.salary * bonusP

	
	def __str__(self):
		return "[Name: "+ self.name +', Age: '+str(self.age)+', Working years: ' + str(self.empyr) + ', Salary: '+str(self.salary) +', Bonus: '+(str(self.MGbonus)) +"]\n"	
	
	def __repr__(self):
		return "{Name: "+ self.name +', Age: '+str(self.age)+', Working years: ' + str(self.empyr) + ', Salary: '+str(self.salary) +', Bonus: '+(str(self.MGbonus)) +"}\n"


newemp = Employee("ali",25,1050,2017)
newemp2 = Employee("bart", 21, 2000, 2010)
newmgr = Manager("Ahmad", 23, 2000, 2019, 0.2)
print(str(newemp))
print(repr(newemp))	
print(str(newemp2))

WTD = ""
MNG = []
Emp = []
while WTD != "5":
	WTD = input("1. ADD an Employee?\n2. ADD a Manager?\n3. SHOW Employees?\n4. SHOW Managers?\n5. ---EXIT---\n\nWhat would you like to do?: ")
	if WTD == "5":
		break
	elif WTD == "1":
		print("-"*20)
		print("\n")
		x=(input("Name: "))
		y=(int(input("Age: "))) 
		z=(int(input("Salary: ")))
		f=(int(input("Year of employmen: ")))
		eip = Employee(x,y,z,f)
		Emp.append(eip)
	elif WTD == "2":
		x=(str(input("name: ")))
		y=(int(input("age: "))) 
		z=(int(input("Salary: ")))
		f=(int(input("Year of employment: ")))
		g=(float(input("Bonus %: " )))
		mip = Manager(x,y,z,f,g)
		MNG.append(mip)
	elif WTD == "3":
		print(Emp)
		time.sleep(1)
	elif WTD == "4":
		print(MNG)
		time.sleep(1)
	else:
		slcterr = "please make sure you input a number between 1~5 \n"
		print(slcterr.capitalize())
		time.sleep(1)



print("\n\t-----------EXITING-----------")
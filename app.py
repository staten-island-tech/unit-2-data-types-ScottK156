""" #Tip and total calculator
def add(x,y):
    print(round(x + y))
bill= float(input("How much was the bill"))
print(bill)
tip = int(bill * 0.15)
print(round(tip))
print(add(tip,bill)) """

""" sentence = input("Make a sentence")  # creates an input where you type your sentence
y = sentence.split() #turns the input into a list
total= len(y)   #counts the amount of items in the list
print("Total number of words in the sentence is",total) #prints the number of items in the list """
""" #madlibs project
print(f"I was *verb1* down the street. Then I saw a *noun*.Right next to *noun* I saw  *famous* they were *verb2* from *number* dog.")
verb1 = input("Verb1")
noun = input("Noun")
famous = input("Famous Person")
verb2 = input("Verb2")
number = input("Number")
if number == 1 :
    dog = "dog" 
else:
    dog ="dogs"
madlib = (f"I was {verb1} down the street. Then I saw a {noun}.Right next to {noun} I saw  {famous} they were {verb2} from {number} {dog}.")
print(madlib) """
""" #Tells if a number is odd or even
number = float(input("Give me a munber"))
if number %  2 == 0 :
 print("The number is even")
else:
 print("This number is odd")
 """
""" #tip calcultor based on service
bill= float(input("How much was the bill"))
service = input("How was the service")
if service == "okay":
    tip = bill * 0.15
elif service == "good":
   tip = bill * 0.20
elif service == "great":
    tip = bill * 0.25
else:
   tip = 0
print(f"Your tip will be {tip}")
 """
""" #facoizees a number(finds the factors)
number = int(input("Give me a Number"))
factors = []
x = 0
for i in range(1,number + 1):
    x = x + 1
    if number % x == 0:
        factors.append(i)
print(factors) """
""" #Finds the GCF
number = int(input("Give me a Number"))
factors = []
x = 0
for i in range(1,number + 1):
    x = x + 1
    if number % x == 0:
        factors.append(i)
print(factors)
numbers = int(input("Give me a Number"))
factorss = []
x = 0
for i in range(1,numbers + 1):
    x = x + 1
    if numbers % x == 0:
        factorss.append(i)
print(factorss)
common_items = []
for item in factors:
    if item in factorss:
      common_items.append(item)
 
greatest_common = max(common_items)
print("The greatest common number is:", greatest_common) """
while True:    
 x = int(input("Give me a number"))
 if x == 0:
   print("Error")
 elif x > 0:
    for i in range(10):
      z = x *  i
      print(z)
      if i == 10:
       done = input("Would you like to continue or exit")
 elif done.lower() == "exit":     
  break
 elif done.lower() == "continue":
   continue
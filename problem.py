y = 1

x = int(input("Give me a number"))

while True:
 if x == 0:
    print("Error give me another number")
    x = int(input("Give me a number"))
 elif x == "exit":
     break
 for i in range(11):
    z = y * x
    print(z)
    y += 1
    if y == 11:
      x = int(input("Give me a number"))
      y = 1
    
  

   
   

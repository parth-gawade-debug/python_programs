print("enter marks out of 100")
marks = int(input())
if(marks >=90 and marks <=100):
    print("grade A")
    
elif(marks >=80 and marks <90):
    print("grade B")
elif(marks >=70 and marks <80):
    print("grade C")
elif(marks >=60 and marks <70):
    print("grade D")
elif(marks >=50 and marks <60):
    print("grade E")
elif(marks >=0 and marks <50):
    print("grade F")
else:
    print("invalid marks")

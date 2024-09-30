x = int(input("Enter a number: "))

c = "#"
s = " "
for i in range(x):
    print(s*(x-i-1) + c*(2*i+1))
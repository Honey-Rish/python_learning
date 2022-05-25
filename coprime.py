num1 = int(input("enter the number 1:"))
num2 = int(input("enter the number 2:"))
ac = min(num1, num2)
for i in range(1, ac + 1):
    # for checking of condtion #any variable count start from 0 to make sure it doesnt get subtract we use ac=1
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

if hcf == 1:
    print("its a coprime")
else:
    print("not a coprime")


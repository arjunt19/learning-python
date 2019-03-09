base  = int(input("enter a base"))
exponent = int(input("exponent?"))
print("the answer is", base ** exponent)
def square(number):  # python method syntax
    number = number**2
    return number #indentations actually matter, its how python distinguishes end
print(square(2))
def tellCelsius():
    Farenheit = float(input("tell F"))
    print(Farenheit, "= celsius ", (Farenheit-32) * (5/9) )
    return Farenheit
tellCelsius();
n = 0;
while n<4:
    print(n)
    n = n+ 1
print("done")
for n in range(1,4):
    print(n)
print("done")


def invest(amt, rate, time):
    for n in range(1 , time):
        amt = (amt * (1 + (rate / 100)))
    return amt


print(invest(1,2,3))
invest(100, 5, 8)

a = 3
b = 6
if (a == 5) and (b==6):
    print("yuihrd")
elif a==6 and b==6:
    print("doggy")
else:
    print("cat")
for n in range(1,6):
    print(n)
try:
    print("doggytime")
except TypeError:
    print("yuhrd")

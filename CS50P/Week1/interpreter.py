ex = input("Expression: ")

a = ex.split(" ")

x = float(a[0])
y = a[1]
z = float(a[2])

if y == "+" :
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    print(x/z)

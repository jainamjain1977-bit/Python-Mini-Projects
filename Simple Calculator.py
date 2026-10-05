a = float(input("enter the first number:"));
b = float(input("enter the second number:"));
print("choose:+ - * /");
op = input("enter operator:");
if op == "+":
    result = a+b;
elif op == "-":
    result = a-b;
elif op == "*":
    result = a*b;
elif op == "/":
    result = a/b;
else:
    result = "invalid operator";
print("Result:",result);

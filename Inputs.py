import sys;

def calc():
    operandOne = int(raw_input("Enter a number"));
    operation = raw_input("Enter an operation (+-*/)");
    operandTwo = int(raw_input("Enter second number"));
    output = 0;
    if (operation == "+"):
        output = operandOne + operandTwo;
    elif (operation == "-"):
        output = operandOne - operandTwo;
    elif (operation == "*"):
        output = operandOne * operandTwo;
    elif (operation == "/"):
        output = operandOne / operandTwo;
    else:
        print("You failed to follow instructions");

    return output;

output = 0;

while(output == 0):
    output = calc();

print(output);

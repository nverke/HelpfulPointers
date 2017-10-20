# Hey so I realized that I never taught you about loops. So here is my best.
# I am trying to stay away from teaching coding as literacy so try not to think
# of all of this as something to memorize. The important thing to think about
# is the data manipulation and flow of an algorithm not that actual nuts and
# bolts of the code itself. With that being said here are some nuts and bolts
# that can help you implement an algoritm.

# There are two major types of loops that you can see implementations of in just
# about every single programming language that exists. They arent exactly
# perfect but programmers clearly think that they are useful.

# The first is the "while" loop. Shown below is a while loop that increments a
# variable x.
variable = 0;
condition = True; #This is a boolean value. It can either be True or False;
while(condition): #Inside of the while() function we have a condition
    # The indented lines under the while loop will get run as long as the
    # condition evaluates to True.

    # set the value of variable equal to its current value + 1.
    variable = variable + 1;

    # If variable is greater than or equal to 100 then set the condition to false.
    if variable >= 9:
        condition = False;

    #This will print out 1-9.
    print(variable);

    # Here the indented code ends so the program will jump back up to the while
    # statement and check if the condition is True or False.


# The second type is a "for" loop. This is really just a more complicated while
# loop that emphasizes iteration (going through everything in some collection).

collection = ["A","B","C","D","E","F"]; # Just an array full of letters.

#The variable "item" will become each letter in "collection" in order.
for item in collection:

    # The item variable will change into each of the items in the collection
    # then run the code that is indented below before changeing to the next letter.

    # This will print out A-F.
    print(item);


# For fun I will go ahead and create a for loop using a while loop.
print(" ");

# This will be used to keep track of which letter we want to print.
index = 0;
#              0   1   2   3   4   5
collection = ["A","B","C","D","E","F"];

# len() is a function that returns the length of an array
lengthOfCollection = len(collection); # This will be equal to 6.

condition = True; # Our boolean variable will be reasigned when we are done.

while(condition):

    # This is python code for "retrieve the element of collection at this index."
    letterToBePrinted = collection[index];

    print(letterToBePrinted);

    index = index + 1; # Increment our index.

    # Be careful with checks like this. They are the cause of one of the most
    # common errors in coding, the "off by one" error. Basically we want to make
    # sure that the loop stops before we try to retrieve something that is not
    # in the array (aka the item at index 6 (the array only goes up to index 5))
    # This is known as an arrayIndexOutOfBounds. Basically we check to make sure
    # that when the index is equal to 6 that we stop looping and dont ever try
    # to get that index of the array.
    if index == lengthOfCollection:
        condition = False;

# See how much more code that is when you use a while loop to iterate?
# Thats why for loops exist!


# Double fun times. To be fair to the while loop this is the same code...
print(" ");

index = 0;
collection = ["A","B","C","D","E","F"];
while index <= len(collection):
    print(collection[index]);
    index += 1;

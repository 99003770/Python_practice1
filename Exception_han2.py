# Program to depict else clause with try-except
# Function which returns a/b
def exp(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
# Driver program to test above function
exp(2.0, 3.0)
exp(3.0, 3.0)

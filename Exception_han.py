# Python program to demonstrate finally
a=5
b=0

try:
    print("resource open")
    print(a/b)
except Exception:
    print("cannot divide a number by zero")
finally:
    print("resource closed")

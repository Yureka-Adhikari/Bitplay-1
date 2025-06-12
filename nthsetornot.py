def setornot(number,n):
    if number & (1<<n):
        print(f"Set bit at position {n} in {number} is set")
        
    else:
        print(f"Set bit at position {n} in {number} is not a set")

number = int(input("Enter a number : "))
n = int(input("Enter the position of bit in the number : "))
setornot(number,n)
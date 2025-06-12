def OnesAndZeroes(n):
    zero = 0
    one = 0
    
    while (n):
        if (n & 1 == 1):
            one += 1
        else:
            zero += 1
            
        n >>= 1
            
    print(f"The number of ones in {n} is {one}")
    print(f"The number of zeroes in {n} is {zero}")
    
n = int(input("Enter a number : "))
OnesAndZeroes(n)
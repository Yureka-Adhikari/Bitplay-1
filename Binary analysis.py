print("\033c", end="")

from tkinter import *

def ones_count(n):
    count = 0
    while n:
        if n & 1 == 1:
            break
        count += 1
        n >>= 1
    return count

def set_bits(n):
    ones = 0
    zero = 0
    while n:
        if n & 1 == 1:
            ones += 1
        else:
            zero += 1
        n >>= 1
    return ones, zero  

def analyze_binary():
    try:
        num = int(entry.get())
        binary_representation = bin(num)[2:]
        first_set = ones_count(num)
        ones, zeroes = set_bits(num)

        result_label.config(text=f"Binary: {binary_representation}\n"
                                 f"First set bit position: {first_set}\n"
                                 f"Number of ones: {ones}\n"
                                 f"Number of zeroes: {zeroes}",
                            fg="#5f0d0d")  # Set text color
    except ValueError:
        result_label.config(text="Please enter a valid integer", fg="#5f0d0d")

# Tkinter Setup
root = Tk()
root.geometry("400x400")
root.title("Binary Analysis Tool")
root.configure(bg="#f2b5b5")  # Set background color

Label(root, text="Enter a number:", font=("Arial", 16), bg="#f2b5b5", fg="#5f0d0d").pack()
entry = Entry(root, font=("Arial", 16), bg="#ffe4e4", fg="#5a0000")
entry.pack(pady=10)

Button(root, text="Analyze", font=("Arial", 14), command=analyze_binary, bg="#5f0d0d", fg="white").pack(pady=20)

result_label = Label(root, text="Results will appear here", font=("Arial", 16), bg="#f2b5b5", fg="#5f0d0d")
result_label.pack(pady=10)

root.mainloop()
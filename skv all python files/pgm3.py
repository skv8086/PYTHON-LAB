N = int(input("Enter the value of N: "))

squares = [i**2 for i in range(1, N+1)]

print("The squares of first N", N, "numbers are:")
print(squares)
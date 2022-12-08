"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def Prime(n):
    for a in range(2, b // 2 + 1):
        if b % a == 0:
            return 0
    return 1
N = int(input("Enter the value of N:"))
a = 2
prime_numbers = []
while 1:
    if Prime(a):
        prime_numbers.append(a)
        if len(prime_numbers) == N:
            break
    a += 1
print("First " + str(N) + " Prime numbers are:", end="")
print(*lst)

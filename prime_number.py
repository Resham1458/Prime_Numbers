print("List of prime numbers between 2 and 100: ")
#creating list of all numbers from 2 to 100:
for a in range(2, 101):
    num = a
    if num > 1:
# checking for factors
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num, "is a prime number")

import math

def main():
    while True:
        num = int(input("Input a number: "))
        n = 2
        if num <= 0:
            print("num is prime")
        else:
            while n < num:
                if (num % n == 0 ):
                    print("num is not prime")
                    print("num is divisible by: ", n)
                    break
                else:
                    n = n + 1
            if n == num:
                print("num is prime")
        

main()

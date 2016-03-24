def main():
    num = eval(input("Enter a num to calc fact: "))
    multi = 1
    while 1 < num:
        multi = multi * num
        num = num - 1

    print(multi)

while True:
    main()

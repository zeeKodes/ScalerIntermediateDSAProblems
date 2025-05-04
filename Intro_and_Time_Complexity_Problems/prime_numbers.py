def main():
    #num = int(input("Enter a number: "))
    num = int(input())
    i = 1
    count = 0
    while i * i <= num:
        if num % i == 0:
            if i*i == num:
                count = count + 1
            else:
                count = count + 2
        i = i + 1

    if count == 2:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
    return 0



if __name__ == "__main__":
    main()
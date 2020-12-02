#!/usr/bin/env /usr/bin/python36

def main():

    limit = 1000

    # Using a list comprehension makes it nice and small
    numbers = (x for x in range(0,limit) if x % 3 == 0 or x % 5 == 0)
    total = sum(numbers)

    print("Result: {}".format(total))


if __name__ == "__main__":
    main()

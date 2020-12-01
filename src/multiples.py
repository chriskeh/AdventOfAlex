#!/usr/bin/env /usr/bin/python36

def sum_multiples(quotient, max):
    """
    Find numbers that can be divided by a given quotient startign at 0 up to max. And add those numbers together.
    :param quotient: the number to be divided by
    :param max: the limit
    :return: the summarized numbers
    """
    sum = 0
    for i in range(0, max, quotient):
        sum += i
    return sum


def main():

    sum_of_3 = sum_multiples(3, 1000)
    sum_of_5 = sum_multiples(5, 1000)
    total = sum_of_3 + sum_of_5

    # print("Sum3: {}".format(sum_of_3))
    # print("Sum5: {}".format(sum_of_5))
    print("Summe: {}".format(total))

if __name__ == "__main__":
    main()
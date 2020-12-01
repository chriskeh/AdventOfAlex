#!/usr/bin/env /usr/bin/python36

def sum_multiples(quotient, upper_limit):
    """
    Find numbers that can be divided by a given quotient starting at 0 up to upper_limit. And add those
    numbers together.
    :param quotient: the number to be divided by
    :param upper_limit: the limit
    :return: the summarized numbers
    """
    result = 0
    for i in range(0, upper_limit, quotient):
        result += i
    return result


def main():

    sum_of_3 = sum_multiples(3, 1000)
    sum_of_5 = sum_multiples(5, 1000)
    total = sum_of_3 + sum_of_5

    # print("Sum3: {}".format(sum_of_3))
    # print("Sum5: {}".format(sum_of_5))
    print("Result: {}".format(total))


if __name__ == "__main__":
    main()

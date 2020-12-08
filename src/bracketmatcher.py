import re

import pytest


def klammer_pruefer_simple(text):
    """
    Bracket Matcher
    Have the function BracketMatcher(str) take the str parameter being passed and return 1 if the brackets
    are correctly matched and each one is accounted for. Otherwise return 0. For example: if str is "(hello (world))",
    then the output should be 1, but if str is "((hello (world))" the the output should be 0 because the brackets
    do not correctly match up. Only "(" and ")" will be used as brackets. If str contains no brackets return 1.

    Examples:
    Input: "(coder)(byte))"
    Output: 0
    Input: "(c(oder)) b(yte)"
    Output: 1

    :param text:
    :return:
    """
    opening = 0
    closing = 0
    for buchstabe in text:
        if buchstabe == "(":
            opening += 1
        elif buchstabe == ")":
            closing +=1
    if opening == closing:
        return 1
    else:
        return 0


def klammer_pruefer_findall(text):
    """
    Let's try to use pattern matching
    :param test:
    :return:
    """
    opening = re.findall(r'\(', text)
    closing = re.findall(r'\)', text)
    if len(opening) == len(closing):
        return 1
    else:
        return 0

def klammer_pruefer_count(text):
    """
    Now with count()
    :param text:
    :return:
    """
    opening = text.count('(')
    closing = text.count(')')
    if opening == closing:
        return 1
    else:
        return 0


def main():

    list_of_words = ["(coder)(byte))", "((coder)(byte))"]
    for wort in list_of_words:
        result = klammer_pruefer(wort)
        print("{} : {}".format(wort, result))


if __name__ == "__main__":
    main()
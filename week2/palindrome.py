class Palindrome:
    def __init__(value, word):
        value.word = word

    def __call__(value):
        word_strip = list([val for val in value.word if val.isalpha() or val.isnumeric()])
        value.word = "".join(word_strip)
        value.word = value.word.lower()

        if value.word == value.word[::-1]:
            return "is a palindrome"
        else:
            return "is not a palindrome"

test_strings = ["A man, a plan, a canal -- Panama", "12321", "definitelynotthisone", "racecar", "jeankim"]

def menu():
    try:
        for n in test_strings:
            palindrome = Palindrome(word=n)
            print(n, palindrome())
    except:
        print("Sorry, there was an error")
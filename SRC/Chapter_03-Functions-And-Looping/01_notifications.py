praise = "You are doing great"
praise = praise.upper()
number_of_characters = len(praise)
result = praise + "!" * number_of_characters

print(result)

# code duplication.
advice = "Don't forget to ask for help"
advice = advice.upper()
number_of_characters = len(advice)
result = advice + "!" * number_of_characters

print(result)


def yell(text):
    text = text.upper()
    number_of_characters = len(text)
    result = text + "!" * number_of_characters
    print(result)


yell(advice)
yell(praise)

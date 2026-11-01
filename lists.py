import random


def my_list():
    words = input(
        "Give me somewords like this format: word1/word2/word3/word4/...etc \n"
    )

    text = [word.strip() for word in words.split("/") if word.strip() != ""]

    random.shuffle(text)

    if len(text) < 10:
        print(text[:2])
    else:
        print(text[-3:])


my_list()

def get_vowels_number(word):

    counter = 0
    found_vowels = []
    vowels = "aeiouAEIOU"

    for letter in word:
        if letter in vowels:
            counter += 1
            found_vowels.append(letter)

    return counter, found_vowels


print(get_vowels_number("Hello, Hola, Privet"))

def get_letters_frequency(phrase):
    letters = "abcdefghijklmnopqrstuvwxyz"
    letters_frequency = {}

    for char in phrase:
        letter = char.lower()
        if letter in letters:
            if letter in letters_frequency:
                letters_frequency[letter] += 1
            else:
                letters_frequency[letter] = 1

    return letters_frequency

if __name__ == "__main__":
    user_input = input("Enter your phrase: ")
    letters_frequency = get_letters_frequency(user_input)
    for letter, freq in letters_frequency.items():
        print(f"'{letter}': {freq}")

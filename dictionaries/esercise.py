def get_letters_frequency(phrase):
    abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
           "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    my_dic = {}
    print(phrase)
    for char in phrase:
        if char in abc:
            print(char)
            if char in my_dic:
                my_dic[char] += 1
            else:
                my_dic[char] = 1
    return my_dic  # You might consider returning a dictionary with the frequency here?


if __name__ == "__main__":
    phrase = input("Enter a string: ")  # Read phrase from user here.
    my_dic = get_letters_frequency(phrase)  # Call get_letters_frequency here
    for key, value in my_dic.items():
        print(f"{key} : {value}")  # Print the result here.

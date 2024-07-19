def read_file(): 
    books_dicretory = './books/frankenstein.txt'
    with open(books_dicretory) as f:
        file_contents = f.read()
        return file_contents
def character_found(file):
    chars_dictionary = { }
    for i in range(97, 123):
        chars_dictionary[chr(i)] = 0
    for x in file: 
        if (ord(x)>=97 and ord(x)<123) or (ord(x) >=65  and ord(x)< 89):
            x = x.lower()
            chars_dictionary[x] = chars_dictionary[x] + 1 
    return chars_dictionary


def count_words(file):
    return file.split()

if __name__ == "__main__":
    print(character_found(read_file()))

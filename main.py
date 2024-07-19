
books_dicretory = './books/frankenstein.txt'
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

def generate_report(count, occurance_dictionary):
    print(f"--- Begin report of {books_dicretory} ---")
    print(f"{count} words found in the document \n \n")
    for x in occurance_dictionary:
        print(f"The '{x}' character was found {occurance_dictionary[x]}  times")


def count_words(file):
    return len(file.split())

if __name__ == "__main__":  
    file = read_file()
    count = count_words(file)
    occurance_dictionary = character_found(file)
    generate_report(count, occurance_dictionary)

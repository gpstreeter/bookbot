def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_word(text)
    chars_dict = count_char(text)
    sorted_list = chars_dict_to_sorted_list(chars_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def count_word(text):
    array = text.split()
    return len(array)

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def count_char(text):
    string = text.lower()
    chars = {}
    for c in string:
        if c in chars:
            chars[c] +=1
        else:
            chars[c]=1
    return chars

main()

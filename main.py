def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    dic_count = get_count_characters(text)
    sorted_char = dict(sorted(dic_count.items(), key=lambda item: item[1], reverse = True))
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    
    for val in sorted_char:
        print(f"The '{val}' character was found {dic_count[val]} times")

    print("--- End of report ---")
        
def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_count_characters(text):
    dic_char = {}
    words = text.split()
    for word in words:
        for c in word:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                c_lower = c.lower()
                if c_lower in dic_char:
                    dic_char[c_lower] += 1
                else:
                    dic_char[c_lower] = 1
    return dic_char

main()

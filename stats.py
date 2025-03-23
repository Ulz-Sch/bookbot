
def get_number_words(text_book):
    words = text_book.split()
    number_words = len(words)
    return number_words

def get_count_words(words):
    letter_count = {}
    words = words.lower()

    for letter in words:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    return letter_count

def get_sorted_dict(letter_count):
    def sort_on(dict):
        return dict["count"]
    
    sorted_dict = {}
    char_list = []

    for char, count in letter_count.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    
    char_list.sort(reverse=True, key=sort_on)

    for item in char_list:
        sorted_dict[item["char"]] = item["count"]

    return sorted_dict

def print_stats(path,num_of_words,sorted_letter_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for char in sorted_letter_count:
        print(f"{char}: {sorted_letter_count[char]}")
    
    pass
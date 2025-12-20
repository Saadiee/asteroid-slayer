def get_word_count(text):
    split_text = text.split()
    word_count = len(split_text)
    return word_count

def get_letter_count(text):
    lower_case_text = text.lower()
    count = {}
    for letter in lower_case_text:
        if letter.isalpha():
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
    return count

def sorted_dict(letter_count_dict):
    sorted_by_count = sorted(
        letter_count_dict.items(), 
        key=lambda item: item[1], 
        reverse=True # Set to True for descending order (highest count first)
    )
    for char, count in sorted_by_count:
        print(f"{char}: {count}")

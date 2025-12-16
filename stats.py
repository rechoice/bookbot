#stats.py

# count words
def count_words(text):
    """ 
    This function takes a string input and returns the number of words in the string.
    """
    words = text.split()
    return len(words)


# count num of each character including space and symbols
def count_characters(text):
    """
    Args:
        text (_str_): text of any txt book file
    
    Returns:
        character_dictionary (dictionary): character - number
    """
    text = text.lower()
    counts = {}

    for char in text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    return counts


# sort dictionary
def get_sorted_char_list(char_dict):
    char_list = []

    for char, num in char_dict.items():
        char_list.append({"char": char, "num": num})

    def sort_on(items):
        return items["num"]

    char_list.sort(reverse=True, key=sort_on)
    return char_list

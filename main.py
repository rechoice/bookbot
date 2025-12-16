import sys
from stats import count_words, count_characters, get_sorted_char_list

EXPECTED_ARGS = 2 # program name + filepath


def get_book_text(filepath):
    """Read and return the text content of a book file.

    Args:
        filepath: Path to the text file

    Returns:
        str: Content of the file
    
    Raises:
        FileNotFoundError: If the file doesn't exist
        PermissionError: If the file can't be read
        UnicodeDecodeError: If file contains non-UTF-8 encoded text
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        sys.exit(1)
    except PermissionError:
        print(f"Error: Permission denied for {filepath}")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Error: Unable to decode file {filepath}. Is it a text file?")
        sys.exit(1)

def print_report(filepath, word_count, char_frequency):
    """Print formatted analysis results.

    Args:
        filepath: Path to the analyzed file
        word_count (int): Total number of words
        char_frequency (list): List of dicts with 'char' and 'num' keys
    """
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in char_frequency:
        char = item["char"]
        count = item["num"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) != EXPECTED_ARGS:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    # Read and analyze
    text = get_book_text(filepath)
    word_count = count_words(text)
    char_frequency = get_sorted_char_list(count_characters(text))
    
    # Display result
    print_report(filepath, word_count, char_frequency)
    

if __name__ == "__main__":
    main()
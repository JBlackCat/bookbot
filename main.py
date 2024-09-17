def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    count_alpha_chars_dict = count_alpha_chars(text)
    sorted_alpha_char_dicts = sort_dict_alpha_chars(count_alpha_chars_dict)
    print_report(book_path, num_words, sorted_alpha_char_dicts)


def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
        return file_contents


def count_words(str):
    words = str.split()
    return len(words)


def count_alpha_chars(str):
    words = str.split()
    char_dict = {}
    for word in words:
        for char in word:
            if not char.isalpha():
                continue
            char_lower = char.lower()
            if char_lower not in char_dict:
                char_dict[char_lower] = 0
            char_dict[char_lower] += 1
    return char_dict


def sort_by_count(dict):
    return dict["count"]


# Can't use dict.items to use array of tuples since exercise wants an array of dictionaries.
# So need to redefine a dict per char that is sortable by static key.
def sort_dict_alpha_chars(dict):
    sorted_char_counts = []

    for char in dict:
        char_count = {"char": char, "count": dict[char]}

        sorted_char_counts.append(char_count)

    sorted_char_counts.sort(reverse=True, key=sort_by_count)

    return sorted_char_counts


def print_report(book_path, num_words, list_alpha_char_count):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for char_count_dict in list_alpha_char_count:
        print(
            f"The '{char_count_dict["char"]}' character was found {char_count_dict["count"]} times"
        )

    print("--- End report ---")


main()

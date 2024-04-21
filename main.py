def main():
    file = "books/frankenstein.txt"
    report(file)


def read_file(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    lowered_text = text.lower()
    dict = {}
    for char in lowered_text:
        if char in dict:
            dict[char] += 1
        if char not in dict:
            dict[char] = 1

    return dict


def convert_dict(dict):
    new_list = []
    for key in dict:
        new_dict = {"char": key, "count": dict[key]}
        new_list.append(new_dict)

    return new_list


def sort_on(dict):
    return dict["count"]


def report(file):
    text = read_file(file)
    count = count_words(text)
    converted = convert_dict(count_letters(text))
    converted.sort(reverse=True, key=sort_on)

    begin = "--- Begin report of " + file + " ---"
    words_found = str(count) + " words found in the document"
    end = "--- End report ---"

    print(begin)
    print(words_found)
    print()
    for dict in converted:
        if dict["char"].isalpha():
            print("The " +
                  "'" + dict["char"] + "'" +
                  " character was found " + str(dict["count"]) + " times")

    print(end)


main()

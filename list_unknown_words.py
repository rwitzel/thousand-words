import re


def read_categories():
    categories = {}
    with open("test_file.txt") as categories_file:
        for line in categories_file:
            line = line.strip()
            category, words = line.split(":")
            if "#" in category:
                continue
            if category.strip() in categories:
                raise Exception(f"duplicate category: {category.strip()}")
            categories[category.strip()] = re.split(r"[,\s.]+", words.strip())
    return categories


categories = read_categories()

def read_all_words():
    with open("thousand_words.txt") as f_all_words:
        return re.split(r"[,\s.]+", f_all_words.read().strip())

all_words = read_all_words()

for category, words_in_category in categories.items():
    for word in words_in_category:
        if word not in all_words:
            print(f"unknown word in category {category}: {word}")

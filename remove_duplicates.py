import re


def read_categories():
    categories = {}
    with open("curated_categories.txt") as categories_file:
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

flat_list = []
valid_categories = []
for category, words_in_category in categories.items():
    valid_words = [word for word in words_in_category if word not in flat_list]
    flat_list += valid_words
    valid_categories.append(category + ": " + ", ".join(valid_words))
with open("curated_categories.txt", "w") as f:
    f.write("\n".join(valid_categories))

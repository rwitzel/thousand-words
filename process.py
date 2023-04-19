import re

def read_words():
    with open('thousand_words.txt') as f:
        word_contents = f.read()

    #print(word_contents)
    words = re.split(r'[\s,.]+', word_contents)
    return words


def read_categories():
    categories = {}
    with open("categories.txt") as categories_file:
        for line in categories_file:
            line = line.strip()
            category, words = line.split(":")
            if "#" in category:
                continue
            if category.strip() in categories:
                raise Exception(f"duplicate category: {category.strip()}")
            categories[category.strip()] = re.split(r"[,\s.]+", words.strip())
    return categories


# Remove words that belong to any category
words = read_words()
categories = read_categories()
flat_list = [item for sublist in categories.values() for item in sublist]
filtered_words_list = [word for word in words if word not in flat_list]

valid_categories = []
for category, words_in_category in categories.items():
    valid_words = [word for word in words_in_category if word in words]
    valid_categories.append(category + ": " + ", ".join(valid_words))
with open("valid_categories.txt", "w") as f:
    f.write("\n".join(valid_categories))


#for word in flat_list:
#    if word not in words:
#        raise Exception(f"chatgpt word '{word}' is not in list")

def write_filtered_words(filtered_words_list):
    with open("filtered_words.txt", "w") as filtered_words_file:
        filtered_words_file.write(", ".join(filtered_words_list))


print(filtered_words_list)
print(len(filtered_words_list))
print(len(words))
write_filtered_words(filtered_words_list)
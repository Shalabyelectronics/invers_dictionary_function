glossary = {
    "fruits": ["Apple", "Orange", "Banana"],
    "vegetables": ["Cucumber", "Lemon", "Tomato"],
    "sweets": ["Mars", "Kitkat", "Galaxy"]

}
# This about invers dictionary values from list to become a keys and their keys became a values that refer to them

def invert_dict(d):
    inverse = dict()
    for key in d:
        val_list = d[key]
        for val in val_list:
            if val not in inverse:
                inverse[val] = [key]
            else:
                inverse[val].append(key)
    print(inverse)


invert_dict(glossary)

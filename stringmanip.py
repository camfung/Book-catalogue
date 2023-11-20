def cap_First_Letter(word):
    new_word = ""
    new_word = word[0].upper()
    for i in range(1, len(word)):
        if word[i - 1] == " ":
            new_word += word[i].upper()
        else:
            new_word += word[i].lower()

    return new_word


def split(word, delim):
    element = ""
    word_list = []
    for i in word:
        if i != delim:
            element += i
        else:
            word_list.append(element)
            element = ""
    word_list.append(element)
    return word_list

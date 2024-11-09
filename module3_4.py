
def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if i.lower().find(root_word.lower()) >= 0:
            same_words.append(i)
        elif root_word.lower().find(i.lower()) >= 0:
            same_words.append(i)
    print(same_words)


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')



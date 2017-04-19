def words(param):
    result = {}
    # Deal with multiple spaces
    proper_sentence = ' '.join(param.split())

    # Create a list containing word items
    proper_words = proper_sentence.split(" ")

    for my_word in proper_words:
        if my_word in result:
            continue
        try:
            result[int(my_word)] = proper_words.count(my_word)
        except:
            result[my_word] = proper_words.count(my_word)
    return result

def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    lst_sentence = sentence.split()
    new_lst = (words[i] + " " for i in lst_sentence)
    return ''.join(new_lst)


def main():
    print(translate("el gato esta en la casa"))


if __name__ == '__main__':
    main()

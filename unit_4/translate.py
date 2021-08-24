def translate(sentence):
    words = {'esta': 'is', 'la': 'the', 'en': 'in', 'gato': 'cat', 'casa': 'house', 'el': 'the'}
    translate_gen = (words[word] for word in sentence.split())
    res = ""
    for word in translate_gen:
        res += word + " "
    return res


def main():
    print(translate("el gato esta en la casa"))


if __name__ == "__main__":
    main()

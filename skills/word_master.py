from cdifflib import CSequenceMatcher


def word_to_word(str1, str2):
    similarity = CSequenceMatcher(a=str1, b=str2)
    return similarity.ratio()

if __name__ == '__main__':
    str1 = input("1 - ")
    str2 = input("2 - ")

    print(word_to_word(str1, str2))
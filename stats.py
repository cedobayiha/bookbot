from collections import Counter

def get_num_words(string):
    number_of_words = len(string.split())
    print("Found", number_of_words, "total words \n")

def count_characters(string):
    lower_case_text = string.lower()
    text_to_list = list(lower_case_text)
    count = dict(Counter(text_to_list))
    sorted_dic = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
    for character, amount in zip(sorted_dic.keys(), sorted_dic.values()):
        print(f'{character}: {amount}')


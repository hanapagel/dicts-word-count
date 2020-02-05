# put your code here.
# input_file = open("test.txt")
import pdb

def count_words(input_file):
    '''Takes a text file as a string. Prints a dictionary of words and word count.'''

    contents = open(input_file).read()
    all_words = contents.split()

    # input_file = open(input_file)
    # all_words = []
    # for line in input_file:
    #     sentence = line.lower()
    #     sentence = sentence.split(" ")
    #     sentence[-1] = sentence[-1][:-1]
    #     all_words = all_words + sentence

    word_dict = {}

    for word in all_words:
        if word not in word_dict:
            word_dict[word] = 1
        elif word in word_dict:
            word_dict[word] += 1


    for word, count in word_dict.items():
        print(f'{word} {count}')


# word_dict.get()


# if word is not in dictionary, add word to dictionary with value of one
# if word is in dictionary, incrememnt value by one

# close("test.txt")

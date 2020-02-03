# put your code here.
input_file = open("test.txt")

all_sentences = []
for line in input_file:
    sentence = line.split(" ")
    sentence[-1] = sentence[-1][:-1]
    all_words = all_words + sentence

print(all_words)

word_dict = {}

for word in all_words:
    if word not in dictionary:
        word_dict[word] = 1


    # word_dict.get()


# if word is not in dictionary, add word to dictionary with value of one
# if word is in dictionary, incrememnt value by one

















# close("test.txt")
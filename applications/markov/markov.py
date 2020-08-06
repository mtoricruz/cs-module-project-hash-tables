import random

# Read in all the words in one go
with open("input.txt", 'r') as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
d = {}
all_words = words.split()
# loop through words in entire txt file
for word in range(len(all_words)):
    # if previous word hasn't been set, create it
    if word == 0:
        prev_word = all_words[word]
    else:
        # if prev word not already in dict, assign prev word value to the current word index value
        if prev_word not in d:
            d[prev_word] = [all_words[word]]
        else:
            # otherwise, create list of 'follow words' from dict and append this word to the list
            cur_list = d[prev_word]
            cur_list.append(all_words[word])
            d[prev_word] = cur_list
        prev_word = all_words[word]
# d now holds all the words that other words can follow
punc = ['.', '?', '!']
start_words = []
end_words = []
keys = d.keys()
for key in keys:
	if (key[0].isupper() or key[0] == '"' and key[1].isupper()) and (key[-1] != '"') and (key[-1] not in punc):
		start_words.append(key)
	if (key[-1] in punc) or (key[-1] == '"' and key[-2] in punc):
		end_words.append(key)

# TODO: construct 5 random sentences
new = True
sentence = 0
while sentence < 5:
    if new:
        word = random.choice(start_words)
        print(word, end=' ')
        new = False
    else:
        if word in end_words:
            new = True
            sentence += 1
        else:
            cur_list = d[word]
            word = random.choice(cur_list)
            print(word, end=' ')

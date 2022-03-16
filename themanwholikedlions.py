from urllib.request import urlopen

url = "https://www.gutenberg.org/files/67603/67603-0.txt"
local_name = "themanwholikedlions.txt"

def save_locally():

    """
    Save the book locally, so we can use it faster and no need to load every time
    :return: None
    """
    with open(local_name, "w") as local_fp:
        with urlopen(url) as fp:
            for line in fp:
                line = line.decode('utf-8-sig').replace("\n", "")
                local_fp.write(line)


punctuation = ",;!.?-()"
def get_unique_words():
    """
    Get the dictionary of unique words and their frequency
    :return: dict
    """
    unique_words = {}
    with open(local_name) as fp:
        for line in fp:
            # remove punctuation
            for p in punctuation:
                line = line.replace(p, " ")
            line = line.lower()
            # get the words:
            for word in line.split():
                unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words
#Defining the number of total of unique words

save_locally()
unique_words = get_unique_words()
most_frequent = list(unique_words.values())
most_frequent.sort(reverse=True)
# print(most_frequent)
for word_frequency in most_frequent[:10]:
    for unique_word, value in unique_words.items():
        if word_frequency == value:
            print(f"common word '{unique_word}' appears {value} times")
            # change the value so we don't get it again if there are multiple words with the same frequency
            unique_words[unique_word] = -1
            break
##New changes for the homeworks
#To get the number of words over 7 characters
retList = []
for x in unique_words:
    if len(x) >= 7:
        retList.append(x)
print(retList)
##For counting the number of unique words
print('Number of words in text file :', len(unique_words))
#To get the total number of words
total_words = 0
with open(local_name) as fp:
    for line in fp:
        words = line.split()
        total_words += len(words)
print("Number of words:", total_words)
#Ratio unique words per total words:
ratio=len(unique_words)/total_words
print(ratio)
#Additionally, I created a program where I can ask for a word in the text file:
def wordssearch():
    file = open("themanwholikedlions.txt")
    search_word = input("enter a word you want to search in file: ")
    if(search_word in file.read()):
        print("word found")
    else:
        print("word not found")
wordssearch()



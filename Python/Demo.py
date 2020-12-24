punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(oldS):
    for i in punctuation_chars:
        oldS = str(oldS).replace('%s' % i, '')
    return oldS

def strip_punctuation(oldS):
    for i in punctuation_chars:
        oldS = str(oldS).replace('%s' % i, '')
    return oldS

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(str):
    str = strip_punctuation(str).split()
    j = 0
    for i in str:
        if i in positive_words:
            j += 1
    return j

def strip_punctuation(oldS):
    for i in punctuation_chars:
        oldS = str(oldS).replace('%s' % i, '')
    return oldS

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            
def get_neg(str):
    str = strip_punctuation(str).split()
    k = 0
    for i in str:
        if i in negative_words:
            k += 1
    return k


def run(file):
    csvFile = open(file, 'r')
    lines = csvFile.readlines()
    
    lines = lines[1:]
    neg_count = []
    pos_count = []
    wordList = []
    for i in lines:
        i = i.strip()
        i = i.split(",")[0]
        wordList.append(i)
    for i in wordList:
        neg_count.append(get_neg(i))
        pos_count.append(get_pos(i))
    res = ['retweet_count,reply_count,pos_count,neg_count,score']
    
    res = []
    for i in lines:
        i = i.strip()
        i = i.split(",")[1:]
        res.append(i)
    temp = []
    for i in res:
        i = list(map(int, i))
        temp.append(i)
    res = temp
    for i in range(len(res)):
        res[i].append(pos_count[i])
        res[i].append(neg_count[i])
        res[i].append(pos_count[i] - neg_count[i])
        
    temp = []
    for i in res:
        temp.append(','.join('%s' %id for id in i))
    res = temp
    
    res.insert(0, "Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    print(res)
    res = '\n'.join('%s' % id for id in res)
    with open("resulting_data.csv", 'w') as csvFile:
        write = csvFile.write(res)


if __name__ == '__main__':
    run('project_twitter_data.csv')

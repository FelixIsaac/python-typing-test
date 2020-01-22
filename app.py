import sys
import time
import random
import os
from nltk.corpus import words

def generateParagraph():
    try:
        paragraph = ""
        wordlist = words.words()

        for i in range(15):
            paragraph += random.choice(wordlist) + " "

        return paragraph
    except:
        from nltk import download

        download('words')
        return generateParagraph()

def show_results():
    # Calculate time
    total_time = time.time() - time_start

    # Calculate accuracy
    count = 0

    for i, c in enumerate(paragraph):
        try:
            if typed[i] == c:
                count += 1
        except:
            pass
        
    accuracy = count / len(paragraph)*100

    # Calculate words per minute
    wpm = len(typed) * 60 / (5 * total_time)

    results = 'Time:'+str(round(total_time)) + " secs   Accuracy:" + str(
        round(accuracy)) + "%" + '   Wpm: ' + str(round(wpm))

    return results

os.system('cls')
time_start = time.time()
paragraph = generateParagraph()
print(paragraph)
typed = input()
print(show_results())
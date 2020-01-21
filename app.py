import pygame
from pygame.locals import *
import sys
import time
import random
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
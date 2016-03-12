# -*- coding: utf-8 -*-
import nltk
from nltk.collocations import *

if __name__ == '__main__':
    ignore_words=nltk.corpus.stopwords.words('english')
    bigram_measures=nltk.collocations.BigramAssocMeasures()
    finder=BigramCollocationFinder.from_words(
        nltk.corpus.gutenberg.words('austen-emma.txt')  #过滤emma
    )

    finder.apply_word_filter(lambda x:not x.isalpha()) #过滤标点符号
    print(sorted(finder.nbest(bigram_measures.raw_freq,20)))  #随便排排序
    print("=======================")

    finder.apply_word_filter(lambda w:w.lower() in ignore_words )
    print(sorted(finder.nbest(bigram_measures.raw_freq,20)))  #用停用词过滤之后再排排序

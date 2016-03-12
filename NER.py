# -*- coding: utf-8 -*-
# http://www.pythontip.com/blog/post/10012/
#词性标注
#出了点问题，不知道为什么
import nltk

if __name__ == '__main__':
    text='''She had been a friend and companion such as few possessed: intelligent,
well-informed, useful, gentle, knowing all the ways of the family,
interested in all its concerns, and peculiarly interested in herself,
in every pleasure, every scheme of hers--one to whom she could speak
every thought as it arose, and who had such an affection for her
as could never find fault.
'''
    sens=nltk.sent_tokenize(text)
    word=[]
    for sent in sens:
        word.append(nltk.word_tokenize(sent))
    print(word)

    tags=[]
    for tokens in word:
        tags.append(nltk.pos_tag(tokens))

    print(tags)

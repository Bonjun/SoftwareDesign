# -*- coding: utf-8 -*-
"""
Created on Tue Sep 23 17:55:49 2014

@author: bonjun
"""


from pattern.web import *
from pattern.en import *

def red_text(text):
    return "<span style='color:red'>"+text+"<br>"
    
def blue_text(text):
    return "<span style='color:blue'>"+text+"<br>"
    
def black_text(text):
    return "<span style='color:black'>"+text+"<br>"

def sentence_subjective(sentence):
    if (sentiment(sentence)[0] > 0):
        return 1
    elif (sentiment(sentence)[0] < 0):
        return -1
    else :
        return 0

def split_Sentences(paragraph):
    ''' break a paragraph into sentences and return a list '''
    import re
            
    sentenceEnders = re.compile('[.!?\n]')
    sentence_list = sentenceEnders.split(paragraph)
    return sentence_list

subjective_count = 0
negative_count = 0
neutral_count = 0

input_URL = raw_input("Input URL : ")
input_name = raw_input("Input Name of the File : ")

full_text = plaintext(URL(input_URL).download())

sentence_list = split_Sentences(full_text)

f = open(input_name+'.html','w')

for r in range(len(sentence_list)):
    current_sentence = sentence_list[r]
    
    if (sentence_subjective(current_sentence)==-1):
        f.write(red_text(current_sentence))
        negative_count += 1
    if (sentence_subjective(current_sentence)==0):
        f.write(black_text(current_sentence))
        neutral_count += 1
    if (sentence_subjective(current_sentence)==1):
        f.write(blue_text(current_sentence))
        subjective_count += 1

f.close()

print "\n"
print str(len(sentence_list))+" Total Sentences.\n"
print str(subjective_count) + " Subjective Sentences.\n"
print str(negative_count) + " Negative Sentences.\n"
print str(neutral_count) + " Neutral Sentences.\n"
print "Successfully created "+input_name+".html"

import pandas as pd
from textblob import TextBlob
import eng_spacysentiment
import contractions
import spacy
import os
import string


nlp_sentiment = eng_spacysentiment.load(disable = ['parser'])
spacy_model = spacy.load("en_core_web_sm")

text = "I'll be glaad to buy thisss prodact. This is very amazing#"

sentence = TextBlob(text)


for sent in sentence.sentences:
    sentence_tokens = []
    for token in sent.split(' '):
        sentence_tokens.append(contractions.fix(token))
    
    sent = ' '.join(sentence_tokens)
    
    sent = sent.translate(str.maketrans('', '', string.punctuation))

    sent = TextBlob(sent)
    sent = sent.correct()
    print(sent)

    doc = nlp_sentiment(str(sent).lower())
    print(doc.cats)
    

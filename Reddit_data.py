# -*- coding: utf-8 -*-
"""
Created on Tue May  3 14:01:59 2022

@author: loklu
"""
import praw
import pandas as pd
from praw.models import MoreComments
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import FreqDist
import emoji
import re
import en_core_web_sm
import spacy

nlp = en_core_web_sm.load()

reddit = praw.Reddit(client_id = "P-oTGSQtizlNcKQb39kvQw",
                     client_secret = "zaOaib_Xts2m-Fm_cL1Ov3h72vkK3g",
                     user_agent = "ua",
                     check_for_async=False)


sub_IDs = []
subreddit = reddit.subreddit('wallstreetbets')
cleaned_output = []
limits = 5


for submission in subreddit.hot(limit=limits):
    
    print(submission.title)
    
    post1 = reddit.submission(str(submission.id))
    
    comments_all = []
    post1.comments.replace_more(limit=None)
    
    for comments in post1.comments.list():
        comments_all.append(comments.body)
    
    list1 = comments_all
    list1 = [str(i) for i in list1]
    
    string_uncleaned = ' , '.join(list1)
    
    string_emojiless = emoji.get_emoji_regexp().sub(u'',string_uncleaned)

    tokenizer = RegexpTokenizer('\w+|\$[\d\.]+|http\S+')
    tokenized_str = tokenizer.tokenize(string_emojiless)

    lower_str_tokenized = [word.lower() for word in tokenized_str]
    all_stops = nlp.Defaults.stop_words

    tokens_without_stops = [word for word in lower_str_tokenized
                            if not word in all_stops]
    
    lemmatizer = WordNetLemmatizer()
    lemmatizer_token = ([lemmatizer.lemmatize(w) for w in tokens_without_stops])
    
    cleaned_output.append(lemmatizer_token)
    
    
    
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []
for i in range(limits):
    for sentences in cleaned_output[i]:
        pol_score = sia.polarity_scores(sentences)
        pol_score['words'] = sentences
        results.append(pol_score)
        
pd.set_option('display.max_columns',None,'max_colwidth',None)
df = pd.DataFrame.from_records(results)

print(pol_score)

    
    
import seaborn as sns
import matplotlib.pyplot as plt

fig,ax = plt.subplots(figsize=(8,8))
counts = df.pos.value_counts(normalize=True)*100
sns.barplot(x=counts.index,y=counts,ax=ax)

    
    
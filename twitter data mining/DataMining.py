import sys
import string
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
from nltk import bigrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re
import operator 
from collections import Counter
from collections import defaultdict
import vincent
import json
 
consumer_key = "LWz0vJRfym0TWnX8OywVZoytX"
consumer_secret = "4zcxQXa3tsGNYzxunEjtRddYXHLc1gqkrfF3f2HUPfNW1NPwFF"
access_token = "1291378563397099521-IyoaY73ZNXyyggvNTDWOQsfPWtOlZk"
access_secret = "szXuVfZTpVZrgiDH2Ls6fL5LowiWjc40x6ujXvaGSaMId"
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth, wait_on_rate_limit=True)

emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens
 
def process_or_store(tweet):
    print(json.dumps(tweet))

with open('data.json', 'w+') as f:
    for tweet in tweepy.Cursor(api.user_timeline).items():
        process_or_store(data._json)
    for line in f:
        try:
            tweet = json.loads(line)
        except:
            print()
        tokens = preprocess(tweet['text'])


fname = 'data.json'
with open(fname, 'r') as f:
    count_all = Counter()
    for line in f:
        try:
            tweet = json.loads(line)
        except:
            print()
        # Create a list with all the terms
        terms_all = [term for term in preprocess(tweet['text'])]
        # Update the counter
        count_all.update(terms_all)
    # Print the first 5 most frequent words
    print(count_all.most_common(5))

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via', 'RT']

terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]


# Count terms only once, equivalent to Document Frequency
terms_single = set(terms_all)
# Count hashtags only
terms_hash = [term for term in preprocess(tweet['text']) 
              if term.startswith('#')]
# Count terms only (no hashtags, no mentions)
terms_only = [term for term in preprocess(tweet['text']) 
              if term not in stop and
              not term.startswith(('#', '@'))] 
              # mind the ((double brackets))
              # startswith() takes a tuple (not a list) if 
              # we pass a list of inputs

terms_bigram = bigrams(terms_stop)

com = defaultdict(lambda : defaultdict(int))
 
# f is the file pointer to the JSON data set
with open(fname, 'r') as f:
    for line in f: 
        try:
            tweet = json.loads(line)
        except:
            print()
        terms_only = [term for term in preprocess(tweet['text']) 
                    if term not in stop 
                    and not term.startswith(('#', '@'))]
 
    # Build co-occurrence matrix
        for i in range(len(terms_only)-1):            
            for j in range(i+1, len(terms_only)):
                w1, w2 = sorted([terms_only[i], terms_only[j]])                
                if w1 != w2:
                    com[w1][w2] += 1


com_max = []
# For each term, look for the most common co-occurrent terms
for t1 in com:
    t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
print(terms_max[:5])


search_word = "#space" # pass a term as a command-line argument
count_search = Counter()
with open(fname, 'r') as f:
    for line in f:
        try:
            tweet = json.loads(line)
        except:
            print()
        terms_only = [term for term in preprocess(tweet['text']) 
                    if term.startswith('#')]
        if search_word in terms_only:
            count_search.update(terms_only)
        print("Co-occurrence for %s:" % search_word)
        print(count_search.most_common(20))

word_freq = count_search.most_common(20)
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('term_freq.json')

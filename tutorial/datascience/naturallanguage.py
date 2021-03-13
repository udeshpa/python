import nltk

nltk.download('stopwords')

messages = [line.rstrip() for line in open('SMSSpamCollection')]

print(len(messages))

#for mess_no, message in enumerate(messages[:10]):
#    print(mess_no, message)

import pandas as pd
messages = pd.read_csv('SMSSpamCollection', sep='\t', names=['label', 'message'])

print(messages.head())

print(messages.describe())

print(messages.groupby('label').describe())

messages['length'] = messages['message'].apply(len)

print(messages.head())

import matplotlib.pyplot as plt
import seaborn as sns

messages['length'].plot.hist(bins=150)

plt.show()

print(messages['length'].describe())

print(messages[messages['length'] == 910]['message'].iloc[0])

messages.hist(column='length', by='label', bins=60, figsize=(12,4))

plt.show()

import string

mess = 'Sample Message! Notice: it has punctuations'

nopunc = [c for c in mess if c not in string.punctuation]

print(nopunc)

from nltk.corpus import stopwords

print(stopwords.words('english'))

nopunc = ''.join(nopunc)

print(nopunc)



clean_mess = [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

print(clean_mess)

def text_process(mess):
    """
      Remove punctuation
      Remove stop words
    :param mess:
    :return:
    """

    nopunc = [c for c in mess if c not in string.punctuation]
    nopunc = ''.join(nopunc)
    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

print(messages['message'].head(5).apply(text_process))

#bag of words model

from sklearn.feature_extraction.text import CountVectorizer

bow_transformer = CountVectorizer(analyzer=text_process).fit(messages['message'])

print(len(bow_transformer.vocabulary_))

mess4 = messages['message'][3]

print(mess4)

bow4 = bow_transformer.transform([mess4])

print(bow4)

print(bow4.shape)

print(bow_transformer.get_feature_names()[4068])

print(bow_transformer.get_feature_names()[9554])

messages_bow = bow_transformer.transform(messages['message'])

print('Shape of Sparse Matrix ', messages_bow.shape)

print(messages_bow.nnz)

sparsity = (100 * messages_bow.nnz/ (messages_bow.shape[0] * messages_bow.shape[1]))

print(f'sparsity: {sparsity}')

from sklearn.feature_extraction.text import TfidfTransformer

tfidf_transformer = TfidfTransformer().fit(messages_bow)

tfidf4 = tfidf_transformer.transform(bow4)

print(tfidf4)

print(tfidf_transformer.idf_[bow_transformer.vocabulary_['university']])

messages_tfidf  = tfidf_transformer.transform(messages_bow)

print(messages_tfidf)

from sklearn.naive_bayes import MultinomialNB

spam_detect_model = MultinomialNB().fit(messages_tfidf, messages['label'])

print(f'predictions: {spam_detect_model.predict(tfidf4)[0]} real: {messages["label"][3]} ')

all_pred = spam_detect_model.predict(messages_tfidf)

print(all_pred)

from sklearn.model_selection import train_test_split

msg_train, msg_test, lable_train, lable_test = train_test_split(messages['message'], messages['label'], test_size=0.3)

from sklearn.pipeline import Pipeline

pipeline = Pipeline(
  [
    ('bow', CountVectorizer(analyzer=text_process)),
    ('tfidf', TfidfTransformer()),
    ('classifier', MultinomialNB())
  ]
)

pipeline.fit(msg_train, lable_train)

predictions= pipeline.predict(msg_test)

from sklearn.metrics import classification_report

print(classification_report(lable_test, predictions))

from sklearn.ensemble import RandomForestClassifier

pipeline = Pipeline(
  [
    ('bow', CountVectorizer(analyzer=text_process)),
    ('tfidf', TfidfTransformer()),
    ('classifier', RandomForestClassifier())
  ]
)

pipeline.fit(msg_train, lable_train)

predictions= pipeline.predict(msg_test)

from sklearn.metrics import classification_report

print(classification_report(lable_test, predictions))

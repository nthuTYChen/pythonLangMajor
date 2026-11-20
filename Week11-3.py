import nltk
from nltk.tokenize import word_tokenize

email_reader = open("sources/email-sample-1.txt", encoding = "utf-8")
email_text = email_reader.read()
email_words = word_tokenize(email_text)
print(email_words[-10:])
email_reader.close()
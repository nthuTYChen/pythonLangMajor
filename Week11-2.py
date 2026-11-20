import nltk

nltk.download("punkt_tab")

from nltk.tokenize import PunktTokenizer

nltk_en_tknz = PunktTokenizer("english")

email_reader = open("sources/email-sample-1.txt", encoding = "utf-8")
email_text = email_reader.read()
# print(email_text)

email_sens = nltk_en_tknz.tokenize(email_text)
# print(email_sens[:5])
email_reader.close()

dracula_reader = open("sources/pg345_2_clean.txt", encoding = "utf-8")
dracula_text = dracula_reader.read()
dracula_sens = nltk_en_tknz.tokenize(dracula_text)
print(dracula_sens[41:50])
dracula_reader.close()
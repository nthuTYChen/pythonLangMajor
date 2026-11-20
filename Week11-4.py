import spacy

def file_loader(filename):
    text_reader = open("sources/" + filename, encoding = "utf-8")
    return text_reader.read()

email_text = file_loader("email-sample-1.txt")
# print(email_text)

spacy_model_en = spacy.load("en_core_web_sm")
email_text_processed = spacy_model_en(email_text)

email_sens = email_text_processed.sents

# for sen in email_sens:
#     print(sen)

for token in email_text_processed:
    print(token.text)
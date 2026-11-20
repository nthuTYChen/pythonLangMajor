import spacy

zh_news_reader = open("sources/zh-tw-news_short.txt", encoding = "utf-8")
# print(zh_news_reader.read())

spacy_model_zh = spacy.load("zh_core_web_sm")

spacy_model_ruler = spacy_model_zh.add_pipe("entity_ruler", first = True)

ruler_patterns = [{"label": "NOUN", "pattern": "AI"}, {"label": "CONJ", "pattern": "因為"}]

spacy_model_ruler.add_patterns(ruler_patterns)

spacy_model_zh.add_pipe("merge_entities", after = "entity_ruler")

news_text_processed = spacy_model_zh(zh_news_reader.read())

for token in news_text_processed:
    print(token.text)


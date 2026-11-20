import spacy  # Import spaCy, a natural language processing library.

# Open the file containing a short Traditional Chinese news text.
# UTF-8 encoding ensures that Chinese characters are read correctly.
zh_news_reader = open("sources/zh-tw-news_short.txt", encoding = "utf-8")

# Print the contents of the news file for inspection (currently commented out).
# print(zh_news_reader.read())

# Load spaCy's small Traditional Chinese language model.
# The model provides Chinese text processing and linguistic analysis.
spacy_model_zh = spacy.load("zh_core_web_sm")

# If you just go ahead and process the text with the Chinese model, some word tokens
# will not be parsed correctly. For instance, "AI" is tokenized as "A" and "I", and "因為"
# is tokenized as "因" and "為". You can skip everything between line xx and xx to check
# this in the output. Therefore, to correct the output tokens, we can add our own rules
# to a spaCy model.

# Add an EntityRuler component to the spaCy processing pipeline.
# first=True places it at the beginning of the pipeline, before other processing components.
spacy_model_ruler = spacy_model_zh.add_pipe("entity_ruler", first = True)

# Define custom patterns for identifying specific words or expressions.
# "label" specifies the entity category; "pattern" specifies the text to match.
# Here, "AI" is labeled as NOUN, and "因為" is labeled as CONJ.
ruler_patterns = [{"label": "NOUN", "pattern": "AI"}, {"label": "CONJ", "pattern": "因為"}]

# Add the custom patterns to the EntityRuler.
# The ruler will identify matching text and assign the specified labels.
spacy_model_ruler.add_patterns(ruler_patterns)

# Add the merge_entities component immediately after the EntityRuler.
# This component merges recognized entities into single tokens in the processed document.
spacy_model_zh.add_pipe("merge_entities", after = "entity_ruler")

# Read the entire news file and process its contents using the modified spaCy pipeline.
# The result is a Doc object containing tokens and their linguistic annotations.
news_text_processed = spacy_model_zh(zh_news_reader.read())

# Loop through all tokens in the processed news text.
# Each token may represent a word, punctuation mark, or a merged entity.
for token in news_text_processed:
    # Print the text of the current token.
    print(token.text)
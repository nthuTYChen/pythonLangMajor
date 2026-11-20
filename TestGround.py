import nltk
import spacy
nltk.download("punkt_tab")
from nltk .tokenize import PunktTokenizer
nltk_en_tknz = PunktTokenizer("english")
spacy_model1 = spacy.load("en_core_web_sm")
spacy_model2 = spacy.load("zh_core_web_sm")
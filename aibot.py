import nltk

nltk.download('punkt')

nltk.download('maxent_ne_chunker')

nltk.download('words')

nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

text = "Merhaba , nasilsin?"
tokens = word_tokenize(text,language="turkish")
print(f'Word Tokens: {tokens}')

tagged_words = pos_tag(tokens)
print(f'Tagged Words: {tagged_words}')
named_entities = ne_chunk(tagged_words)
print(f'Named Entities: {named_entities}')
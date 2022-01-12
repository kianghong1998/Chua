from textblob import TextBlob
from pathlib import Path

text = ('Tommorrow will be a great weekend for us')
blob = TextBlob(text)

#Polarity: -1.0 (Negative) to 1.0 (Positive)
# Subjectivity: 1.0 (Objective) to 1.0 (subjective)
print(blob.sentiment)
print(blob.sentiment.polarity)
print(blob.detect_language())
chinese = blob.translate(to='zh')
print(chinese)
spanish = blob.translate(to='es')
print(spanish)

text1 = ('Yesterday was a beautiful day, but today looks like a bad weather')
blob1 = TextBlob(text1)
print(blob1.sentiment)
print(blob1.sentiment.polarity)

blob2 = TextBlob(Path('RomeoandJuliet.txt').read_text())
items = blob2.word_counts.items()




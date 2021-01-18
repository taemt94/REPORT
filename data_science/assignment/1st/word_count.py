import sys
import re
from collections import Counter

word_counts = Counter()
word_split = (re.findall('[a-zA-Z0-9]+', line.lower()) for line in sys.stdin)

for k in word_split:
    word_counts.update(k)

for word, count in word_counts.most_common(1000):
    print(word, end='\t')
    print(count)

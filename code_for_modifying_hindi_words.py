import codecs

f = codecs.open('hindi_words.txt', encoding='utf-8')
f1 = codecs.open('hindi_words_modified.txt', 'w', encoding='utf-8')

for string in f:
    x = list(string)
    y = []
    for char in x:
        if ord(u'\u0900') <= ord(char) <= ord(u'\u097F'):
            y.append(char)
    s = "".join(y)
    f1.write(s + '\n')
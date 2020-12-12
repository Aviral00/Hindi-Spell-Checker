import codecs

f = codecs.open("hindi.txt", encoding='utf-8')


class TrieNode:  # Trie node class

    def __init__(self):
        self.children = [None] * 128

        self.isEndOfWord = False  # isEndOfWord is True if node represent the end of the word


class Trie:

    def __init__(self):
        self.root = self.getNode()  # Trie data structure class

    def getNode(self):

        return TrieNode()  # Returns new trie node (initialized to NULLs)

    def _charToIndex(self, ch):  # '_' specifies weak Private as Python doesn't support full Private

        return ord(ch) - ord(u'\u0900')  # ord(u'\u0900') returns UTF-8 code for Hindi Letter

    def insert(self, key):

        pCrawl = self.root  # Variable which will move to every level
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])  # Finds index of the character

            if not pCrawl.children[index]:  # This will check if current index is filled or not
                pCrawl.children[index] = self.getNode()  # If not filled it will create node to next level
            pCrawl = pCrawl.children[index]  # It will then jump to next level and fill it

        pCrawl.isEndOfWord = True  # Mark last node as leaf

    def search(self, key):

        pCrawl = self.root  # Variable which will move to every level
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])  # Finds index of the character
            if not pCrawl.children[index]:  # This will check if current index is filled or not
                return False
            pCrawl = pCrawl.children[index]  # It will then jump to next level and fill it

        return pCrawl != None and pCrawl.isEndOfWord


output = ["Incorrect", "Correct"]
t = Trie()
x = []
y = []
for i in f:
    x.append(i)
for i in x:
    m = i.replace("\n", "")
    y.append(m)
for i in y:
    t.insert(i)
a = input()
print("{} ---- {}".format(a, output[t.search(a)]))


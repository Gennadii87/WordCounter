import re


class WordCounter:
    def __init__(self):
        self.words = {}

    def load_words_from_content(self, content):
        words = re.findall(r'\b[A-Za-z]+\b', content)
        for word in words:
            if word.lower() in self.words:
                self.words[word.lower()] += 1
            else:
                self.words[word.lower()] = 1

    def word_count(self, word):
        if word.lower() in self.words:
            return self.words[word.lower()]
        else:
            return 0

    def clear_memory(self):
        self.words = {}

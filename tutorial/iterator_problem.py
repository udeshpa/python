class Sentence:
    def __init__(self, sentence):
        self.tokens = sentence.split(' ')

    def __iter__(self):
        return SentenceItr(self.tokens)


class SentenceItr:
    def __init__(self, tokens):
        self.tokens = tokens
        self.itr = iter(self.tokens)

    def __next__(self):
        return next(self.itr)


s = Sentence('Hello this is a test')

for i in s:
    print(i)



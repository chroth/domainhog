class Tld(object):
    def __init__(self, name):
        self.name = name

    def get_suggestion(self, word):
        word = word.strip().lower()
        if word[-1 * len(self.name):] == self.name:
            return word[:-1 * len(self.name)] + '.' + self.name
        return ''

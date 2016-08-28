class Word:
    def __init__(self, value):
        self.value = value
        self.count = 1


class DataMining:
    """
    Class responsible to compare replicated data and store in a special model IngredientSpec
    and agroup counting repetitions
    """

    def __init__(self):
        self.words = set()

    def analysis(self, ingredient):
        self.save_words(ingredient)

    def save_words(self, word):
        found = False
        for word in self.words:
            if word == word.value:
                word.count += 1
                found = True

        if not found:
            self.words.add(Word(value=word))

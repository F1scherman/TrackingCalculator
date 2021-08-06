import calculatorAdsDataBase
import random
class advertising():
    """A class for managing advertisements"""
    def __init__(self, listOfAds):
        self._ads = listOfAds

    def refresh(self, dataBase):
        weights = eval(dataBase.get().rstrip(')').lstrip('('))
        chances = []
        variables = ["pi","tan","log","ln","e","roots","sin"]
        for i in range(7):
            write = variables[i]
            for j in range(5):
                chances.append(write)
            for j in range(weights[i]):
                chances.append(write)

        choice = chances[random.randint(0,(len(chances)-1))]
        choice = variables.index(choice)
        return self._ads[choice]

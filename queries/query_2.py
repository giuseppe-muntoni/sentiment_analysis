from data.stream import mystream
from data_structures.space_saving import SpaceSaving


class Query2():
    def __init__(self, csv, ss_dim, best_n):
        self.csv = csv
        self.dim = ss_dim
        self.n = best_n
        self.wordsOccs = dict()
        self.exactHH = list()
        self.approxHH = SpaceSaving(ss_dim)

    def resetStream(self):
        self.stream = mystream(self.csv)

    def printExactStats(self):
        print("*************** DATASET " + self.csv + " STATS *************")
        print("Question 2: Spell the 30 favorite words of happy users")
        print("*********************** EXACT **********************")
        for i in range(0, len(self.exactHH)):
            print(self.exactHH[i])

    def printApproximatedStats(self):
        print("*************** DATASET " + self.csv + " STATS *************")
        print("Question 2: Spell the 30 favorite words of happy users")
        print("**************** APPROXIMATED **********************")
        queryRes = self.approxHH.query(self.n)
        for i in range(0, len(queryRes)):
            print("(" + queryRes[i]['value'] + ", " +
                  queryRes[i]['frequency'] + ", " + queryRes[i]['error'] + ')')

    def executeApproximated(self):
        Query2.resetStream(self)

        while self.stream.nextRecord() is not None:
            if self.stream.ispositive():
                words = self.stream.tokenizedTweet()
                for word in words:
                    self.approxHH.add(word)

    def executeExact(self):
        Query2.resetStream(self)
        while self.stream.nextRecord() is not None:
            if self.stream.ispositive():
                words = self.stream.tokenizedTweet()
                for word in words:
                    if word in self.wordsOccs:
                        self.wordsOccs[word] += 1
                    else:
                        self.wordsOccs[word] = 1

        self.exactHH = sorted(self.wordsOccs.items(),
                              key=lambda x: x[1],
                              reverse=True)[0:self.n]

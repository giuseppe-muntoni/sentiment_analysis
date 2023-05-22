from data.stream import mystream
from data_structures.space_saving import SpaceSaving


class Query4():
    def __init__(self, csv, ss_dim, best_n):
        self.csv = csv
        self.dim = ss_dim
        self.n = best_n
        self.happyLengthHH = SpaceSaving(ss_dim)
        self.unhappyLengthHH = SpaceSaving(ss_dim)
        self.happyLengthMean = 0
        self.unhappyLengthMean = 0
        self.happyLenghtMeanApprox = 0
        self.unhappyLenghtMeanApprox = 0

    def resetStream(self):
        self.stream = mystream(self.csv)

    def printExactStats(self):
        print("*************** DATASET " + self.csv + " STATS *************")
        print(
            "Question 4: Decide if in general happy messages are longer or shorter than unhappy messages"
        )
        print("*********************** EXACT **********************")
        print("Mean happy messages len: " + str(self.happyLengthMean))
        print("Mean unhappy messages len: " + str(self.unhappyLengthMean))

    def printApproximatedStats(self):
        print("*************** DATASET " + self.csv + " STATS *************")
        print(
            "Question 4: Decide if in general happy messages are longer or shorter than unhappy messages"
        )
        print("**************** APPROXIMATED **********************")
        print("Mean happy messages len: " + str(self.happyLenghtMeanApprox))
        print("Mean unhappy messages len: " +
              str(self.unhappyLenghtMeanApprox))

    def executeApproximated(self):
        Query4.resetStream(self)

        while self.stream.nextRecord() is not None:
            if self.stream.ispositive():
                self.happyLengthHH.add(self.stream.messageLen())
            else:
                self.unhappyLengthHH.add(self.stream.messageLen())

        for lengthHH in self.happyLengthHH.query(self.n):
            self.happyLenghtMeanApprox += lengthHH['value']

        self.happyLenghtMeanApprox /= self.n

        for lengthHH in self.unhappyLengthHH.query(self.n):
            self.unhappyLenghtMeanApprox += lengthHH['value']

        self.unhappyLenghtMeanApprox /= self.n

    def executeExact(self):
        Query4.resetStream(self)
        totalHappy = 0
        totalUnhappy = 0

        while self.stream.nextRecord() is not None:
            if self.stream.ispositive():
                totalHappy += 1
                self.happyLengthMean += self.stream.messageLen()
            else:
                totalUnhappy += 1
                self.unhappyLengthMean += self.stream.messageLen()

        self.happyLengthMean /= totalHappy
        self.unhappyLengthMean /= totalUnhappy

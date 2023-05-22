from data.stream import mystream
from data_structures.bloom_filter import BloomFilter
from data_structures.linear_counter import LinearCounter


class Query3():
    def __init__(self, csv, lc_dim, bf_dim, bf_k):
        self.csv = csv
        self.wordsOnceBF = BloomFilter(bf_dim, bf_k)
        self.wordsDistinctLC = LinearCounter(lc_dim)
        self.wordsOnceSet = set()
        self.wordsDistinctSet = set()

    def resetStream(self):
        self.stream = mystream(self.csv)

    def printExactStats(self):
        print("*************** DATASET " + self.csv + " STATS *************")
        print(
            "Question 3: Find the number of distinct words used by happy users"
        )
        print("*********************** EXACT **********************")
        print("Happy users distinct words with frequency = 1: " +
              str(len(self.wordsOnceSet)))
        print("Happy users distinct words with frequency > 1: " +
              str(len(self.wordsDistinctSet)))

    def printApproximatedStats(self):
        print("*************** DATASET " + self.csv + " STATS *************")
        print(
            "Question 3: Find the number of distinct words used by happy users"
        )
        print("**************** APPROXIMATED **********************")
        print("Happy users distinct words with frequency > 1: " +
              str(self.wordsDistinctLC.count()))

    def executeApproximated(self):
        Query3.resetStream(self)

        while self.stream.nextRecord() is not None:
            if self.stream.ispositive():
                words = self.stream.tokenizedTweet()
                for word in words:
                    if (self.wordsOnceBF.contains(word)):
                        self.wordsDistinctLC.add(word)
                    else:
                        self.wordsOnceBF.add(word)

    def executeExact(self):
        Query3.resetStream(self)

        while self.stream.nextRecord() is not None:
            if self.stream.ispositive():
                words = self.stream.tokenizedTweet()
                for word in words:
                    if word in self.wordsOnceSet:
                        self.wordsDistinctSet.add(word)
                    else:
                        self.wordsOnceSet.add(word)

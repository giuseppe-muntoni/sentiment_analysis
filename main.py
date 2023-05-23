# 10k random lines from https://www.kaggle.com/kazanova/sentiment140 containing
# the polarity of the tweet ("+", "-")
# the date of the tweet
# the user that tweeted
# the text of the tweet

from queries.query_1 import Query1
from queries.query_2 import Query2
from queries.query_3 import Query3
from queries.query_4 import Query4

if __name__ == "__main__":
    # mini.csv
    # Question 1
    question1Mini = Query1("data/mini.csv", 5000)
    question1Mini.executeExact()
    question1Mini.executeApproximated()
    question1Mini.printExactStats()
    question1Mini.printApproximatedStats()
    # Question 2
    question2Mini = Query2("data/mini.csv", 40, 30)
    question2Mini.executeExact()
    question2Mini.executeApproximated()
    question2Mini.printExactStats()
    question2Mini.printApproximatedStats()
    # Question 3
    question3Mini = Query3("data/mini.csv", lc_dim=50000, bf_dim=4000, bf_k=2)
    question3Mini.executeExact()
    question3Mini.executeApproximated()
    question3Mini.printExactStats()
    question3Mini.printApproximatedStats()
    # Question 4
    question4Mini = Query4("data/mini.csv", 5, 5)
    question4Mini.executeExact()
    question4Mini.executeApproximated()
    question4Mini.printExactStats()
    question4Mini.printApproximatedStats()

    # sample.csv
    # Question 1
    question1Medium = Query1("data/sample.csv", lc_dim=12000)
    question1Medium.executeExact()
    question1Medium.executeApproximated()
    question1Medium.printExactStats()
    question1Medium.printApproximatedStats()
    # Question 2
    question2Medium = Query2("data/sample.csv", ss_dim=400, best_n=30)
    question2Medium.executeApproximated()
    question2Medium.executeExact()
    question2Medium.printExactStats()
    question2Medium.printApproximatedStats()
    # Question 3
    question3Medium = Query3("data/sample.csv", lc_dim=8000, bf_dim=200000, bf_k=8)
    question3Medium.executeApproximated()
    question3Medium.executeExact()
    question3Medium.printExactStats()
    question3Medium.printApproximatedStats()
    # Question 4
    question4Medium = Query4("data/sample.csv", ss_dim=512, best_n=96)
    question4Medium.executeApproximated()
    question4Medium.executeExact()
    question4Medium.printExactStats()
    question4Medium.printApproximatedStats()

    # complete.csv
    # Question 1
    question1Huge = Query1("data/complete.csv", lc_dim=160000000)
    question1Huge.executeExact()
    question1Huge.executeApproximated()
    question1Huge.printExactStats()
    question1Huge.printApproximatedStats()
    # Question 2
    question2Huge = Query2("data/complete.csv", ss_dim=400, best_n=30)
    question2Huge.executeApproximated()
    question2Huge.executeExact()
    question2Huge.printExactStats()
    question2Huge.printApproximatedStats()
    # Question 3
    question3Huge = Query3("data/complete.csv", lc_dim=200000, bf_dim=800000, bf_k=32)
    question3Huge.executeApproximated()
    question3Huge.executeExact()
    question3Huge.printExactStats()
    question3Huge.printApproximatedStats()
    # Question 4
    question4Huge = Query4("data/complete.csv", ss_dim=512, best_n=96)
    question4Huge.executeApproximated()
    question4Huge.executeExact()
    question4Huge.printExactStats()
    question4Huge.printApproximatedStats()

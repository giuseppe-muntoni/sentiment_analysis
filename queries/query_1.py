from data.stream import mystream, dayPart
from data_structures.linear_counter import LinearCounter


class Query1():
    def __init__(self, csv, lc_dim):
        self.m = lc_dim
        self.csv = csv
        self.stream = mystream(csv)
        # Linear counters definition
        self.lc_all = LinearCounter(self.m)
        self.lc_happy = LinearCounter(self.m)
        self.lc_unhappy = LinearCounter(self.m)
        self.lc_morning = LinearCounter(self.m)
        self.lc_afternoon = LinearCounter(self.m)
        self.lc_evening = LinearCounter(self.m)
        self.lc_night = LinearCounter(self.m)
        # Exact counters definition
        self.countAll = 0
        self.countHappy = 0
        self.countUnhappy = 0
        self.countHappyMorning = 0
        self.countHappyAfternoon = 0
        self.countHappyEvening = 0
        self.countHappyNight = 0
        self.countUnhappyMorning = 0
        self.countUnhappyAfternoon = 0
        self.countUnhappyEvening = 0
        self.countUnhappyNight = 0

    def resetStream(self):
        self.stream = mystream(self.csv)

    def printExactStats(self):
        print("*************** DATASET " + self.csv + " STATS *************")
        print(
            "Question 1: Count the percentage of happy users in the different moments of the day (morning, afternoon, evening, night)"
        )
        print("************************ EXACT *********************")
        # Counting total happy and unhappy
        print("Total number of users: " + str(self.countAll))
        print("Total happy: " + str(self.countHappy))
        print("Total unhappy: " + str(self.countUnhappy))
        # Counting happy in different moments of the day
        print("Morning happy: " +
              str((self.countHappyMorning / self.countHappy * 100)))
        print("Afternoon happy: " +
              str((self.countHappyAfternoon / self.countHappy * 100)))
        print("Evening happy: " +
              str((self.countHappyEvening / self.countHappy * 100)))
        print("Night happy: " +
              str((self.countHappyNight / self.countHappy * 100)))
        # Counting unhappy in different moments of the day
        print("Morning unhappy: " +
              str((self.countUnhappyMorning / self.countUnhappy * 100)))
        print("Afternoon unhappy: " +
              str((self.countUnhappyAfternoon / self.countUnhappy * 100)))
        print("Evening unhappy: " +
              str((self.countUnhappyEvening / self.countUnhappy * 100)))
        print("Night unhappy: " +
              str((self.countUnhappyNight / self.countUnhappy * 100)))

    def printApproximatedStats(self):
        print("*************** DATASET " + self.csv + " STATS *************")
        print(
            "Question 1: Count the percentage of happy users in the different moments of the day (morning, afternoon, evening, night)"
        )
        print("**************** APPROXIMATED **********************")
        # Counting total happy and unhappy
        print("Total number of users: " + str(self.lc_all.count()))
        print("Total happy: " + str(self.lc_happy.count()))
        print("Total unhappy: " + str(self.lc_unhappy.count()))
        print("Total happy or unhappy: " +
              str(self.lc_happy.count_union(self.lc_unhappy)))
        # Counting happy in different moments of the day
        print("Morning happy: " +
              str((self.lc_happy.count_intersection(self.lc_morning) /
                   self.lc_happy.count()) * 100))
        print("Afternoon happy: " +
              str((self.lc_happy.count_intersection(self.lc_afternoon) /
                   self.lc_happy.count()) * 100))
        print("Evening happy: " +
              str((self.lc_happy.count_intersection(self.lc_evening) /
                   self.lc_happy.count()) * 100))
        print("Night happy: " +
              str((self.lc_happy.count_intersection(self.lc_night) /
                   self.lc_happy.count()) * 100))
        # Counting unhappy in different moments of the day
        print("Morning unhappy: " +
              str((self.lc_unhappy.count_intersection(self.lc_morning) /
                   self.lc_unhappy.count()) * 100))
        print("Afternoon unhappy: " +
              str((self.lc_unhappy.count_intersection(self.lc_afternoon) /
                   self.lc_unhappy.count()) * 100))
        print("Evening unhappy: " +
              str((self.lc_unhappy.count_intersection(self.lc_evening) /
                   self.lc_unhappy.count()) * 100))
        print("Night unhappy: " +
              str((self.lc_unhappy.count_intersection(self.lc_night) /
                   self.lc_unhappy.count()) * 100))

    def executeApproximated(self):
        self.resetStream()
        # Linear counters init
        while self.stream.nextRecord() is not None:
            self.lc_all.add(self.stream.getUser())
            # Happy tweets
            if self.stream.ispositive():
                self.lc_happy.add(self.stream.getUser())
            # Unhappy tweets
            if self.stream.isnegative():
                self.lc_unhappy.add(self.stream.getUser())
            # Morning tweets
            if self.stream.timeBin() == dayPart.MORNING:
                self.lc_morning.add(self.stream.getUser())
            # Afternoon tweets
            if self.stream.timeBin() == dayPart.AFTERNOON:
                self.lc_afternoon.add(self.stream.getUser())
            # Evening tweets
            if self.stream.timeBin() == dayPart.EVENING:
                self.lc_evening.add(self.stream.getUser())
            # Night tweets
            if self.stream.timeBin() == dayPart.NIGHT:
                self.lc_night.add(self.stream.getUser())

    def executeExact(self):
        self.resetStream()
        while self.stream.nextRecord() is not None:
            self.countAll += 1
            # Happy tweets
            if self.stream.ispositive():
                self.countHappy += 1
                # Morning tweets
                if self.stream.timeBin() == dayPart.MORNING:
                    self.countHappyMorning += 1
                # Afternoon tweets
                if self.stream.timeBin() == dayPart.AFTERNOON:
                    self.countHappyAfternoon += 1
                # Evening tweets
                if self.stream.timeBin() == dayPart.EVENING:
                    self.countHappyEvening += 1
                # Night tweets
                if self.stream.timeBin() == dayPart.NIGHT:
                    self.countHappyNight += 1
            # Unhappy tweets
            if self.stream.isnegative():
                self.countUnhappy += 1
                # Morning tweets
                if self.stream.timeBin() == dayPart.MORNING:
                    self.countUnhappyMorning += 1
                # Afternoon tweets
                if self.stream.timeBin() == dayPart.AFTERNOON:
                    self.countUnhappyAfternoon += 1
                # Evening tweets
                if self.stream.timeBin() == dayPart.EVENING:
                    self.countUnhappyEvening += 1
                # Night tweets
                if self.stream.timeBin() == dayPart.NIGHT:
                    self.countUnhappyNight += 1

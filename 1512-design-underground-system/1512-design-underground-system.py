class UndergroundSystem:

    def __init__(self):
        self.CheckInMap = {} #to store the check in time that we would use in the check out function
        self.TotalTimeMap = {} #to keep track of the total count and the occurence


    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.CheckInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, time = self.CheckInMap[id]

        if (start, stationName) not in self.TotalTimeMap:
            self.TotalTimeMap[(start, stationName)] = [0, 0] #so that a key error does not get raised
        self.TotalTimeMap[(start, stationName)][0] += t - time
        self.TotalTimeMap[(start, stationName)][1] += 1


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.TotalTimeMap[(startStation, endStation)]
        return total / count # no double slash because the average is meant to be a float


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
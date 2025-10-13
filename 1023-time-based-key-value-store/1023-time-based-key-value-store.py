from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.times = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.times:
            self.times[key] = [(timestamp, value)]
        else:
            self.times[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.times:
            left = 0
            right = len(self.times[key]) - 1
            best = ""
            
            while left <= right:
                mid = (left + right)// 2 #indice
                middle_time = self.times[key][mid][0]
                value = self.times[key][mid][1]
            
                if middle_time == timestamp:
                    return self.times[key][mid][1]
                elif timestamp < middle_time:
                    right = mid - 1
                else:
                    best = value
                    left = mid + 1

            return best #we need to return closest timestamp 
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


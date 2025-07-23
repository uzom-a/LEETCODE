class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i ,s in enumerate(senate):
            if s == "R":
                radiant.append(i) #we are keeping track of the position
            else:
                dire.append(i)

        while radiant and dire: # so that once one is empty we stop the loop
            r = radiant.popleft()
            d = dire.popleft()

            if r < d: #the one that comes first kills the other
                radiant.append(r + n) #The winner goes back in line with their index shifted by n to simulate the circular queue.
            else:
                dire.append(d + n)


        return "Radiant" if radiant else "Dire"

        #Time Complexity= 0(n)
        #Space Complexity = O(n)
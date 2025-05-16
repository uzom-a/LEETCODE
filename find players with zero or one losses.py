class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #INITIALIZE VARIABLES
        loss_count = defaultdict(int) #storing the frequency of the losses
        answer = [[], []]
        players = set() #so that we get the unique players
        
        #ITERATE OVER THE MATCHES LIST AND ADD TO THE PLAYERS SET
        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            loss_count[loser] += 1
            
        #LET'S ARRANGE THE OUTPUT      
        for player in players:
            if loss_count[player] == 0:
                answer[0].append(player)
                
            if loss_count[player] == 1:
                answer[1].append(player)
                
        answer[0].sort()
        answer[1].sort()
        
        return answer
                

"""
so the time complexity is O(n log n)
and space complexity is O(n)
"""

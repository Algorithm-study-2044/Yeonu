class Player:
    def __init__(self, idx):
        self.idx = idx
        self.follower = []
        self.following = []
        
    def add_follower(self, follow_idx):
        self.follower.append(follow_idx)
    
    def add_following(self, following_idx):
        self.following.append(following_idx)

class Solution(object): 
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        player_list = []
        result = []
        for idx in range(1, n+1):
            player_list.append(Player(idx))

        for [idx, follow_idx] in trust:
            player_list[idx-1].add_follower(follow_idx)
            player_list[follow_idx - 1].add_following(idx)
        
        for player in player_list:
            if len(player.follower) == 0 and len(player.following) == n-1:
                result.append(player.idx)
        
        if len(result) == 1:
            return result[0]
        else:
            return -1

        
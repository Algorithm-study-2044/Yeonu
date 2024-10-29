class Twitter(object):

    def __init__(self):
        self.postList = defaultdict(list) # userId: [postId]
        self.followList = defaultdict(list) # userId: [userId] # 이차원 배열로 수정 가능
        # 순서가 없다는 의미임. (중복 X)
        # delete할 때 시간복잡도 때문에 사용
        self.order = 0

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId in self.postList:
            self.postList[userId].append((self.order, tweetId))
        else:
            self.postList[userId] = [(self.order, tweetId)]
        
        self.order += 1
        

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        searchUsers = [userId]
        if userId in self.followList:
            searchUsers += self.followList[userId]
        
        targetPost = []
        for searchUserId in searchUsers:
            if searchUserId in self.postList:
                targetPost += self.postList[searchUserId]

        targetPost.sort(key=lambda post: -post[0])
 
        return [post[1] for post in targetPost][:10]

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.followList and followeeId not in self.followList[followerId]:
            self.followList[followerId].append(followeeId)
        else:
            self.followList[followerId] = [followeeId]
            

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followeeId in self.followList[followerId]:
            self.followList[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
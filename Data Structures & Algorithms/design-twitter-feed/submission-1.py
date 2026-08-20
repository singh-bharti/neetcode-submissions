class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = {}
        self.following = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append([tweetId, self.time])
        

    def getNewsFeed(self, userId: int) -> List[int]:
        result = []
        maxHeap = []
        
        users = set()

        users.add(userId)

        if userId in self.following:
            for followeeId in self.following[userId]:
                users.add(followeeId)
        
        for id in users:
            if id not in self.tweets or not self.tweets[id]:
                continue

            tweetIndex = len(self.tweets[id]) - 1
            tweetId, time = self.tweets[id][tweetIndex]

            heapq.heappush(maxHeap, (-time, tweetId, id, tweetIndex))
            
        while maxHeap and len(result) < 10:
            negTime, tweetId, userId, tweetIndex = heapq.heappop(maxHeap)
            result.append(tweetId)

            previousIndex = tweetIndex - 1

            if previousIndex >= 0:

                previousTweetId, previousTime = \
                    self.tweets[userId][previousIndex]

                heapq.heappush(
                    maxHeap,
                    (
                        -previousTime,
                        previousTweetId,
                        userId,
                        previousIndex
                    )
                )
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return 
        
        if followerId not in self.following:
            self.following[followerId] = set()
        
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        

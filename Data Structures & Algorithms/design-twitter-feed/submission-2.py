class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId]) # need to include count to determine the most recent tweets
        self.count -= 1         # negative since we're going to use minHeap, 
                                # hence the most recent tweet will be the leftMost item in the minHeap (least value)

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        # get the list of followeeId that the user follows, including themselves
        self.followMap[userId].add(userId)  
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1      # get the index of the last value in the list of tweets for the particular followee
                count, tweetId = self.tweetMap[followeeId][index]   # retrieve the count and tweetId using the index
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])    # push them in the minHeap 
                                                                # - make sure count is the first in the list as we're using it to sort the heap.
                                                                # - we also include the followeeId and the next tweet list index (index-1) 
                                                                #   we'd want to look at for that same followee -> self.tweetMap[followeeId][nextIdx]
        
        # get the 10 most recent tweets from the minHeap
        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)  # this will pop the most recent tweet first (least count value)
            res.append(tweetId)

            # if current index of the tweet list for the current followeeId is not yet exhausted
            if index >= 0:
                # get the next one from the list of tweets and push it to the heap
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])    # push the next index (index -1) again
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)


## MinHeap Solution
# Time Complexity: O(nlogn) for each getNewsFeed() call and O(1) for remaining methods.
# Space Complexity: O(N∗m+N∗M+n)
# Where 
#   n is the total number of followeeIds associated with the userId, 
#   m is the maximum number of tweets by any user, 
#   N is the total number of userIds and 
#   M is the maximum number of followees for any user.
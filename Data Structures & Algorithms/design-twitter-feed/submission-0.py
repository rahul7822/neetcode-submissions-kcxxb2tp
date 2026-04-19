class MaxHeap:
    def __init__(self):
        self.heap = []

    def length(self):
        return len(self.heap)

    def peek(self):
        if self.heap:
            return self.heap[0]
        return None
    
    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return 2 * index + 1
    
    def right(self, index):
        return 2 * index + 2

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(self.length() - 1)
    
    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            parent = self.parent(index)
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
    
    def remove(self):
        if self.heap:
            root = self.heap[0]
            val = self.heap.pop()
            if self.heap:
                self.heap[0] = val
                self._heapify_down(0)
            return root
        return None
    
    def _heapify_down(self, index):
        left = self.left(index)
        right = self.right(index)
        heap_len = self.length()

        target = index
        if left < heap_len and self.heap[target] < self.heap[left]:
            target = left
        if right < heap_len and self.heap[target] < self.heap[right]:
            target = right

        if target != index:
            self.heap[target], self.heap[index] = self.heap[index], self.heap[target]
            self._heapify_down(target)

class Twitter:

    def __init__(self):
        self.follower_dict = {}
        self.tweets_dict = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets_dict:
            self.tweets_dict[userId] = [tweetId]
        else:
            self.tweets_dict[userId].append(tweetId)

    def getNewsFeed(self, userId: int) -> List[int]:
        max_heap = MaxHeap()
        
        if userId in self.tweets_dict:
            for tweet_id in self.tweets_dict[userId]:
                max_heap.insert(tweet_id)
        
        if userId in self.follower_dict:
            followers = self.follower_dict[userId]
            for follower_id in followers:
                if follower_id in self.tweets_dict:
                    for tweet_id in self.tweets_dict[follower_id]:
                        max_heap.insert(tweet_id)

        result = []
        counter = 0
        while max_heap.peek() and counter <= 10:
            result.append(max_heap.remove())
            counter += 1

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follower_dict:
            self.follower_dict[followerId] = {followeeId}
        else:
            self.follower_dict[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follower_dict:
            self.follower_dict[followerId].discard(followeeId)

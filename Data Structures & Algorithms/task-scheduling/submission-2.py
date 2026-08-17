from collections import Counter, deque
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # We don't need to keep track of the list of tasks execution,
        # we only want to find the min. number of time to complete all tasks
        
        # create a maxHeap where we store the number of counts per task
        counter = Counter(tasks)
        maxHeap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxHeap)      # we'll want to prioritize using the tasks with higher count
                                    # to minimize the amount of idle time

        # create a cooldown queue which will store the count number of a remaining task 
        #       and the time when it will be done with its cooldown 
        q = deque()     # [-cnt, time when it will be available to be pushed back to the heap]

        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                taskCount = heapq.heappop(maxHeap) + 1 # +1 to reduce count since we stored the negative val of count
                # append reduced task count to the cooldown queue along with cooldown time expiration
                if taskCount:                           # if taskCount is not 0, keep adding it to the queue
                    q.append([taskCount, time + n])  
            
            # check cooldown queue if any of its elements can be pushed back to the heap
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0]) # only push the count num back to the heap
        
        return time


# MaxHeap Solution
# Time complexity: O(n * m), where m is the number of tasks and n is the cool down time
# Space complexity: O(1) since we have at most 26 different characters.
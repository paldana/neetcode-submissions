class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Max Heap solution 
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]  # only storing tasks as number of occurences from the tasks list
        heapq.heapify(maxHeap)                      # negative to utilize max heap, so we have the most 
                                                    # number of tasks from the list to be the first one in the heap

        time = 0     # running cycle time which the idleTime will use to compare with 
        q = deque()  # pairs of [-cnt, idleTime] - stores the queue for tasks recently processed;
                     # -cnt: number of tasks remaining in the list
                     # idleTime: the time when it can be pushed back to the heap to be processed again
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                # process the most occuring task from the heap and decrease the number of occurence by 1 
                cnt = 1 + heapq.heappop(maxHeap)    # +1 since we're using negative for counter -> maxHeap purposes
                if cnt:
                    q.append([cnt, time + n])       # add the task along with its idleTime in the queue
                                                    # current time + n given cycles = idleTime 
            # if idleTime of the pair in the queue matches time, it can be processed again
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])     # so we push it back to the heap
        
        # run the loop until there's no more elements in either queue or heap to get the total time
        return time

# Time & Space Complexity
# Time complexity: O(m)
# Space complexity: O(1) since we have at most 26 different characters.
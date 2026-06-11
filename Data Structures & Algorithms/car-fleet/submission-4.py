class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]    # pair the 2 lists and save in another list
        pair.sort(reverse=True)     # reverse the list and have the closest to the target pos be first
        eta = []                    # stack of ETA for each car

        for p, s in pair:
            eta.append((target - p) / s)     # calc fleet ETA and append to stack (less means faster)

            # check if the top 2 in the list will have a chance to merge
            # by checking if the ETA of the farthest position (eta[-2]) 
            # will take longer than the ETA of the most recent fleet (eta[-1]). 
            # If they do, then pop the top one (faster fleet), 
            # since they're going to arrive at the same time as the slower fleet
            if len(eta) >= 2 and eta[-1] <= eta[-2]:
                eta.pop()

        return len(eta)     # len(eta) will be the number of different car fleets 


# Stack method
# time: O(n log n) - n for going through the list; log n for sorting
# space: O(n)
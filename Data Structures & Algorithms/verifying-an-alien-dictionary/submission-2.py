class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        def compare(word):
            return [order_index[c] for c in word]

        return words == sorted(words, key=compare)


## Built-in Python Sorting feature
# Time: O(n * m log(n)) 
# Space: O(n * m)
# - where n = number of words and m average length of a word


## NeetBot AI Complexity Analysis
# Time complexity: O(c), where c is the total number of characters across all words in the input list.
# Space Complexity: O(1)
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_index = {c: i for i, c in enumerate(order)}

        # def compare(word):
        #     return [order_index[c] for c in word]
        """
            the compare helper function returns an array of numerical representation of the letters based on the given order
            dag = [5, 2, 8]
            disk = [5, 9, 18, 11]
            dog = [5, 14, 8]

            the lambda will then sort the words using the values above to determine the given order
        """

        # return words == sorted(words, key=compare)
        
        # alternatively, using lambda expression
        return words == sorted(words, key=lambda word: [order_index[c] for c in word])


## Built-in Python Sorting feature
# Time: O(n * m log(n))         - worst-case
# Space: O(n * m)
# - where n = number of words and m average length of a word


## NeetBot AI Complexity Analysis
# Time complexity: O(c), where c is the total number of characters across all words in the input list.
# Space Complexity: O(1)
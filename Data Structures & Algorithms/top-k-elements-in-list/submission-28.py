class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #Creates the element : freq ratio
        freq = [[] for i in range(len(nums) + 1)] #Create a 2d array of buckets that counts for frequency based on index

        for n in nums: #Appending and modifying the hashmap to get the frequency of each element
            count[n] = 1 + count.get(n, 0)
        
        for num, cnt in count.items(): #Adding the elements to the index with respect to the freq
            freq[cnt].append(num)
        
        res = [] #Creates a new array
        #two for loops are necessary because its a 2d array, (where first we go to the end of the bucket)
        #second, we want to append the elements with the highest frequency into the res array.
        for i in range(len(freq) - 1, 0, -1): 
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res 
        




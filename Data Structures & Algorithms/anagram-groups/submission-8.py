class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26 #since its guaranteed to be lower case letters
            for c in s:
                count[ord(c) - ord('a')] += 1 #makes the freq of each character within the word in the list
            res[tuple(count)].append(s) #this will assign words that have the same exact frequency of the same letters and then appending to the res list
            
            #One example would be: [eat, ate]. Note that the letter placement is dependent on the index of the count array (a = 0, b = 1, etc)
            #tuple(count) = (the count list, but with letters that correspond to the index, having a specific amount added with respect to the word)

        return list(res.values())

        
        
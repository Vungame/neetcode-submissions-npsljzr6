class Solution:

    def encode(self, strs: List[str]) -> str:
        res = [] #make an array that stores the encoding in between the strings
        for s in strs: #
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i #This starts at ('length'#'string) this makes the string in j
            while s[j] != '#':
                j += 1 #This means i is at the 'length' portion of the string and j is at the '#'
            length = int(s[i:j]) #So just the 'length' number would be assigned
            i = j + 1 #The is the starting point of the string
            j = i + length #This is the end point of the string
            res.append(s[i:j])
            i = j #This is necessary to bring j back to then end of the string, ie to where the 'length' part of the string is
        return res

        
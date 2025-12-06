class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        listRansom = list(ransomNote)
        listMag = list(magazine)

        # print(listRansom)
        # print(listMag)

        for letter in listRansom:
            # print(letter)
            if letter in listMag:
                listMag.remove(letter)
            
            # can iterate through ransom note and delete in list mag, because not iterating and deleting same thign
            # checks every letter in the ransom note, if its in magazine, it will remove it and move on
            else:
                # print('letter not in:', letter )
                # if not, return false
                return False

        return True
        
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = 1
        for significance, digit in enumerate(digits):
            result += digit * 10 ** (len(digits) - 1 - significance)
        result = str(result)
        out = []
        for s in result:
            out.append(int(s))
        return out

    def PlusOne2(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits = [1] + digits
        return digits




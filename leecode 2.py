class Solution:
    def romanToInt(self, s: str) -> int:
        Symbol_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        sum = 0
        list_s = list(s)

        for index in range(len(list_s) - 1, -1, -1):
            if index == (len(list_s) - 1):
                sum += Symbol_dict[list_s[index]]
            else:
                if Symbol_dict[list_s[index + 1]] > Symbol_dict[list_s[index]]:
                    sum -= Symbol_dict[list_s[index]]
                else:
                    sum += Symbol_dict[list_s[index]]

        return sum
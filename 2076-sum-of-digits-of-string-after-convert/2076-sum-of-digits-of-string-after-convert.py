class Solution:
    def getLucky(self, s: str, k: int) -> int:
        """
        PSEUDOCODE
        init ans
        convert string to a list
        convert alphabet to corresponding number
        add each result to an integer variable called ans
        k -= 1
        while k and sum > 9:
            get the tens digit
            get the units digit
            sum
            k -= 1
        return sum
        """
        list_numbers = []
        letters = list(s)
        ans = 0
        for ch in letters:
            number = str(ord(ch) - ord("a") + 1)
            list_numbers.append(number)

        joined_digits = "".join(list_numbers)
        temp_list = list(joined_digits)

        for i in range(len(temp_list)):
            temp_list[i] = int(temp_list[i])

        ans = sum(temp_list)
        # print (temp_list)
        # print(ans)

        k -= 1

        while k and ans > 9:
            ans = sum(int(d) for d in str(ans))
            # tens = ans // 10
            # unit = ans % 10
            # current_sum = tens + unit
            # ans = current_sum
            k -= 1
        return ans


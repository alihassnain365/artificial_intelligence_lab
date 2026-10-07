class RomanNumeral:
    def int_to_roman(self, number):
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40,
                   10, 9, 5, 4, 1]

        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL",
                   "X", "IX", "V", "IV", "I"]

        roman = ""

        for i in range(len(numbers)):
            while number >= numbers[i]:
                roman = roman + symbols[i]
                number = number - numbers[i]

        return roman


obj = RomanNumeral()

print(obj.int_to_roman(3))     # III
print(obj.int_to_roman(58))    # LVIII
print(obj.int_to_roman(1994))  # MCMXCIV
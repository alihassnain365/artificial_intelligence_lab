class PairIndices():
    def two_sum(self,numbers:list[int], target)->tuple:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return (i,j)
numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50

obj = PairIndices()

print(obj.two_sum(numbers, target))
            
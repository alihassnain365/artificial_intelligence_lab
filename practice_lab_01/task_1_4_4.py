class ToZero():
    def sum_to_zero(self,numbers:list[int])->tuple:
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                for k in range(j+1, len(numbers)):
                    if numbers[i] + numbers[j] + numbers[k] == 0:
                        return (i,j,k)

numbers = [-25, -10, -7, -3, 2, 4, 8, 10]

obj = ToZero()

print(obj.sum_to_zero(numbers))
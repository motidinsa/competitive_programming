class Solution(object):
    def fizzBuzz(self, n):
        listToBeReturned = []
        i=1
        while i<=n:

            if i % 3 == 0 and i % 5 == 0:
                listToBeReturned.append('FizzBuzz')
            elif i % 3 == 0:
                listToBeReturned.append('Fizz')
            elif i % 5 == 0:
                listToBeReturned.append('Buzz')
            else:
                listToBeReturned.append(str(i))
            i+=1
        return listToBeReturned




print(Solution().fizzBuzz(5))

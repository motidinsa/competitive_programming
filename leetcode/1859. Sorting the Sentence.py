class Solution(object):
    def sortSentence(self, s):
        sentenceArray = s.split()
        sentenceOrder = []
        sortedSentence = []
        for i in range(len(sentenceArray)):
            sentenceOrder.append(int(sentenceArray[i][len(sentenceArray[i]) - 1]))
            sortedSentence.append(int(sentenceArray[i][len(sentenceArray[i]) - 1]))
        sortedSentence.sort()
        for i in range(len(sentenceArray)):
            sortedSentence[sortedSentence.index(sentenceOrder[i])] = sentenceArray[i].replace(
                sentenceArray[i][len(sentenceArray[i]) - 1], '')
        return ' '.join(sortedSentence)


print(Solution().sortSentence("Myself2 Me1 I4 and3"))

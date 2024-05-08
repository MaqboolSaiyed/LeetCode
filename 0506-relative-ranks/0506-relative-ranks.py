class Solution:
    def findRelativeRanks(self, score):
        sorted_scores = sorted(range(len(score)), key=lambda k: score[k], reverse=True)
        result = [None] * len(score)
        for i, rank in enumerate(sorted_scores):
            if i == 0:
                result[rank] = "Gold Medal"
            elif i == 1:
                result[rank] = "Silver Medal"
            elif i == 2:
                result[rank] = "Bronze Medal"
            else:
                result[rank] = str(i + 1)
        return result
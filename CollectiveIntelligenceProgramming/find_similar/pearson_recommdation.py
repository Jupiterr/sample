# -*- coding: utf-8 -*-

from math import sqrt
# A dictionary of movie critics and their ratings of a small
# set of movies
critics = {'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                         'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                         'The Night Listener': 3.0},
           'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                            'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 3.5},
           'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                                'Superman Returns': 3.5, 'The Night Listener': 4.0},
           'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                            'The Night Listener': 4.5, 'Superman Returns': 4.0,
                            'You, Me and Dupree': 2.5},
           'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                            'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                            'You, Me and Dupree': 2.0},
           'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                             'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
           'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}


class recommdator():

	def __init__(self, prefs):
		self.critics = prefs

	def pearson(self, p1, p2):
		si = {}
		for item in self.critics[p1]:
			if item in self.critics[p2]:
				si[item] = 1
		n = len(si)
		if n == 0:
			return 1

		# 对所有求和
		sum1 = sum([self.critics[p1][it] for it in si])
		sum2 = sum([self.critics[p2][it] for it in si])

		# 平方和
		sum_sq1 = sum([pow((self.critics[p1][it]), 2) for it in si])
		sum_sq2 = sum([pow((self.critics[p2][it]), 2) for it in si])

		# 求两者的乘积之和
		p_sum = sum([self.critics[p1][it]*self.critics[p2][it] for it in si])

		# Pearson Recommendation
		num = p_sum - (sum1*sum2)/n
		den = sqrt((sum_sq1 - pow(sum1, 2)/n)*(sum_sq2 - pow(sum2, 2)/n))
		return 0 if (den == 0) else (num / den)

	if __name__ == "__main__":
		from pearson_recommdation import recommdator, critics
		pear = recommdator(critics)
		print "Our Similarity: %s" % pearson(pear, 'Lisa Rose', 'Gene Seymour')
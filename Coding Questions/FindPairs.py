#Write all solutions for a^3+b^3 = c^3 + d^3, where a, b, c, d lie between [0, 10^5].

def find_pairs(n):
	pair_dict = {}
	for a in xrange(1,n):
		for b in xrange(1,n):
			result = a**3 + b**3
			if result in pair_dict:
				print a,b,pair_dict[result][0],pair_dict[result][1]
			else:
				pair_dict[result] = [a,b]

find_pairs(10)

import scipy.stats as stats

observed = [2,	3,	0,	7,	2]

expected = [2.8,	2.8,	2.8,	2.8,	2.8]

print(stats.chisquare(f_obs=observed,f_exp=expected))

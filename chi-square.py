import scipy.stats as stats

observed = [2, 0, 3, 4, 0, 5, 4, 4, 4, 2, 4]

expected = [32/11, 32/11, 32/11, 32/11, 32/11, 32/11, 32/11, 32/11, 32/11, 32/11, 32/11]

print(stats.chisquare(f_obs=observed,f_exp=expected))

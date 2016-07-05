[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> This exercise uses the Cohen's d to investigate whether first babies are lighter or heavier than others. Cohen's d describes the size of an effect by comparing the variability within groups.

>> >> Cohen's d = (Mean of Group1 - Mean of Group2) / (Pooled standard deviation)

>> where

>> >> Pooled standard deviation = Square root(((Number of entries in Group1 * Variance in Group1) + (Number of rows in entries in Group2 * Variance in Group2)) / (Number of entries in Group1 + Group2))

>> In our example, Group1 would be the total weight in lbs of the first babies born to a mother and Group2 would be any other non-first babies born to a mother, indicated by the variable *birthord* in our data set. A *birthord* of one indicates a first-born child. In our data set, weight is recorded in two separate variables indicating pound and ounces of the baby,and *totalwgt_lb* combines these two variables to one in terms of lbs.

>> ```s = math.sqrt( ((len(first.totalwgt_lb) * first.totalwgt_lb.var())+(len(nonfirst.totalwgt_lb) * nonfirst.totalwgt_lb.var()))/(len(first.totalwgt_lb) + len(nonfirst.toatlwgt_lb)))```

>> ```cohens_d = (first.totalwgt_lb.mean() - nonfirst.totalwgt_lb.mean()) / s```

>> This gives us a Cohen's d of -0.08867. This number indicates that the mean of babies' birth weight decreases with non-first babies. The difference between the means of the two groups is 0.08867 standard deviations. Compared to pregnancy length, where the length of a mother's pregnancy for her first pregnancy relative to a mother's non-first pregnancies, where Cohen's d was 0.029. That means that pregnancies of non-first babies tend to be slightly longer than those of the first-born.

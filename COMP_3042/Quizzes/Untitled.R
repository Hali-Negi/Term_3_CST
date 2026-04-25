iterations = 10000
beta = 10
exp_simulation = rexp(iterations, 1/10)
hist(exp_simulation)
mean(exp_simulation)
median(exp_simulation)
length(exp_simulation[exp_simulation<5])/ iteratios

n = 15
sample_means = replicate(iteration, men,(rexp(n, 1/beta)))
hist(sample_means)
mean(sample_means)
median(sample_means)

n = 35
sample_means = replicate(iterations, men,mean(rexp(n, 1/beta)))
hist(sample_means)
mean(sample_means)
median(sample_means)
mean(exp_simulation)
sd(exp_simulation)


#f
sd(sample_means)
mean(sample_means)
10/sqrt(35)


#part h
length(sample-means[sample_means>6])/ iterations



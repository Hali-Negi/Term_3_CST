# part a
set.seed(42)
n= 25
mean = 250
sd = 40
sample_means=  replicate(1000, mean(rnorm(25, mean = 250, sd = 40)))


# part b 
hist(sample_means, breaks = 30,
     main = "Histogram of 1000 Sample Means",
     xlab = "Sample Mean Response Time (ms)",
     ylab = "Density",
     col = "lightblue", border = "white"
     probability = TRUE)

curve(dnorm(x, mean = 250, sd = 40/sqrt(25)),
      add = TRUE, col = "red", lwd = 2)



# part c
mean(sample_means)  
sd(sample_means)    


# part d Theoretical
(pnorm(1.2) - pnorm(-1.2)) * 100


# part d experimental
se = 40 / sqrt(25) 
mean(sample_means >= 250 - 1.2*se & sample_means <= 250 + 1.2*se) * 100
#from Environment pane, import WeatherData Excel file
# to see the first few rows of the data set:
head(WeatherData)

#to see the first few rows of colum MeanTemp:
head(WeatherData$MeanTemp)

#to calculate the mean of the MeanTemp column:
mean(WeatherData$MeanTemp)


#to calculate the mean of the TotalPrecip column:
mean(WeatherData$TotalPrecip)

#to calculate the sample standard deviation of MeanTemp:
sd(WeatherData$MeanTemp)


#to calculate a summary statistics of MeanTemp :
summary(WeatherData$MeanTemp)




#to find the 25th and the 90th percentiles within MeanTemp: 
quantile(WeatherData$MeanTemp, probs = c(0.25, 0.90))


#to make a histogram of the MeanTemp column:

hist(WeatherData$MeanTemp, 
     main= "Histogram of Temperature",
     xlab="Temeprature in degree Celsius",
     xlim=c(-10,25),
     col="lightblue",
     freq=TRUE
)


# change freq to FALSE to get probability distribution instead of frequency
hist(WeatherData$MeanTemp, 
     main= "Histogram of Temperature",
     xlab="Temeprature in degree Celsius",
     xlim=c(-10,25),
     col="lightgreen",
     freq=FALSE
)






#to make comparable plots (two plots next to each other):
par(mfrow=c(2,2))
hist(WeatherData$MeanTemp, 
     main= "Histogram of Temperature",
     xlab="Temeprature in degree Celsius",
     xlim=c(-10,25),
     col="lightblue",
     freq=TRUE
)

hist(WeatherData$MeanTemp, 
     main= "Histogram of Temperature",
     xlab="Temeprature in degree Celsius",
     xlim=c(-10,25),
     col="lightpink",
     freq=FALSE
)


#to construct a histogram where we want to control the width of classes:
hist(WeatherData$MeanTemp, 
     breaks = seq(-6,25,5),
     main= "Histogram of Temperature",
     xlab="Temeprature in degree Celsius",
     xlim=c(-10,25),
     col="lightgray",
     freq=FALSE
)




#to construct a boxplot of temperature:
boxplot(WeatherData$MeanTemp, 
        main="Mean Daily Temperature oC",
        xlab="2016-YVR",
        ylab= "Daily Temp",
        col="gold",
        border="brown",
        horizontal = FALSE,
        notch = FALSE
)



#to make a scatter plot of TotalPrecip versus MeanTemp:
input=WeatherData[,c("MeanTemp","TotalPrecip")]
plot(x=input$MeanTemp,y=input$TotalPrecip,
     xlab = "Daily Mean Temp oC",
     ylab = "Total Percipitation",
     xlim = c(-10,25),
     ylim = c(0,40),
     main = "Percipitation vs. Temperatutre for 2016",
     col="red", cex=0.8
)



#to find a subset of dataset where the percipitation is greater than 20:
rainy=subset(WeatherData, WeatherData$TotalPrecip>20)
head(rainy)

#to find a subset of dataset where the percipitation is greater than 20 and the MeanTemp is greater than 6
rainyandhot=subset(WeatherData, WeatherData$TotalPrecip>20 & WeatherData$MeanTemp>6)
head(rainyandhot)


#######################################
# R Commands from the lab handout     #
#######################################

Percents = c(10,30,5,35,20)
homeType = c("on campus", "with parents", "alone", "with roommates", "with spouse")
pie(Percents, homeType)
library(MASS) 
View(survey)
hands = survey$W.Hnd
tab = table(hands)
tab
pie(table(hands))

lbls = paste(rownames(tab), tab)
lbls
pie(table(hands), labels = lbls)
barplot(tab , horiz = TRUE)
numHeights = survey$Height[!is.na(survey$Height)]
range(numHeights)
breaks = seq(150, 205, by=5)  
breaks
numHeights.cut = cut(numHeights, breaks, right=FALSE)
numHeights.freq = table(numHeights.cut)
cbind(numHeights.freq)
hist(numHeights)
library(lattice)
xyplot(survey$Wr.Hnd ~ survey$Height)



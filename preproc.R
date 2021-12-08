install.packages("dplyr")
install.packages("caret")
install.packages("corrplot")
library(pROC)
require(dplyr)
require(caret)

data <- read.csv("~/PycharmProjects/bda_594/BDA594-Group10/cleaned_data.csv", header=TRUE)

df <- data

colnames(df)
dim(df)

# remove first column
data <- data[-1]
colnames(data)
df <- data

########## remove outliers from predictors ##########
# remove temp < 75 or > 108
temp_range <- (75:108)
data <- subset(data, data$temperature %in% temp_range)

# remove resprate > 100 or < 10
resp_rate <- (10:100)
data <- subset(data, data$resprate %in% resp_rate)

# remove O2 state below 60
o2_rate <- (60:1000)
data <- subset(data, data$o2sat %in% o2_rate)

# remove pain levels outside of 0-10 range
pain_range <- (0:10)
data <- subset(data, data$pain %in% pain_range)

# compare descriptive stats before and after
summary(df) # original dataset
summary(data)
removed_rows = dim(df[1]) - dim(data[1])
removed_rows <- removed_rows[1]
removed_rows

# replace values on acuity column with yes or no........
data$acuity[data$acuity == 0] <- "No"
data$acuity[data$acuity == 1] <- "Yes"

###### CENTER AND SCALE THE VARIABLES #####
set.seed(199)
preProcValues <- preProcess(data, method=c('center', 'scale'))
data_transformed <- predict(preProcValues, data)



## write a new csv file of cleaned dataset
write.csv(data_transformed, 'cleaned_data5.csv', row.names = FALSE)




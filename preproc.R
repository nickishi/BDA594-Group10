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

## write a new csv file of cleaned dataset
write.csv(data, 'cleaned_data2.csv', row.names = FALSE)


######### analyses ######### 

data <- read.csv("~/cleaned_data2.csv", header=TRUE)
View(data)

# split data into training and test set
# training set = .7

# replace values on acuity column with yes or no........
data$acuity[data$acuity == 0] <- "No"
data$acuity[data$acuity == 1] <- "Yes"

# create factor of 2 levels
data$acuity <- as.factor(data$acuity)

set.seed(199)
trainIndex <- createDataPartition(data$acuity, p = .7, list=F)
train_data <- data[trainIndex,]
test_data <- data[-trainIndex,]

# checking for imbalances
d.table<- table(data$acuity)
prop.table(d.table)


#setup control function for resampling and binary classification performance
#using 10 fold cross validation
ctrl <- trainControl(method = "cv", number=10, summaryFunction=twoClassSummary,
                     classProbs=T, savePredictions=T) #saving predictions from each resample fold


# simple additive logistic regression ON TRAINING DATA
set.seed(199)
default_glm_method = train(acuity ~ ., train_data, method="glm", family="binomial", metric="ROC", trControl=ctrl)
summary(default_glm_method)
varImp(default_glm_method)

set.seed(199)
mylogit <- glm(data ~ ., family="binomial", data=train_data)

#setup control function for resampling and binary classification performance
#using 10 fold cross validation
ctrl <- trainControl(method = "cv", number=10, summaryFunction=twoClassSummary,
                     classProbs=T, savePredictions=T) #saving predictions from each resample fold

##logistic regression
set.seed(199)#ALWAYS USE same SEED ACROSS trains to ensure identical cv folds
d.log <-  train(acuity ~ ., data=train_data, method="glm", family="binomial", metric="ROC", trControl=ctrl)
summary(d.log)
varImp(d.log)
d.log

#calculate resampled accuracy/confusion matrix using extracted predictions from resampling
confusionMatrix(d.log$pred$pred, d.log$pred$obs) #take averages

##linear discriminant analysis
set.seed(199)
d.lda <-  train(acuity~ ., data=train_data, method="lda", metric="ROC", trControl=ctrl)
d.lda
varImp(d.lda)
confusionMatrix(d.lda$pred$pred, d.lda$pred$obs) #take averages

#k nearest neighbors classification
set.seed(199) 
d.knn <-  train(acuity ~ ., data=train_data, method="knn", metric="ROC", trControl=ctrl, tuneLength=10) #let caret decide 10 best parameters to search
d.knn
plot(d.knn)
getTrainPerf(d.knn)

confusionMatrix(d.knn$pred$pred, d.knn$pred$obs) #make sure to select resamples only for optimal parameter of K


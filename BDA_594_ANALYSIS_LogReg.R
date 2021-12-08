install.packages("dplyr")
install.packages("caret")
install.packages("corrplot")
library(pROC)
require(dplyr)
require(caret)

######### analyses ######### 

data <- read.csv("~/cleaned_data5.csv", header=TRUE)
#data <- read.csv("cleaned_data2.txt")
View(data)

# split data into training and test set
# training set = .7

# replace values on acuity column with yes or no........
data$acuity[data$acuity == 0] <- "No"
data$acuity[data$acuity == 1] <- "Yes"

# create factor of 2 levels
data$acuity <- as.factor(data$acuity)

# relevel the yes category as the positive class
data$acuity <- relevel(data$acuity, ref="Yes")


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

##logistic regression
set.seed(199)#ALWAYS USE same SEED ACROSS trains to ensure identical cv folds
d.log <-  train(acuity ~ ., data=train_data, method="glm", family="binomial", metric="ROC", trControl=ctrl)
summary(d.log)
varImp(d.log)
d.log
d.log$finalModel

#calculate resampled accuracy/confusion matrix using extracted predictions from resampling
confusionMatrix(d.log$pred$pred, d.log$pred$obs) #take averages

#really need test set to get more accurate idea of accuracy when their is a rare class
#can either use model on cross validation of complete training data or hold out test set


#calculate ROC curves on resampled data

d.log.roc<- roc(response= d.log$pred$obs, predictor=d.log$pred$Yes)

#build to combined ROC plot with resampled ROC curves
plot(d.log.roc, legacy.axes=T)

#extract threshold from roc curve  get threshold at coordinates top left most corner
d.log.Thresh<- coords(d.log.roc, x="best", best.method="closest.topleft")
d.log.Thresh #sensitivity increases to 88% by reducing threshold to .0396 from .5


### TEST DATA ### 
# LOGISTIC REGRESSION

#predict probabilities on test set with log trained model
d.test <- test_data

test.pred.prob <- predict(d.log, d.test, type="prob")

test.pred.class <- predict(d.log, d.test) #predict classes with default .5 cutoff

#calculate performance with confusion matrix
confusionMatrix(test.pred.class, d.test$acuity)

#let draw ROC curve of training and test performance of logit model
test.log.roc<- roc(response= d.test$acuity, predictor=test.pred.prob[[1]]) #assumes postive class Yes is reference level
plot(test.log.roc, legacy.axes=T, col="red")
plot(d.log.roc, add=T, col="blue")
legend(x=.2, y=.7, legend=c("Test Logit", "Train Logit"), col=c("red", "blue"),lty=1)

#test performance slightly lower than resample
auc(test.log.roc)
auc(d.log.roc)

#calculate test confusion matrix using thresholds from resampled data
test.pred.class.newthresh <- factor(ifelse(test.pred.prob[[1]] > d.log.Thresh[1], "Yes", "No"))

#recalculate confusion matrix with new cut off predictions
confusionMatrix(test.pred.class.newthresh, d.test$acuity)


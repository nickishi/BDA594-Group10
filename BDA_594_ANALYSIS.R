install.packages("dplyr")
install.packages("caret")
install.packages("corrplot")
library(pROC)
require(dplyr)
require(caret)

######### analyses ######### 

#data <- read.csv("~/cleaned_data2.csv", header=TRUE)
data <- read.csv("cleaned_data2.txt")
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
ctrl <- trainControl(method = "cv", number=5, summaryFunction=twoClassSummary,
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
d.lda <-  train(acuity ~ ., data=train_data, method="lda", family="binomial", metric="ROC", trControl=ctrl)
d.lda
varImp(d.lda)
confusionMatrix(d.lda$pred$pred, d.lda$pred$obs) #take averages

#k nearest neighbors classification
set.seed(199) 
d.knn <-  train(acuity ~ ., data=train_data, method="knn", metric="ROC", trControl=ctrl, tuneLength=3) #let caret decide 10 best parameters to search
d.knn
plot(d.knn)
getTrainPerf(d.knn)

confusionMatrix(d.knn$pred$pred, d.knn$pred$obs) #make sure to select resamples only for optimal parameter of K

#really need test set to get more accurate idea of accuracy when their is a rare class
#can either use model on cross validation of complete training data or hold out test set

#lets compare all resampling approaches
d.models <- list("logit"=d.log, "lda"=d.lda,
                 "knn"=d.knn)
d.resamples = resamples(d.models)


#plot performance comparisons
bwplot(d.resamples, metric="ROC") 
bwplot(d.resamples, metric="Sens") #predicting default dependant on threshold
bwplot(d.resamples, metric="Spec") 

#calculate ROC curves on resampled data

d.log.roc<- roc(response= d.log$pred$obs, predictor=d.log$pred$Yes)
d.lda.roc<- roc(response= d.lda$pred$obs, predictor=d.lda$pred$Yes)
#when model has parameters make sure to select final parameter value
d.knn.roc<- roc(response= d.knn$pred[d.knn$pred$k==23,]$obs, predictor=d.knn$pred[d.knn$pred$k==23,]$Yes) 

#build to combined ROC plot with resampled ROC curves
plot(d.log.roc, legacy.axes=T)
plot(d.lda.roc, add=T, col="Blue")
plot(d.knn.roc, add=T, col="Red")
legend(x=.2, y=.7, legend=c("Logit", "LDA", "QDA", "KNN"), col=c("black","blue","green","red"),lty=1)

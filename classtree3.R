setwd("~/Desktop/BDA-594/Project")
mimicdata <-read.csv('cleaned_data2.csv')

library(rpart) 
library(tree) 
library(rpart.plot)

#create a test and train set
create_train_test <- function(mimicdata, size = 0.8, train = TRUE) {
  n_row = nrow(mimicdata)
  total_row = size * n_row
  train_sample <- 1: total_row
  if (train == TRUE) {
    return (mimicdata[train_sample, ])
  } else {
    return (mimicdata[-train_sample, ])
  }
}

#test your function and check the dimension
data_train <- create_train_test(mimicdata, 0.7, train = TRUE)
data_test <- create_train_test(mimicdata, 0.7, train = FALSE)
dim(data_train)

#use function prop.table() combined with table() to verify if the randomization process is correct
prop.table(table(data_train$acuity))
prop.table(table(data_test$acuity))

#build classification tree
mimic.ctree <- rpart(acuity~., data = data_train, method = 'class')
rpart.plot(mimic.ctree, extra = 106)

#get CP
opt.cp <- mimic.ctree$cptable[which.min(mimic.ctree$cptable[,"xerror"]),"CP"] #we get 0.016

#prune tree
printcp(mimic.ctree)
rpart.plot(prune(mimic.ctree,cp=0.016))

#make a prediction
predict(mimic.ctree, mimicdata, type = 'class')
predict_unseen <-predict(mimic.ctree, data_test, type = 'class')

#create confusion matrix to check accuracy
table_mat <- table(data_test$acuity, predict_unseen)
table_mat

#measure performance
accuracy_Test <- sum(diag(table_mat)) / sum(table_mat)
print(paste('Accuracy for test', accuracy_Test))

#tune hyoer-porameters
accuracy_tune <- function(mimic.ctree) {
  predict_unseen <- predict(mimic.ctree, data_test, type = 'class')
  table_mat <- table(data_test$acuity, predict_unseen)
  accuracy_Test <- sum(diag(table_mat)) / sum(table_mat)
  accuracy_Test
}

control <- rpart.control(minsplit = 4,
  minbucket = round(5 / 3),
  maxdepth = 3,
  cp = 0)
tune_mimic.ctree<- rpart(acuity~., data = data_train, method = 'class', control = control)
accuracy_tune(tune_mimic.ctree)

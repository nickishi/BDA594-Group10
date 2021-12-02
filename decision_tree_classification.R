# Decision Trees

#import data
mimicdata <-read.csv('cleaned_data2.csv')

#using rpart for regression tree
library(rpart) #faster than tree
library(tree) #has useful functions to use with rpart

#create tree
mimic.rtree <- rpart(acuity ~., data=mimicdata)

#summarize full tree (no pruning)
mimic.rtree

#by default tree plot needs some adjustments and labeling
plot(mimic.rtree)
text(mimic.rtree, pretty=0)

#rather than using default lets use new library
library(rpart.plot)

#very readable defaults
rpart.plot(mimic.rtree)

#tree is too bushy and has too much variance (overfit)
printcp(mimic.rtree) #display crossvalidated error for each tree size
plotcp(mimic.rtree) #plot cv error

#select CP with lowest crossvalidated error 
#we can grab this from the plotcp table automatically with 
opt.cp <- mimic.rtree$cptable[which.min(mimic.rtree$cptable[,"xerror"]),"CP"]

#lets prune the tree
mimic.rtree.pruned <- prune(mimic.rtree, cp=opt.cp)

#lets review the final tree
rpart.plot(mimic.rtree.pruned)

##MSE training Error of pruned decision tree
yhat.rtree<- predict(mimic.rtree.pruned, mimicdata)
mean((mimicdata$acuity - yhat.rtree)^2)
#we get an MSE of 0.2067742


#let's build classification tree
mimic.ctree <- rpart(acuity ~., data=mimicdata, method="class")

mimic.ctree

rpart.plot(mimic.ctree)

#lets prune this tree
printcp(mimic.ctree) 


rpart.plot(prune(mimic.ctree,cp=0.028))
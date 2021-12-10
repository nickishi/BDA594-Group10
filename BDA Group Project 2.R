triage_data = read.csv('/BDA Final Project/cleaned_data2_python.csv')

install.packages("scatterplot3d")
library("scatterplot3d")

library(ggplot2)

triage_sample2 = triage_data[seq(1,448972, by = 90),]
shapiro.test(triage_sample2$heartrate)

qqnorm(triage_data$heartrate, pch = 1, frame = FALSE , main = "Heartrate Normal Q-Q Plot")
qqline(triage_data$heartrate, col = "steelblue", lwd = 2)

hist(triage_data$heartrate,prob=TRUE,breaks="scott", main = "Histogram of Heartrate")

boxplot(triage_data$heartrate ~ triage_data$acuity, main="Patients Acuity per Heartrate (BPM) ", xlab = "Acuity", ylab = "Heartrate")
boxplot(triage_data$resprate ~ triage_data$acuity, main="Patients Acuity per Resprate (BPM)", xlab = "Acuity", ylab = "Resprate")

qqnorm(triage_data$sbp, pch = 1, frame = FALSE, main = "SBP Normal Q-Q Plot")
qqline(triage_data$sbp, col = "steelblue", lwd = 2)

qqnorm(triage_data$dbp, pch = 1, frame = FALSE, main = "DBP Normal Q-Q Plot")
qqline(triage_data$dbp, col = "steelblue", lwd = 2)

hist(triage_data$sbp,prob=TRUE,breaks="scott", main = "Histogram of SBP")
hist(triage_data$dbp,prob=TRUE,breaks="scott", main = "Histogram of DBP")

hist(triage_data$heartrate, triage_data$sbp)

qqnorm(triage_data$dbp, pch = 1, frame = FALSE)
qqline(triage_data$dbp, col = "steelblue", lwd = 2)

cor.test(triage_data$heartrate, triage_data$dbp)
cor.test(triage_data$heartrate, triage_data$sbp)
cor.test(triage_data$sbp, triage_data$dbp)

plot(triage_data$heartrate, triage_data$sbp)
abline(lm(triage_data$heartrate ~ triage_data$sbp), col = "red")

plot(triage_data$heartrate, triage_data$dbp)
abline(lm(triage_data$heartrate ~ triage_data$dbp), col = "red")

triage_sample = triage_data[seq(1,448972, by = 4),]
ggplot(data=triage_data, aes(x=pain, y=heartrate, colour=pain)) + geom_jitter()

counts = table(triage_sample$sbp, triage_sample$pain)
barplot(counts, main="Pain Distribution SBD",
        xlab="Pain Level", col=c("darkblue","red"),
        legend = rownames(counts), beside=TRUE)

str(triage_sample)

my.lm <- lm(triage_data$heartrate ~ triage_data$dbp + triage_data$sbp)
s3d <- scatterplot3d(triage_data$heartrate,triage_data$dbp, triage_data$sbp, angle = 55,pch = 16, highlight.3d = TRUE, type = "h", main = "scatterplot3d - 5")
s3d$plane3d(my.lm)
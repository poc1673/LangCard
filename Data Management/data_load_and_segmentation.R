# Script to take a small subsegment of the text corpus for testing.

library(pacman)
p_load(data.table,magrittr,stringr)
. <- "C:/Users/USER/Downloads/wikipediaTXT.txt"
a <- readLines(con = .,n = 10000)
short_inds <- sapply(X = a,FUN = function(x){ nchar(a) >= 2 })
b <- a[short_inds]
write.csv(b[!is.na(b)],file = "2019-11-24 Testing Data.csv")



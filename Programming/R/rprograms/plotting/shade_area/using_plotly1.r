#!/usr/bin/env Rscript

# Author  : Bhishan Poudel
# Date    : Apr 10, 2016
# Ref     :
# Program :

# set working directory
#this.dir <- dirname(parent.frame(2)$ofile)
#setwd(this.dir)

# libraries
library(plotly)

set.seed(1)
y <- sin(seq(1, 2*pi, length.out = 100))
x <- 1:100
plotdata <- data.frame(x=x, y=y, lower = (y+runif(100, -1, -0.5)), upper = (y+runif(100, 0.5, 1)))

ggplot(plotdata) + geom_line(aes(y=y, x=x, colour = "sin"))+
    geom_ribbon(aes(ymin=lower, ymax=upper, x=x, fill = "band"), alpha = 0.3)+
    scale_colour_manual("",values="blue")+
    scale_fill_manual("",values="grey12")

ggplotly()

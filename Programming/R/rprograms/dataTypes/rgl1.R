#!/usr/bin/Rscript

#Bhishan Poudel
# Jan 20, 2016

gwd <- "~/Copy/Programming/R/rprograms/dataTypes/"
setwd(gwd)
library(rgl)
df <- data.frame(x=runif(10,0,1),
                y=runif(10,0,1),
                z=runif(10,0,1),
                color=round(runif(10,1,3)))

plot3d(df$x, df$y, df$z, col=df$color, size=2, type='s')

rgl.snapshot("rgl1.png",fmt="png",top=TRUE)
#!/usr/bin/env Rscript

# Written by Myeong Lee (calculating the ethnic heterogeneity of urban areas in the U.S.)

library(ggplot2)
library(stringr)
library(readr)
library(dplyr)
library(data.table)
library(SnowballC)
library(reshape2)
library(DescTools)
library(diverse)
library(tidyr)

setwd("~/git/ASSIP-2022/data_csv/")

df <- read.csv("0722_game.csv")
df <- df[!duplicated(df$id),]

length(unique(df$id))
length(unique(df$snippet.title))
length(unique(df$snippet.channelId))

nrow(df[str_detect(string = tolower(df$snippet.title), pattern = "minecraft"),])

write.csv(df, "0722_game_unique.csv")

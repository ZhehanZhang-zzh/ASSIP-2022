#!/usr/bin/env Rscript

# Written by Myeong Lee 

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

# Game Data
df <- read.csv("0722_game.csv")
df <- df[!duplicated(df$id),]

length(unique(df$id))
length(unique(df$snippet.title))
length(unique(df$snippet.channelId))

nrow(df[str_detect(string = tolower(df$snippet.title), pattern = "minecraft"),])
write.csv(df, "0722_game_unique.csv")


channels <- df %>% group_by(snippet.channelId) %>% 
  summarise(num_videos = n())

ggplot(data=channels, aes(y=num_videos, x=snippet.channelId)) +
  geom_bar(stat="identity")
plot(channels, snippet.channelId~num_videos)


# Descriptive Statistics of Channels
df <- read.csv("072622_samples/game_channels.csv")
channel_ids <- as.data.frame(as.character(df$id))
write.csv(channel_ids, "channel_ids.csv", row.names = F)

playlist_ids <- as.data.frame(as.character(df$contentDetails.relatedPlaylists.uploads))
write.csv(playlist_ids, "game_playlist_ids.csv", row.names = F)

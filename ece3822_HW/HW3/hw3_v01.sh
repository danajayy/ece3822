#!/bin/sh
# Homework 3 mp3 music player shuffle

# get to Music directory
#
cd
cd Music


# generate counter so know when to reshuffle and repeat songs list
#
counter=$(ls -1 | wc -l)


# store mp3 paths in .list file
#
find -name "*.mp3" > songs.list

# will loop forever until shut down
#
while true
do

    #randomly shuffle playlist
    #
    sort -R songs.list > playlist.list

    for i in $(seq 1 $counter);
    do
	echo "$i" # debugging
	song=$(head -n1 playlist.list)
	sed '1d' playlist.list > playlist_1.list
	cp playlist_1.list playlist.list
	murp=$(head -n1 playlist.list)
	echo "$murp"
	echo "---------"
    done	
done

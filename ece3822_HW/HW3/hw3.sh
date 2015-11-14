#!/bin/sh
# Homework 3 mp3 music player shuffle

# get to Music directory
#
cd
cd Music

# store mp3 paths in .list file
#
find -name "*.mp3" > songs.list

# will loop forever until shut down
#
while true
do

    # check if playlist.list has already been made
    # to make sure the mp3 player starts where it left off
    #
    if [ -f "/home/djj/Music/playlist.list" ]
    then

	# get the number of songs in playlist.list
	#
        counter=$(more playlist.list | wc -l)
	
	# loop through the songs in playlist.list
	#
	for i in $(seq 1 $counter);
	do
	    # get song on top of list
	    #
	    song=$(head -n1 playlist.list)

	    # remove 1st line from playlist.list, save playlist_1.list
	    #
	    echo "$(sed '1d' playlist.list)" > playlist.list

	    # copy new list to playlist.list
	    # cp playlist_1.list playlist.list
	    
	    # play song
	    #
	    mpg123 "$song"

	    # a divider to organize the music being played
	    #
	    echo "---------"
	
	done # end for loop

	sort -R songs.list > playlist.list
	
    else
	
	# generate playlist.list
	#
	sort -R songs.list > playlist.list
	
    fi # end if statement
    
done # end while loop

# Bennett Medcalf Project 1 Checkpoint

## Heroku URL: https://blooming-shore-20385.herokuapp.com/

## Set Up For Local Use
1. The only files you will need are the ones in the `/project1` directory
2. Make sure you have the directories set up as in the project1 directory
3. This means: `/static/style.css`
4. and `/templates/index.html`
5. For python libraries, the only external one you should have to install is spotip, which can be done by running `pip install spotipy --upgrade` in your command line
6. You should be set!

## Two Known Problems and How I would Address Them
1. My first known problem is that if there is no preview URL for a song, the interface for the browser player still displays, but shows 0:00/0:00 for a song length. I tried to add a jinja2 `if` function in my HTML code to solve this, but I coouldn't get the exact syntax down, so I just kinda left it. With more time, I would go back and fix this issue to improve user experience.
2. A second problem is an index out of bounds error that is thrown every so often as well as Various Artists being displayed as the artist for a few tracks. I'm pretty sure I fixed this gy adding a -1 to `track = results['tracks'][chosen_song - 1]`, but I'm not completely sure. With more time I would more exhaustivley search my code and refresh the page to see if the errors are still present.

## Two Technical Issues and How I resolved Them
1. The first technicl issue I had was getting the verification for spotipy to work properly. For a while my code was throwing an error like "API KEY not present" or something similar. What I did tp fix this issue was read the spotipy docs, strangely enough. Going through the detailed processes there on how to get auth access set me straight. Ironically enough, going straight to Stack Overflow was what messed me up and almost made me start over, as none of the answers fixed anything.
2. The second set of issues I ran into was anything relating to getting the data from app.py into html via flask. My process was asking my friend Brandon for help and him walking me through a lot of the issues. Some of these included splitting up the code into functions and then calling the functions from the flask function, as well as initializing the variables that I wanted to transfer to index.html, like preview, song_name, artist, and so on. I'd just like to shout out Brandon and if you can give him like 5% extra credit for helping me so much that would be awesome.
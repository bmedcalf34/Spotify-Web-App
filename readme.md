# Bennett Medcalf Project 1 Checkpoint 2

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


# Bennett Medcalf Project 1 Milestone 2



## Set Up For Local Use
1. Only thing you may need to run locally is SQLAlchemy, flask-login. You should have spotipy and other libraries from the first milestone.
2. A note about how this app functions: when entering an invalid username, you will be redirected to the signup form. From there, enter your desired username and hit submit to be redirected back to login, where you can input your username to login.
3. Another note: the app DOES save favorite artists across sessions, what you have to do is hit the "Submit" button at the bottom of the "artists" page to refresh the page and display a song.

## Two Known Problems and How I would Address Them
1. My first known problem is that an incorrect login does not flash an error. Instead, it simply redirects to the sign up page for you to enter 
a new username. If I had more time, I would add a flash message saying that the password is incorrect and that the user is being
redirected to the sign up screen.
2. A second known problem is that my app accepts invalid Spotify URIs. If I had more time, I would add a conditional statement that checks the Spotify endpoint on whether it returns a top ten tracks for the given URI. If it returns "None" or "null", then it will flash a warning that the entered URI is incorrect and that it was not accepted into the database.

## Two Technical Issues and How I Resolved Them
1. The first technical issue I had was with an error along the lines of "id not found" at the Spotify API endpoint. The root of this error was an incorrect URI input that was not found when checking Spotify. My solution to this was actually quite silly, as the cause of the problem was me getting the URI from a playlist I created instead of from the artist. Making sure to go to the artist's Spotify page and get the correct URI wa the solution to this problem.
2. A second technical issue I ran into was when I input a new username into the database. because the username was new, there were no artist IDs associated with it in the database. The solution to this was also quite simple, but tricky at the same time. What I did to fix this issue was switch around my flask redirects in the different functions. This was mostly trial and error as well as tracing through my code and seeing what cases led to what redirects. The root cause of this error was that upon signup, the user was redirected to the "artists" page, which displays saved artists, instead of the "add_artists" function which adds artists to new users.

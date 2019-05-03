Fetch script vers 0.1

simple system for users to share scripts with each other.
when he sciprt is run it makes a menu with all of the available scripts.
when a script is downloaded it is tagged with a comment line saying it came from fetch and the time and date.  Therefore users can edit the scipts all they want without fear of confusing versions.

update the fetchdir variable to specify the directory that holds the scripts.  
Users should then make their subdirectories in there.

Each user should put files called MESSAGE.txt and HELP.txt in their directories, then just pop in the scipts.

The spiderexts variable defines extensions that are for spider files, which use a different comment character than #.

The sciprt saves statistics for who downloaded what.  Run it with a -s flag for "snodown" or "shuan" mode, which doesn't track usage.

TO DO: 

will eventually make a script that produces nice graphs of usage

Rather than having a specific loop to handle spider scripts having a wonky comment character, will update it to have a dictionary of code types and the appropriate comment character.

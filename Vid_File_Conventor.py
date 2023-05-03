import ffmpeg
#at the moment this will be statically typed wrther this could be automated with a csv or other finder file reader

for i in ():

vid_name = '/Volumes/Untitled/samples/Retro Chicago Acid House Ableton Course/Detroit Techno Lesson 1.wmv'
out_name = '/Users/nathancassells/Documents/ableton/Outfolder'
# Use ffmpeg to run commands, for example to convert a video file:
ffmpeg.input(vid_name).output(out_name).run()

#!Script to convert YouTube videos to mp3 format
#!Author: ImRohan01
from __future__ import unicode_literals
import youtube_dl
import os
from sys import argv
#--------------------------------------------------------------------------
#!The future module is used to add features available in future versions
# of python to the current version. The unicode literals is used to encode
# in unicode, rather than the default ASCII code.
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#!The library youtube_dl is used to download youtube videos in required
# quality and format. The argv is imported to pass a commandline parameter
# that accepts URL of youtube link and downloads from the link.
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#!DOWNLOAD CONFIGURATIONS
#!The below json tag contains the download parameters
#!The json tag is used as query for the curl required for youtube_dl
download_options = {
    'format' : 'bestaudio/best',
    'outtmpl' : '%(title)s.%(ext)s',
    'nocheckcertificate' : True,
    'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }]
}
#!The format tag contains a set of commands specified by youtube_dl
#!The bestaudio/best selects the best quality format
#!The outtmpl tag specifies the name of the file that we will save as in
# our system.
#!The nocheckcertificate tag allows you to do an insecure request, without
# checking the SSL certificate. This is inorder to prevent the SSL
# certificate errors that might occur.
#!The postprocessor tag contains a json element that contains details for
# specifiying the conversion formats using FFmpeg. There are set of codes
# in the documentation of the youtube_dl and FFmpeg to be used for this.
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#!SONGS DIRECTORY
#!Create a directory to save your songs or change directory if exists
if not os.path.exists('Music'):
    os.mkdir('Music')
else:
    os.chdir('Music')
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#!DOWNLOAD PROCESS
#!The 'with' statement is used for clean exception handling in python.
# Example: I don't have to do file.close() after I open a file, because
#          'with' does that inherently.
with youtube_dl.YoutubeDL(download_options) as dl:
     song_url = argv[1]
     dl.download([song_url])
#!YoutubeDL is a class in the youtube_dl package. We create an object to
# this class by passing as parameter the download configurations. We set
# argv[1] that holds the url to a variable and download the mp3 via the
# download function with the variable as the parameters
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------

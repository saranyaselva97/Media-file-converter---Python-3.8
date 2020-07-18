import sys
import os
from moviepy.editor import *
from pathlib import Path
import shutil
path = input("Enter Video Location : ")
outputpath = input("Enter Output Path : ")
print("select the Convertion Format")
print("****Type 1 for mp4*****")
print("****Type 2 for mp3*****")
option = input("Choose option : ")
if option == "2":
    outputfile=outputpath+"\mp3"
    if os.path.exists(outputfile):
        
        print("Your Converted File %s will be here : " % outputfile)

        mp4_file ="%s"%(path)
        mp3_file="%s/audio.mp3" % (outputfile)
        VideoClip=VideoFileClip(mp4_file)
        AudioClip= VideoClip.audio
        AudioClip.write_audiofile(mp3_file)
        AudioClip.close()
        VideoClip.close()
    else:    

            try:
                os.mkdir(outputfile)
            except OSError:
                print("Creattion of the directory %s failed" % outputfile)
            else:
                print("Successfully Created the directory %s" % outputfile)

                mp4_file ="%s"%(path)
                mp3_file="%s/audio.mp3" % (outputfile)
                VideoClip=VideoFileClip(mp4_file)
                AudioClip= VideoClip.audio
                AudioClip.write_audiofile(mp3_file)
                AudioClip.close()
                VideoClip.close()
     
            
     
elif option =="1":
        outputfile=outputpath+"\mp4"
        if os.path.exists(outputfile):
            source_file ="%s"%(path)
            filename = Path(source_file) 
            filename_replace = filename.with_suffix('.avi')
            print("File Converted : ")
            outtemp = "%s\\test.mp4" % (outputfile)
            shutil.move(filename_replace,outtemp)
            
        else:    
            try:
                os.mkdir(outputfile)
            except OSError:
                print("Creattion of the directory %s failed" % outputfile)
            else:
                print("Successfully Created the directory %s" % outputfile)
            source_file ="%s"%(path)
            filename = Path(source_file) 
            filename_replace = filename.with_suffix('.avi')
            print("File Converted : ")
            outtemp = "%s\\test.mp4" % (outputfile)
            shutil.move(filename_replace,outtemp)   




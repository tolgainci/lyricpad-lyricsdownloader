#################################
#                               #
# Author: Anoop S  & Tolga Inci #
#                               #
#################################


from bs4 import BeautifulSoup
from mutagen.mp3 import MP3
import requests
import glob

keywords={"lyricsfolder":"/Users/tolgainci/Lyrics/",
          "mp3folder":"/Users/tolgainci/Lyrics/mp3/*.mp3"
         }        
filenames = glob.glob(keywords['mp3folder'])
for i in range(0, len(filenames)):
    songname = filenames[i][filenames[i].find("mp3/")+4:filenames[i].find(".mp3")]
    audio = MP3(filenames[i])
    seconds = (audio.info.length)
    m, s = divmod(seconds, 60)
    songlength = "%02d:%02d" % (m, s)    
    slink="https://genius.com/"+songname+"-lyrics"
    if slink:
        r = requests.get(slink)
        page = r.text.encode('ascii','ignore')
        r.close()
        soup = BeautifulSoup(page, "html.parser")
        whole = soup.find("div", { "class" : "lyrics" })
        if whole == None:  
            print("Lyrics not found for "+songname)   
        else:
            wholetext = "@!title " + songname + "\n" + "@!duration " + songlength + "\n" + whole.text
            with open(keywords['lyricsfolder']+songname+'.txt','w+') as f:
                f.write(str(wholetext))
                print("Lyrics saved as "+songname+".txt")


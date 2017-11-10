# Lyrics Downloader for LyricPad

![](LyricsPad-LyricsDownloader.png)

This script is based on Anoop S's LyricsDownloader that you can find here: https://github.com/anoopajay91/LyricsDownloader It needs user input, works one file at a time, and uses azlyrics which doesn't work anymore. I modified the script to run in batch mode without user input and switched the lyrics website to genius.

This script downloads lyrics for your mp3 files from the genius website and saves them as txt files compatible with LyricPad. Your mp3 file names should be in the format band-name-song-name.mp3 with a dash in between each word. You can lookup the exact name from the genius website at https://genius.com/ to be sure. You can set your mp3 folder and lyrics folder paths in the keywords section. Be sure to leave the /*.mp3 part at the end of your mp3folder keyword.

When set correctly, the script reads the names of your mp3 files, finds the lyrics for them on the genius website and saves them in your lyrics folder as txt files. It also adds @!title and @!duration tags at the start of the file, taking the title and duration from the mp3 file. The duration tag is important for scrolling at the right time in LyricPad.

Dependencies:

1.Python3<br />
2.BeautifulSoup<br />
3.Requests<br />
4.Mutagen<br />
5. Glob

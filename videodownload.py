# python download video from instagram
# works with python 3+
from sys import argv
import urllib
from bs4 import BeautifulSoup
import datetime
import os

def ShowHelp():
    print ("python videodownload.py -u https://www.instagram.com/p/XXXXXX/")
    print ("python videodownload.py -f /user/myVideodownloadList.txt")


def Download_video(videoURL, savePath = ''):
    # og:video:secure_url
    try:
        # HTML Source Retrieve
        fhtml = urllib.request.urlopen(videoURL)
        htmlSource = fhtml.read()
        soup = BeautifulSoup(htmlSource, 'html.parser')
        metaTag = soup.find_all('meta', {'property': 'og:video:secure_url'})
        vidURL = metaTag[0]['content'] 

        print("Downloading video ...")
        videoFormat = os.path.splitext(vidURL)[1]
        f = urllib.request.FancyURLopener()
        fileName = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + videoFormat
        f.retrieve(vidURL, fileName)
        print("Done. Image saved to disk as " + fileName)
    except Exception as e:
        print (e)
        print ("Skipping Download")

if __name__ == '__main__':
    if len(argv) == 1:
        ShowHelp()

    if argv[1] in ('-h', '--help'):
        ShowHelp()
    
    elif argv[1] == '-u':
        instagramURL = argv[2]
        Download_video(instagramURL)

    elif argv[1] == '-f':
        filePath = argv[2]
        f = open(filePath)
        line = f.readline()
        while line:
            instagramURL = line.rstrip('\n')
            Download_video(instagramURL)
            
            line = f.readline()
        f.close()

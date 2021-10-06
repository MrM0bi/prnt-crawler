from bs4 import BeautifulSoup
from time import sleep
import random
import requests
import os

CHROMEDRIVER = os.getenv("CHROMEDRIVER")
OUTPUTDIR = "E:\\Downloads\\prnt\\"

b = [0, 3]
z = 0000
agents = ["Chrome"]

def loadAgents():
    try:
        with open("useragents.txt", "r") as f:
            for l in f.readlines():
                agents.append(str(l).replace("\n", ""))
    except:
        print("[WARN] ### The User-Agents could not be imported! Current working directory has to be \'prnt-crawler\' ###")
        sleep(10)
        pass

def download(id):
    rndagent = str(random.choice(agents))

    url = "https://prnt.sc/{}".format(id)
    headers = {'User-Agent': rndagent}

    html = requests.get(url, headers=headers).text

    if len(str(html)) > 500:
        imglink = None

        soup = BeautifulSoup(html, "html.parser")
        img = soup.find("img", {"class": "screenshot-image"})

        if img is not None:
            imglink = img["src"]

        # Check if screenshot is present
        if imglink is not None and imglink != "//st.prntscr.com/2021/04/08/1538/img/0_173a7b_211be8ff.png":
            try:
                print("["+id+"] -> "+str(imglink))

                fullpath = OUTPUTDIR + imglink[imglink.rindex("/")+1 : ]

                with open(fullpath, 'wb') as f:
                    f.write(requests.get(imglink).content)
            except:
                print("["+id+"] -> Exception")
                pass
        else:
            print("["+id+"] -> Screenshot removed")

    else:
        print("["+id+"] -> Not been able to get Image")


### START ########

loadAgents()

while True:
    if z < 9999:
        id = "{}{}{}".format(chr(b[0]+97), chr(b[1]+97), str(z).rjust(4, "0"))
        download(id)
        z += 1
    else:
        if b[1] < 25:
            b[1] += 1
            z = 0
        else:
            if b[0] < 25:
                b[0] += 1
                z = 0
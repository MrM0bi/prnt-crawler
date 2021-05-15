import requests
from selenium import webdriver
from bs4 import BeautifulSoup

CHROMEDRIVER = "F:\Programme\Chromedriver\chromedriver.exe"
OUTPUTDIR = "E:\\Downloads\\prnt\\"
b = [0, 0]
z = 0


o = webdriver.ChromeOptions()

o.add_argument("--headless")
o.add_argument("--silent")
o.add_argument('--log-level=3')
o.add_argument("--disable-gpu")
o.add_experimental_option('excludeSwitches', ['enable-logging'])
d = webdriver.Chrome(executable_path=CHROMEDRIVER, options=o)

def download(id):
    d.get("https://prnt.sc/"+id)
    html = d.page_source


    if len(str(html)) > 100:
        soup = BeautifulSoup(html, "html.parser")

        imglink = soup.find("img", {"class": "screenshot-image"})["src"]

        if imglink != "//st.prntscr.com/2021/04/08/1538/img/0_173a7b_211be8ff.png":
            try:
                print("["+id+"] -> "+str(imglink))

                fullpath = "{}{}".format(OUTPUTDIR, imglink[imglink.rindex("/")+1 : ])

                with open(fullpath, 'wb') as f:
                    f.write(requests.get(imglink).content)
            except:
                print("["+id+"] -> Exception")
                pass
        else:
            print("["+id+"] -> Screen removed")

    else:
        print("["+id+"] -> Not been able to get Image")


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

d.close()
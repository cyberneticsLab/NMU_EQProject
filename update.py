import urllib
from urllib.request import urlopen
import gitPython

def update():
    update = False

    versionSource = open('version.txt', 'r')
    versionContents = versionSource.read()

    updateSource = urlopen("https://github.com/cyberneticsLab/NMU_EQProject/blob/master/update.txt")
    updateContents = updateSource.read()

    print(updateContents)

    if versionContents != updateContents: print('Outdated')


update()
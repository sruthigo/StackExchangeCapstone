import requests
import os
#from pyunpack import Archive
from py7zr import unpack_7zarchive
import shutil

def downloadstackexchangefiles(configlist):
    """
    This function downloads the files from stackexchange archive web portal and saves in the local with same name and same format.

    Args:
    configlist - list of domainames, files related to each element will be download and saved

    Returns:
    Nothing
    """
    for domainname in configlist:
        try:
            downloadurl = 'https://archive.org/download/stackexchange/'+domainname+'.stackexchange.com.7z'
            outputpath = '/Users/SG/Documents/DE2020/DataDirrectory/'+domainname+'.meta.stackexchange.7z'
            r=requests.get(downloadurl)
            if r == False:
                print('Response not received. Check your input.')
                continue
            #r = requests.get('https://archive.org/download/stackexchange/coffee.meta.stackexchange.com.7z')
            with open(outputpath,'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print('Download finished for ',domainname)
        except Exception as e:
            print(e)
            return
    return
def unzip7zfile(configlist):
    """
    This function helps in unzipping/extracting the files from 7z files. 
    A folder is created for each fileset that is being unzipped.

    Args:
    configlist - list of domainames, files related to each element will be unzipped and saved within a child folder.

    Returns:
    Nothing
    """
    shutil.register_unpack_format('7zip', ['.7z'], unpack_7zarchive)
    for domainname in configlist:
        outputpath = '/Users/SG/Documents/DE2020/DataDirrectory/'+domainname+'.meta.stackexchange'
        inputpath = '/Users/SG/Documents/DE2020/DataDirrectory/'+domainname+'.meta.stackexchange.7z'
        os.mkdir(outputpath)
        shutil.unpack_archive(inputpath, outputpath)
        print('Extraction finished for ', domainname)
        #Archive(inputpath).extractall(outputpath)
    return
#main
#This config file can be updated with values based on the space availability. 
configlist = ['coffee','vegetarianism','conlang','health','bioinformatics']
downloadstackexchangefiles(configlist)
unzip7zfile(configlist)

"""
import threading
import requests

def download(link, filelocation):
    r = requests.get(link, stream=True)
    with open(filelocation, 'wb') as f:
        for chunk in r.iter_content(1024):
            if chunk:
                f.write(chunk)

def createNewDownloadThread(link, filelocation):
    download_thread = threading.Thread(target=download, args=(link,filelocation))
    download_thread.start()

for i in range(0,5):
    file = "C:\\test" + str(i) + ".png"
    print file
    createNewDownloadThread("http://stackoverflow.com/users/flair/2374517.png", file)

"""
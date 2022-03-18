import requests
import os
import subprocess
import sys

# install third-party libs
# the 'clint' library was created by the same author as the 'requests' library
try:
    subprocess.call("python -m pip install clint", shell=True)
    from clint.textui import progress
except:
    print("Error in installing and importing clint")
    sys.exit()

print("\nNote that the repository requires its visibility to be set to Public, else the requests library will not work\n")

# GET REMOTE URL
remoteURL = os.popen("git config --get remote.origin.url").read()
if remoteURL == "":
    print("This script is not located inside of a local repository. This script works without git, but it requires gh. Program ending now.")
    sys.exit()
remoteURL = remoteURL[:-1] 

# user choice: get DESTINATION directory from user. Blank by default
destination = ""

# destination confirmation
while destination == "":
    destination = input("\nEnter in destination folder (leave blank to safe to current directory).\n>>> ")
    if destination != "":
        if input("Destination folder: "+destination+"\nConfirm? [Y/N]: ").upper() == "Y":
            # what if user used slash instead of backslash? filter it
            destination = ''.join([x if x != "/" else "\\" for x in destination])

            try:
                subprocess.call("mkdir "+destination, shell=True)
            except:
                print("Error occured making directory, saving assets into current working directory: "+os.getcwd())
        else:
            destination = ""

# user choice: get tag from user, while listing existing tags
print("\n"+os.popen("gh release list").read())
tagName = input("Which release you want to download (enter in the tag, i.e. 'main'\n>>> ")

# TODO: add tagName check: if not in os.popen("gh release list").read()

# loop through each asset in stated release
##url = remoteURL+'/releases/download/'+tagName+'/jp.studiopixel.keroblaster_1.6.0.apk'
##print(repr(url))
##r = requests.get(url, allow_redirects=True, stream=True)
##try:
####    open(destination+'\jp.studiopixel.keroblaster_1.6.0.apk', 'wb').write(r.content)
##    with open(destination+'\jp.studiopixel.keroblaster_1.6.0.apk', 'wb') as f:
##        total_length = int(r.headers.get('content-length'))
##        for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
##            if chunk:
##                f.write(chunk)
##                f.flush()
##except:
##    print("Error occured when saving file.")
##

release_details = os.popen("gh release view "+tagName).read().split('\n')
for i in release_details:
    if "asset" in i:
        print("\nDownloading: "+i[7:])
        url = remoteURL+'/releases/download/'+tagName+'/'+i[7:]
        r = requests.get(url, allow_redirects=True)
        try:
##            open(destination+'\\'+i[7:], 'wb').write(r.content)
            with open(destination+'\\'+i[7:], 'wb') as f:
                total_length = int(r.headers.get('content-length'))
                for chunk in progress.bar(r.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
                    if chunk:
                        f.write(chunk)
                        f.flush()
        except:
            print("Error occured when saving file.")

        

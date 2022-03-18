# os to read, subprocess to use cmd without opening a seperate console window
import os
import subprocess
import sys

# win10toast is optional.
try:
    from win10toast import ToastNotifier
except:
    subprocess.call('python -m pip install win10toast', shell=True)
    from win10toast import ToastNotifier


print(
    'GitHub Release Asset Uploader  \n'
    '- built and run on Python 3.9.4\n'
    '- requires gh auth to run first\n'
    'before running this script.    \n'
    '- assets are required to be in \n'
    'the following location:        \n'
    '    - releases/<tag>/<assets>  \n'
)


# list existing releases with gh
print("Current Releases listed below\n"+os.popen("gh release list").read())

# get tag from user
tagName = input("Enter tag name: ")

# use cmd to view existing files
existing = os.popen("gh release view "+tagName).read()

# check if user is logged in to gh, or if tag doesn't exist. either way, the program will stop
if not(tagName in existing):
    print(existing)
    sys.exit()

# get the files in a specified folder (configurable). if assets are in the same dir, use os.getcwd()
files = [f for f in os.listdir('releases/'+tagName) if os.path.isfile(os.path.join('releases/'+tagName, f))]

# output and upload. uses existing string to see if file exists
for f in files:
    #print("Checking if "+f+" exists... ", end="")
    if f in existing:
        print("EXISTING  : "+f)
        continue
    else:
        print("UPLOADING : "+f)
        subprocess.call('gh release upload '+tagName+' releases/'+tagName+'/'+f, shell=True)

# most of the time i would be doing other stuff, so I like to use this library to notify me
toaster = ToastNotifier()
toaster.show_toast("Finished uploading","Check scripts and files")

# subprocess for running ffmpeg commands
# os for getting files lists and names
# mimetypes for getting formats functional with FFMPEG
import subprocess
import os
import mimetypes
# mimetypes.init() is important as it (bluntly) increases the format list
mimetypes.init()

# win10toast is optional
try:
    from win10toast import ToastNotifier
except:
    subprocess.call('python -m pip install win10toast', shell=True)
    from win10toast import ToastNotifier

# message
print('-----FFMPEG Converter-----\n'
      'best optimally use in a   \n'
      'folder with target files. \n'
      'FFMPEG is used in handling\n'
      'multimedia files.         \n'
      'Prerequisites:            \n'
      '- ffmpeg to be installed  \n'
      '- script must be in cwd   \n'
)

# input and expected output extensions
ext_in = "."+input("Enter input extension  : ")
ext_out= "."+input("Enter output extension : ")

# get extensions that is compatible(?) with your machine
def get_mimetype(general_type):
    for ext in mimetypes.types_map:
        if mimetypes.types_map[ext].split('/')[0] == general_type:
            yield ext
extVIDEO = tuple(get_mimetype('video'))
extAUDIO = tuple(get_mimetype('audio'))
extIMAGE = tuple(get_mimetype('image'))

# get all existing files in current working directory
files = [f for f in os.listdir(os.getcwd()) if os.path.isfile(os.path.join(os.getcwd(), f))]

# IF VIDEO allow user to set video density
density = input("Set density (<n>M): ") if ext_out in MIME.extVIDEO else "NOTVIDEO"
density = density if density.isnumeric() else "1"

# other files options will be available soon

# actual processing
for f in files:
    
    # exclude this file and files that does not end with ext_in
    if f != os.path.basename(__file__) and f.endswith(ext_in):
        print("Converting "+f+" to "+f[:-4]+ext_out)
        if ext_out in extVIDEO: # IF VIDEO
            subprocess.call("ffmpeg -i "+f+" -c:v libvpx -b:v "+density+"M -c:a libvorbis "+f[:-4]+ext_out, shell=True)

# end and call the Toast
toaster = ToastNotifier()
toaster.show_toast("Finished converting","Check scripts and files")

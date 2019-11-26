import os
import errno

if os.path.isfile('./rdr2dir.txt'):
    f = open("rdr2dir.txt", "r")
    rdr_dir = f.readlines()[0]
    if len(rdr_dir.strip()) == 0:
        rdr_dir = os.path.expanduser('~') + "\Documents\Rockstar Games\Red Dead Redemption 2\Profiles"
else:
    rdr_dir = os.path.expanduser('~') + "\Documents\Rockstar Games\Red Dead Redemption 2\Profiles"

if os.path.isfile('./photodir.txt'):
    f = open("photodir.txt", "r")
    photo_dir = f.readlines()[0]
    if len(photo_dir.strip()) == 0:
        photo_dir = "Images\\"
else:
    photo_dir = "Images\\"

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

def convert(name, path):
    with open(path + "/" + name, 'rb') as in_file:
        with open(photo_dir +name + '.jpg', 'wb') as out_file:
            out_file.write(in_file.read()[300:])

mkdir_p(photo_dir)

for folderName in os.listdir(rdr_dir):
        folder = rdr_dir + "\\" + folderName
        for filename in os.listdir(folder):
                if(filename.startswith( 'PRDR' )):
                        convert(filename, folder)

import io
import os
import sys
import urllib2 as urllib

from PIL import Image

url_source = None
file_source = None
image = None

for arg in sys.argv:
    if str(arg).startswith('--url='):
        url_source = str(arg)[6:]
    elif str(arg).startswith('--file='):
        file_source = str(arg)[7:]

if url_source and file_source:
    print 'Only one source may be provided. Please choose either to use a URL or file.'
    sys.exit()
elif not url_source and not file_source:
    print 'You must specify an image source to use this script with either --url or --file'

if url_source:
    try:
        fd = urllib.urlopen(url_source)
        image_bytes = io.BytesIO(fd.read())
        image = Image.open(image_bytes)
    except IOError:
        print 'Image could not be read from URL. Please be sure you have a valid URL pointing to an image.'

if file_source:
    try:
        image = Image.open(file_source)
    except IOError:
        print 'Image could not be read from file. Please be sure you have a valid path pointing to a file.'

try:
    res = 'res/'
    if not os.path.exists('res/'):
        os.makedirs('res/')

    sizes = {
                48: 'mipmap-mdpi/',
                72: 'mipmap-hdpi/',
                96: 'mipmap-xhdpi/',
                144: 'mipmap-xxhdpi/',
                192: 'mipmap-xxxhdpi/'
            }

    for pixels, path in sizes.iteritems():
        basewidth = pixels
        wpercent = (basewidth / float(image.size[0]))
        hpath = int((float(image.size[1]) * float(wpercent)))
        new_img = image.resize((basewidth, hpath), Image.ANTIALIAS)
        if not os.path.exists(res + path):
            os.makedirs(res + path)
        new_img.save(res + path + 'ic_launcher.png')

except IOError:
    print 'Images could not all be generated. Please check the image source and destination permissions.'
    sys.exit()

print 'Images successfully generated! Check in the res directory.'

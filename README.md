# AndroidLauncherResizer
Quickly resize an image from either a URL or file to Android compatible mipmap drawable launcher icons for various screen densities

### Usage
```
source venv/bin/activate
pip install -r requirements.txt
```

Then to use the script, you can either grab an image from a URL:
```
python script.py --url=<url here>
```
where `<url here>` is the direct image URL

or

```
python script.py --file=<file here>
```
where `<file here>` is the relative path from the script to the desired source image.


Thats it! The images should then be generated under the `res/` folder.

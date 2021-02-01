Title: Lost Data

Category: Steganography

Rank: Epic

Question: While I was developing image-sharing software, I made a mistake. Now my png file is seriously damaged.

Hint: "All files have patterns"

File: WeirdFile

This file seemed really weird as the file does not have any extension and when you open it in a text editor I only see gibberish. So I installed a tool called "exiftool" that would help me identify this file.

```
sudo apt-get install -y exiftool
```

Then I used a exif command: `exiftool WeirdFile`. I was not able to find anything, after using that command, so I looked at the hint. The hint said all files have pattern, and looking closer to the question I see that the question was talking about "png" file.

Knowing that I searched up "png file signature/pattern". After searching it up I found a wiki page that [listed all the file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures). From that website I found out that png files have file signature of:

```
89 50 4E 47 0D 0A 1A 0A
```

To view the hex value of png signature to utilize this command:

```
xxd WeirdFile  | less
```

After comparing the correct file signature and the file signature of the WeirdFile, I know that you are supposed to change the file signature in the WeirdFile. 

Then, I change the file extension to .png.

I was able to use this cmd to change the file signature:
```
printf '\x89\x50\x4E\x47\x0D\x0A\x1A\x0A' | dd of=WeirdFile.png bs=1 seek=0 count=8 conv=notrunc
```

Answer: flag{png_fil3s_have_pattern}
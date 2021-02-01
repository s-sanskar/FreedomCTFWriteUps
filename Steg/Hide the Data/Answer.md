Title: Hide the Data

Category: Steganography

Rank: Rare

Question: There is a message hidden within this image, try to find it.

Hint: Look up some common steg tools

File: FreedomHS1steg.jpg

The hint says look at some common steg tools.
After searching up "common steg tools" I found
a [website that listed tools for Steganography.](https://0xrick.github.io/lists/stego/)

The first tools in the list was StegHide, and the description said that there is a
"message hidden withing this image" so I try to use [StegHide.](https://github.com/StefanoDeVuono/steghide)

To Download steghide in linux:

```
sudo apt-get install steghide
```

After downloading it, I try use

```
steghide --help
```

to find out how this tool works

Now it's time to extract the hidden message. To extract the message I use

```
 steghide --extract -sf FreedomHS1steg.jpg
```
Extracted filename: steg1.txt

When extracting the file there was a message that said
 `Enter Enter passphrase:` 
I tried entring no password to see if it works and it worked.

Note: You could use 
```
 steghide info nameofthefile
```
to see if there is any embedded data.

Answer: flag{data_1ns1de_1mag3}

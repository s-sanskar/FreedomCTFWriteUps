Title: Reveal

Category: Steganography

Rank: Legendary

Question: Uncover the mysteries hidden in this file and unveil the truth.

Hint: You might need to use a password cracker

File: Hidden.txt

First of all, the file that is given in the question just containes base64. From my knowlege, I could deduce that the base64 is probably a file that has been converted to base64. Therefore, I searched up base64 to file and found a [website that could do it](https://base64.guru/converter/decode/file).

I was able to get a image from there. In the image there was a qr code, I tried scanning that and it lead me back to the freedomctf.org website. The image seemed weird so I downloded it, I made sure to not screenshot the image, as the flag might get lost. 

In the file I saw that exiftool was used, however I did'nt get any flag using that :(

Just to be sure I tried using steghide, and I was sucessfully able to get a file.
```
steghide info image.jpg
```
Yup, I was able to get a file called "ghost.png"

I used exiftool before check what was in the file and I found out that the file was supposed to a text file, so I changed the extension.

``` 
exiftool ghost.png
```

Because I was too lazy to open a file, I printed out the file from the terminal
```
    cat ghost.png
```

There was no flag in the file, howeever I found some weird texts/symbol there, so I opened it from a GUI text editor, but I didn't see those weird symbol. So, I thought that symbol might give me some flag. After searching for hours I finally found something called "stegcloak". It really catched my eyes because the image from before showed a "cloak". 

I installed the stegcloak tool:
``` 
npm install -g stegcloak
```
Note: You might need to have node, installed

After installing stegcloak, I used `stegcloak -h` to see how the package works.

``` 
stegcloak reveal
? Enter message to decrypt: All ⁣‍‌‌⁡⁢‍⁡‍⁢‍⁢‌⁤‍‌‌⁡‍⁡⁡‌‌⁡‌‌⁢⁡‌⁡‍⁡‌⁢‌‍⁤⁣‍‌⁡⁤‍⁢⁡‌‌⁡⁡⁡⁢‍⁤⁢‍⁡‍⁢⁣‌‌‌‌‍⁢⁡‌⁢⁡⁤‍⁢‍⁢⁡⁢‌⁤‍⁢⁡⁣⁡⁢⁡⁢⁡⁣⁡⁢‌⁤‌⁤‍⁢⁡‌⁢⁡⁡⁢⁣⁡‌⁡‌‍‌‍⁤⁤⁢‌‌‍‌⁣⁢‌⁤‌⁡‌⁢‌
⁡⁢⁡‌‌‌⁢⁣‌⁣⁢⁡⁡‌⁣‌⁡‌⁣the Stenography challenges are making me lose hope. - Quentin from Web Warm-Up
```

After using this, I found out that password was required. The hint said that I might need to use a password cracker, so I created a bash script that would loop though a [password wordlist](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) until it I got the answer. After couple of minutes, I was able to get the flag.

Answer: flag{IHopeNoOneGetsThisAlsoGhost}

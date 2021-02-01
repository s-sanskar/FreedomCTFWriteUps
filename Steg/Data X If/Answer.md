Title: Data X If

Category: Steganography

Rank: Epic

Question: Phalerovia was sending this picture in a secret conversation, we got a hold of it. Can you find the hidden secret?

Hint: Combine your knowledge from previous challenges

File: colorCat.jpg

The image file did not seem suspicious, other that the really obvious use of microsoft paint. First of all, I read the hint. The hint said "Combine your knowledge from previous challenges". Form that last challenge I learned that I should read my question (*so let me just quickly read it*). I noticed that the file is a .jpg file. From previous challenges I found out that the tool steghide only takes in .jpg file, therefore I try using steghide. 

```
 steghide info colorCat.jpg
```

This asked for the password, however this time empty password did not work, however I was able to confim that this image used steghide. After trying lots of stuff to find the password, I used a tool called `exiftool` to see if there is any relevent information.

```
exiftool colorCat.jpg
```
After using exiftool I saw a line that said:
```
XP Comment = 50617373776f72643a614756355132463051323973623349784d6a4d304e51
```
The comment seemed like a hex so I used online hex decoder to decode it. After decoding it, I got 
Password:aGV5Q2F0Q29sb3IxMjM0NQ

I tried using the password in the steghide password field
```
steghide --extract -sf colorCat.jpg
```

Using this I was able to extract a file with the flag

Answer: flag{staring_st3g_cat}
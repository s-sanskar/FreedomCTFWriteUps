**Title:** :0 :0 XM :L

**Hint:** Sometimes you must check things manually :(

**Category:** Forensic/Steg

**Question:**

Find the secret hidden within this file.


**How to solve this:**
### OPTION ONE
1. OOXML Viewer extension in VSCODE lets you view the files in .docx

### OPTION TWO
1. You could also just unzip the .docx file
``` 
 unzip FreedomCTF.docx
```

> All office files are made up diffrent files. Unzipping the file lists out diffrent files. After unziping or using OOXML go to the styles.xml file inside of /word directory

There you will find:
`<\!--F1@g: u1qq3a_grkg_1244 (r13)-->`

Looking at the text you can see that the flag is encoded. Due to r13 in the bracket you could speculate that the cipher is rot13. (rot13 to text)

**Answer:**
flag{h1dd3n_text_1244}



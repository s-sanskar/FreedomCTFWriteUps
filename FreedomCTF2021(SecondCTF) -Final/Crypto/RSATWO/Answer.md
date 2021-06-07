**Title:** RSA-TWO

**Hint:** None

**Category:** Crypto

**Question:**
```
e: 23
n: 194247505596496023881578032915335008633
ct: 65205298022099085283449917096537195340, 152080695252271793478056704090860133614
```

**How to solve:**
1. To solve this question you will first have to find p and q
    - Go to [factorDB](http://factordb.com/) and find p & q.
```
q: 14978383016497116121
p: 12968523063040435873
```

2. Use the python [decode script](./decode.py) to get the plain text.
Pt: 102108097103123114115097095116114111,117098108101095100121120049120125

3. convert the [decimal to ascii](https://onlineasciitools.com/convert-decimal-to-ascii)

**Answer:**
 
flag{rsa_trouble_dyx1x}
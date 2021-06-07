**Title:** T-REX?

**Hint:** OR REGEX?

**Question:**

Find a password that starts with "A".
The third character must be "t".
The password must end with "o".
The third last character must be a number between 0 to 9.

**How to solve it:**

```
grep '^A.t.*[0-9].o$' 33333pass.txt
```

**Answer:**

flag{Aetowoo4ohm7ET0Wee2pheew2Ep4oo}

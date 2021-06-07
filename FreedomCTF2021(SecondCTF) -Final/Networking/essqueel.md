**Title:** ess-que-el Running?

**Category:** Networking

**Rank:** Common

**Question:** 

Where is the ess-que-el Running? Note: flag{port}

**How TO find the answer:**
```
nmap -Pn -sV -p- --script=banner 18.189.22.84
```

```
5702/tcp  open   mysql          MySQL
```

**Answer:**

flag{5702}

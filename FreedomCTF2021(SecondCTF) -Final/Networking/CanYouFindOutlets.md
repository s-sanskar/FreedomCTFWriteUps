**Title:** Can you find outlets?

**Category:** Networking

**Rank:** Common

**Hint:** Map It

**Link:** http://networking.freedomctf.org/

**Question:** How many Outlets are unfiltered on this server?

**How to solve it:**
```
nmap -Pn -p- networking.freedomctf.org
```
```
PORT      STATE  SERVICE

21/tcp    open   ftp
22/tcp    open   ssh
80/tcp    open   http
5702/tcp  open   unknown
30000/tcp closed ndmps
30001/tcp closed pago-services1
30002/tcp closed pago-services2
30003/tcp closed amicon-fpsu-ra
30004/tcp closed amicon-fpsu-s
30005/tcp closed unknown
30006/tcp closed unknown
30007/tcp closed unknown
30008/tcp closed unknown
30009/tcp closed unknown
```

**Answer:** 

flag{14}

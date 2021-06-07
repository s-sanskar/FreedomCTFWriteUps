**Title:** SecQ

**Category:** SE

**Hint 1:** net...k
**Hint 2:** The website is a subdomain of freedom CTF. Look at the common link pattern in Web Exploitation challenges.

**Description:**

*(FINAL CHAINED MISSION: SE1005)*

Through some luck, we found out that the "person" has a website where he records events in his life. Find the website and get the flag.

**How to solve it:**
1. Look around the [website](https://spenevankshyanak.freedomctf.org/**login). In there you will see a place to login.

2. As we don't have the login information of Spenevank, we will go to `Forgot Password Or Username` ([link](https://spenevankshyanak.freedomctf.org/**login)). 

3. If you look at the security question, you will find that you will be able to answer these question

4. Answer for the questions:
    * `Name: Spenevank Shyanak` (You can find this in the website)
    * `Maiden Name: Abernathy` (You can find this in facebook)
    * `Birth City: Alexandria` (You can find this in facebook)
    * `First Pet: Huckleberry` (You can find this in pintrest)
    * `Fav Book: The Dance of the Lost` (You can find this in facebook)

5. After you sumbit the answers you will have to open developer tool and go to `newtwork` tab. After you reach there hit confirm and look at the response you get.

**Answer:**

flag{Fxhtkvdadv_detgc-3456975}

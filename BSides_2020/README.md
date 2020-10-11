# Log
## Description

GET the right file.

Author: Ph03N1X

[Link](http://3.7.251.179/) 

## Solution
#### Recon
First, we opened the website, there we given lots of links. But when we clicked on most of the link, we were greeted with an error page. After some observation, we realized that there is a link that's different with another link.

![](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/BSides_2020/img/Log_1.png) 

Clicking on that link would redirect us to a different page :

![](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/BSides_2020/img/Log_2.png).

We also learned some things in this phase :
- There are some files that we can't get (.htaccess would return 403 Forbidden)
- The server was run in Apache (we know it from error message that was triggered when we requested a non-existent file )

#### LFI
After that, we spent some times figuring what to do next. With the hint in the title (_**Log**_) and the info that the server run in Apache, we assumed that we have to read the log file. So... LFI perhaps?

We tried the word 'file' as parameter to include file, and it works!

 ![](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/BSides_2020/img/Log_3.png) 
 
#### Journey to RCE

Okay, so far we can do LFI, but no sign of flag here... So we assumed that we have to escalate our LFI to RCE. Doing a data:// wrapper wasn't working because of _allow_url_include_ config was set to 0. 

Finally, we tried a RCE by using Apache log file. There are two types of Apache log file : **access.log** (For logging successful requests) and **error.log** (For logging failed requests). But, when we include access.log, we were failed because the file isn't exist. So, we tried to include error.log and it worked. 

![](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/BSides_2020/img/Log_4.png) 

#### Triggering error.log

So next we have to trigger error.log to log our failed request. We can do it by requesting .htaccess. But how to log our crafted request?

Turns out, it was possible to request .htaccess[ABRITRARY_STRING] to trigger the logging. So we successfully logged our crafted request. 

Here's a script that automated our request.

	import requests
	link = "http://3.7.251.179/"
	
	log = 'http://3.7.251.179/click-here_00.php?file=/var/log/apache2/error.log'
	def gs(pl):
		return link + '.htaccess' + pl
	
	payload = '<%3Fphp echo "PAYLOAD HERE" %3F>'
	r = requests.get(gs(payload))
	r2 = requests.get(log)
	print(r2.text)

#### Filter Bypassing

Yay! We can do LFI to error.log, so we can do a RCE...

...right?

It's not that easy. The system seems to blocked some strings so we can't do a RCE easily.

First, obviously we tried to executed some script to execute `shell_exec`. So we tried executing `<%3Fphp echo shell_exec("id") %3F>` as our payload with the script. And the result?

> [authz_core:error] [pid 84] [client 114.4.219.126:54871] AH01630: client denied by server configuration: /var/www/html/.htaccess<?php echo shell_exec("id"); ?>

Oops! Seems that we can't do `shell_exec` here.

Let's try another approach. How if we do a path traversal to find the flag with scandir() function?  We tried `<%3Fphp var_dump(scandir("/")); %3F>` but it doesn't work. So we bypassed the "/" filter by using chr(47) and it worked.

Long story short, after some path traversals, we found an interesting file in `/f/l/a/g/somethingUneed.txt`. And including it in our LFI will return our flag.

![](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/BSides_2020/img/Log_5.png) 

**Flag** :  `BSDCTF{L0cal_f1L3_InClu$10N_1$_v3RY_P015On0u$} `

**Disclaimer** : Some of the exploit in this writeup doesn't work in the writeup making phase.


# Robot Master
## Description

You know what to do, collect them all.

Author: Ph03N1X

[Link](http://15.206.202.26/) 

## Solution
#### Recon
As the title, the first thing we saw is the `robots.txt` file. We found an interesting file in /cookie.php
![](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/BSides_2020/img/Robot_1.png) 

Opening `cookie.php` revealing us some interesting cookies.

![](https://raw.githubusercontent.com/kerupuksambel/ctf-writeup/master/BSides_2020/img/Robot_2.png) 

#### Cookie Unifying
Trying to google the value of `Our_Favourite_Cookie` tells us that the value is actually a SHA256 hash of 'O'. Then, when we change the value of `Piece`, we got a different hash. Realizing that this maybe is a SHA256 of an individual letter of a flag, we tried to automate the process. Here's the script we craft to request every hash piece of the flag.

	import requests
	import hashlib
	import string
	
	link = 'http://15.206.202.26/cookie.php'
	
	poss = string.printable
	table = {}
	
	flag = ""
	
	for _ in poss:
		sha = hashlib.sha256(_.encode()).hexdigest()
		table[_] = sha
	
	for i in range(50):
		cookie = {
			"Piece" : str(i),
			"Our_Fav_Cookie" : "rinrin!"
		}
		r = requests.get(link, cookies=cookie)
	
		d = (dict(r.cookies))
		for t in table:
			if table[t] == d["Our_Fav_Cookie"]:
				flag += t
	
		print(flag)

After running the script, we realized there's a flag-like string on the result, 
> OFQPGS{P00x135_ne3_o35g_cy4p3_70_pu3px}

Shifting the string with Caesar cipher with N = 13 giving us our flag.

**Flag** : `BSDCTF{C00k135_ar3_b35t_pl4c3_70_ch3ck}`

## Username Enumeration using Response Time — PortSwigger Web Security Academy

## Tools used:Burp Suite-Intruder

## The Vulnerability
Username enumeration is when an attacker is able to observe changes in the website's behavior in order to identify whether a given username is valid.Here,it is the responses to different input

## How I Found It
When i tried brute-forcing with multiple usernames to check whether the responses are different.It didn't work out,as they blocked the brute forcing through some means of ip-verififcation.I tried whether the request supports `X-Fork Header` and tried changing its id through the header.It worked!!

## The Exploit
The best practice from the beginning itself is to find the username.To do so,we will try all the username list and understand is there a change in response lengths.Here,since the statement `Invalid username or password.`Since `IP-address`is a major concern for the brute forcing.We use the `Pitchfork` method of adding multiple payloads for the `header` and `username` .Since ,there is no response change from different usernames,We would need to find some other alternative.Here,we could measure some response delays.By guessing the username with highest delay would have gone through some authentication delays,we now brute force it with the password-list.

## What I Learned
Never trust the users with client side validation.

## How to Defend Against It
The application should only process X-Forwarded-For headers if the request comes directly from a known, trusted internal IP address.If the request comes from anywhere else, the application should ignore the header and use the actual network-level (TCP) connection IP.
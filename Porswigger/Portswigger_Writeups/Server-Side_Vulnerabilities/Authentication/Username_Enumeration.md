## Username Enumeration = — PortSwigger Web Security Academy

## Tools used:Burp Suite

## The Vulnerability
Username Enumeration using different usernames.If website signals the user differently based on the credentials,
the attacker can understand the patterns to exploit the vulnerability.

## How I Found It
I tried brute forcing the usernames and passwords using Burp Intruder and found the exploit by monitoring the response length.

## The Exploit
The username gave a response signalling the password was invaliid,which means the username was valid.This means
we have the valid username given and now we have to brute force the passwords with this username.

## What I Learned
Never let users guess the valid usernames by signalling different responses with different usernames
And also learned the basics of Burp Suite Intruder.

## How to Defend Against It
Resonses must be same for invalid credentials.
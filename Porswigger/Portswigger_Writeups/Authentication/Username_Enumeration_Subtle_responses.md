## Username Enumeration = — PortSwigger Web Security Academy

## Tools used:Burp Suite-Intruder

## The Vulnerability
Username enumeration is when an attacker is able to observe changes in the website's behavior in order to identify whether a given username is valid.Here,it is the responses to different input

## How I Found It
Since,what we want to know is the response change with different credentials.   Looks like some developers might even miss a small `.`.

## The Exploit
The best practice from the beginning itself is to find the username.To do so,we will try all the username list and understand is there a change in response lengths.Here,since the statement `Invalid username or password.` is present across different response lengths,its not practical to tail it.So,we need to find is there a response change apart from the actual statement.Here for the username `arlington` has a response of `Invalid username or password` which clearly states the developers probably missed the `.` for valid usernames.Hence,brute-forcing this username with passwords should give the password.

## What I Learned
Never let users guess the valid usernames by signalling different responses with different usernames
And also learned the basics of Burp Suite Intruder as using payloads and grep extract.

## How to Defend Against It
Responses must be same for invalid credentials.
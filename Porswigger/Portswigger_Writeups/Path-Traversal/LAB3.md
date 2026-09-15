# File path traversal, traversal sequences stripped non-recursively — PortSwigger Web Security Academy

## Tools used:Burp Suite

## The Vulnerability
This is called the path traversal vulnerability,where you can change the url's by manipulating the get request in burp suite

## How I Found It
Go to HTTP History after visiting the website,there you might see GET /image?filename=22.jpg HTTP/2 or something similar

## The Exploit
Here,the developers made it a bit challenging trying to strip away any parameters `../`.So inorder to bypass any traversal,we could add an extra traversal sequence ultimately turning the sequence into `....//`.Change the `filename=....//....//....//etc/passwd` replacing the imagename.This will change the directory to the root and enter etc/passwd effectively.This gives us the access to the passwords or password hashes.

## What I Learned
If the similar requests are not shown in the HTTP history,you might need to turn off the filter and recheck them,I missed the request and was confused for a while.

## How to Defend Against It
Actively reject any input containing directory traversal sequences, such as `../`, `..\\`, or complex variations of URL-encoded bypasses.
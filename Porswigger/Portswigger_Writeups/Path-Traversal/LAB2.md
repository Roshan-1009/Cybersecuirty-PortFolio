# File path traversal, traversal sequences blocked with absolute path bypass — PortSwigger Web Security Academy

Tools used:Burp Suite

## The Vulnerability
This is called the path traversal vulnerability,where you can change the url's by manipulating the get request in burp suite

## How I Found It
Go to HTTP History after visiting the website,there you might see GET /image?filename=22.jpg HTTP/2 or something similar

## The Exploit
Change the `filename=/etc/passwd` replacing the imagename.This will change the directory to the root and enter etc/passwd effectively.This gives us the acces to the passwords or password hashes.

## What I Learned
If the similar requests are not shown in the HTTP history,you might need to turn off the filter and recheck them,I missed the request and was confused for a while.

## How to Defend Against It
Actively reject any input containing directory traversal sequences, such as `../`, `..\\`, or complex variations of URL-encoded bypasses.
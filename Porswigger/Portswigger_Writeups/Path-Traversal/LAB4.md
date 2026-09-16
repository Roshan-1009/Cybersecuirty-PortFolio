# File path traversal, traversal sequences stripped non-recursively — PortSwigger Web Security Academy

## Tools used:Burp Suite

## The Vulnerability
This is called the path traversal vulnerability,where you can change the url's by manipulating the get request in burp suite

## How I Found It
Go to HTTP History after visiting the website,there you might see GET /image?filename=22.jpg HTTP/2 or something similar

## The Exploit
Web servers may strip any directory traversal sequences before passing your input to the application. You can sometimes bypass this kind of sanitization by URL encoding, or even double URL encoding, the ../ characters. This results in %2e%2e%2f and %252e%252e%252f respectively. Various non-standard encodings, such as ..%c0%af or ..%ef%bc%8f, may also work..So inorder to bypass any traversal,we could add traversal sequence ultimately turning the sequence into `....//....//....//etc/passwd` by changing the `filename=%252e%252e%252fetc/passwd` replacing the imagename.This will change the directory to the root and enter etc/passwd effectively.This gives us the access to the passwords or password hashes.

## What I Learned
Path Traversal Vulnerabiltites can be bypassed in most cases.

## How to Defend Against It
Actively reject any input containing directory traversal sequences, such as `../`, `..\\`, or complex variations of URL-encoded bypasses.
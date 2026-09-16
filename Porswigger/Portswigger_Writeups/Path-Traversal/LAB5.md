# File path traversal, traversal sequences stripped non-recursively — PortSwigger Web Security Academy

## Tools used:Burp Suite

## The Vulnerability
An application may require the user-supplied filename to start with the expected base folder.In this case, it might be possible to include the required base folder followed by suitable traversal sequences.

## How I Found It
Go to HTTP History after visiting the website,there you might see GET /image?filename=22.jpg HTTP/2 or something similar

## The Exploit
So inorder to bypass some traversal restrictions,we could add the base folder into traversal sequence ultimately turning the sequence into `/var/www/images/../../../etc/passwd`.This will change the directory to the root and enter etc/passwd effectively.This gives us the access to the passwords or password hashes.

## What I Learned
Path Traversal Vulnerabiltites can be bypassed in most cases.

## How to Defend Against It
Actively reject any input containing directory traversal sequences, such as `../`, `..\\`, or complex variations of URL-encoded bypasses.
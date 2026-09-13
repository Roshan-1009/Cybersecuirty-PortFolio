## File Upload Vulnerabilites = — PortSwigger Web Security Academy

## Tools used:Burp Suite-Repeater

## The Vulnerability
Remote code execution via web shell upload.

## How I Found It
Access the lab and log in using the credentials wiener:peter. Once logged in, navigate to the "My Account" page. Use the avatar upload form to select any form of file and upload it.I tried changing several headers of the content-type and found out that changing the MIME type to image/jpeg was allowed.Hence,after changing it ,the file was succesfully uploaded. 
The web page should return a message indicating the file was successfully uploaded, confirming the lack of file type validation. 

## The Exploit
Create a new text file on your computer and name it exploit.php. Inside this file, paste the following PHP code, which uses a built-in function to read the contents of the target file.The following code works:`<?php echo file_get_contents('/home/carlos/secret'); ?>`.Send this uploaded request to repeater.Then,change the filepath to `exploit.php`.Before hitting the upload button,make sure to change the MIME type to the `image/jpeg`.This would trick the server into thinking it as an image and would pass the restriction.

## What I Learned
The most challenging part is to find the exact file path.This could be done in various ways.When testing a file upload vulnerability, an attacker rarely uploads a script hardcoded to read just one specific file.Instead, they usually upload a more flexible web shell that allows them to execute system commands or list directories dynamically.This could let them see the directories ad find the exact file path.

## How to Defend Against It
Never rely on a blacklist (blocking .php, .exe, etc.), as attackers can easily bypass them using alternate extensions (e.g., .php5, .phtml). Instead, enforce a strict allowlist that only permits specific, expected extensions (like .jpg, .png, or .pdf).
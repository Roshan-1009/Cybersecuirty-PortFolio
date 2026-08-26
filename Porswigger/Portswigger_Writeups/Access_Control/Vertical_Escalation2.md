## Vertical Privilege Escalation = — PortSwigger Web Security Academy

Tools used:None

## The Vulnerability
This is called the Vertical Privilage vulnerability,where you a non-administrative user can get admin privileges.

## How I Found It
You don't need fancy tools for this,try viewing the page source.You can see a javaascript code revealing the obfuscated link.

## The Exploit
After visiting the `/admin-e90qmy` ,you would avail the admin privileges.From there you can delete
the `carlos` user.

## What I Learned
As Portswigger gave us tracks like admin urls might exist in some known files,this might be easy.But it could be way more easy if you are using Gobuster ,you can track down the url's containing potentially unprotected pages with admin functionality.Remember-Obfuscation is just a way to push the time for hackers.It is never meant to hide anything,there are so many de-obfuscating online tools .

## How to Defend Against It
Don't give access to admin privileges using url's ,Never trust the user(Client-Side),always prioritze a server-side authentication.
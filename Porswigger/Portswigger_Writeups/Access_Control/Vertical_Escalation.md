## Vertical Privilege Escalation = — PortSwigger Web Security Academy

Tools used:None

## The Vulnerability
This is called the Vertical Privilage vulnerability,where you a non-administrative user can get admin privileges.

## How I Found It
Just add `/robots.txt` at the end of the link.You would find the trace for the admin panel which is 
`/administrator-panel`

## The Exploit
After visiting the `/administrator-panel` ,you would avail the admin privileges.From there you can delete
the `carlos` user.

## What I Learned
As Portswigger gave us tracks like admin urls might exist in some known files,this might be easy.But it could be way more easy if you are using Gobuster ,you can track down the url's containing potentially unprotected pages with admin functionality

## How to Defend Against It
Don't give access to admin privileges using url's ,Never trust the user(Client-Side)
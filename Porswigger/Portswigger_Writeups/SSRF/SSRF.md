## SSRF = — PortSwigger Web Security Academy

## Tools used:Burp Suite

## The Vulnerability
An attacker tricks a vulnerable server into making an HTTP request to a destination chosen by the attacker.

## How I Found It
I tried tampering with the `stockapi` parameter using `Burp Intruder` to check whether it accepts `localhost` urls.So i tried https://localhost and responded with a valid page.This means the server helps us access the admin panel acting as a proxy.

## The Exploit
http://localhost/admin would take you to the admin page,but still we won't be able to delete the carlos user because we are not authenticated as an admin.

## What I Learned
We have to send every action using get request including deleting users.We can't authenticate ourselves using urls.

## How to Defend Against It
Restict URL'S to a greater extent.No matter how much we fiter the urls using whitelist or blocking the `localhost` parameters-They are bypassable.
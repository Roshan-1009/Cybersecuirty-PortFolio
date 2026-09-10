## SSRF against backend system = — PortSwigger Web Security Academy

## Tools used:Burp Suite-Intruder

## The Vulnerability
An attacker tricks a vulnerable server into making an HTTP request to a destination chosen by the attacker.

## How I Found It
I tried tampering with the `stockapi` parameter using `Burp Intruder` to check whether it accepts `192.168.0.1-255`,here Wr have to try with all the 255 private routings by simultaneously checking the status code to `200`. 

## The Exploit
http://192.168.0.169:8080/admin would take you to the admin page,but still we won't be able to delete the carlos user because we are not authenticated as an admin.You can add the delete query `/delete?username=carlos`

## What I Learned
We have to send every action using get request including deleting users.We can't authenticate ourselves using urls.

## How to Defend Against It
Restict URL'S to a greater extent.No matter how much we fiter the urls using whitelist or blocking the `localhost` parameters-They are bypassable.
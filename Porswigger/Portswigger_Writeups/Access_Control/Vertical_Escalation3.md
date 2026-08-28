## Vertical Privilege Escalation = — PortSwigger Web Security Academy

## Tools used:Burp Suite

## The Vulnerability
This is called the Vertical Privilage vulnerability,where you a non-administrative user can get admin privileges.
Type:`Forgeable Session Cookie`

## How I Found It
The crux is finding the `Admin=True` statement

## The Exploit
Modify the traffic at every GET request changing to `Admin=True` from `Admin=False`.Until you find the `Admin Panel`,keep changing the privilege to `Admin=True`,Also do not skip this until you have deleted the user `carlos`.

## What I Learned
You will need Burp Suite for this.Especially,the Repeater tab.Think it as the Repeater is capable of sending requests without bothering the browser.This catches the traffic and you can modify and send to the server,this is the best reason of why `Server-Side authentication` is needful.

## How to Defend Against It
Never trust the user(Client-Side),always prioritze a server-side authentication.
This could be:
`Hidden Field`
`Forgeable Session Cookie`
`Query String alteration`
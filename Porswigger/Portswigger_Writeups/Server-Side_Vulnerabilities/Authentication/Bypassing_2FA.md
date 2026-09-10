## Bypassing 2FA = — PortSwigger Web Security Academy

## Tools used:None

## The Vulnerability
Bypassing 2fA by tricking the website into convincing that the website has already been logged in.

## How I Found It
Some websites might login the user the moment they type the credentials redirecting them to the 2FA verification dummy page.From there we can take any known webpages using url.

## The Exploit
After typing in the credentials,you would encounter the 2FA page,change the url to `/myaccount` which will redirect to the pages logged in as the user.

## What I Learned
Never authenticate user before they actually type in the verification code.

## How to Defend Against It
Only issue a fully authenticated session token after 2FA succeeds. Before that, issue a separate, limited pending 2FA token that grants access to nothing except the 2FA verification endpoint.Never let the client dictate which step of the flow it's on.The server should track this itself, tied to the session
## Horizontal Privilege Escalation = — PortSwigger Web Security Academy

## Tools used:None

## The Vulnerability
This is called the Horizontal Privilage vulnerability,in this lab,this could be also encountered as IDOR.


## How I Found It
In this we have a masked password input forged into the user's account.But the masked input is somewhat disclosed in the page source,so all we have to find the admin url,enter it.Then,read the masked input.

## The Exploit
In the page source,you might see `value='u7kiy2u9fzx69dicni8d`,this is the masked input,which is also the password.

## What I Learned
Masked input was never supposed to store information,its only used to conceal it for a couple of time for anyone peeking to your screen.Some people might question that "If we get access to the page,why do we need th password.Well,maybe you just be able to get to the page,but may not have the access to the admin privileges.So,accessing the password maybe the only way.

## How to Defend Against It
Never feel satisfied in password masking,think that its only a way to hide your live screen typing.
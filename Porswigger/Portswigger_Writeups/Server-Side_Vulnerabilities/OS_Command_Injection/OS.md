## File Upload Vulnerabilites = — PortSwigger Web Security Academy

## Tools used:Burp Suite-Repeater

## The Vulnerability
 It allows an attacker to execute operating system (OS) commands on the server that is running an application, and typically fully compromise the application and its data. Often, an attacker can leverage an OS command injection vulnerability to compromise other parts of the hosting infrastructure, and exploit trust relationships to pivot the attack to other systems within the organization. It allows an attacker to execute operating system (OS) commands on the server that is running an application, and typically fully compromise the application and its data. Often, an attacker can leverage an OS command injection vulnerability to compromise other parts of the hosting infrastructure, and exploit trust relationships to pivot the attack to other systems within the organization.

## How I Found It
Take some parameters and test some commands using `& echo <some command> &`.If that executes,then we know that shell injection works.

## The Exploit
Create a new text file on your computer and name it exploit.php. Inside this file, paste the following PHP code, which uses a built-in function to read the contents of the target file.The following code works:`<?php echo file_get_contents('/home/carlos/secret'); ?>`.Send this uploaded request to repeater.Then,change the filepath to `exploit.php`.The response should be the secret key.We can use the `whoami` command to find out the privileges by giving some parameter `| echo whoami` .

## What I Learned
Some commands would come handy to test the shell injection vulnerabilities.
## How to Defend Against It
To protect against OS command injection, avoid calling OS commands directly from your application and use safe platform APIs or parameterized functions instead.
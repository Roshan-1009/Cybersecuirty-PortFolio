## SQL Injection = — PortSwigger Web Security Academy

## Tools used:Burp Suite

## The Vulnerability
SQL injection (SQLi) is a web security vulnerability that allows an attacker to interfere with the queries that an application makes to its database. This can allow an attacker to view data that they are not normally able to retrieve. This might include data that belongs to other users, or any other data that the application can access

## How I Found It
SQL vulnerabilities can be found by manipulating SQL queries.I tried many input and understood different responses.

## The Exploit
I tried `+OR+1=1--` with parameter.This is used to futile the intial command using the `OR` operator.This gave us the all the unreleased categories as the effective query was ``SELECT * FROM products`

## What I Learned
Most of the empty field SQL Queries are run by the `SELECT * FROM products WHERE category = <xxxxx> AND released= <xxxxxxx>`.So,by adjusting queries and commenting out unwanted parameters,we can access the accounts regardless of the password.

## How to Defend Against It
The single most effective defense against SQL injection is using prepared statements with parameterized queries, which ensure user input is always treated as data rather than executable code.
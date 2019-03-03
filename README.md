# Postfix Queue Move
Switch Postfix and Sendmail mail queue between two servers if the mail server unable to send it’s queued emails.

Postfix Deferred Emails Movement 
Form Postfix Server to another Postfix Server
Version: 1.0
By: Eyad Abu arqoub
Email: eyad-arqoub@live.com
Date: Thursday, August 23, 2018.
Notes:
	You must be install paramiko Python library on local PC.
	You must be install "sshpass" on the remote Linux server.
	You must run a scp command for first time you use scp from local PC to remote PC, to do next scp automatically.

When I can use this tool?
If your primary Postfix mail server cannot send emails to the destination and have deferred emails in the queue, for many reasons like:
	Your primary Postfix mail server does not reach the destination at network level.
	Your primary Postfix mail server static IP is blacklisted in Real-time Blackhole List (RBL) [Domain Name System-based Blackhole List (DNSBL)], and many mail servers reject the emails which received from your mail server.
	Your primary Postfix mail server, domain name or email account was put on blacklist of destination mail server.
	Your primary Postfix mail server has error configuration and not configured well.

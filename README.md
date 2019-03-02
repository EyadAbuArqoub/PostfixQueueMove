# Postfix Queue Move
Switch Postfix and Sendmail mail queue between two servers if the mail server unable to send it’s queued emails.

Postfix Deferred Emails Movement 
Form Postfix Server to Another Postfix Server

Version: 1.0

By: Eyad Abu arqoub
Email: eyad-arqoub@live.com

Date: Thursday, August 23, 2018.

Notes:
  [1] You must be install "sshpass" on the remote Linux server.
  [2] You must run a scp command for first time you use scp to do next scp automatically.
  [3] You must install paramiko library.

When I can use this tool?
If your primary Postfix mail server cannot send emails to the destination and have deferred emails in the queue, for many reasons like:
  [1] Your primary Postfix mail server doesn't reach the destination at network level.
  [2] Your primary Postfix mail server static IP is blacklisted in Real-time Blackhole List (RBL) [Domain Name System-based Blackhole List (DNSBL)], and many mail servers reject the emails which received from your mail server.
  [3] Your primary Postfix mail server was put on blacklist of destination mail server.
  [4] Your primary Postfix mail server has error configuration and not configured well.

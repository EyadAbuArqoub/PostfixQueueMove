# Postfix Queue Move
Switch Postfix mail queue between two servers if the mail server unable to send it’s queued emails.

<p>Postfix deferred emails movement form Postfix server to another Postfix server</p>
<p>Version: 1.0</p>
<p>By: Eyad Abu arqoub</p>
<p>Email: <a href="mailto:eyad-arqoub@live.com">eyad-arqoub@live.com</a></p>
<p>Date: Thursday, August 23, 2018</p>
<p><u>Notes:</u></p>
<ul>
<li>You must be install paramiko Python library on local PC.</li>
<li>You must be install "sshpass" on the remote Linux server.</li>
<li>You must run a scp command for first time you use scp from local PC to remote PC, to do next scp automatically.</li>
</ul>
<p><u>When I can use this tool?</u></p>
<p>If your primary Postfix mail server cannot send emails to the destination and have deferred emails in the queue, for many reasons like:</p>
<ul>
<li>Your primary Postfix mail server does not reach the destination at network level.</li>
<li>Your primary Postfix mail server static IP is blacklisted in Real-time Blackhole List (RBL) [Domain Name System-based Blackhole List (DNSBL)], and many mail servers reject the emails which received from your mail server.</li>
<li>Your primary Postfix mail server, domain name or email account was put on blacklist of destination mail server.</li>
<li>Your primary Postfix mail server has error configuration and not configured well.</li>
</ul>
<p>&nbsp;</p>
<p>&nbsp;</p>

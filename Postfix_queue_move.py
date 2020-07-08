
'''

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
    [3] Your primary Postfix mail server, domain name or email account was put on blacklist of destination mail server.
    [4] Your primary Postfix mail server has error configuration and not configured well. 


'''


# --------------------------------------------------------------------------------------------------------------------------------- #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Import Modules ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# --------------------------------------------------------------------------------------------------------------------------------- #

import os
import subprocess
import paramiko



# --------------------------------------------------------------------------------------------------------------------------------- #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Define Functions ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# --------------------------------------------------------------------------------------------------------------------------------- #


# To pass commands to server via SSH
def ssh_cmd(server_ip, ssh_port, user_name, password, cmd):

    try:

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, ssh_port, user_name, password)
        ssh.exec_command(cmd)
        
        #print "The task performed successfully.\n" + cmd + "\t on \t" + server_ip + "\n"

        return True
        
    except Exception as e:

        print "Unable to perform this task successfully."
        print str(e) + "."


# To Flush Emails in Mail Queue
def flush_postfix():

    server_ip = 'ip_here'
    ssh_port = port
    user_name = 'user_here'
    password = 'password_here'
    cmd = '/usr/sbin/postqueue -c /etc/postfix -f'
    
    try:

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, ssh_port, user_name, password)
        ssh.exec_command(cmd)
        
        print "The task performed successfully.\n" + cmd + "\t on \t" + server_ip + "\n"
        
    except Exception as e:

        print "Unable to perform this task successfully."
        print str(e) + "."



# To List Files in a Directory on Remote Server via SSH
def get_files(server_ip, ssh_port, user_name, password, remote_directory):

    try:

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server_ip, ssh_port, user_name, password)

        cmd = 'ls ' + remote_directory
        
        stdin, stdout, stderr = ssh.exec_command(cmd)
        outlines = stdout.readlines()
        resp = ''.join(outlines)
        
        resp = resp.split('\n')
        resp = resp[:-1]

        return resp
        
    except Exception as e:

        print "Unable to perform this task successfully."
        print str(e) + "."




# --------------------------------------------------------------------------------------------------------------------------------- #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Define Variables ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# --------------------------------------------------------------------------------------------------------------------------------- #


server_ssh_access = ['ip_here', port_here, 'user_here', 'password_here']

remote_server_path = "/var/spool/postfix/deferred/"

local_path = "/var/spool/postfix/deferred/"

defer_mails_count = 0

copy_count = 0


# List all directories in remote server
dirs = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']





# --------------------------------------------------------------------------------------------------------------------------------- #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Movement Steps ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# --------------------------------------------------------------------------------------------------------------------------------- #



print '\nPostfix Tool - Move Deferred Emails From Server To Another\n'



continue_input = raw_input('To continue running this tool type "yes", to exit type "no".\n')

if continue_input == 'yes':
    pass
else:
    exit()

print '\nRunning Postfix Tool ...\n'




# Folder in Folders Loop

for d in dirs:

    # Git Files in the Directory
    
    remote_directory = str(remote_server_path) + str(d)

    dst = str(local_path) + str(d)

    if not os.path.exists(dst):
        os.makedirs(dst)

    files = get_files(server_ssh_access[0], server_ssh_access[1], server_ssh_access[2], server_ssh_access[3], remote_directory)

    # File in Folder Loop

    for f in files:

        defer_mails_count = defer_mails_count + 1
        
        src_file = remote_directory + '/' + f
        
        # Copy the File    
            
        copy_file_cmd = 'sshpass -p "' + server_ssh_access[3] + '" scp -r ' + server_ssh_access[2] + '@' + server_ssh_access[0] + ':' + src_file + ' ' + dst

        
        if subprocess.call(copy_file_cmd, shell = True) == 0:
            copy_count = copy_count + 1
            print 'copied\t', src_file
        else:
            print 'not copied\t', src_file

        
        # Delete the File

        del_src = 'rm ' + src_file

        if os.path.exists(src_file):
            if (ssh_cmd(server_ssh_access[0], server_ssh_access[1], server_ssh_access[2], server_ssh_access[3], del_src)):
                print 'deleted\t', src_file
        



    # Change MOD and Owner
    
    if files != []:
        
        # Change the MOD of Folder
        # /var/spool/postfix/deferred/* 700
   
        chmod_cmd = 'chmod 700 ' + remote_directory + '/*'
    
        if subprocess.call(chmod_cmd, shell = True) == 0:
            print 'chmod done\t', remote_directory
        else:
            print 'chmod failed\t', remote_directory


        # Change owner postfix
        chown_cmd = 'chown postfix:postfix ' + remote_directory + '/*'
        
        if subprocess.call(chown_cmd, shell = True) == 0:
            print 'chown done\t', remote_directory
        else:
            print 'chown failed\t', remote_directory

            

        print '-' * 60




# --------------------------------------------------------------------------------------------------------------------------------- #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Flush Emails ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# --------------------------------------------------------------------------------------------------------------------------------- #

# Flush Emails in Local Server to Resend it
#flush_postfix()




# --------------------------------------------------------------------------------------------------------------------------------- #
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Report Section ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# --------------------------------------------------------------------------------------------------------------------------------- #

print "\n", "Deferred Emails Count:\t", defer_mails_count
print "Copied Emails:\t", copy_count
print '\n'




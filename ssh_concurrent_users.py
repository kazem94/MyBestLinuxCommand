import subprocess
output = subprocess.check_output("ps x | grep sshd | awk '{print $1,$6}'", shell=True).decode()
allprocess = {}
for line in output.split('\n'):
    line = line.strip()
    if line:
        pid,username = line.split()
        allprocess[pid] = username
#print(allprocess)
allrow = {}
f = open("m.txt", "r")
for row in f:
    row = row.strip()
    if row:
        usrname,count = row.split('=')
        allrow[count] = usrname
#print(allrow)
f.close()
killuser = {}
for cnt,usr in allrow.items():
    fnd = 0
    for id,user in allprocess.items():
        if(usr == user):
            fnd = fnd + 1
        if(int(fnd) > int(cnt)):
            #print(usr,'=',fnd)
            command = 'kill ' + id
            killoutput = subprocess.check_output(command, shell=True).decode()
            #print(killoutput)

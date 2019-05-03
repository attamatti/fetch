#!/usr/bin/python
vers = '0.1'
fetchdir = '/fbs/emsoftware2/LINUX/fbsmi/scripts/new_fetch'
spiderexts = ("spi","mgi","sab")

import os
import sys
import glob
import datetime
import getpass

finalpick = "HELP.txt"
if "-s" in sys.argv:
    print "SHAUN MODE! SHAUN MODE!  Snowden would be proud!!"
    print """You are making it hard for me to do statistcs!"""

# - FUNCT: pick a file/dir make a menu------------------------#
def make_menu(tdir):
    options = glob.glob("{0}/*".format(tdir))
    coptions =[]
    if tdir[-1] == "/":
        tdir = tdir[:-1]
    for i in options:
        if os.path.isfile(i) == True and i not in ('{0}/MESSAGE.txt'.format(tdir),'{0}/fetch.py'.format(tdir),'{0}/HELP.txt'.format(tdir),'{0}/DL.log'.format(tdir)):
            coptions.append(i)
    coptions.sort()
    doptions = []
    for i in options:
        if os.path.isdir(i) == True:
            doptions.append(i)
    print "\n"
    os.system("cat {0}/MESSAGE.txt".format(tdir))
    print ""
    n = 1
    for i in coptions:
        print "{0:>2d}]  {1}".format(n,i.replace(tdir,'').strip('/'))
        n+=1
    letters = []
    if len(doptions) >=1:
        print "\n-- additional scripts --"
        letters = map(chr,(range(97,97+len(doptions))))
        l=0
        dirdic = {}
        for i in doptions:
            print "{0}]  {1}/".format(chr(l+97),i.replace(tdir,'').strip('/'))
            dirdic[chr(l+97)] = i
            l+=1
    selection = raw_input("\n--\nq] QUIT\t\t  z] HELP\n\nSelect an option:")
    assert selection in map(str,range(0,n+1)) or selection in letters or selection =='z', sys.exit("Goodbye") 

    if selection in letters:
        make_menu(dirdic[selection])
    elif selection == "z":
            os.system("less {0}/HELP.txt".format(tdir))
            return make_menu(tdir)
    elif selection in map(str,range(0,n+1)):
        global finalpick
        finalpick = coptions[int(selection)-1]
#----------------------------------------------------------#

# - FUNCT: add a version control tag to script and copy it-----------------------------------#
def tag_script(script):
    sdata = open(script,'r').readlines()
    
    if script.split("/")[-1].split('.')[1] in spiderexts:
        tdata = [';##############################################\n',';### FETCH COPY - ({0}{1}) - download a fresh copy if necessary\n'.format(getpass.getuser(),datetime.datetime.now()),';#############################################\n\n']
    else:
        tdata = ['{0}'.format(sdata[0]),'##############################################\n','### FETCH COPY - ({0}{1}) - download a fresh copy if necessary\n'.format(getpass.getuser(),datetime.datetime.now()),'##############################################\n\n']
    if script.split("/")[-1].split('.')[1] in spiderexts:
        for i in sdata:
            tdata.append(i)
    else:
        for i in sdata[1:]:
            tdata.append(i) 
    output = open('{0}'.format(script.split('/')[-1]),'w')
    for i in tdata:
        output.write(i)
    os.system('chmod u+x {0}'.format(script.split('/')[-1]))
    if "-s" not in sys.argv:
        log = open("{0}/DL.log".format(fetchdir),'a')
        log.write(getpass.getuser()+"\t"+str(datetime.datetime.now())+"\t"+script+"\n")
#----------------------------------------------------------#

### PROGRAM
make_menu(fetchdir+"/scripts_fetch")
print "downloaded {0}".format(finalpick)
tag_script(finalpick)


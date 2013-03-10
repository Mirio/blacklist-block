#                                    LICENSE BSD 2 CLAUSE                                       #
#   Copyright 2013 Mirio. All rights reserved.                                                  #
#   Redistribution and use in source and binary forms, with or without modification, are        #
#   permitted provided that the following conditions are met:                                   #
#       1. Redistributions of source code must retain the above copyright notice, this list of  #
#      conditions and the following disclaimer.                                                 #
#       2. Redistributions in binary form must reproduce the above copyright notice, this list  #
#      of conditions and the following disclaimer in the documentation and/or other materials   #
#      provided with the distribution.                                                          #
#                                                                                               #
#   THIS SOFTWARE IS PROVIDED BY Mirio ''AS IS'' AND ANY EXPRESS OR IMPLIED                     #
#   WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND    #
#   FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR    #
#   CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR         #
#   CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR    #
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON    #
#   ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING          #
#   NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF        #
#   ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.                                                  #
#                                                                                               #
#   The views and conclusions contained in the software and documentation are those of the      #
#   authors and should not be interpreted as representing official policies, either expressed   #
#   or implied, of Mirio                                                                        #
import urllib2, subprocess, shlex, time

def addrule(ip):
    dot = ip.split('.')
    if len(dot)==4:
        time.sleep(0.1)
        subprocess.Popen(shlex.split("iptables -A BLACKLIST -s "+ip+" -j DROP"))
    else:
        pass

def main():
    tor_list = urllib2.urlopen('http://torstatus.blutmagie.de/ip_list_exit.php/Tor_ip_list_EXIT.csv')
    blacklist = urllib2.urlopen('http://infiltrated.net/blacklisted')

    subprocess.Popen(shlex.split("iptables -N BLACKLIST"))
    subprocess.Popen(shlex.split("iptables -F BLACKLIST"))

    for ip_tor in tor_list.readlines():
        addrule(ip_tor)
    for ip_bl in blacklist.readlines():
        try:
            addrule(ip_bl.split()[0])
        except IndexError:
            pass
try:
    main()
except OSError:
    print "You don't have Permission!"

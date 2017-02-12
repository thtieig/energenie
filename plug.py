from energenie import switch_on, switch_off
from time import sleep
import sys

if len(sys.argv) == 1:
    print "Use:\n# python plug.py <plug_ID> <ON/OFF>\ne.g. # python plug.py 1 ON"
    exit(1)

else:
    plug = sys.argv[1]
    status = sys.argv[2]

if status.lower() == 'on':
   switch_on(int(plug))
else:
   switch_off(int(plug))     
 
# turn all plug sockets on and off
#switch_on()
#switch_off()

# turn a plug socket on and off by number
#switch_on(2)
#sleep(2)
#switch_off(2)

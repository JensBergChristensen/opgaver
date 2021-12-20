from gpizero import MCP3008 as mcp
from time import sleep


signal1 = mcp(channel=3)
signal2 = mcp(channel=4)

while true:
    print("Signal1: ",signal1)
    print("Signal2: ",signal2)
    sleep(3)


#Termometer skal have strom fra forskellige steder.
#Gang signal med volt?

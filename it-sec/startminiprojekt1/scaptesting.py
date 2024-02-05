
# IMPORT STATEMENTS
from scapy.all import ARP, Ether, srp
import sqlite3

# This script is used to scan the network for devices and store them in a database
# network scanning copied from article: https://thepythoncode.com/article/building-network-scanner-using-scapy

# create a database connection
conn = sqlite3.connect('miniprojekt.db')
c = conn.cursor()

# create a table
c.execute('''CREATE TABLE IF NOT EXISTS devices
             (mac TEXT PRIMARY KEY, ip TEXT)''')



target_ip = "192.168.1.1/24"
# IP Address for the destination
# create ARP packet
arp = ARP(pdst=target_ip)
# create the Ether broadcast packet
# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
ether = Ether(dst="ff:ff:ff:ff:ff:ff")
# stack them
packet = ether/arp

result = srp(packet, timeout=3, verbose=0)[0]

# a list of clients, we will fill this in the upcoming loop
clients = []

for sent, received in result:
    # for each response, append ip and mac address to `clients` list
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

# print clients
print("Available devices in the network:")
print("IP" + " "*18+"MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))

# insert the devices into the database
for client in clients:
    try:
        c.execute("INSERT INTO devices (mac, ip) VALUES (?, ?)", (client['mac'], client['ip']))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Device already in database")



# View table devices
c.execute("SELECT * FROM devices")
rows = c.fetchall()
print("Devices in the database:")
for row in rows:
    print("MAC: {}, IP: {}".format(row[0], row[1]))


# close the database connection
conn.close()






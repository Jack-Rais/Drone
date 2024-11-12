#from nrf24 import NRF24    # pip install nrf24
import pigpio               # pip install pigpio
import sys

# You can get the HOST by running from the raspberry (sudo pigpoid) and then (hostname -I)

HOST = 'localhost'      # "localhost" if run directly in the raspberry, else the ip (ex: "192.168.1.100")
PORT = 8888             # Usually 8888 by default, might change

pi = pigpio.pi(
    HOST,
    PORT
)

if not pi.connected:
    print('Raspberry pi isn\'t connected retry')
    sys.exit()


print(f"Raspberry pi connected at host={HOST}, port={PORT}")
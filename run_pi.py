# pip install nrf24, gigpio

from nrf24 import NRF24, RF24_DATA_RATE, RF24_PA
import pigpio                               
import sys

# You can get the HOST by running from the raspberry (sudo pigpoid) and then (hostname -I)

HOST = 'localhost'      # "localhost" if run directly in the raspberry, else the ip (ex: "192.168.1.100")
PORT = 8888             # Usually 8888 by default, might change

CE_PIN = 22
CSN_PIN = 0
ADRESS = '1ACK'

DATA_RATE = RF24_DATA_RATE.RATE_1MBPS       # Can be RF24_DATA_RATE.RATE_(250KBPS, 1MBPS, 1MBPS)
PA_LEVEL = RF24_PA.LOW                      # Can be RF24_PA.(LOW, HIGH, MIN, MAX)


pi = pigpio.pi(
    HOST,
    PORT
)

if not pi.connected:
    print('Raspberry pi isn\'t connected retry')
    sys.exit()

print(f"Raspberry pi connected at host={HOST}, port={PORT}")


radio = NRF24(
    pi,
    CE_PIN,
    data_rate = DATA_RATE,
    pa_level = PA_LEVEL
)
radio.set_address_bytes(len(ADRESS))

radio.set_retransmission(15, 15)
radio.open_writing_pipe(ADRESS)

radio.show_registers()
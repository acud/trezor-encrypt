#!/usr/bin/python3
import binascii
from trezorlib.tools import parse_path
from trezorlib import tezos, ui, device
from trezorlib import messages as proto
from trezorlib.transport import TransportException  
from trezorlib.exceptions import TrezorFailure
from trezorlib.client import TrezorClient
from trezorlib.transport import get_transport
from trezorlib import misc

device = get_transport()
client = TrezorClient(transport=device, ui=ui.ClickUI())


def encrypt(key, value):
    addr = [0,1,2]
    enc = misc.encrypt_keyvalue(client, addr, key, value, ask_on_encrypt=True, ask_on_decrypt=True)
    return enc

def decrypt(key, value):
    addr = [0,1,2]
    dec = misc.decrypt_keyvalue(client, addr, key, binascii.unhexlify(value), ask_on_encrypt=True, ask_on_decrypt=True)
    return dec

plain = input("Enter message: ")
plain = plain.ljust(256, ' ')
message = plain.encode()

key = "password"
res = encrypt(key, message)
print(res.hex())

dec = decrypt(key,res.hex())
print(dec)

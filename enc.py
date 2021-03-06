#!/usr/bin/python3
import binascii
import getpass
import sys
from trezorlib import ui, device
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

print(sys.argv)
if len(sys.argv) != 2:
    raise ValueError("not enough args")

plain = input("Enter message: ")
plain = plain.ljust(256, ' ')

f = open(sys.argv[1],'r')
msg = f.read()

if msg == "":
    raise ValueError("empty file to encrypt")

message = plain.encode()

passk = getpass.getpass("Enter Password: ")
res = encrypt(passk, message)
print(res.hex())

passs = input("Enter Password:")

dec = decrypt(passs,res.hex())
print(dec)

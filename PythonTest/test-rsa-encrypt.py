"""
openssl genrsa -des3 -out rsa_private_key.pem 1024
openssl rsa -pubout -in rsa_private_key.pem -out rsa_public_key.pub
"""

#! /usr/bin/python3
# coding: utf-8

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

#pool = Crypto.Util.randpool.RandomPool()
#rsa  = Crypto.PublicKey.RSA.generate(1024, pool.get_bytes)

pub  = RSA.importKey(open('rsa_public_key.pub', 'r').read())
priv = RSA.importKey(open('rsa_private_key.pem', 'r').read())

text = '12345678'.encode("utf-8")
print(text)

#crypto = pub.encrypt(text, '')
cipher_encode = PKCS1_OAEP.new(pub)
cipher_encode_text = cipher_encode.encrypt(text)
print(base64.b64encode(cipher_encode_text))

cipher_decode = PKCS1_OAEP.new(priv)
message = cipher_decode.decrypt(cipher_encode_text)
print(message)
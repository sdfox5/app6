from flask import Flask, jsonify
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
#from GetWishListItems_pb2 import CSGetWishListItemsRes

app = Flask(__name__)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GetWishListItems.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16GetWishListItems.proto\x12\x05proto\"+\n\x15\x43SGetWishListItemsReq\x12\x12\n\naccount_id\x18\x01 \x01(\x04\"5\n\x0cWishItemInfo\x12\x0f\n\x07item_id\x18\x01 \x01(\r\x12\x14\n\x0crelease_time\x18\x02 \x01(\x04\";\n\x15\x43SGetWishListItemsRes\x12\"\n\x05items\x18\x01 \x03(\x0b\x32\x13.proto.WishItemInfob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetWishListItems_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CSGETWISHLISTITEMSREQ']._serialized_start=33
  _globals['_CSGETWISHLISTITEMSREQ']._serialized_end=76
  _globals['_WISHITEMINFO']._serialized_start=78
  _globals['_WISHITEMINFO']._serialized_end=131
  _globals['_CSGETWISHLISTITEMSRES']._serialized_start=133
  _globals['_CSGETWISHLISTITEMSRES']._serialized_end=192
# @@protoc_insertion_point(module_scope)



BASE64_TOKEN = "eyJhbGciOiJIUzI1NiIsInN2ciI6IjEiLCJ0eXAiOiJKV1QifQ.eyJhY2NvdW50X2lkIjoxMTE1NjM4ODE3OSwibmlja25hbWUiOiLvta7vta7vta7vta7vta7vta7vta7vta7vta7vta7vta4iLCJub3RpX3JlZ2lvbiI6Ik1FIiwibG9ja19yZWdpb24iOiJNRSIsImV4dGVybmFsX2lkIjoiMmU1Y2U1MTNhYWRiYWY0YzczMzcxMWNiODlmYTNlNTgiLCJleHRlcm5hbF90eXBlIjo0LCJwbGF0X2lkIjoxLCJjbGllbnRfdmVyc2lvbiI6IjEuMTA4LjMiLCJlbXVsYXRvcl9zY29yZSI6MCwiaXNfZW11bGF0b3IiOmZhbHNlLCJjb3VudHJ5X2NvZGUiOiJVUyIsImV4dGVybmFsX3VpZCI6Mzc2NDc0MjUzMCwicmVnX2F2YXRhciI6MTAyMDAwMDA3LCJzb3VyY2UiOjAsImxvY2tfcmVnaW9uX3RpbWUiOjE3Mzk3NTg2ODIsImNsaWVudF90eXBlIjoyLCJzaWduYXR1cmVfbWQ1IjoiNzQyOGIyNTNkZWZjMTY0MDE4YzYwNGExZWJiZmViZGYiLCJ1c2luZ192ZXJzaW9uIjoxLCJyZWxlYXNlX2NoYW5uZWwiOiJhbmRyb2lkIiwicmVsZWFzZV92ZXJzaW9uIjoiT0I0NyIsImV4cCI6MTc0MDA4ODA1NH0.2j-TmoXaCgsUa9NzjGKqMNor5b28wDbwFLiQ-5eTQ6g"

def Encrypt_ID(x):
    x = int(x)
    dec = [ '80', '81', '82', '83', '84', '85', '86', '87', '88', '89', '8a', '8b', '8c', '8d', '8e', '8f', '90', '91', '92', '93', '94', '95', '96', '97', '98', '99', '9a', '9b', '9c', '9d', '9e', '9f', 'a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'c0', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'd0', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'da', 'db', 'dc', 'dd', 'de', 'df', 'e0', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'f0', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff']
    xxx= [ '1','01', '02', '03', '04', '05', '06', '07', '08', '09', '0a', '0b', '0c', '0d', '0e', '0f', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '1a', '1b', '1c', '1d', '1e', '1f', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '2a', '2b', '2c', '2d', '2e', '2f', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '3a', '3b', '3c', '3d', '3e', '3f', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '4a', '4b', '4c', '4d', '4e', '4f', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '5a', '5b', '5c', '5d', '5e', '5f', '60', '61', '62', '63', '64', '65', '66', '67', '68', '69', '6a', '6b', '6c', '6d', '6e', '6f', '70', '71', 
    '72', '73', '74', '75', '76', '77', '78', '79', '7a', '7b', '7c', '7d', '7e', '7f']
    x= x/128 
    if x>128:
        x =x/128
        if x >128:
            x= x/128
            if x>128:
                x= x/128
                strx= int(x)
                y= (x-int(strx))*128
                stry =str(int(y))
                z = (y-int(stry))*128
                strz =str(int(z))
                n =(z-int(strz))*128
                strn=str(int(n))
                m=(n-int(strn))*128
                return dec[int(m)]+dec[int(n)]+dec[int(z)]+dec[int(y)]+xxx[int(x)]
            else:
                strx= int(x)
                y= (x-int(strx))*128
                stry =str(int(y))
                z = (y-int(stry))*128
                strz =str(int(z))
                n =(z-int(strz))*128
                strn=str(int(n))
                return dec[int(n)]+dec[int(z)]+dec[int(y)]+xxx[int(x)]



def encrypt_api(plain_text):
    plain_text = bytes.fromhex(plain_text)
    key = bytes([89, 103, 38, 116, 99, 37, 68, 69, 117, 104, 54, 37, 90, 99, 94, 56])
    iv = bytes([54, 111, 121, 90, 68, 114, 50, 50, 69, 51, 121, 99, 104, 106, 77, 37])
    cipher = AES.new(key, AES.MODE_CBC, iv)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return cipher_text.hex()

from datetime import datetime

def convert_timestamp(release_time):
    return datetime.utcfromtimestamp(release_time).strftime('%Y-%m-%d %H:%M:%S')

# مثال:

@app.route('/wishlist/<int:uid>', methods=['GET'])
def get_wishlist(uid):
    encrypted_id = Encrypt_ID(uid)
    encrypted_api = encrypt_api(f"08{encrypted_id}1007")
    TARGET = bytes.fromhex(encrypted_api)
    
    url = "https://clientbp.ggblueshark.com/GetWishListItems"
    headers = {
        "Authorization": f"Bearer {BASE64_TOKEN}",
        "X-Unity-Version": "2018.4.11f1",
        "X-GA": "v1 1",
        "ReleaseVersion": "OB47",
        "Content-Type": "application/x-www-form-urlencoded",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-N975F Build/PI)",
        "Host": "clientbp.common.ggbluefox.com",
        "Connection": "close",
        "Accept-Encoding": "gzip, deflate, br",
    }
    
    response = requests.post(url, headers=headers, data=TARGET, verify=False)
    decoded_response = CSGetWishListItemsRes()
    decoded_response.ParseFromString(response.content)
    
    wishlist = [
        {"item_id": item.item_id, "release_time": convert_timestamp(item.release_time)}
        for item in decoded_response.items
    ]
    
    return jsonify({"uid": uid, "wishlist": wishlist})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

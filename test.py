import struct
from pwn import *

DATA_TYPE_EMPTY = 0x0
DATA_TYPE_INTEGER = 0x1
DATA_TYPE_FLOAT = 0x2
DATA_TYPE_STRING = 0x3
DATA_TYPE_ARRAY = 0x4
DATA_TYPE_TERM = 0xff

context.log_level = "debug"
p = remote("127.0.0.1", 9999)

def make_int(num:int):
    return struct.pack(b">HQ", DATA_TYPE_INTEGER, num)

def make_float(num:float):
    return struct.pack(b">Hd", DATA_TYPE_FLOAT, num)

def make_string(_str:bytes):
    return struct.pack(b">HI", DATA_TYPE_STRING, len(_str)) + _str

def make_array(count:int, items):
    p = struct.pack(b">HI", DATA_TYPE_ARRAY, count)
    for i in range(count):
        if(items[i][0] == DATA_TYPE_INTEGER):
            p += make_int(items[i][1])
        elif(items[i][0] == DATA_TYPE_FLOAT):
            p += make_float(items[i][1])
        elif(items[i][0] == DATA_TYPE_STRING):
            p += make_string(items[i][1])
        elif(items[i][0] == DATA_TYPE_ARRAY):
            p += make_array(items[i][1], items[i][2])
    return p

def cmd_add(key:bytes, value:bytes):
    payload = b"KVDB"
    payload += struct.pack(b">H", 3) + b"ADD"
    payload += key + value
    p.send(payload)

def cmd_del(key:bytes):
    payload = b"KVDB"
    payload += struct.pack(b">H", 3) + b"DEL"
    payload += key
    p.send(payload)

def cmd_mdf(key:bytes, new_value:bytes):
    payload = b"KVDB"
    payload += struct.pack(b">H", 3) + b"MDF"
    payload += key + new_value
    p.send(payload)

def cmd_rnm(old_key:bytes, new_key:bytes):
    payload = b"KVDB"
    payload += struct.pack(b">H", 3) + b"RNM"
    payload += old_key + new_key
    p.send(payload)

def cmd_cpy(src_key:bytes, dst_key:bytes):
    payload = b"KVDB"
    payload += struct.pack(b">H", 3) + b"CPY"
    payload += src_key + dst_key
    p.send(payload)

def cmd_get(key:bytes):
    payload = b"KVDB"
    payload += struct.pack(b">H", 3) + b"GET"
    payload += key
    p.send(payload)

def cmd_dump():
    payload = b"KVDB"
    payload += struct.pack(b">H", 4) + b"DUMP"
    payload += b"" # payload
    p.send(payload)

def cmd_shut():
    payload = b"KVDB"
    payload += struct.pack(b">H", 4) + b"SHUT"
    payload += b"" # payload
    p.send(payload)

def cmd_xxx():
    payload = b"KVDB"
    payload += struct.pack(b">H", 3) + b"AAA"
    payload += b"" # payload
    p.send(payload)

'''
array1_1_1 = [
    (DATA_TYPE_STRING, b"a"*0x10),
    (DATA_TYPE_STRING, b"b"*0x10),
    (DATA_TYPE_STRING, b"c"*0x10)
]

array1_1 = [
    (DATA_TYPE_INTEGER, 0xdeadbeef),
    (DATA_TYPE_INTEGER, 0xdeadbeef),
    (DATA_TYPE_INTEGER, 0xdeadbeef),
    (DATA_TYPE_ARRAY, len(array1_1_1), array1_1_1)
]

array1 = [
    (DATA_TYPE_FLOAT, 0.1234),
    (DATA_TYPE_INTEGER, 0xdeadbeef),
    (DATA_TYPE_STRING, b"aaaaaaaa"),
    (DATA_TYPE_ARRAY, len(array1_1), array1_1)
]
cmd_add(make_int(0x1111), make_array(len(array1), array1))
'''
cmd_add(make_int(0x1111), make_string(b"a"*0x1000))
p.recv()
cmd_get(make_int(0x1111))
p.recv()
p.interactive()
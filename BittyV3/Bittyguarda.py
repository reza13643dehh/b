#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import random
import threading
import time
from datetime import datetime
from rich import print
import httplib2, json
import platform
import os
import sys
import ctypes
mizogg= '''[red]
              ___            ___  
             (o o)          (o o) 
            (  V  ) MIZOGG (  V  )
            --m-m------------m-m--
[/red]'''
print(mizogg)
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141

if platform.system().lower().startswith('win'):
    dllfile = 'ice_secp256k1.dll'
    if os.path.isfile(dllfile) == True:
        pathdll = os.path.realpath(dllfile)
        miz = ctypes.CDLL(pathdll)
    else:
        print('File {} not found'.format(dllfile))
    
elif platform.system().lower().startswith('lin'):
    dllfile = 'ice_secp256k1.so'
    if os.path.isfile(dllfile) == True:
        pathdll = os.path.realpath(dllfile)
        miz = ctypes.CDLL(pathdll)
    else:
        print('File {} not found'.format(dllfile))
    
else:
    print('[-] Unsupported Platform currently for ctypes dll method. Only [Windows and Linux] is working')
    sys.exit()

miz.privatekey_to_address.argtypes = [ctypes.c_int, ctypes.c_bool, ctypes.c_char_p]
miz.privatekey_to_address.restype = ctypes.c_void_p
miz.free_memory.argtypes = [ctypes.c_void_p]
miz.init_secp256_lib()

def privatekey_to_address(addr_type, iscompressed, pvk_int):
    if pvk_int < 0: pvk_int = N+pvk_int
    pass_int_value = fl(pvk_int).encode('utf8')
    res = miz.privatekey_to_address(addr_type, iscompressed, pass_int_value)
    addr = (ctypes.cast(res, ctypes.c_char_p).value).decode('utf8')
    miz.free_memory(res)
    return addr
def fl(sstr, length=64):
    if type(sstr) == int: fixed = hex(sstr)[2:].zfill(length)
    return fixed

lines = '=' * 80
min_p = 1
max_p = 904625697166532776746648320380374280100293470930272690489102837043110636675
def RandomInteger(minN, maxN):
    return random.randrange(minN, maxN)
    
def load_settings():
    global start_range, end_range, stop, add, offline_scan
    load_addresses('puzzle.txt')
    addr_count = len(add)
    print('  Mizogg.co.uk 2023  Bitty Version 3 ' )
    print(f'  [{timing}]  Total Bitcoin addresses Loaded and Checking  : ' + str(addr_count))
    print(f' {lines}\n  A private key is basically just a number between 1Bit and 256Bits. \n  This Program generates keys for all of those numbers, \n  128 keys 256 Addresses Per Scan. \n  To get Started Pick a Option Highlighed in Red \n {lines}')
    print(f'''
[red]  1.[/red] Search By Page Ranges
[red]  2.[/red] Search By DEC Ranges
[red]  3.[/red] Search By HEX Ranges
[red]  4.[/red] Search By BIT Ranges (ERROR with RANGES)
''')
    startingscan = int(input(' Pick a Option Highlighed in Red ->  -> '))
    if startingscan == 1:
        print ('[green]Puzzle66 = 576460752303423489 1152921504606846977 [/green]')
        print('[yellow]  Start search... Pick Page to start \n( Min= 1 Max= 904625697166532776746648320380374280100293470930272690489102837043110636674 )  [/yellow] ')
        start_range = int(input(' starting  Page ->  -> '))
        print(f'[yellow]  Stop search... Pick Page to Stop \n( Min= 2 Max= {max_p} )  [/yellow] ')
        end_range = int(input('  Stop Page -> -> '))
    
    if startingscan == 2:
        print ('[green]Puzzle66 = 36893488147419103232 73786976294838206463 [/green]')
        print('[yellow]  Start search... Pick DEC to start \n( Min= 1 Max= 115792089237316195423570985008687907852837564279074904382605163141518161494335 )  [/yellow] ')
        startdec = (input(' starting  DEC ->  -> '))
        num = int(startdec, 10)
        num = num // 128
        start_range = num + 1
        print(f'[yellow]  Stop search... Pick DEC to Stop \n(Max= 115792089237316195423570985008687907852837564279074904382605163141518161494336 )  [/yellow] ')
        enddec = (input('  Stop DEC -> -> '))
        num1 = int(enddec, 10)
        num1 = num1 // 128
        end_range = num1 + 1
    
    if startingscan == 3:
        print ('[green]Puzzle66 = 20000000000000000 3ffffffffffffffff [/green]')
        print('[yellow]  Start search... Pick HEX to start \n( Min= 1 Max= fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364140 )  [/yellow] ')
        starthex = str(input(' starting  HEX ->  -> '))
        num = int(starthex, 16)
        num = num // 128
        start_range = num + 1
        print(f'[yellow]  Stop search... Pick HEX to Stop \n(Max= fffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141 )  [/yellow] ')
        endhex = str(input('  Stop HEX -> -> '))
        num1 = int(endhex, 16)
        num1 = num1 // 128
        end_range = num1 + 1
    
    if startingscan == 4:
        print('[yellow]  Start search... Pick BITS to start \n( Min= 1 Max= 255 )  [/yellow] ')
        startbit = int(input(' starting  BIT ->  -> '))
        startbit = str(startbit**2)
        num = int(startbit, 10)
        num = num // 128
        start_range = num + 1
        print(f'[yellow]  Stop search... Pick BITS to Stop \n(Max= 256 )  [/yellow] ')
        endbit = int(input('  Stop BITS -> -> '))
        endbit = str(endbit**2)
        num1 = int(endbit, 10)
        num1 = num1 // 128
        end_range = num1 + 1
    print('[green]Do you want to perform an offline scan? Offline FASTER (y/n) -> [/green]')
    offline_scan = input('(y/n) ')

def load_addresses(filename):
    global addresses, add
    print(f'\n  [{timing}] Creating database from \'{filename}\' ...Please Wait...')
    with open(filename) as file:
        add = file.read().split()

def get_keys(page):
    global addresses, found, add, actual_page, offline_scan
    actual_page = page
    max = max_p
    stride = 1
    num = int(page, 10)
    previous = num - 1
    if previous == 0:
        previous = 1
    next = num + stride
    if next > max:
        next = max

    startPrivKey = (num - 1) * 128 + 1

    for i in range(0, 128):
        dec = int(startPrivKey)
        starting_key_hex = hex(startPrivKey)[2:].zfill(64)
        if startPrivKey == 115792089237316195423570985008687907852837564279074904382605163141518161494336:
            break
        if offline_scan == 'y':
            caddr = privatekey_to_address(0, True, dec).strip()
            uaddr = privatekey_to_address(0, False, dec).strip()
            if caddr in add:
                found += 1
                output = f'''\n
      Found @ [{timing}]
    {lines}
      : Private Key Page : {num}
    {lines}
      : Private Key DEC : {startPrivKey}
    {lines}
      : Private Key HEX : {starting_key_hex}
    {lines}
      : BTC Address Compressed : {caddr}
    {lines}
    '''
                print(output)
                with open('foundcaddr.txt', 'a', encoding='utf-8') as f:
                    f.write(output)

            if uaddr in add:
                found += 1
                output = f'''\n
      Found @ [{timing}]
    {lines}
      : Private Key Page : {num}
    {lines}
      : Private Key DEC : {startPrivKey}
    {lines}
      : Private Key HEX : {starting_key_hex}
    {lines}
      : BTC Address Uncompressed : {uaddr}
    {lines}
    '''
                print(output)
                with open('founduaddr.txt', 'a', encoding='utf-8') as f:
                    f.write(output)
        if offline_scan == 'n':
            caddr = privatekey_to_address(0, True, dec).strip()
            url = 'https://btcbook.guarda.co/api/v1/address/'+ caddr
            http_obj = httplib2.Http()
            response, content = http_obj.request(url, 'GET')
            if response.status == 200:
                data = json.loads(content)
                balance = (data['balance'])
                totalReceived = (data['totalReceived'])
                totalSent = (data['totalSent'])
                txs = (data['txApperances'])
                Info = f'''Wallet Address {caddr} \nBalance = {balance} Total Received = {totalReceived} Total Sent = {totalSent} Transactions = {txs}\n'''
                print (Info)
                if int(txs) > 0:
                    print (Info)
                    found += 1
                    with open("Transactions.txt", "a") as file:
                        file.write(f"DEC Key: {startPrivKey} \nHEX Key: {starting_key_hex} \n{Info}")
                if float(balance) > 0 :
                    print (Info)
                    found += 1
                    with open("winner.txt", "a") as file:
                        file.write(f"DEC Key: {startPrivKey} \nHEX Key: {starting_key_hex} \n{Info}")
            else:
                print('Error occurred:', response.status)
                return None
        startPrivKey += 1
    addresses.clear()

def search(typeScan):
    global start_time, total_tested_keys, start_range, end_range, stop, SequentialTypes, jump_size
    while stop == False:
        try:
            if typeScan == typeScans[0]:
                try:
                    jump_size_scan = jump_size
                    i = start_range
                    while i <= end_range:
                        get_keys(str(i))
                        total_tested_keys += 128
                        i += jump_size_scan
                except Exception as e:
                    print(str(e))
                stop = True
            elif typeScan == typeScans[1]:
                try:
                    jump_size_scan = jump_size
                    i = end_range
                    while i >= start_range:
                        get_keys(str(i))
                        total_tested_keys += 128
                        i -= jump_size_scan
                except Exception as e:
                    print(str(e))
                stop = True
            elif typeScan == typeScans[2]:
                for i in range(start_range, end_range):
                    try:
                        get_keys(str(i))
                        total_tested_keys += 128
                    except Exception as e:
                        print(str(e))
                stop = True
            elif typeScan == typeScans[3]:
                for i in reversed(range(start_range, end_range)):
                    try:
                        get_keys(str(i))
                        total_tested_keys += 128
                    except Exception as e:
                        print(str(e))
                stop = True
            elif typeScan == typeScans[4]:
                while True:
                    try:
                        page = str(RandomInteger(start_range, end_range))
                        get_keys(page)
                        total_tested_keys += 128
                    except Exception as e:
                        print(str(e))
                        break
            elif typeScan == typeScans[5]:
                try:
                    for i in range(start_range, end_range):
                        if i % 2 == 0:
                            get_keys(str(i))
                            total_tested_keys += 128
                except Exception as e:
                    print(str(e))
                stop = True
            elif typeScan == typeScans[6]:
                try:
                    for i in reversed(range(start_range, end_range)):
                        if i % 2 == 0:
                            get_keys(str(i))
                            total_tested_keys += 128
                except Exception as e:
                    print(str(e))
                stop = True
            elif typeScan == typeScans[7]:
                try:
                    for i in range(start_range, end_range):
                        if i % 2 != 0:
                            get_keys(str(i))
                            total_tested_keys += 128
                except Exception as e:
                    print(str(e))
                stop = True
            elif typeScan == typeScans[8]:
                try:
                    for i in reversed(range(start_range, end_range)):
                        if i % 2 != 0:
                            get_keys(str(i))
                            total_tested_keys += 128
                except Exception as e:
                    print(str(e))
                stop = True
            else:
                break
        except Exception as e:
            print(str(e))

def search_stats():
    global start_time, total_tested_keys, typeScan, stop, actual_page
    while stop == False:
        now = time.time()
        since_start = now - start_time
        now1 = datetime.now()
        timing = now1.strftime("%H:%M:%S")
        try:
            keys_per_second = int(total_tested_keys / since_start)
            addresses_per_second = keys_per_second * 2
        except:
            keys_per_second = 0
            addresses_per_second = keys_per_second * 2
        dots = random.choice(['    ', '.   ', '..  ', '... ', '....'])
        print(' [ %s ]  Searching %s (%s Addresses/s | %s Keys/s) | MODE: %s | Actual Page: %s | Found : %s' % (
        timing, dots, addresses_per_second, keys_per_second, typeScan, actual_page, found), end='\r')
    print(f'\n{lines}\n  Finished Scanning Please Try Again \n')

if __name__ == '__main__':
    addresses = list()
    add = set()
    found = start_rang = end_range = total_tested_keys = 0
    stop = False
    total_addresses = []
    start_time = time.time()
    now = datetime.now()
    timing = now.strftime("%H:%M:%S")
    settings_config = {}
    load_settings()
    if stop == False:
        typeScans = ['Range + Jump [Forward]', 'Range + Jump [Backward]', 'Sequential [Forward]', 'Reverse  [Backward]', 'Random', 'Odd Numbers [Forward]','Odd Numbers [Backward]', 'Even Numbers [Forward]', 'Even Numbers [Backward]']
        scanN = 0
        print('[purple]  Please choose how to scan: \n[/purple]')
        for scan in typeScans:
            print(' ', scanN, '=>', scan)
            scanN += 1

        inputUserTypeScan = -1
        while inputUserTypeScan < 0 or inputUserTypeScan > len(typeScans):
            inputUserTypeScan = int(input('\n  Scan Type Number : '))

        typeScan = typeScans[inputUserTypeScan]
        if typeScan == typeScans[0]:
            print('[yellow]  Pick how many Wallet to Jump/Skip/Magnitude/Stride  [/yellow] ')
            jump_size = int(input('Magnitude Jump Stride -> '))
            nThreads = 1
            print(f''''\n
  Starting {typeScan}  @ [{timing}]
{lines}
  Searching Start {start_range}
{lines}
  End {end_range}
{lines}
  Magnitude/Jump {jump_size}
{lines}''')
        
        elif typeScan == typeScans[1]:
            print('[yellow]  Pick how many Wallet to Jump/Skip/Magnitude/Stride  [/yellow] ')
            jump_size = int(input('Magnitude Jump Stride -> '))
            nThreads = 1
            print(f''''\n
  Starting {typeScan}  @ [{timing}]
{lines}
  Searching Start {start_range}
{lines}
  End {end_range}
{lines}
  Magnitude/Jump {jump_size}
{lines}''')
        
        elif typeScan == typeScans[4]:
            nThreads = int(input('\n  How many Threads 2? 10? 100? or try more : '))
            print(f'''\n
  Starting {typeScan} With [{nThreads}] Threads  @ [{timing}]
{lines}
  Searching Start {start_range}
{lines}
  End {end_range}
{lines}
''')
        else:
            nThreads = 1
            print(f''''\n
  Starting {typeScan}  @ [{timing}]
{lines}
  Searching Start {start_range}
{lines}
  End {end_range}
{lines}''')

        for i in range(nThreads):
            x = threading.Thread(target=search, args=(typeScan,))
            x.start()

        x = threading.Thread(target=search_stats)
        x.start()
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread
from multiprocessing import cpu_count
from time import sleep
import requests
import random
from rich import print
from rich.panel import Panel
from rich.console import Console
import platform
import os
import sys
import ctypes
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

console = Console()
console.clear()
ctypes.windll.kernel32.SetConsoleTitleW('Mizogg Corp.(blockstream.py)')
mizogg= '''[red]
              ___            ___  
             (o o)          (o o) 
            (  V  ) MIZOGG (  V  )
            --m-m------------m-m--
[/red]'''
print(mizogg)

threads_count = int(input('\n  How many Threads 2? 10? 100? or try more : '))
threads = list()
print ('[green]Puzzle66 = 36893488147419103232 73786976294838206463 [/green]')
print('[yellow]  Start search... Pick DEC to start \n( Min= 1 Max= 115792089237316195423570985008687907852837564279074904382605163141518161494335 )  [/yellow] ')
START=int(input(' starting  DEC ->  -> '))
print(f'[yellow]  Stop search... Pick DEC to Stop \n(Max= 115792089237316195423570985008687907852837564279074904382605163141518161494336 )  [/yellow] ')
STOP=int(input('  Stop DEC -> -> '))

def check_balance(addr, dec, HEX, count, count1):
    try:
        response = requests.get("https://blockstream.info/api/address/" + str(addr))
        totalReceived = response.json()['chain_stats']['funded_txo_sum']
        totalSent = response.json()['chain_stats']['spent_txo_sum']
        txs = response.json()['chain_stats']['funded_txo_count']
        balance = totalReceived - totalSent
        Info = f'''Wallet Address {addr} \nBalance = {balance} Total Received = {totalReceived} Total Sent = {totalSent} Transactions = {txs}\n'''
        ctypes.windll.kernel32.SetConsoleTitleW('Total : ' + str(count1) + ' ₿al : ' + str(balance) + ' TXS : ' + str(txs))
        running_print_main = str('[gold1 on grey7]\nScan:[light_goldenred1]'+str(count) +'[green] Balance :[white]'+str(balance) +'[green] Transactions :[white]'+str(txs) +'[red][*]Dec :[*][/red][purple] >> ' + str(dec)[1:10] +'[/][gold1 on grey15] Addr: '+'[white] '+str(addr)+'[/]')
        style = "gold1 on grey7"
        console.print(Panel(str(running_print_main) , title = "[white]\n mizogg.co.uk powerbalcolour.py [/]" , subtitle = "[green_yellow blink] Good Luck Happy Hunting [/]" , style = "green") , style = style , justify = "full")
        if txs > 0:
            length = len(bin(dec))
            length -=2
            running_print_trans = str(
            '[green on grey15]Total Checked: '+'[orange_red1]'+str(count)+'[/][gold1 on grey15] '+'[/][gold1] TX: '+'[/][aquamarine1]'+str(txs)+'[gold1]  BAL:[aquamarine1]'+str(balance)+'\n[/][gold1 on grey15]Addr: '+'[white] '+str(addr)+'[/][green] \nDec => [/green] ' +str(dec) + '[green]Bits = [/green]'+str(length) + '[green]\n HEX => [/green]'+ str(HEX))
            style = "gold1 on grey11"
            console.print(Panel(str(running_print_trans) , title = "[white]Found Wallet WITH Transactions[/]" , subtitle = "[green_yellow blink] Close One Active Wallet Found ! [/]" , style = "green") , style = style , justify = "full")
            with open("Transactions.txt", "a") as file:
                file.write(f'DEC Key: {dec} \nHEX Key: {HEX} \n{Info}')
                file.close()
                sleep(5)
                
        if balance > 0 :
            length = len(bin(dec))
            length -=2
            running_print_Balance = str(
            '[green on grey15]Total Checked: '+'[orange_red1]'+str(count)+'[/][gold1] TX: '+'[/][aquamarine1]'+str(txs)+'[gold1]  BAL:[aquamarine1]'+str(balance)+'\n[/][gold1 on grey15]Addr: '+'[white] '+str(addr) +'[/][green] \nDec => [/green] ' +str(dec) + '[green]Bits = [/green]'+str(length) + '[green]\n HEX => [/green]'+ str(HEX))
            style = "gold1 on grey11"
            console.print(Panel(str(running_print_Balance) , title = "[white]Found Wallet WITH Balance [/]" , subtitle = "[green_yellow blink] WOW OMG YOU HAVE FOUND ! [/]" , style = "green") , style = style , justify = "full")
            with open("winner.txt", "a") as file:
                file.write(f'DEC Key: {dec} \nHEX Key: {HEX} \n{Info}')
                file.close()
                sleep(5)

    except TypeError:
        print("Oops! There was some kind of error, don't be afraid, everything is written in errors.txt")
        with open("errors.txt", "a") as errors:
            errors.write(f"Dec: {dec}\nPrivateKey: {HEX}\n")
        sleep(5)
        check_balance(addr, dec, HEX, count, count1)

def BTC_generate():
    count=count1=0
    while True:
        dec =int(random.randrange(START, STOP))
        uaddr = privatekey_to_address(0, False, dec)
        caddr = privatekey_to_address(0, True, dec)
        HEX = "%064x" % dec
        check_balance(caddr, dec, f"{HEX}", count, count1)
        count+=1
        check_balance(uaddr, dec, f"{HEX}", count, count1)
        count+=1
        count1+=2*threads_count

for _ in range(threads_count):
    thread = Thread(target=BTC_generate)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
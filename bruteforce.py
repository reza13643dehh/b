import secp256k1 as ice
from multiprocessing import cpu_count, Process
from lxml import html
import requests
from time import sleep
import random
from bloomfilter import BloomFilter, ScalableBloomFilter, SizeGrowthRate
from rich import print

with open('puzzle.bf', "rb") as fp:
    bloom_filterbtc = BloomFilter.load(fp)
addr_count = len(bloom_filterbtc)    
print('Total Bitcoin Addresses Loaded and Checking : ',str (addr_count))  

max_p = 115792089237316195423570985008687907852837564279074904382605163141518161494336

def RandomInteger(minN, maxN):
    return random.randrange(minN, maxN)

# random bruteforce
# Will randomly generate addresses
def Random_Bruteforce(r, sep_p):
    print(f'Instance: {r + 1} - Generating random addresses...')
    while True:
        dec =int(RandomInteger(1, 115792089237316195423570985008687907852837564279074904382605163141518161494336))
        caddr = ice.privatekey_to_address(0, True, dec)
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: {r + 1} - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        else:
            dots = random.choice(["   ", ".  ", ".. ", "...", "...."])
            print("  Searching %s " % (dots), end="\r")


# random bruteforce output
def Debug_Random_Bruteforce(r, sep_p):
    print(f'Instance: {r + 1} - Generating random addresses random bruteforce with output...')
    while True:
        dec =int(RandomInteger(1, 115792089237316195423570985008687907852837564279074904382605163141518161494336))
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: {r + 1} - Generated: {caddr}')
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: {r + 1} - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')


# traditional bruteforce (slowest)
# Will try every INT from 0 to max possible
def Sequential_Bruteforce(r, sep_p):
    sint = sep_p * r if sep_p * r != 0 else 1
    mint = sep_p * (r + 1)
    print(f'Instance: {r + 1} - Generating addresses Sequential_Bruteforce ...')
    while sint < mint:
        dec = int(sint)
        caddr = ice.privatekey_to_address(0, True, dec)
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: {r + 1} - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        else:
            dots = random.choice(["   ", ".  ", ".. ", "...", "...."])
            print("  Searching %s " % (dots), end="\r")
        sint += 1
        
    print(f'Instance: {r + 1}  - Done')


# online bruteforce (randomized)
def Online_Bruteforce(r, sep_p):
    print(f'Instance: {r + 1} - Generating random addresses online bruteforce (randomized) ...')
    while True:
        dec =int(RandomInteger(1, 115792089237316195423570985008687907852837564279074904382605163141518161494336))
        caddr = ice.privatekey_to_address(0, True, dec)
        HEX = "%064x" % dec
        wifc = ice.btc_pvk_to_wif(HEX)
        ammountbtc = '0 BTC'
        try:
            urlblock = "http://35.237.92.187/address/"+ caddr
            respone_block = requests.get(urlblock)
            byte_string = respone_block.content
            source_code = html.fromstring(byte_string)
            received_id = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[1]/td[2]'
            receivedid = source_code.xpath(received_id)
            totalReceived = str(receivedid[0].text_content())
            sent_id = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
            sentid = source_code.xpath(sent_id)
            totalSent = str(sentid[0].text_content())
            balance_id = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[3]/td[2]'
            balanceid = source_code.xpath(balance_id)
            balance = str(balanceid[0].text_content())
            txs_id = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
            txsid = source_code.xpath(txs_id)
            txs = str(txsid[0].text_content())
            if int(txs) > 0:
            #  if str(balance) != ammountbtc:
                length = len(bin(dec))
                length -=2
                print ('[green on grey15]Addr: '+'[orange_red1]'+str(caddr)+'[/][gold1] Balance: '+'[/][aquamarine1]'+str(balance)+'[gold1]  Transactions:[aquamarine1]'+str(txs)+'\n[/][gold1 on grey15]WIF : '+'[white] ' +str(wifc)+'[/][green] \nDec => [/green] ' +str(dec) + '[green]Bits = [/green]'+str(length) + '[green]\n HEX => [/green]'+ str(HEX)+'[/]')
                with open('found.txt', 'a') as result:
                    result.write(f'DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
                print(f'Instance: {r + 1} - Added address to found.txt')
                sleep(2.5)
            else:
                print ('[gold1 on grey7]\nAddr:[light_goldenred1]'+str(caddr) +'[green] Balance :[white]'+str(balance) +'[green] Transactions :[white]'+str(txs) +'[red]\n[*]Dec :[*][/red][purple] >> ' + str(dec) +'[/][gold1 on grey15] \n[*]HEX:[*] '+'[white] '+str(HEX)+'[/]')
                print(f'Instance: {r + 1} - Generated: {caddr} balance: {balance}')
        except ValueError:
            print(f'Instance: {r + 1} - ValueError address: {caddr} wif: {wifc}')
            sleep(2.5)
            continue


def Sequential_Online_Bruteforce(r, sep_p):
    Start= 1
    Stop=115792089237316195423570985008687907852837564279074904382605163141518161494336
    print(f'Instance: {r + 1} - Generating Sequential addresses online bruteforce (Sequential) EDIT LINE 130 for START ...')
    sleep(1.0)
    while Start < Stop:
        dec = int(Start)
        caddr = ice.privatekey_to_address(0, True, dec)
        HEX = "%064x" % dec
        wifc = ice.btc_pvk_to_wif(HEX)
        ammountbtc = '0 BTC'
        try:
            urlblock = "http://35.237.92.187/address/"+ caddr
            respone_block = requests.get(urlblock)
            byte_string = respone_block.content
            source_code = html.fromstring(byte_string)
            received_id = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[1]/td[2]'
            receivedid = source_code.xpath(received_id)
            totalReceived = str(receivedid[0].text_content())
            sent_id = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[2]/td[2]'
            sentid = source_code.xpath(sent_id)
            totalSent = str(sentid[0].text_content())
            balance_id = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[3]/td[2]'
            balanceid = source_code.xpath(balance_id)
            balance = str(balanceid[0].text_content())
            txs_id = '/html/body/main/div/div[2]/div[1]/table/tbody/tr[4]/td[2]'
            txsid = source_code.xpath(txs_id)
            txs = str(txsid[0].text_content())
            if int(txs) > 0:
            #  if str(balance) != ammountbtc:
                length = len(bin(dec))
                length -=2
                print('[green on grey15]Addr: '+'[orange_red1]'+str(caddr)+'[/][gold1] Balance: '+'[/][aquamarine1]'+str(balance)+'[gold1]  Transactions:[aquamarine1]'+str(txs)+'\n[/][gold1 on grey15]WIF : '+'[white] ' +str(wifc)+'[/][green] \nDec => [/green] ' +str(dec) + '[green]Bits = [/green]'+str(length) + '[green]\n HEX => [/green]'+ str(HEX)+'[/]')
                with open('found.txt', 'a') as result:
                    result.write(f'DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
                print(f'Instance: {r + 1} - Added address to found.txt')
                sleep(2.5)
            else:
                print('[gold1 on grey7]\nAddr:[light_goldenred1]'+str(caddr) +'[green] Balance :[white]'+str(balance) +'[green] Transactions :[white]'+str(txs) +'[red]\n[*]Dec :[*][/red][purple] >> ' + str(dec) +'[/][gold1 on grey15] \n[*]HEX:[*] '+'[white] '+str(HEX)+'[/]')
                print(f'Instance: {r + 1} - Generated: {caddr} balance: {balance}')
            Start += 1
        except ValueError:
            print(f'Instance: {r + 1} - ValueError address: {caddr} wif: {wifc}')
            sleep(2.5)
            continue

# traditional bruteforce output
def Debug_Sequential_Bruteforce(r, sep_p):
    sint = sep_p * r if sep_p * r != 0 else 1
    mint = sep_p * (r + 1)
    print(f'Instance: {r + 1} - Generating addresses Sequential Bruteforce ...')
    while sint < mint:
        dec = int(sint)
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: {r + 1} - Generated: {caddr}')
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: {r + 1} - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        sint += 1
    print(f'Instance: {r + 1}  - Done')


# optimized traditional bruteforce
# Will try every INT between 10**75 and max possibility.
# This methode is based on the best practice to get the safest address possible.
def Optimized_Sequential_Bruteforce(r, sep_p):
    sint = (sep_p * r) + 10 ** 75 if r == 0 else (sep_p * r)
    mint = (sep_p * (r + 1))
    print(f'Instance: {r + 1} - Generating addresses...')
    while sint < mint:
        dec = int(sint)
        caddr = ice.privatekey_to_address(0, True, dec)
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: {r + 1} - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        else:
            dots = random.choice(["   ", ".  ", ".. ", "...", "...."])
            print("  Searching %s " % (dots), end="\r")
        sint += 1
    print(f'Instance: {r + 1}  - Done')


# optimized traditional bruteforce ouput
def Debug_Optimized_Sequential_Bruteforce(r, sep_p):
    sint = (sep_p * r) + 10 ** 75 if r == 0 else (sep_p * r)
    mint = (sep_p * (r + 1))
    print(f'Instance: {r + 1} - Generating addresses...')
    while sint < mint:
        dec = int(sint)
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: {r + 1} - Generated: {caddr}')
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: {r + 1} - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        sint += 1
    print(f'Instance: {r + 1}  - Done')


def main():
    # set bruteforce mode
    mode = (None, Random_Bruteforce, Sequential_Bruteforce, Optimized_Sequential_Bruteforce, Online_Bruteforce, Sequential_Online_Bruteforce, Debug_Random_Bruteforce, Debug_Sequential_Bruteforce, Debug_Optimized_Sequential_Bruteforce)

    # print menu
    menu_string = 'Select bruteforce mode:\n'
    for count, function in enumerate(mode):
        try:
            if 'debug' in function.__name__:
                menu_string += f'{count} - {function.__name__} (Prints output)\n'
            else:
                menu_string += f'{count} - {function.__name__}\n'
        except AttributeError:
            menu_string += f'{count} - Exit\n'
    print(menu_string)

    try:
        choice = int(input('> '))
        if choice == 4:
            option = 4
            cpu_cores = 1
        elif choice != 0:
            print(f'How many cores do you want to use ({cpu_count()} available)')
            cpu_cores = int(input('> '))
            cpu_cores = cpu_cores if 0 < cpu_cores < cpu_count() else cpu_count()
            option = choice if 0 < choice <= len(mode) - 1 else 0
        else:
            option = 0
            cpu_cores = 0
    except ValueError:
        option = 0
        cpu_cores = 0

    print(f'Starting bruteforce instances in mode: {mode[option].__name__} with {cpu_cores} core(s)\n')

    instances = []
    for i in range(cpu_cores):
        instance = Process(target=mode[option], args=(i, round(max_p / cpu_cores)))
        instances.append(instance)
        instance.start()

    for instance in instances:
        instance.join()

        print('Stopping...')


if __name__ == '__main__':
    main()

import secp256k1 as ice
import random
from bloomfilter import BloomFilter, ScalableBloomFilter, SizeGrowthRate
import dask

    
with open('puzzle.bf', "rb") as fp:
    bloom_filterbtc = BloomFilter.load(fp)
addr_count = len(bloom_filterbtc)    
print('Total Bitcoin Addresses Loaded and Checking : ',str (addr_count))  

max_p = 115792089237316195423570985008687907852837564279074904382605163141518161494336


def RandomInteger(minN, maxN):
    return random.randrange(minN, maxN)

@dask.delayed
def Random_Bruteforce(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')


@dask.delayed
def Random_Bruteforce1(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Random_Bruteforce Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce1 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce1 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')


@dask.delayed
def Random_Bruteforce2(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Random_Bruteforce1 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce2 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce2 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')


@dask.delayed
def Random_Bruteforce3(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Random_Bruteforce3 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce3 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce3 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')


@dask.delayed
def Random_Bruteforce4(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Random_Bruteforce4 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce4 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce4 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')


@dask.delayed
def Random_Bruteforce5(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Random_Bruteforce5 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce5 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce5 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')


@dask.delayed
def Random_Bruteforce6(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Random_Bruteforce6 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce6 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce6 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')


@dask.delayed
def Random_Bruteforce7(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Random_Bruteforce7 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce7 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce7 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')


@dask.delayed
def Random_Bruteforce8(startdec, stopdec):
    while True:
        
        dec =int(RandomInteger(startdec, stopdec))
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Random_Bruteforce8 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Random_Bruteforce8 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Random_Bruteforce8 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')


@dask.delayed
def Sequential_Bruteforce(startdec, startdec1):
    START = startdec
    STOP = startdec1
    print(f'Instance:  - Generating addresses Sequential_Bruteforce ... \n Start = {START} \n Stop = {STOP}')
    while START < STOP:
        dec = int(START)
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Sequential_Bruteforce Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Sequential_Bruteforce - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Sequential_Bruteforce \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        START += 1
        
    print(f'Instance: Sequential_Bruteforce - Done')
    

@dask.delayed
def Sequential_Bruteforce1(startdec1, startdec2):
    START = startdec1
    STOP = startdec2
    print(f'Instance:  - Generating addresses Sequential_Bruteforce1 ... \n Start = {START} \n Stop = {STOP}')
    while START < STOP:
        dec = int(START)
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Sequential_Bruteforce1 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Sequential_Bruteforce1 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Sequential_Bruteforce1 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        START += 1
        
    print(f'Instance: Sequential_Bruteforce1 - Done')
    

@dask.delayed
def Sequential_Bruteforce2(startdec2, startdec3):
    START = startdec2
    STOP = startdec3
    print(f'Instance:  - Generating addresses Sequential_Bruteforce2 ... \n Start = {START} \n Stop = {STOP}')
    while START < STOP:
        dec = int(START)
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Sequential_Bruteforce2 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Sequential_Bruteforce2 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Sequential_Bruteforce2 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        START += 1
        
    print(f'Instance: Sequential_Bruteforce2 - Done')


@dask.delayed
def Sequential_Bruteforce3(startdec3, startdec4):
    START = startdec3
    STOP = startdec4
    print(f'Instance:  - Generating addresses Sequential_Bruteforce3 ... \n Start = {START} \n Stop = {STOP}')
    while START < STOP:
        dec = int(START)
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Sequential_Bruteforce3 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Sequential_Bruteforce3 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Sequential_Bruteforce3 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        START += 1
        
    print(f'Instance: Sequential_Bruteforce3 - Done')
    

@dask.delayed
def Sequential_Bruteforce4(startdec4, startdec5):
    START = startdec4
    STOP = startdec5
    print(f'Instance:  - Generating addresses Sequential_Bruteforce4 ... \n Start = {START} \n Stop = {STOP}')
    while START < STOP:
        dec = int(START)
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Sequential_Bruteforce4 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Sequential_Bruteforce4 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Sequential_Bruteforce4 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        START += 1
        
    print(f'Instance: Sequential_Bruteforce4 - Done')


@dask.delayed
def Sequential_Bruteforce5(startdec5, startdec6):
    START = startdec5
    STOP = startdec6
    print(f'Instance:  - Generating addresses Sequential_Bruteforce5 ... \n Start = {START} \n Stop = {STOP}')
    while START < STOP:
        dec = int(START)
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Sequential_Bruteforce5 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Sequential_Bruteforce5 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Sequential_Bruteforce5 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        START += 1
        
    print(f'Instance: Sequential_Bruteforce5 - Done')


@dask.delayed
def Sequential_Bruteforce6(startdec6, startdec7):
    START = startdec6
    STOP = startdec7
    print(f'Instance:  - Generating addresses Sequential_Bruteforce6 ... \n Start = {START} \n Stop = {STOP}')
    while START < STOP:
        dec = int(START)
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Sequential_Bruteforce6 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Sequential_Bruteforce6 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Sequential_Bruteforce6 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        START += 1
        
    print(f'Instance: Sequential_Bruteforce6 - Done')


@dask.delayed
def Sequential_Bruteforce7(startdec7, startdec8):
    START = startdec7
    STOP = startdec8
    print(f'Instance:  - Generating addresses Sequential_Bruteforce7 ... \n Start = {START} \n Stop = {STOP}')
    while START < STOP:
        dec = int(START)
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Sequential_Bruteforce7 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Sequential_Bruteforce7 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Sequential_Bruteforce7 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        START += 1
        
    print(f'Instance: Sequential_Bruteforce7 - Done')


@dask.delayed
def Sequential_Bruteforce8(startdec8, stopdec):
    START = startdec8
    STOP = stopdec
    print(f'Instance:  - Generating addresses Sequential_Bruteforce8 ... \n Start = {START} \n Stop = {STOP}')
    while START < STOP:
        dec = int(START)
        caddr = ice.privatekey_to_address(0, True, dec)
        print(f'Instance: Sequential_Bruteforce8 Address Compressed: {caddr} ', end="\r")
        if caddr in bloom_filterbtc:
            HEX = "%064x" % dec
            wifc = ice.btc_pvk_to_wif(HEX)
            length = len(bin(dec))
            length -=2
            print(f'Instance: Sequential_Bruteforce8 - Found: {caddr}')
            print(f'WINNER WINNER Check found.txt \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
            with open('found.txt', 'a') as result:
                result.write(f'Instance: Sequential_Bruteforce8 \n DEC Key: {dec} bits {length} \n HEX Key: {HEX} \nBTC Address Compressed: {caddr} \nWIF Compressed: {wifc}\n')
        START += 1
        
    print(f'Instance: Sequential_Bruteforce8 - Done')

    
def main():

    # set bruteforce mode
    mode = (None, Random_Bruteforce, Sequential_Bruteforce)

    # print menu
    menu_string = 'Select bruteforce mode:\n'
    for count, function in enumerate(mode):
        try:
            menu_string += f'{count} - {function.__name__}\n'
        except AttributeError:
            menu_string += f'{count} - Exit\n'
    print('All scans are offline and require BloomFilter Database of Bitcoin Addresses')
    print(menu_string)


    choice = int(input('> '))
    if choice == 1:
        startdec = int(input("start range Min bytes 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 ->  "))
        stopdec = int(input("stop range Max bytes 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
        x = dask.delayed(Random_Bruteforce(startdec, stopdec))
        y = dask.delayed(Random_Bruteforce1(startdec, stopdec))
        z = dask.delayed(Random_Bruteforce2(startdec, stopdec))
        x1 = dask.delayed(Random_Bruteforce3(startdec, stopdec))
        y1 = dask.delayed(Random_Bruteforce4(startdec, stopdec))
        z1 = dask.delayed(Random_Bruteforce5(startdec, stopdec))
        x2 = dask.delayed(Random_Bruteforce6(startdec, stopdec))
        y2 = dask.delayed(Random_Bruteforce7(startdec, stopdec))
        z2 = dask.delayed(Random_Bruteforce8(startdec, stopdec))
        dask.compute(x,y,z,x1,y1,z1,x2,y2,z2)
    
    
    if choice == 2:
        start=int(input("start range Min bytes 1-115792089237316195423570985008687907852837564279074904382605163141518161494335 ->  "))
        stop=int(input("stop range Max bytes 115792089237316195423570985008687907852837564279074904382605163141518161494336 -> "))
        rangediv= 6
        remainingtotal=stop-start
        div = round(remainingtotal / rangediv)
        startdec= start
        
        percent1 = div * 2
        startdec1= start+percent1
        
        percent2 = div * 3
        startdec2= start+percent2
        
        percent3 = div * 4
        startdec3= start+percent3
        
        percent4 = div * 5
        startdec4= start+percent4
        
        percent5 = div * 6
        startdec5= start+percent5
        
        percent6 = div * 7
        startdec6= start+percent6
        
        percent7 = div * 8
        startdec7= start+percent7
        
        percent8 = div * 9
        startdec8= start+percent8
        
        stopdec = stop
        
        x = dask.delayed(Sequential_Bruteforce(startdec, startdec1))
        y = dask.delayed(Sequential_Bruteforce1(startdec1, startdec2))
        z = dask.delayed(Sequential_Bruteforce2(startdec2, startdec3))
        x1 = dask.delayed(Sequential_Bruteforce3(startdec3, startdec4))
        y1 = dask.delayed(Sequential_Bruteforce4(startdec4, startdec5))
        z1 = dask.delayed(Sequential_Bruteforce5(startdec5, startdec6))
        x2 = dask.delayed(Sequential_Bruteforce6(startdec6, startdec7))
        y2 = dask.delayed(Sequential_Bruteforce7(startdec7, startdec8))
        z2 = dask.delayed(Sequential_Bruteforce8(startdec8, stopdec))
        dask.compute(x,y,z,x1,y1,z1,x2,y2,z2)

if __name__ == '__main__':
    main()
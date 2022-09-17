# bitcoin-bruteforce [![CodeFactor](https://www.codefactor.io/repository/github/meesvw/bitcoin-bruteforce/badge)](https://www.codefactor.io/repository/github/meesvw/bitcoin-bruteforce)
Bitcoin public address brute force written in Python with simplicity and speed in mind

## Functions
- Compare multiple wallets to increase cracking speed
- Divide workload over multiple CPU cores
- Multiple bruteforce functions
- Online wallet lookup (OBF)
- Print generation output

### Upcoming features
- GPU optimization (NVIDIA only)
- Cython optimization
- Automatic payout system
- Save bruteforce progress
- Create wallet database
- See hash rate

## Setup

**THIS IS FOR EDUCATIONAL PURPOSES ONLY, YOU ARE RESPONSIBLE FOR YOUR ACTIONS**



Check if the wallet has balance using [Blockchain Explorer](https://www.blockchain.com/explorer). You can use any wallet checker you like.

### Start program
This Python script has multiple functions:
- OTBF (Optimized traditional bruteforce) <- **This is faster than TBF**
- TBF  (Traditional bruteforce) <- **Will try every wallet possible**
- RBF  (Random bruteforce)
- OBF  (Online bruteforce)

In this example we will run the RBF attack on the wallets inside of the [puzzle.bf](puzzle.bf) file:
```
 1. $ python bruteforce.py                                         # start the python program
 2. $ Select bruteforce mode:
 3. $ 0 - Exit
 4. $ 1 - Random_Bruteforce
 5. $ 2 - Sequential_Bruteforce
 6. $ 3 - Optimized_Sequential_Bruteforce
 7. $ 4 - Online_Bruteforce
 8. $ > 1                                                          # choose the function to use
 9. $ How many cores do you want to use (8 available):
10. $ > 8                                                          # choose how many cores you want to use
11. $ 
12. $ Starting bruteforce instances in mode: RBF with 8 core(s)    # feedback that it started bruteforcing
```

After line 12 you will see the instances that started, depending on the CPU cores you picked.

### Found a wallet
When the bruteforce matches an address in the [wallets.txt](wallets.txt) file. It will add or create the found.txt file. The Python program will also print the following:
```bash
$ Instance: 1 - Found: 1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ
```

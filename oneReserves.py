#import dependencies
import BancorFormulas as bf

# Initalise Global variables:
R = 60000.0     # Reserve balance
S = 300000.0    # Smart token supply
F = 0.2         # Constant reserve ratio
count = 0
start_price = bf.calcPrice(R,S,F)

# Print Result of transaction: New Balance, New Supply and New Price
def result():
    global R,S,F
    print ('   *** Results ***')
    print ('   Reserve Balance: ', R)
    print ('   BNT Supply: ',S)
    #price = R/(S*F)
    price = bf.calcPrice(R, S, F)
    print ('   New Price(Ether/BNT): ', price)
    print ('===============================================')
    print ('')
    return price


def getSmartTokens(E):
    global R, S, F, count, start_price
    count += 1
    t = bf.calcTokensIssued(S, E, R, F)
    R = bf.increaseBalance(R, E)     #increment Reserve Balance
    S = bf.increaseBalance(S, t)     #issue Smart Token
    effect_price = bf.calcEffectivePrice(E,t)
    print('======Transaction: No. ', count,'====================')
    print( '   Paid: ', E, ' ETH')
    print( '   Received:', t, ' BNT')
    print( '   Effective Rate: ', effect_price, ' ETH/BNT \n')
    start_price = result()	# start_price = new effective price
    return t


def getReserveTokens(T):
    global R, S, F, count, price, start_price
    count += 1
    e = bf.calcReserveIssued(S, T, R, F)
    R = bf.decreaseBalance(R, e) # decrement reserve balance
    S = bf.decreaseBalance(S, T) # destroys Smart Token
    effect_price = bf.calcEffectivePrice(e,T)
    print('======Transaction: No. ', count,'====================')
    print( '   Paid: ', T, ' BNT')
    print( '   Received:', e, ' ETH')
    print( '   Effective Rate: ', effect_price, ' ETH/BNT \n')
    start_price = result()	# start_price = new effective price
    return e

#### Run code ####
print("============Initial Parameters================")
print(f"    The reserve balance is: {R} ETH")
print(f"    The smart token supply is: {S} BNT")
print(f"    The constant reserve ratio is: {F}")
print(f"    The initial conversion rate is: {start_price}")
print("=============================================== \n")

#===============Transactions ===================
# Parameters should be float type
# Transaction execute in chronological order
getSmartTokens(300.0)			# Transaction 1: Convert 300.0 ETH to BNT
getSmartTokens(700.0)			# Transaction 2:Convert 700.0 ETH to BNT
getReserveTokens(1302.0)		# Transaction 3: Convert 1302.0 BNT to ETH
getSmartTokens(100.0)			# Transaction 4:Convert 100.0 ETH to BNT
getReserveTokens(20000.0)       # Transaction 5: Convert 20000.0 BNT to ETH
getSmartTokens(10000.0)         # Transaction 6: Convert 10000.0 ETH to BNT
getReserveTokens(20000.0)       # Transaction 7: Convert 40000.0 BNT to ETH

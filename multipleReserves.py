import BancorFormulas as bf
# Initalise Global variables:
R1 = 5000.0     # Reserve balance of BNT
R2 = 10000.0    # Reserve balance of ABC
S  = 10000.0    # Smart token supply NWC
F1 = 0.5        # Constant reserve ratio of BNT
F2 = 0.5        # Constant reserve ratio of ABC
count = 0

# Calculates price of BNT/Reserve token
P1 = bf.calcPrice(R1, S, F1) #Calculates the price of Smart token/R1
P2 = bf.calcPrice(R2, S, F2) #Calculates the price of Smart token/R2
reserve_price = bf.calcReserveRate(P1,P2) #Calculates the price of BNT/ABC

def result():
    global R1,S,F1
    print ('   *** Results ***')
    print ('   R1 Balance: ', R1)
    print ('   R2 Balance: ', R2)
    print ('   NWC Supply: ',S)
    #price = R/(S*F)
    price = bf.calcPrice(R1, S, F1)
    print ('   New Price(Ether/BNT): ', price)
    print ('===============================================')
    print ('')
    return price


def getSmartTokensWithR1(E):
    global count, price, S, P1, R1, F1
    count += 1
    t = bf.calcTokensIssued(S, E, R1, F1)
    R1 = bf.increaseBalance(R1, E) # increment R1 Balance
    S = bf.increaseBalance(S, t) # issue Smart Token
    effect_price = bf.calcEffectivePrice(E,t)
    print('======Transaction: No. ', count,'====================')
    print( '   Paid: ', E, ' ETH')
    print( '   Received:', t, ' BNT')
    print( '   Effective Rate: ', effect_price, ' BNT/NWC \n')
    start_price = result()
    return t



#### Run code ####
print("============Initial Parameters================")
print(f"    Reserve balance 1 is: {R1} ABC")
print(f"    Constant reserve ratio 1 is: {F1} \n")
print(f"    Reserve balance 2 is: {R2} BNT")
print(f"    Constant reserve ratio 2 is: {F2} \n")
print(f"    The smart token supply is: {S} NWC")
print(f"    The initial conversion rate for ABC/NWC: {P1}")
print(f"    The initial conversion rate for BNT/NWC: {P2}")
print(f"    The conversion rate for ABC/BNT is: {reserve_price}")
print("=============================================== \n")

#===============Transactions ===================
# Parameters should be float type
# Transaction execute in chronological order

getSmartTokensWithR1(30.0)			# Transaction 1: Convert 300.0 ETH to BNT

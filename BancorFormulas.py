# Bancor Formulas #


# Calculate price given R,S and F given reserve balance, supply and CRR
def calcPrice(reserve_balance, supply, CRR):
    price = reserve_balance / (supply * CRR)
    return price


# Calculates Tokens issued T in Exchange for reserve tokens E given R,S and F
def calcTokensIssued(supply, tokens_given, reserve_balance, CRR):
    tokens_issued = supply*((1.0+tokens_given/reserve_balance)**CRR-1.0)
    return tokens_issued


# Calculates Reserve tokens issued E in Exchange for smart tokens paid T
# given R,S and F
def calcReserveIssued(supply, tokens_given, reserve_balance, CRR):
    reserve_issued = reserve_balance*(1.0-(1.0-tokens_given/supply)**(1.0/CRR))
    return reserve_issued


# Calculates Effective Price to account for price slippage
def calcEffectivePrice(tokens_given, tokens_issued):
    effective_price = tokens_given / tokens_issued
    return effective_price


# Calculates the conversion rate for of Token1/Token2
def calcReserveRate(reserve_balance1, reserve_balance2):
    price = reserve_balance1 / reserve_balance2
    return price


# Increase the balance by the amount given
def increaseBalance(balance, amount):
    balance = balance + amount
    return balance


# Decrease the balance by the amount given
def decreaseBalance(balance, amount):
    balance = balance - amount
    return balance

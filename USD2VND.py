# USD to VND

def IsPositive(N):
    if N > 0:
        return True
    else:
        return False

def alert():
    print("Enter the positive number only!!!")
    print()

while True:
    try:
        usd = int(input("Enter the amount of USD you want to exchange: "))
        if IsPositive(usd):
            while True:
                try:
                    rate = float(input("Input the exchange rate: "))
                    if IsPositive(rate):
                        break
                    else:
                        alert()
                except Exception:
                    alert()
            break
        else:
            alert()
    except Exception:
        alert()

print("Here you are. {usd} USD is equivalent to {vnd} VND".format(usd = usd, vnd = usd * rate))


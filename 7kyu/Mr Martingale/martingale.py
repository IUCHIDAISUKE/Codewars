def martingale(bank, outcomes):
    achive = 100
    for i in outcomes:
        if i == 1:
            bank += achive
            achive = 100
        else:
            bank -= achive
            achive *= 2
    return bank

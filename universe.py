def get_universe():

    SP500 = [...]  # (deine komplette Liste einsetzen)
    NASDAQ100 = [...]
    RUSSELL2000 = [...]

    EUROPE = [
        "ASML.AS","SAP.DE","SIE.DE","BMW.DE","VOW3.DE",
        "NESN.SW","NOVN.SW","AIR.PA","OR.PA","MC.PA"
    ]

    CRYPTO_STOCK_LIKE = [
        "COIN","MSTR","RIOT","MARA"
    ]

    ALL = SP500 + NASDAQ100 + RUSSELL2000 + EUROPE + CRYPTO_STOCK_LIKE

    return list(set(ALL))

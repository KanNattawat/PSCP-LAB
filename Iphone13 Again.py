"""pscp"""
def mini(mem):
    """mini"""
    if mem == "128 GB":
        print(25900)
    elif mem == "256 GB":
        print(29900)
    elif mem == "512 GB":
        print(37900)
    else:
        print("Not Available")

def normal(mem):
    """normal"""
    if mem == "128 GB":
        print(29900)
    elif mem == "256 GB":
        print(33900)
    elif mem == "512 GB":
        print(41900)
    else:
        print("Not Available")

def pro(mem):
    """pro"""
    if mem == "128 GB":
        print(38900)
    elif mem == "256 GB":
        print(42900)
    elif mem == "512 GB":
        print(50900)
    elif mem == "1 TB":
        print(58900)
    else:
        print("Not Available")

def promax(mem):
    """promax"""
    if mem == "128 GB":
        print(42900)
    elif mem == "256 GB":
        print(46900)
    elif mem == "512 GB":
        print(54900)
    elif mem == "1 TB":
        print(62900)
    else:
        print("Not Available")

def main(model, mem):
    """main"""
    if model == "iPhone 13 mini":
        mini(mem)
    elif model == "iPhone 13":
        normal(mem)
    elif model == "iPhone 13 Pro":
        pro(mem)
    elif model == "iPhone 13 Pro Max":
        promax(mem)
    else:
        print("Not Available")
main(input(), input())

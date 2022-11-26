import math

def inDict(key_val: dict, target:dict) -> bool:
    key = [i for i in key_val.keys()][0]
    val = [i for i in key_val.values()][0]

    if key in target:
        return True if target[key] == val else False

    return False

def dictIndex(key_val: dict, target:dict) -> int | bool:
    key = [i for i in key_val.keys()][0]
    val = [i for i in key_val.values()][0]

    if key in target:
        if target[key] == val:
            for index, k in enumerate(target.keys()):
                if k == key and target[k] == val: return index

    return False

def getPairByIndex(index: str, target:dict) -> dict | bool:
    current_index = 0

    for k, v in target.items():
        if int(index) == current_index: return {k:v}

        current_index += 1

    return False

def getKeyFromDictPair(pair:dict) -> str:
    return [i for i in pair.keys()][0]
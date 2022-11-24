import include.analyzer

def var(name: str, value: any, var_type:str) -> dict:
    value = include.analyzer.type_keys_dict[var_type](value)

    return {name:value}
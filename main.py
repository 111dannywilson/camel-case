def payload(data: dict, field: str):
    if type(data) != dict:
        return f"Your input is of type {type(data).__name__}, it should be of type dict"
    for key, value in data.items():
        if field not in data.keys():
            return f"{field} not in provided data"
        if type(value) != bool:
            return f"{field} value should bo of type boolean"
        data[key] = False
        data[field] = True
    return data


data = {
    "male": True,
    "female": False,
    "other": True,
    "child": False,
}

output = payload(data, "male")
print(output)

# Added functionalities will be selecting new value for required key

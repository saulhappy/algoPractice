def truthy_or_falsy(argument):
    if bool(argument) == True:
        return f"The value {argument} is truthy"
    else:
        return f"The value {argument} is falsy"


print(truthy_or_falsy(0))

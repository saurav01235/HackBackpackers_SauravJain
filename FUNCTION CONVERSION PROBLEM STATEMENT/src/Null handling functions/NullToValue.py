def NullToValue(value, default_value):
    if isNull(value):
        return default_value
    return value
def string_reversal(str: str) -> str:
    if len(str) == 0:
        return str
    else:
        return string_reversal(str[1:]) + str[0]

sample_str = 'reversal'

print(string_reversal(sample_str)) # lasrever (slice function w/ recursion)
print(sample_str[::-1])            # lasrever (slice function)

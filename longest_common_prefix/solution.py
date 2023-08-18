def longest_pref(words):
    short = min(words, key=len)
    for word in words:
        while len(short) > 0:
            if word.startswith(short):
                break
            else:
                short = short[:-1]
    return short

print(longest_pref(words=['flower', 'flow', 'flight', 'flour']))


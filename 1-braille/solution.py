def solution(s):
    to_ret, d = "", {'a': "100000", 'b': "110000", 'c': "100100", 'd': "100110", 'e': "100010", 'f': "110100", 'g': "110110", 'h': "110010", 'i': "010100", 'j': "010110", 'k': "101000", 'l': "111000", 'm': "101100", 'n': "101110", 'o': "101010", 'p': "111100", 'q': "111110", 'r': "111010", 's': "011100", 't': "011110", 'u': "101001", 'v': "111001", 'w': "010111", 'x': "101101", 'y': "101111", 'z': "101011", 'SPACE': "000000", 'CAP': "000001", 'ALLCAP': "000011"}
    words = s.replace(" "," # ").split()
    for word in words:
        if word.isupper():
            to_ret += d['ALLCAP']
            word = word.lower()
        for char in word:
            if char.isupper():
                to_ret += d['CAP']
                to_ret += d[char.lower()]
            elif char == "#":
                to_ret += d['SPACE']
            else:
                to_ret += d[char]
    return to_ret
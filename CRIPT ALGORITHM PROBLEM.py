import itertools

def solve():
    letters = 'SENDMORY'
    digits = '0123456789'
    for perm in itertools.permutations(digits, len(letters)):
        s = dict(zip(letters, perm))
        if s['S'] == '0' or s['M'] == '0':
            continue
        send = int(''.join(s[c] for c in 'SEND'))
        more = int(''.join(s[c] for c in 'MORE'))
        money = int(''.join(s[c] for c in 'MONEY'))
        if send + more == money:
            print(f"SEND = {send}, MORE = {more}, MONEY = {money}")
            return

solve()

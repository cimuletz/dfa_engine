import sys
f = open(sys.argv[1], "r")
def sigma():
    sig = []
    word = f.readline().replace("\n", '')
    while word[0] == '#':
        word = f.readline().replace("\n", '')
    word = f.readline().replace("\n", '').strip() # trecem peste Sigma
    while word != "End":
        sig.append(word)
        word = f.readline().replace("\n", '').strip()
    return sig

def states():
    si = []
    sf = []
    s = []
    state = f.readline().replace("\n", '')
    while state[0] == '#':
        state = f.readline().replace("\n", '')
    state = f.readline().replace("\n", '').strip() #
    while state != "End":
        if ', F' in state: # F - dictionar pentru stari finale
            sf.append(state[:len(state)-3])

        if ', S' in state: # S - dictionar pentru stari initiale
            si.append(state[:len(state)-3])

        if ', F' in state or ', S' in state:
            s.append(state[:len(state)-3])
        else:
            s.append(state)
        state = f.readline().replace("\n", '').strip()
    if len(si) != 1:
        print("Stari invalide.")
    return si, sf ,s

def transitions(si, sf, s, sig):
    trans = []
    dict = {}
    tranzitie = f.readline().replace("\n", '').strip()
    while tranzitie[0] == '#':
        tranzitie = f.readline().replace("\n", '').strip()
    tranzitie = f.readline().replace("\n", '').strip()
    while tranzitie != "End":
        sx, w, sy = tranzitie.split(", ") #sx - stare x, w - word, sy - stare y
        tranzitie = f.readline().replace("\n", '').strip()
        if sx in s and sy in s and w in sig:
            if sx not in dict:
                dict[sx] = {w:sy}
            else:
                dict[sx][w] = sy
            trans.append((sx,w,sy))
    return dict

def process(sig, si, sf, dict, str):
    currentState = si[0]
    for c in str:
        if c not in sig or c not in dict[currentState]:
            return "reject"
        next = dict[currentState][c]
        currentState = next
    if currentState not in sf:
        return "reject"
    else:
        return "accept"


sig = sigma()
si, sf, s = states()
dict = transitions(si, sf, s, sig)
#print("Sigma:" , *sig)
#print("Stari initiale:" ,*si)
#print("Stari finale:" , *sf)
#print("Stari:" , *s)
#print("Tranzitii:" , dict)

print(process(sig, si, sf, dict, sys.argv[2]))



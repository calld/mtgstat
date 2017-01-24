from random import randrange


drawTable = {drawn:{land:[0 for x in range(12)] for land in range(20, 29)} for drawn in range(7, 12)}

testsize = 10000

def testdraw(drawamount, landsize):
    deck = [1 for x in range(landsize)] + [0 for x in range(60 - landsize)]
    total = 0
    def draw(d):
        return deck.pop(randrange(len(deck)))
    for x in range(drawamount):
        total = total + draw(deck)
    return total

for drawn, t in drawTable.items():
    for land, l in t.items():
        for x in range(testsize):
            d = testdraw(drawn, land)
            l[d] = l[d] + 1
        #for i in range(12):
        #    l[i] = l[i]/testsize

results = [[drawn, [[land, l]  for land, l in t.items()]] for drawn, t in drawTable.items()]

results.sort(key = lambda x: x[0])
for el in results:
    el[1].sort(key = lambda x: x[0])

lines = []

for result in results:
    lines.append("number drawn: {}".format(result[0]))
    lines.append('\t' + '\t'.join([str(x) for x in range(12)]))
    for row in result[1]:
        lines.append(str(row[0]) + '\t' + '\t'.join([str(v) for v in row[1]]))

out = open('landdrawrate.txt', 'w')
out.write('\n'.join(lines))
out.close

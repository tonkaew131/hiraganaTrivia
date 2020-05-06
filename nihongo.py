from random import randrange

a   = list("あいうえお")
Ra  = ["a", "i", "u", "e", "o"]
ka  = list("かきくけこ")
Rka = ["ka","ki","ku","ke","ko"]
sa  = list("さしすせそ")
Rsa = ["sa","shi","su","se","so"]
ta  = list("たちつてと")
Rta = ["ta","chi","tsu","te","to"]
na  = list("なにぬねの")
Rna = ["na","ni","nu","ne","no"]
ha  = list("はひふへほ")
Rha = ["ha","hi","fu","he","ho"]
ma  = list("まみむめも")
Rma = ["ma","mi","mu","me","mo"]
ya  = list("やゆよ")
Rya = ["ya","yu","yo"]
ra  = list("らりるれろ")
Rra = ["ra","ri","ru","re","ro"]
wa  = list("わゐゑを")
Rwa = ["wa","wi","we","wo"]
n   = list("ん")
Rn  = ["n"]

questionlist = [
    ["a", [a,Ra]],
    ["ka",[ka,Rka]],
    ["sa",[sa,Rsa]],
    ["ta",[ta,Rta]],
    ["na",[na,Rna]],
    ["ha",[ha,Rha]],
    ["ma",[ma,Rma]],
    ["ya",[ya,Rya]],
    ["ra",[ra,Rra]],
    ["wa",[wa,Rwa]],
    ["n", [n,Rn]]
]

print("a/ka/sa/ta/na/ha/ma/ya/ra/wa/n")
startfrom = input("Choose from: ")
stopat    = input("to: ")
testlist = []
answlist = []
for i in range(len(questionlist)):
    if(startfrom==questionlist[i][0]):
        startindex = i
    if(stopat==questionlist[i][0]):
        stopindex = i
for i in range(startindex,stopindex+1):
    for el in questionlist[i][1][0]:
        testlist.append(el)
    for el in questionlist[i][1][1]:
        answlist.append(el)
wrongcount = 0
for i in range(len(testlist)):
    curquestindex = randrange(len(testlist))
    print("What is this :" + testlist[curquestindex])
    answ = input()
    if( answ == answlist[curquestindex]):
        testlist.remove(testlist[curquestindex])
        answlist.remove(answlist[curquestindex])
        print("Correct!!!")
    else:
        print("Wrong, please try again")
        wrongcount += 1
print("You have finish from {} to {} with {} mistakes".format(startfrom,stopat,wrongcount))

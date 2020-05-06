from random import randrange
from collections import Counter
import time

questionlist = [
    ["a", [['あ','い','う','え','お'],["a","i","u","e","o"]]],
    ["ka",[['か','き','く','け','こ'],["ka","ki","ku","ke","ko"]]],
    ["sa",[['さ','し','す','せ','そ'],["sa","shi","su","se","so"]]],
    ["ta",[['た','ち','つ','て','と'],["ta","chi","tsu","te","to"]]],
    ["na",[['な','に','ぬ','ね','の'],["na","ni","nu","ne","no"]]],
    ["ha",[['は','ひ','ふ','へ','ほ'],["ha","hi","fu","he","ho"]]],
    ["ma",[['ま','み','む','め','も'],["ma","mi","mu","me","mo"]]],
    ["ya",[['や','ゆ','よ'],["ya","yu","yo"]]],
    ["ra",[['ら','り','る','れ','ろ'],["ra","ri","ru","re","ro"]]],
    ["wa",[['わ','ゐ','ゑ','を'],["wa","wi","we","wo"]]],
    ["n", [['ん'],["n"]]]
]

print("  Welcome to Hiragana Trivia! ")
print("a/ka/sa/ta/na/ha/ma/ya/ra/wa/n")
startfrom = input("Choose from: ").lower()
stopat    = input("to: ").lower()
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
wronglist = []
starttime = time.time()
while True:
    if(len(testlist)==0):
        endtime = time.time()
        break
    curquestindex = randrange(len(testlist))
    print("What is this :" + testlist[curquestindex])
    answ = input().lower()
    if( answ == answlist[curquestindex] ):
        testlist.remove(testlist[curquestindex])
        answlist.remove(answlist[curquestindex])
        print("Correct!!!")
    else:
        print("Wrong, please try again")
        wronglist.append(testlist[curquestindex])
        wrongcount += 1
print("Time elapsed : " + str(round(endtime-starttime, 2)) + " seconds")
print("You have finish from {}({}) to {}({}) with {} mistakes".format(questionlist[startindex][1][0][0],startfrom,questionlist[stopindex][1][0][0],stopat,wrongcount))
if(wrongcount!=0):
    print("Most mistake is :", end='')
    result = [item for items, c in Counter(wronglist).most_common() 
        for item in [items] * c]
    result = list(dict.fromkeys(result))[:5]
    for i in result:
        print(" " + i, end="")

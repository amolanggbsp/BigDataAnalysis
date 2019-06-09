docA="blockchainand global corporate owned data."
docB="Global blockchain in is expected to grow to 2.3 billion."
docC=""
docD=""
docE=""
docF=""
docG=""
docH=""
docI=""
docJ=""
docK=""

bowA=docA.split(" ")
bowB=docB.split(" ")
bowC=docC.split(" ")
bowD=docD.split(" ")
bowE=docE.split(" ")
bowF=docF.split(" ")
bowG=docG.split(" ")
bowH=docH.split(" ")
bowI=docI.split(" ")
bowJ=docJ.split(" ")
bowK=docK.split(" ")


wordSet=set(bowA).union(set(bowB),set(bowC))


wordDictA=dict.fromkeys(wordSet, 0)
wordDictB=dict.fromkeys(wordSet, 0)
wordDictC=dict.fromkeys(wordSet, 0)
for word in bowA:
    wordDictA[word]+=1
    
for word in bowB:
    wordDictB[word]+=1

for word in bowC:
    wordDictC[word]+=1

for word in bowD:
    wordDictD[word]+=1
    
for word in bowE:
    wordDictE[word]+=1

for word in bowF:
    wordDictF[word]+=1

for word in bowG:
    wordDictG[word]+=1

for word in bowH:
    wordDictH[word]+=1

for word in bowI:
    wordDictI[word]+=1

for word in bowJ:
    wordDictJ[word]+=1

for word in bowK:
    wordDictK[word]+=1
    
import pandas as pd
print(pd.DataFrame([wordDictA, wordDictB, wordDictC, wordDictD, wordDictE, wordDictF, wordDictG, wordDictH, wordDictI, wordDictJ, wordDictK]))



def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)

    for word, count in wordDict.items():
        tfDict[word]=count/ float(bowCount) 
    return tfDict

tfBowA= computeTF(wordDictA, bowA)
tfBowB= computeTF(wordDictB, bowB)
tfBowC= computeTF(wordDictC, bowC)
tfBowD= computeTF(wordDictD, bowD)
tfBowE= computeTF(wordDictE, bowE)
tfBowF= computeTF(wordDictF, bowF)
tfBowG= computeTF(wordDictG, bowG)
tfBowH= computeTF(wordDictH, bowH)
tfBowI= computeTF(wordDictI, bowI)
tfBowJ= computeTF(wordDictJ, bowJ)
tfBowK= computeTF(wordDictK, bowK)



def computeIDF(docList):
    import math
    idfDict={ }
    N=len(docList)

    idfDict= dict.fromkeys(docList[0].keys(),0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] +=1
    for word, val in idfDict.items():
        idfDict[word]=math.log(N/ float(val))
    return idfDict

idfs=computeIDF([wordDictA, wordDictB, wordDictC, wordDictD, wordDictE, wordDictF, wordDictG, wordDictH, wordDictI, wordDictJ, wordDictK])





def computeTFIDF(tfBow, idfs):
    tfidf= { }
    for word, val in tfBow.items():
        tfidf[word]=val*idfs[word]
    return tfidf

tfidfBowA =  computeTFIDF(tfBowA, idfs)
tfidfBowB =  computeTFIDF(tfBowB, idfs)

import pandas as pd
print(pd.DataFrame([tfidfBowA, tfidfBowB]))



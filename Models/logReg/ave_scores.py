scores = {"ROCK": [0.7340385989992853, 0.6547346752058555], "POP": [0.7325886301657227, 0.590604026845637], "ALTERNATIVE": [0.8115918455866407, 0.6738234656256777], "HEAVY METAL": [0.9702493551160791, 0.6932599724896836], "COUNTRY": [0.9557582668187001, 0.5742935278030994], "R&B/SOUL": [0.9383915022761761, 0.4720873786407767], "CHRISTIAN & GOSPEL": [0.989891426432048, 0.7514970059880239], "SINGER/SONGWRITER": [0.998389694041868, 0.6189710610932476], "HIP HOP/RAP": [0.9969749351771824, 0.5561312607944733], "ELECTRONIC": [0.9908653846153846, 0.6717850287907869], "MUSIC": [0.9993197278911564, 0.6032608695652174], "JAZZ": [0.9881456392887383, 0.5641891891891891], "DANCE": [0.9924953095684803, 0.5168539325842697], "BLUES": [0.9978991596638656, 0.6764705882352942], "REGGAE": [0.9973333333333333, 0.46808510638297873], "HARD ROCK": [1.0, 0.47435897435897434], "PUNK": [1.0, 0.7755102040816326], "VOCAL": [1.0, 0.6618705035971223], "DEATH METAL/BLACK METAL": [1.0, 0.8103448275862069], "INDIE ROCK": [0.995475113122172, 0.5495495495495496], "HOLIDAY": [0.9705882352941176, 0.8378378378378378], "WORLD": [0.9976303317535545, 0.6792452830188679], "POP/ROCK": [1.0, 0.5789473684210527], "ADULT ALTERNATIVE": [1.0, 0.6], "GOSPEL": [1.0, 0.8192771084337349], "CCM": [1.0, 0.8813559322033898], "SOUNDTRACK": [0.9947368421052631, 0.6666666666666666], "PROG-ROCK/ART ROCK": [1.0, 0.7906976744186046], "COMEDY": [1.0, 0.7674418604651163], "FOLK": [1.0, 0.6216216216216216], "LATIN": [1.0, 0.5555555555555556], "SOUL": [1.0, 0.4074074074074074], "FOLK-ROCK": [1.0, 0.7692307692307693], "ALTERNATIVE FOLK": [1.0, 0.625], "EASY LISTENING": [1.0, 0.6666666666666666], "NEW WAVE": [0.989010989010989, 0.6521739130434783], "TRADITIONAL FOLK": [1.0, 0.8181818181818182], "NEW AGE": [1.0, 0.6363636363636364], "FRENCH POP": [1.0, 0.631578947368421], "HIP-HOP": [1.0, 0.6666666666666666], "ALTERNATIVE & ROCK IN SPANISH": [1.0, 0.6111111111111112], "ROCK & ROLL": [1.0, 0.5555555555555556], "CHRISTIAN ROCK": [1.0, 0.7222222222222222], "GOTH ROCK": [1.0, 0.9411764705882353], "CONTEMPORARY R&B": [1.0, 0.5625], "SOFT ROCK": [1.0, 0.625], "CHRISTMAS": [1.0, 0.5333333333333333], "BLUES-ROCK": [1.0, 0.2857142857142857], "RAP": [1.0, 0.5714285714285714], "CONTEMPORARY COUNTRY": [1.0, 0.6428571428571429]}

train_score = 0
test_score = 0
for k, v in scores.items():
    train_score += v[0]
    test_score += v[1]
    
c = len(s)
print('Ave training score:', train_score/c)
print('Ave testing score:', test_score/c)

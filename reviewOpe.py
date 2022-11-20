import numpy as np
import statistics as stat
import stringOpe as so
import csvOpe as co

fileName = "TripadvisorHotelReviews.csv"

def returnReview(csvEmotionDict: dict[str,str]):
    returnReviewScore = co.csvfileToList(fileName)
    scoreMemory = ""
    stringValue = ""
    for i in range(0,len(returnReviewScore),1):
        #1から5までいくつだったのか記憶しておく
        scoreMemory = returnReviewScore[i][1]
        #文字数がいくつか
        stringValue = len(returnReviewScore[i][0].split(' '))
        returnReviewScore[i][1] = [scoreMemory,stringValue]
        returnReviewScore[i][0] = so.stringSplit(returnReviewScore[i][0])
        #これによりリストは[[総合点,評価できない単語数],[レビューのスコア,総単語数]]になる
        returnReviewScore[i][0] = co.serach(returnReviewScore[i][0],csvEmotionDict)
        #1文字あたりの点数を出す総合点　÷（総単語数　-　評価できない単語数）　
        returnReviewScore[i][0] = returnReviewScore[i][0][0] / (returnReviewScore[i][1][1] - returnReviewScore[i][0][1])
        #レビューのスコアを[i][1]番目に入れておく
        returnReviewScore[i][1] = returnReviewScore[i][1][0]
    return returnReviewScore

#スコアのいろいろな評価方法と渡された数値から評価付け
def assessmentReviewValue(soughtReviewScore: list[list[str]]):
    scoreListall = []
    averageList = []
    medianList = []
    rangeList = []
    #0から5まででそれぞれに対応した配列に入れていく1ならばscoreListall[0]
    for number in range(5):
        scoreList = []
        for i in range(0,len(soughtReviewScore),1):
            if soughtReviewScore[i][1] == str(number + 1):
                scoreList.append(soughtReviewScore[i][0])
        scoreListall.append(scoreList)
    #平均
    for i in range(5):
        averageList.append(stat.mean(scoreListall[i]))
    scoreListall.append(averageList)
    #中央値
    for i in range(5):
        medianList.append(stat.median(scoreListall[i]))
    scoreListall.append(medianList)
    #範囲
    for i in range(5):
        rangeList.append(min(scoreListall[i]))
        rangeList.append(max(scoreListall[i]))
    scoreListall.append(rangeList)
    del scoreListall[:5]
    return scoreListall

#評価を点数付け
def scoringReviews(reviewValue: float,score: list):
    #平均値から判定する方法
    reviewScoreValue = np.abs(np.asarray(score[0]) - reviewValue).argmin()+1
    print("平均値で判定: "+str(reviewScoreValue)+" → 元の値: "+str(reviewValue)+" それに近い値: "+str(score[0][reviewScoreValue - 1])
    +" その差: "+str(np.abs(np.abs(score[0][reviewScoreValue - 1]) - np.abs(reviewValue))))
    #中央値から判定する方法
    reviewScoreValue = np.abs(np.asarray(score[1]) - reviewValue).argmin()+1
    print("中央値で判定: "+str(reviewScoreValue)+" → 元の値: "+str(reviewValue)+" それに近い値: "+str(score[1][reviewScoreValue - 1])
    +" その差: "+str(np.abs(np.abs(score[1][reviewScoreValue - 1]) - np.abs(reviewValue))))
    return
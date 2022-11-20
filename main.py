import sys
import stringOpe as so
import csvOpe as co
import reviewOpe as ro

returnCsvEmotionDict = {}
fileName = "EnglishWordEmotionPolarity.csv"

returnCsvEmotionDict = co.csvfileToDict(fileName)

strInput = input("口コミを入力してください:")
strSplit = so.stringSplit(strInput)
print("入力した口コミ: "+str(strSplit))
#総単語数
print("総単語数: "+str(len(strSplit)))
#総合点÷単語数で1単語あたりの点数を出す→これが必要になった背景　単語数が違うのに同じ点数の場合があったため
resultSearch = co.serach(strSplit,returnCsvEmotionDict)
print("総合点,判定不可単語数: "+str(resultSearch))
try:
    revewValue = resultSearch[0] / (len(strSplit) - resultSearch[1])
except:
    revewValue = -100
    print("Error:判定不能です。")
    #プログラムを強制終了させる
    sys.exit()
print("1単語あたりの点数: "+str(revewValue))
#出してきた点数から1～5まで判定させる
reviewScore = ro.returnReview(returnCsvEmotionDict)

score =  ro.assessmentReviewValue(reviewScore)
print(score)
ro.scoringReviews(revewValue,score)
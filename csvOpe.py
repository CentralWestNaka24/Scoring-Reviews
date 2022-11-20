import csv

#レビュー用
def csvfileToList(fileName: str):
    #レビューのCSVから中の要素をリスト型にして取得する
    fileEmo = open(fileName,'r',encoding="utf-8")
    reader = csv.reader(fileEmo)
    csvEmotionList = [i for i in reader]
    return csvEmotionList

#英語単語感情極性対応表用
def csvfileToDict(fileName: str):
    #英語単語感情極性対応表から中の要素をリスト型にして取得する
    fileEmo = open(fileName,'r',encoding="utf-8")
    reader = csv.reader(fileEmo)
    csvEmotionList = [i for i in reader]
    #リストから辞書に変換
    csvEmotionDict = dict(csvEmotionList)
    return csvEmotionDict

#検索用（数値を返す）
def serach(strList: list[str],csvEmotionDict: dict[str,str]):
    #配列の0番目に総合点、配列の1番目に判定できなかった単語数
    numberSum = []
    score = 0.0
    count = 0
    for i in strList:
        try:
            #print(csvEmotionDict[i])
            score += float(csvEmotionDict[i])
        except:
            count += 1
    numberSum.append(score)
    numberSum.append(float(count))
    return numberSum
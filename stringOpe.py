#文字列を分割するメソッド
def stringSplit(strSpi: str):
    stringlist = []
    ansList = []
    #文字列を文字に分割 大文字だと判定できないため、全て小文字に変換
    stringlist = strSpi.lower().split()
    #,や.を削除する
    for i in stringlist:
        if(',' in i):
            #,を削除
            ansList.append(i.replace(',',''))
        elif('.' in i):
            #.を削除
            ansList.append(i.replace('.',''))
        else:
            #そのまま
            ansList.append(i)
    return ansList
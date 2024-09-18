

class ListUtil:

    @staticmethod
    def assign(trackList:list):
        arrlist = []
        for temp in trackList:
            arrlist.append({1: temp[2], 2: temp[3], 3: temp[4], 4: temp[5], 5: temp[6], 6: temp[7], 7: temp[8],
                                 8: temp[9], 9: temp[10], 10: temp[11], 11: temp[12], 12: temp[13], 13: temp[14],14: temp[17]})
        return arrlist

    @staticmethod
    def initAssign():
        arrlist = []
        for _ in range(20):
            arrlist.append({1: "", 2: "直线", 3: "", 4: "", 5: "", 6: "", 7: "", 8: "", 9: "", 10: "", 11: "", 12: "", 13: "",14: ""})
        return arrlist


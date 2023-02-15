import re

class wordNum:
    def text2int (self, textnum, numwords={}):
        if not numwords:
            #Satuan
            units = [
            "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan",
            "sembilan", "sepuluh", "sebelas"]
    
            #Scales
            teens = ["belas"]
            tens = ["puluh"]
            bigNumbers = ["ratus", "ribu", "juta", "miliar", "triliun"]
    
            numwords["and"] = (1, 0)
            for idx, word in enumerate(units):  numwords[word] = (1, idx+1)
            #for idx, word in enumerate(tens):   numwords[word] = (1, idx * 10)
            for idx, word in enumerate(teens): numwords[word] = (1, 10 ** (idx * 2 or 1))
            for idx, word in enumerate(tens): numwords[word] = (10 ** (idx * 2 or 1), 0)
            for idx, word in enumerate(bigNumbers): numwords[word] = (10 ** (idx * 3 or 2), 0)
    
        ordinal_words = {'pertama':1, 'seratus':100, 'seribu':1000}
        #ordinal_starts = [('se', 'satu')]
        
        textnum = textnum.casefold()
        
        textnum = re.sub("ke", "ke ", textnum)
    
        textnum = textnum.replace('-', ' ')
    
        current = result = 0
        curstring = ""
        onnumber = False
        for word in textnum.split():
            if word in ordinal_words:
                scale, increment = (1, ordinal_words[word])
                current = current * scale + increment
                if scale > 100:
                    result += current
                    current = 0
                onnumber = True
            else:
                # for starts, replacement in ordinal_starts:
                #     if word.startswith(starts):
                #         word = "%s%s" % (word[:len(starts)], replacement)
    
                if word not in numwords:
                    if onnumber:
                        curstring += repr(result + current) + " "
                    curstring += word + " "
                    result = current = 0
                    onnumber = False
                else:
                    scale, increment = numwords[word]
    
                    current = current * scale + increment
                    if scale > 100:
                        result += current
                        current = 0
                    onnumber = True
    
        if onnumber:
            curstring += repr(result + current)
    
        return curstring
        
    
# def main():
#     wordToNumberFormat = wordNum()
#     print(wordToNumberFormat.text2int("saya pesan Tiga puluh kamar untuk Pertama, dua ratus sa, dan kedua"))
    
# if __name__ == "__main__":
#     main()
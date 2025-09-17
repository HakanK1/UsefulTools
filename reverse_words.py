def reverse_words(text):
    separated = text.split(' ')
    separatedlist = []
    for word in separated:
        separatedlist.append([word])
    
    list35 = []
    
    for element in separatedlist:
        stringversion = ''.join(element) # converts it into string
        stringtolist = list(stringversion)
        start = 0
        end = len(stringtolist) - 1
        
        while(start<end):
            temp = stringtolist[start]
            stringtolist[start] = stringtolist[end]
            stringtolist[end] = temp
            start += 1
            end -= 1
        
        stringversion2 = ''.join(stringtolist)

        list35.append(stringversion2)

    
    return ' '.join(list35)
    
sentence = "Jack come here!"
reversed = reverse_words(sentence)
print(reversed)
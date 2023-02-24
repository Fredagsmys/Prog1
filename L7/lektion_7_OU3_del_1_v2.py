import re
infil = open('gubben noak.txt', 'r')
text = infil.read()
infil.close()

def freq(text):
    freq = {}              
    for c in text:             
        c = c.lower()      
        if c in freq:      
            freq[c] += 1   
        else:              
            freq[c] = 1    

    return freq

wordlist = re.findall(r'[a-zA-ZåäöÅÄÖ]+', text)
freq = str(freq(wordlist))

text_letters = re.findall(r'[a-zA-ZåäöÅÄÖ]+',freq)
text_numbers = re.findall(r'[0-9]+',freq)

text_numbers = sorted(text_numbers,key=int,reverse = True)


text_total = []
for i in range(len(text_numbers)):
    
    text_total.append(text_numbers[i] + ' '+ text_letters[i])


print('antal ord: ',len(wordlist))
print('antal olika ord: ', len(text_total))
m = int(input('hur många av de ovanligaste orden vill du veta? '))
n = int(input('hur många av de vanligaste orden vill du veta? '))


text_total_letters = re.findall(r'[a-zA-ZåäöÅÄÖ]+',str(text_total))

print('de ovanligaste orden är ',text_total_letters[:m])

print('de vanligaste orden är ',text_total_letters[:-n-1:-1])
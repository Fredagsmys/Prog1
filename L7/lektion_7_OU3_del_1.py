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

print(f'antal ord: {len(wordlist)}')
print(f'antal olika ord: {len(text_letters)}')

m = int(input('hur många av de ovanligaste orden vill du veta? '))
n = int(input('hur många av de vanligaste orden vill du veta? '))

print(f'de {m} ovanligaste orden är {text_letters[-m:]}')

print(f'de {n} vanligaste orden är {text_letters[:n]}')
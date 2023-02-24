
text = '''Kvällens gullmoln fästet kransa.
Älvorna på ängen dansa,
och den bladbekrönta näcken
gigan rör i silverbäcken.
'''

#print(len([c for c in text if c.lower() in 'ä']))

test_text = 'aVcdgdrdåäöäöåäÅÄgyjgdÖüéáöåäöåjgyjäöèîçÇôÜÁxyZX'
letters = 'abcdefghijklmnopqrstuvwxyz'
n = 0
m=0
for c in test_text:
    if c.lower() in letters:
        n+=1
print(f'ammount of national letters: {len(test_text)-n}')

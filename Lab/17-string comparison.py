word = 'bnanana'
if word == 'banana':
    print('All right, bnananas.')

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('All right, bnananas.')

dete = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14"16 2008'
atpos = dete.find('@')
print(atpos)
sppos = dete.find(' ',atpos)
host = dete[atpos+1 : sppos]
print(host)
sen = input('Enter the sentence to count Upper case and Lower case in sebtence')
print(len(sen))
print(sen.isupper())
count1,count2,space = 0, 0, 0
print('Upper And Lower')
for i in range(len(sen)):

    if sen[i].isupper() :
        count1=count1+1
    elif sen[i].islower():
        count2=count2+1
    elif sen[i]==' ':
        space=space+1

print("upper case=", count1)
print("lower case=", count2)
print("Space=", space)
print('how many vovle and conso....')
vov,con=0,0
for j in range(len(sen)):
    if sen[j]=='a' or sen[j]=='e' or sen[j]=='i' or sen[j]=='o' or sen[j]=='u' or sen[j]=='A' or sen[j]=='E' or sen[j]=='I' or sen[j]=='O' or sen[j]=='U':
        vov=vov+1
    else:
        con=con+1

print('vovel=',vov)
print('cons=',con)
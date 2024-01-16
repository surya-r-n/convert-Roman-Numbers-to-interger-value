def roman2dec(numeral):
    d={"M":1000,"D":500,"C":100,"L":50,"X":10,"V":5,"I":1}
    ans=0
    n=len(numeral)
    for (index,character) in enumerate(numeral):
        if index<n-1 and d[character]<d[numeral[index+1]]:
            ans-=d[character]
        else:
            ans+=d[character]
    return ans

romanstr=input("enter the roman number")
print(roman2dec(romanstr))
            

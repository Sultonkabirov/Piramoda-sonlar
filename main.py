son=int(input("Sonni kiriting:"))
coun=0
coun1=0
while son>=0:
  i =son//10
  if son==0:
      break
  if i%2==0 and i>0:
     coun1+=1 
  if son%10>=0:
        coun+=1
  son=son//10 
print("Xonlari soni:",coun,"\nJuft sonlari:",coun1) 
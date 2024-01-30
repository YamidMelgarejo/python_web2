x = range(100)

suma=99
for i in range(0,len(x)):

  for j in range(i+1,len(x)):
      res=x[i]+x[j]

      if res == suma:
          print(x[i],",",x[j])
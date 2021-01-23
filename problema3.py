#Problema 3

def countPairs(ar, n, k): 
    freq=[0]*k #array para contar os restos quando dividido por K
	
    for i in range(n): 
        freq[ar[i]%k]+=1 #conta restos
		
    sum=freq[0]*(freq[0]-1)/2; 
      
    i = 1
    while(i <=k//2 and i != (k - i) ): 
        sum += freq[i] * freq[k-i] 
        i+= 1
  
    if(k%2==0): #caso k seja par
        sum+= (freq[k//2]*(freq[k//2]-1)/2); 
    return int(sum) 
  
ar=[1, 2, 3, 4, 5, 6]
n = len(ar) 
k = 5
print(countPairs(ar, n, k)) 
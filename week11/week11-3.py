#輾轉相除法
a = 1234567
b = 7654321

def gcd(a, b): #函式
  print(a, b) #印出來看過程
  if a==0: return b # 終止條件，遇到0的話，另一邊式答案
  if b==0: return a #同上
  return gcd(b, a%b) #函式呼叫函式，一直到成功為止

ans = gcd(a, b)
print(ans)
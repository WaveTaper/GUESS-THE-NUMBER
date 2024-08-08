import random
count = 0
r = random.randint(1,100) 
while True:
    num = input('請輸入0-100的整數')
    num = int( num ) 
    count = count + 1 
    if num == r :
        print('猜中了!')
        break
    elif num > r :
        print('在小一點')  
    elif num < r :
        print('再大一點')
    print('你猜了', count , '次')
    
    
    



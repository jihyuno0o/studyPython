#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/82612

# 새로 생긴 놀이기구는 인기가 매우 많아 줄이 끊이질 않습니다. 이 놀이기구의 원래 이용료는 price원 인데, 놀이기구를 N 번 째 이용한다면 원래 이용료의 N배를 받기로 하였습니다. 즉, 처음 이용료가 100이었다면 2번째에는 200, 3번째에는 300으로 요금이 인상됩니다.
# 놀이기구를 count번 타게 되면 현재 자신이 가지고 있는 금액에서 얼마가 모자라는지를 return 하도록 solution 함수를 완성하세요.
# 단, 금액이 부족하지 않으면 0을 return 하세요.
# 
# - 놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
# - 처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
# - 놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수
# 

# In[6]:


price = 3
money = 20
count = 4


# In[7]:


pay = 0


# In[8]:


for i in range(count):
    pay += price * (i+1)


# In[9]:


if pay <= money:
    print(0)
else:
    print(pay - money)


# solution

# In[ ]:


def solution(price, money, count):
    pay = 0
    for i in range(count):
        pay += price * (i+1)
    
    if pay <= money:
        return 0
    else:
        return pay-money
    
    return -1


# 다른 사람 코드 : 등차수열 공식으로 품
# 
# (a+l)*n/2
# 근데 하나씩 증가하니까
# 
# price* n(=count) * (5 => a=1, l=4) /2

# In[ ]:


def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)


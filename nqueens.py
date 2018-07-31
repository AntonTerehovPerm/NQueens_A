
# coding: utf-8

# # Стандартный алгоритм с улучшенным условием нахождения особи

# Реализуется: Добавилось условие по которому генетический алгоритм будет стремиться к 8 ферзям в коде особи

# In[3]:


class Solver_8_queens:
    def __init__(self, pop_size=100, cross_prob=0.50, mut_prob=0.25):
        pass
    def solve(self, min_fitness=0.9, max_epochs=10000):
        import random
        osob ={}
        kol = Solver_8_queens.pop_size
        minus = []
        pod = []
        k=True
        t = 0
    
        StartPopulation()
        
        while k:
            maom = 64
            maomi = 0
            miom = 64
            miomi = 0
            for z in range(1,kol):
                WaveStar(z)
            Сrossing()
            t+=1
            if t >= Solver_8_queens.max_epochs: 
                k = False
                best_fit = 1
                epoch_num = t
                if maomi == 0: vizualization = osob[miomi][1] #извините что не выводится с табуляцией
                else: vizualization = osob[maomi][1]
        return best_fit,epoch_num, vizualization
        


# In[4]:


#это функция создания стартовой популяции",
def StartPopulation():
        global osob,kol
        for x in range(1,kol):
            s = ''
            i = 0
            for u in range(0,64):
                s = s + random.choice(['+','Q'])
                if s[u-1] == 'Q': i += 1
                #if u % 8 == 0: s = s + '\n',
            osob[x] = i,s,'',64    


# In[5]:


def star(s): #проверка особи, сколько пересекающихся ферзей стоит на поле для каждого ферзя
    s ='~'+s
    i = s.count('Q')
    kolQ = 0
    while i!= 0:
            i = s.count('Q')
            k = s.find('Q')
            n1 = k-(k%8-1)
            n2 = k+(8-k%8)
            if n2 > 64: n2 = 64
            s = cut(s,k)
            kof = 7
            z =True
            j=1
            k7 = True
            k7m = True
            k9 = True
            k9m = True,
            while z:
                if (k-7*j>=0)and(k7m):
                        if s[k-7*j] == 'Q':
                            kolQ += 1
                        s = cut(s,k-7*j)
                if (k+7*j<=64)and(k7):
                        if s[k+7*j] == 'Q':
                            kolQ += 1
                        s = cut(s,k+7*j)
                if k+8*j<=64:
                        if s[k+8*j] == 'Q':
                            kolQ += 1
                        s = cut(s,k+8*j)
                if k-8*j>=0:
                        if s[k-8*j] == 'Q':
                            kolQ += 1
                        s = cut(s,k-8*j)
                if (k+9*j<=64)and(k9):
                        if s[k+9*j] == 'Q':
                            kolQ += 1
                        s = cut(s,k+9*j)
                if (k-9*j>=0)and(k9m):
                        if s[k-9*j] == 'Q':
                            kolQ += 1
                        s = cut(s,k-9*j)
                if k+1*j <= n2:
                        if s[k+1*j] == 'Q':
                            kolQ += 1
                        s = cut(s,k+1*j)
                if k-1*j >= n1:
                        if s[k-1*j] == 'Q':
                            kolQ += 1
                        s = cut(s,k-1*j)
                if ((k+7*j) % 8 == 1) or ((k+7*j) % 8 == 0): k7 = False
                if ((k-7*j) % 8 == 1) or ((k-7*j) % 8 == 0): k7m = False
                if ((k+9*j) % 8 == 1) or ((k+9*j) % 8 == 0): k9 = False
                if ((k-9*j) % 8 == 1) or ((k-9*j) % 8 == 0): k9m = False    
                if (k+7*j > 64)and(k-7*j<0)and(k+8*j > 64)and(k-8*j<0)and(k+9*j > 64)and(k-9*j<0)and(k-1*j<n1)and(k+1*j>n2): z =False
                j += 1
    return kolQ   


# In[6]:


#это функция проверки популяции на условие 8 ферзей
def WaveStar(z):
    global osob,kol,pod,minus,miom,miomi,k,maom,maomi
    if osob[z][0] <= 8: 
        pr(osob[z])
        osob[z] = osob[z][0],osob[z][1],'Подходит'
        pod.append(z)
        perOs = star(osob[z][1])
        if  maom > perOs : # >= если нужна последняя особь
            maom = perOs 
            maomi = z
            miom = osob[z][0]
            miomi = z
        osob[z] = osob[z][0],osob[z][1],'Подходит',perOs
    else: 
        pr(osob[z])
        osob[z] = osob[z][0],osob[z][1],'Мусор',64
        minus.append(z)
        if miom >= osob[z][0]: 
                miom = osob[z][0]
                miomi = z


# In[7]:


#это функция изменяет популяцию мутацией
def Сrossing():
    global osob,kol,pod,minus,miom,miomi,k,maom,maomi
    if (maom == 0)and(osob[maomi][1].count('Q') == 8): 
        print('Решение найдено ')
        print(osob[maomi])
        k=False
    s1 = osob[miomi][1]
    for x in range(1,kol):
        a = random.randint(1,63) 
        s2 = str(s1[0:a]) + random.choice(['+','Q']) + str(s1[a+1:len(s1)])
        osob[x] = s2.count('Q'),s2,'',64
    osob[kol-1] = s1.count('Q'),s1,'',maom


# In[8]:


def pr(g):
    print(g)


# In[9]:


def cut(s,k):
    s = str(s[0:k]) + '~' + str(s[k+1:len(s)])
    return s


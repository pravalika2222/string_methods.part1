# a='hi'
# print(a.capitalize())  # hi 

# b='hello'
# print(b.casefold())   # hello

# c='pravalika'
# print(c.center(10))    #    pravalika

# d='i love rabbit,rabbit is my favorite pet'
# print(d.count('rabbit'))     # 2

# e='hi,how are you.' 
# print(e.endswith('.'))  # true

# f='p\tr\ta\tv\ta'
# print(f.expandtabs(5))   # prava

# g='happy brithday'
# print(g.find('b'))   # 6

# h='hello, good morning'
# print(h.index('g'))  #  7

# i='computer12'
# print(i.isalnum()) # true,if all the charaters in string are alphanumeric 
# j='computer 12'
# print(j.isalnum()) # false

# k='rajesh' 
# print(k.isalpha()) # true
# l='rajesh23'
# print(l.isalpha()) # false

# m='2222'
# print(m.isdecimal()) # true
# n='p2222'
# print(n.isdecimal()) # false

# o='769'
# print(o.isdigit()) # true

# p='python'
# print(p.isidentifier()) # true
# q='9python'
# print(q.isidentifier()) # false

# r='beauty'
# print(r.islower()) # true

# s='BEAUTY'
# print(s.isupper()) # true

# t='657467'
# print(t.isnumeric()) # true

# u='  '
# print(u.isspace()) # true
# v='hey'
# print(v.isspace()) # false

# w='Hello,Welcome To World'
# print(w.istitle()) # true 
# x='HELLO,WELCOME TO WORLD'
# print(x.istitle()) # false

# p='mango'
# print(p.ljust(20,'0')) # mango00000000000000

# txt='    agra   '
# x=txt.lstrip()
# print('of all places',x,'is my favorite') # of all places agra   is my favorite

# a='hello friend'
# b=(a.maketrans('f','p'))
# print(a.translate(b))   # replace f answer priend

# p='i listen stories'
# print(p.replace('stories','songs')) # replace songs  i listen songs

# p='i want to eat maggi by tomorrow morning'
# r=p.partition('maggi')
# print(r)                # 'i want to eat','maggi','by tomorrow morning'

# f='pizza'
# s=f.rjust(15)
# print(s,'is my favorite food')   #             pizza is my favorite food

# a="hello!this is prava"
# print(a.rindex('prava'))  # 14

# v="i like rose flower"
# print(v.rfind('rose'))       # 7

# a='welcome to the zoo park'
# print(a.split())           # ['welcome','to','the','zoo','park']

# b= 'hello welcome\nto my house'
# print(b.splitlines())          # ['hello welcome','to my house]

# c='rat,cat,dog'
# print(c.rsplit(','))                 # ['rat','cat','dog']

# d='    kerela   '
# e=d.rstrip()
# print('my favorite place',e,'one of the best place') # my favorite place      kerela one of the best place

# a='bUrGer pIzzA sAnDwIcH FrEncH fRieS'
# print(a.swapcase())       #  BuRgER PiZZa SaNdWiCh fReNch FrIEs

# a='hello,welcome to party.'
# x=a.startswith('hello')
# print(x)                   # true

# a=("apple","orange","strawberry")
# x="#".join(a)
# print(x)                         #     apple#orange#strawbeery

# a='welcome to the world'
# print(a.title())     # starting letter is uppercase answer Welcome To The World

# a='267'
# p=a.zfill(12)
# print(p)                 # 000000000267

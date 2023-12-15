# set()
s = {1,2,3,4} #地一種，用大括號
print(s)
s = set( (1,3,5,7) ) #第二種用set( )，立面放要加入的東西，可用圓括號 tuple
print(s)
s = set( [1,2,3,4] ) #用set( )，可以用方括號
print(s)
s = set( 'Hello' ) #用set( )，也可以放字串，會把字拆開來
print(s)

#試試 .add() 和 .remove()
s.add(100)
print(s)
s.remove('H')
print(s)
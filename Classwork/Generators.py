'''def showfeed(l):
    for i in l:
        yield i
reels=['1....100','101....200','201....300','301....400','401....500','501....600','601....700']
nextfeed=showfeed(reels)
print(next(nextfeed))
print(next(nextfeed))
print(next(nextfeed))
print(next(nextfeed))
'''
def showfeed(l):
    for i in l:
        yield i
reels=['1....100','101....200','201....300','301....400','401....500','501....600','601....700']
nextfeed=showfeed(reels)

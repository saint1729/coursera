import numpy as np

def Reader(X, N, m):
    score=0
    if N!=15000:
        print('N is incorrect!')
    else:
        score+=1
    if m>10:
        print('Some features were not cleaned!')
    else:
        if m<10:
            print('Some feature are lost!')
        else:
            score+=1
    if X.shape[0]!=N or X.shape[1]!=m:
        print('Dimensions of the X matrix do not agree with N and m!')
    else:
        score+=1
    if score==3:
        print('All passed')
    print('Total check: ', score, '/3')

def lossOK(loss, X, y):
    score=0
    from time import time
    for i in range(10):
        w=np.random.uniform(0, 1, X.shape[1]+1)
        t1=time()
        lvu=loss(w, X, y)
        if not(isinstance(lvu, float)):
            print('Loss dimenstion mismatch!')
            print('Random test ', i, ':  FAILED DIMENSION')
        else:
            t2=time()
            lvt=np.sum(np.power(y-np.dot(np.concatenate([np.ones((X.shape[0], 1)), X], axis=1), w), 2))/X.shape[0]
            t3=time()
            if np.abs(lvu-lvt)/lvt<1e-2:
                print('Random test ', i, ':  OK, time_User=', t2-t1, 's;  timeBaseline=', t3-t2, 's')
                score+=1
            else:
                print('Random test ', i, ':  FAILED VALUE, time_User=', t2-t1, 's;  timeBaseline=', t3-t2, 's')
    if score==10:
        print('All passed')
    print('Total check: ', score, '/10')
    
def gradOK(grad, X, y):
    score=0
    from time import time
    for i in range(10):
        w_k=np.random.uniform(0, 1, X.shape[1]+1)
        t1=time()
        lvu=grad(w_k, X, y)
        if lvu.shape[0]!=X.shape[1]+1:
            print('Gradient dimenstion mismatch!')
            print('Random test ', i, ':  FAILED DIMENSION')
        else:
            t2=time()
            Xtmp=np.concatenate([np.ones((X.shape[0], 1)), X], axis=1)
            lvt=-2./X.shape[0]*(Xtmp.T.dot(y-Xtmp.dot(w_k)))
            t3=time()
            if np.sum(np.power(lvu-lvt, 2))/np.sum(np.power(lvt, 2))<1e-2:
                print('Random test ', i, ':  OK, time_User=', t2-t1, 's;  timeBaseline=', t3-t2, 's')
                score+=1
            else:
                print('Random test ', i, ':  FAILED VALUE, time_User=', t2-t1, 's;  timeBaseline=', t3-t2, 's')
    if score==10:
        print('All passed')
    print('Total check: ', score, '/10')

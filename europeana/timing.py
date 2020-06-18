from EuropeanaAPI import EuropeanaAPI

import time
#import matplotlib.pyplot as plt





eu = EuropeanaAPI('xCQ6FUorp')

x = list(range(1,10000,1000))
y = []
for i in x:
    start = time.time()
    #r = eu.search('Amsterdam',n = i)
    r = eu.search('Amsterdam',n = i, where = 'Spain')
    t = time.time()-start
    y.append(t)

    print(f'{i}')
    print(f'{t}')
    print(50*'-')



#print('requested results: {}'.format(r.n))
print('total number of results: {}'.format(r.totalResults))
print('parameters: {}'.format(r.params))
print('number of EDM objects: {}'.format(r.num_items))



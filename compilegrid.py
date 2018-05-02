import numpy as np


threshold = 0.3603

alist = np.linspace(threshold, 5*threshold, 21)

blist = np.linspace(0, threshold, 11)

endpointlist = [(a, b) for a in alist for b in blist]


np.set_printoptions(linewidth=400, precision = 3)

for functiontype in ['native', 'predicted', 'cubic', 'margin-0-00']:
    accuracyarray = np.zeros([21,11,16])
    for j, a in enumerate(alist):
        for k, b in enumerate(blist):
            f = open('results/%.3f-%.3f/%s-results.txt' % (a, b, functiontype), 'r')
            
            acclist = []
            
            for i, line in enumerate(f.readlines()):
                if i % 4 == 2:
                    splitline = line.split()
                    ppv, sen, acc = splitline[1:6:2]
                    #print(ppv, sen, acc)
                    acclist.append(float(acc))
            
            
                
            #acclist.append(np.mean(acclist))
            
            #print(a, b, functiontype)
            #print(acclist)
            
            accuracyarray[j,k] = acclist
            
            
            #print('%-24s' % (fi,) + '      '.join(['%0.3f' % (k,) for k in acclist]))
            
            f.close()
    print(np.average(accuracyarray, axis = -1))[::-1]
    print('\n')

print(alist[::-1])

print(blist)
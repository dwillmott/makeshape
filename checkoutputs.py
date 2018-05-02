import glob

filenames = ['noshape.txt',
             'exp-real-state.txt',
             'exp-pred-state.txt',
             #'expected.txt',
             #'expected-cube.txt',
             #'exp-quartic.txt',
             'margin-0-00.txt',
             'margin-0-05.txt',
             'margin-0-10.txt',
             'margin-0-15.txt',
             'margin-0-20.txt',
             'margin-0-25.txt',
             'margin-0-30.txt',
             'margin-0-35.txt',
             'margin-0-40.txt',
             'margin-0-45.txt',
             'margin-0-49.txt',
             'margin-0-50.txt',
             'cubic.txt',
             'quartic.txt',
             'cubic-pieces.txt'
             ]

filenames = ['margin-0-00-results.txt',
             'noshape-results.txt',
             'native-results.txt',
             'predicted-results.txt',
             'cubic-results.txt']

#filenames += glob.glob('results/*.txt')



#filenames += ['margin-0-' + str(mar) + '.txt' for mar in range(0, 55)]

#print(filenames)

zsnames = ['cuniculi', 'vnecatrix', 'celegans', 'nidulansM',
           'TabacumC', 'cryptomonasC', 'musM', 'gallisepticum',
           'syne', 'ecoli', 'subtilis', 'desulfuricans',
           'reinhardtiiC', 'maritima', 'tenax', 'volcanii']

print('file                    ' + '   '.join(['%-8.8s' % (z,) for z in zsnames]))

for fi in filenames:
    f = open(''+fi, 'r')
    
    acclist = []
    
    for i, line in enumerate(f.readlines()):
        if i % 4 == 2:
            acclist.append(float(line[-6:-1]))
        
    
    print('%-24s' % (fi,) + '      '.join(['%0.3f' % (k,) for k in acclist]))
    
    f.close()
    

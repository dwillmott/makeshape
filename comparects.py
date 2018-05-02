import numpy as np
import sys

tocompare = sys.argv[1]

def getpairs(structfile):
    real_struct_file = open(structfile, 'r');

    real_seq = []; 
    real_pairing = [];
    pairs = []

    firstline = real_struct_file.readline();

    for line in real_struct_file.readlines():
        splitline = line.split();
        position = int(splitline[0])
        pairedwith = int(splitline[4])
        if pairedwith and position < pairedwith:
            pairs.append((position, pairedwith))
    
    return set(pairs)


def printmetrics(native, predicted, name = None):
    tp = native.intersection(predicted)
    fn = native.difference(predicted)
    fp = predicted.difference(native)
    
    PPV = len(tp)/float(len(predicted))
    sen = len(tp)/float(len(native))
    accuracy = 0.5*(PPV + sen)
    
    return PPV, sen, accuracy

if __name__ == "__main__":

    zsnames = ['cuniculi', 'vnecatrix', 'celegans', 'nidulansM',
            'TabacumC', 'cryptomonasC', 'musM', 'gallisepticum',
            'syne', 'ecoli', 'subtilis', 'desulfuricans',
            'reinhardtiiC', 'maritima', 'tenax', 'volcanii']

    noshape_pairlist = []
    realstate_genshape_pairlist = []
    genstate_genshape_pairlist = []

    for zsname in zsnames:
        print('--------  %s  --------\n' % (zsname,))
        native_pairs = getpairs('zs/%s-native-nop.ct' % (zsname,))
        
        
        
        noshape_pairs = []
        realstate_genshape_pairlist = []
        genstate_genshape_pairlist = []
        
        comparison_pairs = getpairs('structures/%s/%s-%s.ct' % (tocompare, zsname, tocompare))
        metrics = printmetrics(native_pairs, comparison_pairs, tocompare)
        print('PPV: %0.3f     sen: %0.3f     acc: %0.3f\n' % tuple(metrics))
        
        #numpredictions = 300
        
        #for i in range(numpredictions):
            #num = str(i).zfill(3)
            #realstate_genshape_pairlist.append(set(getpairs('structurepredictions/%s/%s-realstate-genshape-%s.ct' % (zsname, zsname, num))))
            #genstate_genshape_pairlist.append(set(getpairs('structurepredictions/%s/%s-genstate-genshape-%s.ct' % (zsname, zsname, num))))
        
        #realstate_genshape_metriclist = np.array([printmetrics(native_pairs, p, 'Real state, gen SHAPE') for p in realstate_genshape_pairlist])
        #genstate_genshape_metriclist = np.array([printmetrics(native_pairs, p, 'Gen state, gen SHAPE') for p in genstate_genshape_pairlist])
        
        #realstate_genshape_avgs = np.mean(realstate_genshape_metriclist, axis=0)
        #realstate_genshape_std = np.std(realstate_genshape_metriclist, axis=0)
        #print('Real state, generated SHAPE')
        #print('PPV: %0.4f    sen: %0.4f    acc: %0.4f' % tuple(realstate_genshape_avgs))
        #print('  +/-%0.4f      +/-%0.4f      +/-%0.4f\n' % tuple(realstate_genshape_std))
        
        #genstate_genshape_avgs = np.mean(genstate_genshape_metriclist, axis=0)
        #genstate_genshape_std = np.std(genstate_genshape_metriclist, axis=0)
        #print('Generated state, generated SHAPE')
        #print('PPV: %0.4f    sen: %0.4f    acc: %0.4f' % tuple(genstate_genshape_avgs))
        #print('  +/-%0.4f      +/-%0.4f      +/-%0.4f\n' % tuple(genstate_genshape_std))
        
        #print('\n')
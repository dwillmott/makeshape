import os
import sys
import subprocess

subfolder = sys.argv[1]

zsnames = ['cuniculi', 'vnecatrix', 'celegans', 'nidulansM', 'TabacumC', 'cryptomonasC', 'musM', 'gallisepticum', 'syne', 'ecoli', 'subtilis', 'desulfuricans', 'reinhardtiiC', 'maritima', 'tenax', 'volcanii']

filepath = 'structures/%s' % (subfolder,)
shapefolder = 'shape/%s' % (subfolder,)
if not os.path.exists(filepath):
    os.makedirs(filepath)

for zsname in zsnames:
    runstring = 'gtmfe zs/%s-sequence.txt ' % (zsname,)
    outputstring = '--output %s/%s-%s' % (filepath, zsname, subfolder)
    
    print('\n\nmaking %s structure for %s \n\n' % (subfolder, zsname))
    
    if subfolder == 'noshape':
        subprocess.call(runstring + outputstring, shell=True)
    else:
        shapestring = ' --useSHAPE %s/%s-%s.shape' % (shapefolder, zsname, subfolder)
        subprocess.call(runstring + outputstring + shapestring, shell=True)
    
    
    
    #subprocess.call(runstring + outputstring + shapestring, shell=True)
    
    #for i in range(300):
        #num = str(i).zfill(3)
        #realstate_genshape = '--output structurepredictions/%s/%s-realstate-genshape-%s --useSHAPE SHAPEfiles/%.5s/realstate-%s.shape' % (zsname, zsname, num, zsname, num)
        #genstate_genshape = '--output structurepredictions/%s/%s-genstate-genshape-%s --useSHAPE SHAPEfiles/%.5s/predstate-%s.shape' % (zsname, zsname, num, zsname, num)
        
        #os.system(runstring + realstate_genshape)
        #os.system(runstring + genstate_genshape)
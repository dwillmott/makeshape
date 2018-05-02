import numpy as np
import subprocess
import os

threshold = 0.3603

alist = np.linspace(threshold, 4+threshold, 21)

blist = np.linspace(0, threshold, 11)

endpointlist = [(a, b) for a in alist for b in blist]

#print(alist)
#print(blist)



for a, b in endpointlist:
    a = 0.6624
    b = 0.214
    for shapetype in ['native', 'predicted', 'cubic']:
        #print("python makeshape.py %s %f %f" % (shapetype, a, b))
        #print("python makestructures.py %s" % (shapetype,))
        #print("python comparects.py %s > results/%.3f-%.3f/%s-results.txt" % (shapetype, a, b, shapetype))
        #print("\n")
        
        subprocess.call("python makeshape.py %s %f %f" % (shapetype, a, b), shell=True)
        
        subprocess.call("python makestructures.py %s" % (shapetype,), shell=True)
        
        subfolder = "results/%.3f-%.3f" % (a, b)
        if not os.path.exists(subfolder):
            os.makedirs(subfolder)
        
        subprocess.call("python comparects.py %s > results/%.3f-%.3f/%s-results.txt" % (shapetype, a, b, shapetype), shell=True)
        quit()
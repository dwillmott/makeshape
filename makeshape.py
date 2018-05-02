import os
import sys
import random
from math import exp, pow, sqrt, fabs

#probfile = functiontype
#name = sys.argv[2]

#to run this, python shape_generator_lstm.py volcanii-prob.txt volcanii

functiontype = sys.argv[1]

#a = 0.6624
#s = 0.3603
#b = 0.214

a = 0.6801
s = 0.3603
b = 0.222

if len(sys.argv) > 2:
    a = float(sys.argv[2])
    b = float(sys.argv[3])


print(a)
print(b)
print(functiontype)

resultfolder = 'shape/'+functiontype+'/';

if not os.path.exists(resultfolder):
    os.system('mkdir ' + resultfolder)

zsnames = ['cuniculi', 'vnecatrix', 'celegans', 'nidulansM',
           'TabacumC', 'cryptomonasC', 'musM', 'gallisepticum',
           'syne', 'ecoli', 'subtilis', 'desulfuricans',
           'reinhardtiiC', 'maritima', 'tenax', 'volcanii']

zslengths = [1295, 1244, 697, 1437, 1486, 1493, 956, 1519, 1488, 1542, 1553, 1551, 1474, 1562, 1503, 1474]


def pairedProb(x):
    s = 0.3603 #Threshold
    t = b
    if functiontype in ['native', 'predicted']:
        shape = t
    if 'margin' in functiontype:                                  # piecewise linear, margin around 0.5
        m = float(functiontype.split('-')[2])/100.0
        shape = ((t-s)/(0.5-m))*(x-1)+t if 0.5+m < x else s
    #elif functiontype == 'cubic':                                 # cubic, interpolate and f'(1) = 0
        #shape = -1.384*x*x*x + 4.024*x*x - 3.881*x + 1.468
    elif functiontype == 'quartic':                             # quartic spline, hermite + f''(1/2) = 0
        shape = t+(x-1)*(x-1)*(-4*t+4*s)+(x-1)*(x-1)*(x-0.5)*(-16*t+16*s)+(x-0.5)*(x-0.5)*(x-1)*(x-1)*(-48*t+48*s)
    elif functiontype == 'cubic':
        shape = t + (x-1)*(x-1)*4*(s-t) + (x-1)*(x-1)*(x-0.5)*16*(s-t)
    #Probability of being paired
    
    #m = 0.0
    #shape = 2*(a-s)*(x-0.5) + s                                        
    #shape = 1.928*x*x - 3.174*x + 1.468                                 # quadratic
    #shape = -1.384*x*x*x + 4.024*x*x - 3.881*x + 1.468                  
    #shape = t+(x-1)*(x-1)*(-4*t+4*s)+(x-1)*(x-1)*(x-0.5)*(-16*t+16*s)+(x-0.5)*(x-0.5)*(x-1)*(x-1)*(-48*t+48*s)   
    
    #shape = ((t-s)/(0.5-m))*(x-1)+t if 0.5+m <= x else s                 # piecewise linear, margin around 0.5
    return shape; #shape value between 0 and s

def unpairedProb(x):
    #Probability of being unpaired
    s = 0.3603
    t = a
    if functiontype in ['native', 'predicted']:
        shape = t
    if 'margin' in functiontype:                                  # piecewise linear, margin around 0.5
        m = float(functiontype.split('-')[2])/100.0
        shape = ((s-t)/(0.5-m))*x+t if x < 0.5-m else s
    #elif functiontype == 'cubic':                              # cubic, interpolate and f'(1) = 0
        #shape = -1.384*x*x*x + 4.024*x*x - 3.881*x + 1.468
    elif functiontype == 'quartic':                          # quartic spline, hermite + f''(1/2) = 0
        shape = t+x*x*(4*s-4*t)+x*x*(x-0.5)*(-16*s+16*t)+x*x*(x-0.5)*(x-0.5)*(-48*t+48*s)
    elif functiontype == 'cubic':
        shape = t + x*x*4*(s-t) + x*x*(x-0.5)*16*(t-s)
    #shape = t - (x/0.5)*(t-s); 
    #shape = -4*(t-s)*x**2 + t
    #shape = 1.928*x*x - 3.174*x + 1.468
    #shape = -1.384*x*x*x + 4.024*x*x - 3.881*x + 1.468
    #shape = t+x*x*(4*s-4*t)+x*x*(x-0.5)*(-16*s+16*t)+x*x*(x-0.5)*(x-0.5)*(-48*t+48*s)           # quartic spline, hermite + f''(1/2) = 0
    #shape = ((s-t)/(0.5-m))*x+t if x <= 0.5-m else s
    return shape; #shape value between s and 2
    

for zs, zslength in zip(zsnames, zslengths):
    probfile = 'probabilities/%s-prob.txt' % (zs,)
    name = zs
    
    #read in probability file
    prob_file = open(probfile, 'r');
    
    prob_file.readline()
    prob_file.readline()

    seq_index = []; 
    lstm_prob = [];
    
    
        
    if functiontype in ['native', 'predicted']:
        if functiontype == 'native':
            ind = 2
        elif functiontype == 'predicted':
            ind = 3
        
        for line in prob_file.readlines():
            if line != '\n':
                splitline = line.split();
                seq_index.append(int(splitline[0]));
                if splitline[ind] == 'U':
                    lstm_prob.append(float(0))
                elif splitline[ind] == 'P':
                    lstm_prob.append(float(1))
    
    else:
        for line in prob_file.readlines():
            if line != '\n':
                splitline = line.split();
                seq_index.append(int(splitline[0]));
                
                lstm_prob.append(float(splitline[5]));
        
    length = len(lstm_prob);

    prob_file.close();

    #open output file
    outfile = name+ '-%s.shape' % (functiontype,)
    output_file = open(resultfolder+outfile, 'w');

    #for each position, write a SHAPE value depending on the LSTM probability 
    for i in range(zslength):
        if lstm_prob[i] >= 0.5:
            shapevalue = pairedProb(lstm_prob[i]);
        elif lstm_prob[i] < 0.5:
            shapevalue = unpairedProb(lstm_prob[i]);    
        else:
            print 'error'
        position = seq_index[i];
        #print('%d %.3f \n' % (position, shapevalue))
        output_file.write('%d %.3f \n' % (position, shapevalue)); 

    output_file.close();


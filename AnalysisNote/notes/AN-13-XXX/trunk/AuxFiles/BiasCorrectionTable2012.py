import array
import os

# dictionary 
# key = filename with the correction parameters
# value = array ('double') filled vith the values of the parameters

scaleSetter = {}

# initialization
scaleSetter['MuScleFit_2011_DATA_44X.txt'] = array.array('d')
scaleSetter['MuScleFit_2011_MC_44X.txt'] = array.array('d')
scaleSetter['MuScleFit_2012ABC_DATA_ReReco_53X.txt'] = array.array('d')
scaleSetter['MuScleFit_2012D_DATA_ReReco_53X.txt'] = array.array('d')
scaleSetter['MuScleFit_2012_MC_53X_smearReReco.txt'] = array.array('d')

# loop on the available corrections
for k,v in scaleSetter.items():
#    file = open(os.path.join('MuScleFitCorrector_vX',k),'r')
    file = open(os.path.join('.',k),'r')
    lines = file.readlines()[2:29]   # this is the range relevant for the parameters of the bias corrections
    for line in lines:
        tmp=line.split("+-")
        text, value = tmp[0].split("value")
        v.append(float(value))

# the following parameters are related to the boundaries in eta
# debug #    print v[4], v[7], v[8], v[11], v[12], v[15], v[16]
    fvalue = v[7]*(v[4]-v[8])+v[11]*v[8]     
    v.append(fvalue) # 27
    fvalue = v[11]*v[8]     
    v.append(fvalue) # 28
    fvalue = v[11]*v[12]     
    v.append(fvalue) # 29
    fvalue = v[15]*(v[16]-v[12])+v[11]*v[12]     
    v.append(fvalue) # 30

    file.close()
    del lines [:]

parameterNames=[
('$p_0$',0), 
('$a_1$',1),  ('$\phi_1$',2),  ('$a_2$',21), ('$\phi_2$',23), ('$b$',3), 
('$\eta_0$ (fixed)',4), ('$b_0$',27),
('$a_1$',5),  ('$\phi_1$',6),  ('$b$',7),
('$\eta_0$ (fixed)',8), ('$b_0$',28),
('$a_1$',9),  ('$\phi_1$',10), ('$b$',11), 
('$a_1$',13), ('$\phi_1$',14), ('$b$',15), 
('$\eta_0$ (fixed)',12), ('$b_0$',29),
('$a_1$',17), ('$\phi_1$',18), ('$a_2$',24), ('$\phi_2$',26), ('$b$',19), 
('$\eta_0$ (fixed)',16), ('$b_0$',30),
('$\delta$',20), 
]







str = 'Sample'
#for ks in scaleSetter.iterkeys():
for ks in 'MuScleFit_2011_DATA_44X.txt', 'MuScleFit_2011_MC_44X.txt', 'MuScleFit_2012ABC_DATA_ReReco_53X.txt', 'MuScleFit_2012D_DATA_ReReco_53X.txt', 'MuScleFit_2012_MC_53X_smearReReco.txt':
    str += ' & '+ks[10:-4]
str += ' \\\\'
print str


for pn_pair in parameterNames:    
    str=pn_pair[0]
#for ks in scaleSetter.iterkeys():
    for ks in 'MuScleFit_2011_DATA_44X.txt', 'MuScleFit_2011_MC_44X.txt', 'MuScleFit_2012ABC_DATA_ReReco_53X.txt', 'MuScleFit_2012D_DATA_ReReco_53X.txt', 'MuScleFit_2012_MC_53X_smearReReco.txt':
        str += ' & %0.5f ' % scaleSetter[ks][pn_pair[1]]
#        str += ' & %g ' % scaleSetter[ks][pn_pair[1]]
    str += ' \\\\'
    print str


"""
\documentclass[12pt]{article}
\pagestyle{empty}
\begin{document}

\[
\kappa' = (1+p_0) \left(\kappa - C(\eta,\phi) -\frac{1}{2} \delta \right)
\]

\[
C(\eta,\phi) = a_1 \sin(\phi+\phi_1) + a_2 \sin(2\phi+\phi_2) + b (\eta-p_9)
\]
\end{document}
"""

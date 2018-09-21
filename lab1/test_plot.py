#display plots in notebook
import skrf as rf
%matplotlib inline
from pylab impor *
rf.stylely
net = rf.Network('FF-THRU.S2P')
net.plot_s_smith()

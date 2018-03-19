from scipy.signal import lti,step2,impulse2
import matplotlib.pyplot as plt

g1=lti([2],[1,2])
g2=lti([0.33],[0.2,1])
g3=lti([0.67],[10,1])
g=g1*(g2+g2*g3)
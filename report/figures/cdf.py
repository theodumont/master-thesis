import numpy as np
from scipy.special import erf
def cdf(mu, sigma):
    return lambda x: (1 + erf((x-mu) / (sigma*np.sqrt(2)))) / 2

mu1 = 1.45
mu2 = 1.7
sigma1 = 0.15
sigma2 = 0.07

fun1 = cdf(mu1, sigma1)
fun2 = cdf(mu2, sigma2)
xx = np.linspace(.9,2.1,100)
eps = 1e-2

res1 = fun1(xx)
print("for mu", 100 - (res1 >eps).sum(), "zeros")
print("for mu", 100 - (res1 <1-eps).sum(), "ones")
res2 = fun2(xx)
print("for nu", 100 - (res2 >eps).sum(), "zeros")
print("for nu", 100 - (res2 <1-eps).sum(), "ones")

tosave1 = np.stack([xx, res1],axis=1)
tosave2= np.stack([xx, res2],axis=1)
print(tosave1.shape)
np.savetxt("figures/1d-cdf-mu.csv", tosave1, delimiter=",")
np.savetxt("figures/1d-cdf-nu.csv", tosave2, delimiter=",")

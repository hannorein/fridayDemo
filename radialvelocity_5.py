# Import the rebound module
import numpy as np
import emcee
import rebound

data  = np.loadtxt("data.txt") #format: time [days]  velocity [m/s]

def lnprob(x):
    m, a = x
    if a <0.1 or a>10.:  # simplest prior 
        return -np.inf
    if m <1e-6 or m>1e-1: 
        return -np.inf
    rebound.reset()
    rebound.particle_add( m=1. )                    
    rebound.particle_add( m=m, x=a, vy=np.sqrt(1./a) ) 
    rebound.move_to_center_of_momentum()
    particles = rebound.particles_get()
    
    model = np.zeros(len(data)) 
    for i in xrange(len(data)):
        rebound.integrate(data.T[0][i]/58.130101)
        model[i] = particles[0].vx*29785.891   # to m/s

    return -np.sum(  (data.T[1]-model)**2  )

ndim, nwalkers = 2, 20
pos0 = [ [1e-3 + 1e-4*np.random.normal(), 1. + 1e-1*np.random.normal()] for i in xrange(nwalkers)]
sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob)
pos1, prob, state  = sampler.run_mcmc(pos0, 100)


import matplotlib; matplotlib.use("pdf")
import matplotlib.pyplot as pl

pl.plot(data.T[0],data.T[1],".")
print pos1.shape
for x in pos1:
    m, a = x
    rebound.reset()
    rebound.particle_add( m=1. )                    
    rebound.particle_add( m=m, x=a, vy=np.sqrt(1./a) ) 
    rebound.move_to_center_of_momentum()
    particles = rebound.particles_get()
    
    times = np.linspace(0,2000.,200)
    model = np.zeros(len(times)) 
    for i,t in enumerate(times):
        rebound.integrate(t/58.130101)
        model[i] = particles[0].vx*29785.891   # to m/s
    pl.plot(times,model,"r-", alpha=0.2)

pl.savefig("rv.pdf")

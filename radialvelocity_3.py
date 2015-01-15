# Import the rebound module
import rebound

rebound.particle_add( m=1. )                    # Star
rebound.particle_add( m=1e-3, x=1., vy=1. )     # Planet
rebound.move_to_center_of_momentum()

N = rebound.get_N()
particles = rebound.particles_get()

t = []
vr = []

while rebound.get_t()<30.:
    rebound.step()
    t.append(rebound.get_t())
    vr.append(particles[0].vx)

import matplotlib; matplotlib.use("pdf")
import matplotlib.pyplot as pl

pl.plot(t,vr)
pl.savefig("orbit.pdf")

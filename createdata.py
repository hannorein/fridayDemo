# Import the rebound module
import rebound
import random
import math

rebound.particle_add( m=1. )                    # Star
rebound.particle_add( m=3.2345e-3, x=1.5, vy=math.sqrt(1./1.5) )     # Planet
rebound.move_to_center_of_momentum()

N = rebound.get_N()
particles = rebound.particles_get()

while rebound.get_t()<30.:
    rebound.step()
    if random.random()>0.4:
        print rebound.get_t()*58.130101, random.normalvariate(0.,5.)+ particles[0].vx*29785.891


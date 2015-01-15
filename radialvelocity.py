# Import the rebound module
import rebound

rebound.particle_add( m=1. )                    # Star
rebound.particle_add( m=1e-3, x=1., vy=1. )     # Planet
rebound.move_to_center_of_momentum()
rebound.integrate(100.)

N = rebound.get_N()
particles = rebound.particles_get()

for i in range(N):
    print particles[i].x, particles[i].y, particles[i].z


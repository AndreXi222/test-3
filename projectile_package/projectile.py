
import numpy as np

def flying_mass(vx_initial, vy_initial, mass=1.0, k=0.035, dt=0.1):
    
    t = 0
    x, y = 0, 0
    vx, vy = vx_initial, vy_initial

    times, xs, ys, vxs, vys = [t], [x], [y], [vx], [vy]

    
    while y >= 0:
        ax = -np.sign(vx) * k * vx**2 / mass
        ay = -9.81 - np.sign(vy) * k * vy**2 / mass

        
        vx += ax * dt
        vy += ay * dt
        x += vx * dt
        y += vy * dt

        t += dt

        
        times.append(t)
        xs.append(x)
        ys.append(y)
        vxs.append(vx)
        vys.append(vy)

    return times, xs, ys, vxs, vys
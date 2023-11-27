
import numpy as np

def flying_mass(vx_initial, vy_initial, mass=1.0, k=0.035, dt=0.1):
    
    # initialize the time, the position of object in X axis, the position of object in Y axis, the velocity of object in X axis, the velocity of objecr in Y axis
    t = 0
    x = 0
    y = 0
    vx = vx_initial
    vy = vy_initial

    # Lists to store data of motion at each time step
    times, xs, ys, vxs, vys = [t], [x], [y], [vx], [vy]

    
    while y >= 0:
        #calculate the acceleration in x axis and y axis
        ax = -np.sign(vx) * k * vx**2 / mass
        #calculate velovity in x axis and y axis
        ay = -9.81 - np.sign(vy) * k * vy**2 / mass

        # object velocity in x axis
        vx += ax * dt
        # object velocity in y axis
        vy += ay * dt
        #update x axis velocity and y axis velocity
        x += vx * dt
        y += vy * dt
        #update time 
        t += dt

        #append data to each list
        times.append(t)
        xs.append(x)
        ys.append(y)
        vxs.append(vx)
        vys.append(vy)

    return times, xs, ys, vxs, vys
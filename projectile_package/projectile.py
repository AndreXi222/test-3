import numpy as np

def calculate_acceleration_x(v, k=0.0, mass=1.0):

    force_air = -np.sign(v) * k * v**2
    a = force_air / mass
    return a

def calculate_acceleration_y(v, k=0.0, mass=1.0, gravity=-9.81):
    
    force_gravity = mass * gravity
    force_air = -np.sign(v) * k * v**2
    total_force = force_gravity + force_air
    a = total_force / mass
    return a

def update_state(t, x, y, vx, vy, ax, ay, dt):
   
    x += vx * dt + 0.5 * ax * (dt**2)
    y += vy * dt + 0.5 * ay * (dt**2)
    vx += ax * dt
    vy += ay * dt
    t += dt
    return t, x, y, vx, vy

def flying_mass(vx0, vy0, k=0.0, mass=1.0, dt=0.1):
    
    x, y, vx, vy = 0, 0, vx0, vy0
    t = 0
    trajectory = []

    while y >= 0:  
        ax = calculate_acceleration_x(vx, k, mass)
        ay = calculate_acceleration_y(vy, k, mass, gravity=-9.81)
        t, x, y, vx, vy = update_state(t, x, y, vx, vy, ax, ay, dt)
        trajectory.append((t, x, y, vx, vy))

    return trajectory
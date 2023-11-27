mport matplotlib.pyplot as plt

def plot_xy(trajectory):
    
    x = [point[1] for point in trajectory]  
    y = [point[2] for point in trajectory]  
    
    plt.figure(figsize=(10, 6))  
    plt.plot(x, y, '-o')  
    plt.title('Projectile Motion')  
    plt.xlabel('X Position (m)')  
    plt.ylabel('Y Position (m)')  
    plt.grid(True)  
    plt.show()  
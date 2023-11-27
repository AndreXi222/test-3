import matplotlib.pyplot as plt

def plot_xy(x, y):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y)
    plt.title("Projectile Motion")
    plt.xlabel("X Position (m)")
    plt.ylabel("Y Position (m)")
    plt.grid(True)
    plt.show()
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def update_plot(frame, positions, velocities, sunMass, G, deltaT):
    # Unpack positions and velocities
    x, y = positions
    vx, vy = velocities
    
    # Calculate the distance between the Earth and the Sun
    r = math.sqrt(x**2 + y**2)
    
    # Calculate the force due to gravity
    force = G * sunMass / r**2
    
    # Calculate acceleration in both x and y directions
    ax = -force * (x / r)
    ay = -force * (y / r)
    
    # Update velocity
    vx = vx + ax * deltaT
    vy = vy + ay * deltaT
    
    # Update position
    x = x + vx * deltaT
    y = y + vy * deltaT
    
    # Update positions and velocities for the next frame
    positions[:] = [x, y]
    velocities[:] = [vx, vy]
    
    # Clear the plot and replot the points
    plt.clf()
    plt.plot(0, 0, marker="o", markersize=20, markeredgecolor="yellow", markerfacecolor="yellow")  # Sun
    plt.plot(x, y, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="green")  # Earth
    plt.gca().axes.xaxis.set_visible(False)
    plt.gca().axes.yaxis.set_visible(False)
    plt.xlim(-1.6e11, 1.6e11)
    plt.ylim(-1.6e11, 1.6e11)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Planet orbit around a sun")
    
    return plt

def velocitySim():
    # Initial conditions
    x = 1.5146 * 10**11  # Initial position of Earth (meters)
    y = 0
    sunMass = 1.9891 * 10**30  # Mass of the Sun (kg)
    G = 6.67430 * 10**-11  # Gravitational constant (m^3 kg^-1 s^-2)
    deltaT = 86400  # Time step (1 day in seconds)
    vx = 0             # Initial x velocity (m/s)
    vy = 2.80 * 10**4  # Initial y velocity (m/s)
    
    positions = [x, y]
    velocities = [vx, vy]
    
    fig = plt.figure()
    ani = animation.FuncAnimation(fig, update_plot, fargs=(positions, velocities, sunMass, G, deltaT), interval=50, cache_frame_data=False)
    
    plt.show()

velocitySim()
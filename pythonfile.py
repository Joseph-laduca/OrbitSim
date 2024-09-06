import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def calculatePos(positions, velocities, sunMass, G, deltaT):
    x, y = positions
    vx, vy = velocities
    
    # Calculate the distance between the Planet and the Sun
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
    

def update_plot(frame, positionsEarth, velocitiesEarth,positionsMercury,velocitiesMercury,  positionsVenus, velocitiesVenus,
    positionsMars,velocitiesMars, sunMass, G, deltaT):
    calculatePos(positionsEarth, velocitiesEarth, sunMass, G, deltaT)
    calculatePos(positionsMercury,velocitiesMercury, sunMass, G, deltaT)
    calculatePos(positionsVenus,velocitiesVenus, sunMass, G, deltaT)
    calculatePos(positionsMars, velocitiesMars, sunMass, G, deltaT)

    xEarth, yEarth =positionsEarth
    xMercury, yMercury = positionsMercury
    xVenus, yVenus = positionsVenus
    xMars, yMars = positionsMars
    
    # Clear the plot and replot the points
    plt.clf()

    plt.plot(0, 0, marker="o", markersize=20, markeredgecolor="yellow", markerfacecolor="yellow")  # Sun
    plt.plot(xEarth, yEarth, marker="o", markersize=10, markeredgecolor="blue", markerfacecolor="green")  # Earth
    plt.plot(xMercury, yMercury, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="grey") # Mercury
    plt.plot(xVenus, yVenus, marker="o", markersize=10, markeredgecolor="white", markerfacecolor="orange") #Venus
    plt.plot(xMars, yMars, marker="o", markersize=10, markeredgecolor="black", markerfacecolor="red") #Mars

    plt.gca().axes.xaxis.set_visible(False)
    plt.gca().axes.yaxis.set_visible(False)

    plt.xlim(-2.5e11, 2.5e11)
    plt.ylim(-2.5e11, 2.5e11)

    plt.gca().set_aspect('equal', adjustable='box')
    plt.title("Planets orbit around the sun")
    
    return plt

def velocitySim():
    # Initial conditions
    xearth = 1.49597 * 10**11  # Initial position of Earth (meters)
    yearth = 0

    xmercury = 4.9097 * 10**10 # Initial position of mercury (meters)
    ymercury = 0

    xvenus = 1.0815 * 10**11 # Initial position of venus (meters)
    yvenus = 0

    xmars = 2.2043 * 10**11 # Initial position of mars (meters)
    ymars = 0

    sunMass = 1.9891 * 10**30  # Mass of the Sun (kg)
    G = 6.67430 * 10**-11  # Gravitational constant (m^3 kg^-1 s^-2)
    deltaT = 86400  # Time step (1 day in seconds)

    vxearth = 0             # Initial x velocity (m/s)
    vyearth = 2.80 * 10**4  # Initial y velocity (m/s)

    vxmercury = 0
    vymercury = 4.6 * 10**4

    vxvenus = 0
    vyvenus = 3.4 * 10**4

    vxmars = 0
    vymars = 2.3 * 10**4

    positionsEarth = [xearth, yearth]
    velocitiesEarth = [vxearth, vyearth]

    positionsMercury = [xmercury, ymercury]
    velocitiesMercury = [vxmercury, vymercury]

    positionsVenus = [xvenus, yvenus]
    velocitiesVenus = [vxvenus, vyvenus]

    positionsMars = [xmars, ymars]
    velocitiesMars = [vxmars, vymars]
    
    fig = plt.figure()
    ani = animation.FuncAnimation(fig, update_plot, fargs=(positionsEarth, velocitiesEarth,positionsMercury,velocitiesMercury,  positionsVenus, velocitiesVenus,
    positionsMars,velocitiesMars,  sunMass, G, deltaT), interval=50,cache_frame_data=False)
    
    plt.show()

velocitySim()

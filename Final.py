
# N body simulation
# generate N Particles
# each Particle has mass M and charge Q
# each particle interacts with each other particle by pulling/pushing each other
# each particle moves according to coulombs law and newtons law of gravitation
#in an x-y plane

#Extra things to do (ranked in order from easiest to implement):
# 1) make coulombs constant and newtons constant scalable
# 2) make the size of the objects proportional to the mass value
# 3) show electric and gravitational field lines


import numpy as np
import matplotlib.pyplot as plt


def get_accel(pos,Mass,G,Softening,N):
    #pos matrix of all initial positions (only initial until function is called)
    #mass matrix of all particle masses
    #G gravitational constant
    #Softening "Minimum Distance" parameter, makes it so that a doesnt blow up as dist -> 0
    #N number of particles
    # this function will do one time step of the accelarations, doing this multiple times will advance the system in time

    accel = np.zeros((N,3)) # initial starting accel provides matrix full of 0's

    for i in range(N):
        # for every particle i, calculate the acceleration due to every other particle, j
        for j in range(N):
            # component distances from the jth particle to the ith particle
            dx = pos[j,0] - pos[i,0]
            dy = pos[j,1] - pos[i,1]
            dz = pos[j,2] - pos[i,2]
            m = Mass[j]
            dist = (dx**2+dy**2+dz**2+Softening**2)**(-3/2) #just multiply by dist, includes 1/ in the negative sign


            # += in this context means add this value to the original value everytime the function is called

            accel[i,0] += G * m * dx * dist #accel in x for ith particle
            accel[i,1] += G * m * dy * dist #accel in y for ith particle
            accel[i,2] += G * m * dz * dist #accel in z for ith particle

    return accel



# main body of simulation
def main():

    # set parameters
    N = 20              # Number of Particles
    t = 0
    tFinal = 10         # start at 0 seconds and go to 10 seconds
    dt = 0.1            #timestep value
    Softening = 0.1     # "minimum distance"
    G = 1               # value of the gravitational constant
    plotRealTime = True # to plot graphs as the simukation advances

    #initial conidtions
    np.random.seed(13)

    Mass = 25 * np.ones((N,1))/N   #gives uniform mass distribution, every particle has mass 25/N
    pos = np.random.randn(N,3)     # random number for particle position
    vel = np.random.randn(N,3)

    vel -= np.mean(Mass * vel,0) / np.mean(Mass) # covnerting to COM frame
    acc = get_accel(pos,Mass,G,Softening,N)         # provide initial acceleration before particles start moving

    # number of timesteps (frames)
    Nt = int(np.ceil(tFinal/dt))

    #save particle locations so we can animate them later
    pos_save = np.zeros((N, 3, Nt + 1)) #like a 3d brick where each slice of the brick is a frame/ all positions at time t
    pos_save[:, :, 0] = pos
    t_all = np.arange(Nt + 1) * dt # list of incremented time steps t = (0.1s,0.2s,....)

    #matplotlib figure settings
    fig = plt.figure(figsize=(8, 8), dpi=100)
    ax1 = plt.subplot()


    #timestepper loop
    for i in range(Nt):
        vel = vel + acc * dt / 2.0 # step once updating the velocity with the velocity from before

        pos = pos + vel * dt    # update position using velocity from before

        acc = get_accel(pos, Mass, G, Softening,N)  # update acceleration

        vel = vel + acc * dt / 2.0  #update veloctiy with new acceleration
        t = t + dt  #advance time

        #save position trail
        pos_save[:, :, i + 1] = pos #saves the current position as a frame in the 3d brick with position i+1

        #plot in real time
        if plotRealTime or (i == Nt - 1):
            plt.sca(ax1)
            plt.cla()

            # the max bit makes it so that not ALL of the trails are saved, and the start dissappearing after more than 50 timesteps have elapsed
            xx = pos_save[:, 0, max(i - 50, 0):i + 1] #save all saved positions up until the current one as xx
            yy = pos_save[:, 1, max(i - 50, 0):i + 1] #save all saved positions up until the current one as yy
            print(xx)

            plt.scatter(xx, yy, s=1, color=[.7, .7, 1])             #plot previous point from possave (trail, light blue)
            plt.scatter(pos[:, 0], pos[:, 1], s=10, color='blue')   #plot current points (dot, dark blue)


            ax1.set(xlim=(-4, 4), ylim=(-4, 4))
            ax1.set_aspect('equal', 'box')
            ax1.set_xticks([-4,-3,-2, -1, 0, 1, 2,3,4])
            ax1.set_yticks([-4,-3,-2, -1, 0, 1, 2,3,4])

            plt.pause(0.01)  # this loop basically just updates the graph every 0.001 seconds, creating a new graph. however the pos save allows you to update the next frame with the position of the particle in the old frame

    plt.show()

    return 0




main()







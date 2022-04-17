
# N body simulation
# generate N Particles
# each Particle has mass M and charge Q
# each particle interacts with each other particle by pulling/pushing each other
# each particle moves according to coulombs law and newtons law of gravitation
#in an x-y plane

#Extra things to do (ranked in order from easiest to implement
# 2.5 ) make graphs of the distributions (average velocity/ KE, AVG energy (constant) + ke and pe vs time)

#THIS ONE MAKES THE 2D SIMULATION

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def get_accel(pos,Mass,G,Softening,N,Charge,K):
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
            qm1 = Charge[i]/Mass[i]
            q2 = Charge[j]

            dist = (dx**2+dy**2+dz**2+Softening**2)**(-3/2) #just multiply by dist, includes 1/ in the negative sign


            # += in this context means add this value to the original value everytime the function is called

            accel[i,0] += (G * m * dx * dist) - (K * qm1 * q2 * dx * dist)  #accel in x for ith particle
            accel[i,1] += (G * m * dy * dist) - (K * qm1 * q2 * dy * dist)  #accel in y for ith particle
            accel[i,2] += (G * m * dz * dist) - (K * qm1 * q2 * dz * dist)  #accel in z for ith particle

    return accel



# main body of simulation
def main():

    # set parameters
    N = 8               # Number of Particles
    t = 0
    tFinal = 10         # start at 0 seconds and go to 10 seconds
    dt = 0.1            #timestep value
    Softening = 0.1     # "minimum distance"
    G = 1               # value of the gravitational constant
    K = 10
    plotRealTime = True # to plot graphs as the simukation advances

    #initial conidtions
    np.random.seed(13)
    Mass = np.ones((N, 1))
    for i in range(N):
        Mass[i] = np.random.randint(1,25)

    pos = np.random.randn(N,3)     # random number for particle position
    vel = np.random.randn(N,3)
#--------- loop below gives a charge array with uniform charge where 1/2 is negative and 1/2 is positive
    Charge = np.ones((N, 1))
    for i in range(N):
        Charge[i] = 25 * np.random.uniform(-1,1)

#---------
    vel -= np.mean(Mass * vel,0) / np.mean(Mass) # covnerting to COM frame
    acc = get_accel(pos,Mass,G,Softening,N,Charge,K)         # provide initial acceleration before particles start moving

    # number of timesteps (frames)
    Nt = int(np.ceil(tFinal/dt))

    #save particle locations so we can animate them later
    pos_save = np.zeros((N, 3, Nt + 1)) #like a 3d brick where each slice of the brick is a frame/ all positions at time t


    pos_save[:, :, 0] = pos
    t_all = np.arange(Nt + 1) * dt # list of incremented time steps t = (0.1s,0.2s,....)

    #matplotlib figure settings
    fig = plt.figure(figsize=(8, 8), dpi=100)
    fig.suptitle('N-Body Simulation', color="Black",font="serif",size="20")
    #fig.set_title("K/G = ")
    fig.text(0.42, 0.93, "K/G = {}".format(K/G), ha='left', va='top',size="10")

    fig.patch.set_facecolor('xkcd:beige')
    ax1 = plt.subplot()


    #timestepper loop
    for i in range(Nt):
        vel = vel + acc * dt / 2.0 # step once updating the velocity with the velocity from before

        pos = pos + vel * dt    # update position using velocity from before

        acc = get_accel(pos, Mass, G, Softening,N,Charge,K)  # update acceleration

        vel = vel + acc * dt / 2.0  #update veloctiy with new acceleration
        t = t + dt  #advance time

        #save position trail
        pos_save[:, :, i + 1] = pos #saves the current position as a frame in the 3d brick with position i+1

        #plot in real time
        if plotRealTime or (i == Nt - 1):
            plt.sca(ax1)
            plt.cla()


            # the max bit makes it so that not ALL of the trails are saved, and the start dissappearing after more than 50 timesteps have elapsed
            # code before seperating into pos and neg
            '''
            xx = pos_save[:, 0, max(i - 50, 0):i + 1] #save all saved positions up until the current one as xx
            yy = pos_save[:, 1, max(i - 50, 0):i + 1] #save all saved positions up until the current one as yy
            #plt.scatter(xx, yy, s=1, color=[.7, .7, 1])             #plot previous point from possave (trail, light blue)
            #plt.scatter(pos[:, 0], pos[:, 1], s=10, color='black')   #plot current points (dot, dark blue)
            '''

            for j in (range(len(Charge))):
                if Charge[j] < 0:
                    xneg = pos_save[j,0,max(i - 40, 0):i + 1]
                    yneg = pos_save[j, 1, max(i - 40, 0):i + 1]
                    plt.scatter(xneg, yneg, s=Mass[j]*1, color=[.7, .7, 1],zorder=5,marker="x")
                    plt.scatter(pos[j, 0], pos[j, 1], s= Mass[j]*10, color='blue',edgecolors='black',zorder = 20)
                if Charge[j] >= 0:
                    xpos = pos_save[j, 0, max(i - 40, 0):i + 1]
                    ypos = pos_save[j, 1, max(i - 40, 0):i + 1]
                    plt.scatter(xpos, ypos, s=Mass[j]*1, color=[1, .7, .7],zorder=5,marker="x")
                    plt.scatter(pos[j, 0], pos[j, 1], s=Mass[j]*10, color='red',edgecolors='black',zorder = 20)



            ax1.set(xlim=(-4, 4), ylim=(-4, 4))
            ax1.set_aspect('equal', 'box')
            ax1.set_xticks([-4,-3,-2, -1, 0, 1, 2,3,4])
            ax1.set_yticks([-4,-3,-2, -1, 0, 1, 2,3,4])

            red_patch = mpatches.Patch(color='red', label='Positive Charge')
            blue_patch = mpatches.Patch(color='blue', label='Negative Charge')
            ax1.legend(handles=[red_patch, blue_patch],loc="lower left")

            plt.pause(0.01)  # this loop basically just updates the graph every 0.01 seconds, creating a new graph. however the pos save allows you to update the next frame with the position of the particle in the old frame
    #plt.get_current_fig_manager().full_screen_toggle()



    plt.show()

    return 0




main()








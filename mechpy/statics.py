# coding: utf-8

'''
Module to be used for static analysis
'''
import numpy as np
import sympy as sp
import scipy
import matplotlib.pyplot as plt
from matplotlib import patches
from mpl_toolkits.mplot3d import Axes3D  
    
def simple_support():
    L = 15
    P = 5
    Ploc = 5
    
    plt.rcParams['figure.figsize'] = (10, 8)  # (width, height)
    
    fig1 = plt.figure()
    ax1 = fig1.add_subplot(311)#, aspect='equal')
    
    def add_beam():
        #plt.subplot(3,1,1)
        #ax = plt.gca()
        
        plt.xlim([-1, L+1])
        plt.ylim([-1, P*2])
        
        # add rigid ground
        rectangle = plt.Rectangle((-1, -2), L+2, 2, hatch='//', fill=False)
        ax1.add_patch(rectangle)
        
        # add rigid rollers
        #circle = plt.Circle((0, 5), radius=1, fc='g')
        #ax.add_patch(circle)
        e1 = patches.Ellipse((0, 2), L/20, 4, angle=0, linewidth=2, fill=False, zorder=2)
        ax1.add_patch(e1)
        
        # add triangle
        points = [[L, 4], [L-L/40, 0], [L+L/40,0]]
        polygon = plt.Polygon(points, fill=False)
        ax1.add_patch(polygon)
        
        # add beam
        rectangle = plt.Rectangle((0, 4), L, 4, fill=False)
        ax1.add_patch(rectangle)
    
    def point_load():
        # point load shear
        x = np.linspace(0,L,100)
        y = np.ones(len(x))*P/2
        y[x>Ploc] = y[x>Ploc]-P
        x[0]=0
        x[-1]=0
        
        plt.subplot(3,1,2)
        plt.ylabel('Shear, V')
        plt.title('Shear Diagram')
        plt.fill(x, y, 'b', alpha=0.25)
        plt.grid(True)
        plt.xlim([-1, L+1])
        
        # point load bending
        x = np.linspace(-L/2,L/2,100)
        y = -(x**2)+(np.max(x**2))
        x = np.linspace(0,L,100)
        plt.subplot(3,1,3)
        plt.title('Bending Diagram')
        plt.ylabel('Moment, M')
        plt.fill(x, y, 'b', alpha=0.25)
        plt.grid(True)
        plt.xlim([-1, L+1])    
        
        # add point load
        plt.subplot(3,1,1)
        plt.annotate('P=%i'%P, ha = 'center', va = 'bottom',
                     xytext = (Ploc, 15), xy = (Ploc,7.5),
                    arrowprops = { 'facecolor' : 'black', 'shrink' : 0.05 })    
        plt.title('Free Body Diagram')
        plt.axis('off') # removes axis and labels       
        
        #    # add point load
        #    ax1.arrow(3, 11+L/10, 0, -3, head_width=L*0.02, head_length=L*0.1, fc='k', ec='k')
        #    plt.title('Free Body Diagram')
        #    plt.axis('off') # removes axis and labels
        #    #ax1.set_yticklabels('')            
    
    def dist_load():
        
                # add distributed load
        plt.subplot(3,1,1)
        for k in np.linspace(0,L,20):
            ax1.arrow(k, 11+L/10, 0, -3, head_width=L*0.01, head_length=L*0.1, fc='k', ec='k')
        plt.title('Free Body Diagram')
        plt.axis('off') # removes axis and labels
        #ax1.set_yticklabels('') 
        
        # dist load shear
        x = [0,0,L,L]
        y = [0,5,-5,0]
        plt.subplot(3,1,2)
        plt.ylabel('Shear, V')
        plt.title('Shear Diagram')
        plt.fill(x, y, 'b', alpha=0.25)
        plt.grid(True)
        plt.xlim([-1, L+1])
        
        # dist load bending
        x = np.linspace(-L/2,L/2,100)
        y = -(x**2)+(np.max(x**2))
        x = np.linspace(0,L,100)
        plt.subplot(3,1,3)
        plt.title('Bending Diagram')
        plt.ylabel('Moment, M')
        plt.fill(x, y, 'b', alpha=0.25)
        plt.grid(True)
        plt.xlim([-1, L+1])
        
    add_beam()
    dist_load()
    #point_load()
    plt.tight_layout()
    plt.show()
    
def moment_calc():

    fig = plt.figure()
    
    ax = plt.axes(projection='3d')
    
    # bar
    x=[0,0,4,4]
    y=[0,5,5,5]
    z=[0,0,0,-2]
    
    # Applied Forces
    X=[0,0,4]
    Y=[5,5,5]
    Z=[0,0,-2]
    U=[-60,0 ,80]
    V=[40 ,50,40]
    W=[20 ,0 ,-30]
    
    ax.plot(x, y, z, '-b', linewidth=5)
    ax.view_init(45, 45)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Hibbler pg 129 example')
    ax.set_xlim([min(X)-2, max(X) + 2])
    ax.set_ylim([min(Y)-5, max(Y) + 2])
    ax.set_zlim([min(Z)-2, max(Z) + 2])
    
    #plt.tight_layout()
    
    ax.quiver3D(X, Y, Z, U, V, W, pivot='tail');
    
    rA = np.array([0,5,0])  # start of F1 and F2
    rB = np.array([4,5,-2])  # start of F3
    F1 = np.array([-60,40,20])
    F2 = np.array([0,50,0])
    F3 = np.array([80,40,-30])
    M = np.cross(rA,F1) + np.cross(rA,F2) + np.cross(rB,F3)
    print('Total Moment vector') 
    print(M)
    
    print('Total Force Vector about point O')
    print(sum([F1,F2,F3]))
    
    print('unit vector of the moment')
    u = M/np.linalg.norm(M)
    print(u)
    
    print('angles at which the moments react')
    print(np.rad2deg(np.arccos(u)))
    
    
if __name__ == '__main__':
    # executed when script is run alone
    #moment_calc()
    simple_support()
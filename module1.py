from matplotlib import pyplot as plt
from math import sin,cos,tan,sqrt,radians,degrees,asin ,atan#needed for definition of pi
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

v0=133
g=10
a=45
x0=12
y0=13
Hmax=40
f_type1='sobachka\n'
def ReadTXT(filename):
    global v0,a,x0,y0
    f=open(filename,"r")
    com = f.readline()
    nums=f.readline().split()    
    if com==f_type1:  
        v0=int(nums[0])
        a=radians(int(nums[1]))
        x0=int(nums[2])
        y0=int(nums[3])
    else:
        print("ERROR: file content invalid")
    f.close()
def WriteTXT(filename):
    global v0,a,x0,y0
    f=open(filename,"w")
    f.write(f_type1)
    f.write(str(v0)+" "+str(degrees(a))+" "+str(x0)+ " "+str(y0))
    f.close()    


def ReadNPZ(npzname):
    global x,y
    npa=np.load(npzname)
    x=npa['x1']
    y=npa['y1']
def WriteNPZ(npzname):
    global x,y
    np.savez(npzname,x1=x,y1=y)
    ##TODO:Добавить x0,y0##
def Solve1(T,Hmax,A):
    v0=g*T/2*sin(A)
    l=v0*cos(A)*T
    print(l)
def Solve2(T,Hmax,l):
    A=atan(sqrt(Hmax*T**2/L**2*2*g))
    print(A)
def Solve3(T,A,l):
    v0=g*T/2*sin(A)
    Hmax=v0**2*sin(A)**2/2*g
    print(Hmax)
def Solve4(Hmax,A,l):
    v0=sqrt(L*g/2*sin(A)*cos(A))
    T=L/v0*cos(A)
    print(T)

print(v0,a,x0,y0)
L=x0+v0*cos(a)*(v0*sin(a)/g + sqrt(v0**2*sin(a)**2/g**2 + 2*y0/g))



X = np.arange(x0, L, 0.05)
#x = np.arange(0, )
Y = y0+(X-x0)*tan(a)-(g/(2*(v0**2)*cos(a)**2)*(X-x0)**2)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=20, metadata=dict(artist='Me'), bitrate=1800)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.title('trajectory')
plt.show()

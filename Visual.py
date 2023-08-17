from tkinter import *
import matplotlib 
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import tkinter as tk
from matplotlib import pyplot as plt
import numpy as np
from tkinter import filedialog as fd
from tkinter import messagebox as mb
from pathlib import Path
import webbrowser
from matplotlib.animation import FuncAnimation

from math import sin,cos,tan,sqrt,radians,degrees,asin,atan
##Initialization##
class Menu(Tk):
    def __init__(self):
        super().__init__()

#root.geometry("500x500")
        
        #Mbutton3
        ##LabelRegion##
        Mlabel1=Label(self,text="Главное Меню")
        Mlabel1.place(x=205,y=0)
        ##Functios##
        def Grafic(event):
            buildg=BuildGraphic(self)
            buildg.geometry("900x600")
            buildg.resizable(0,0)
            buildg.title('Построение графика, без учёта сопротивления среды')
            buildg.mainloop()
        def GraficOUT(event):
            buildg1=BuildGraphicOUT(self)
            buildg1.geometry("900x600")
            buildg1.resizable(0,0)
            buildg1.title('Построение графика, с учётом сопротивления среды')
            buildg1.mainloop()
        def Salvation(event):
            solvator=Solve(self)
            solvator.geometry("500x500")
            solvator.resizable(0,0)
            solvator.title('Решение задач')
            solvator.mainloop()
        def CloseProgramm():
            self.destroy()
        def Theory():
            theory=TheoryBox(self)
            theory.geometry("600x500")
            theory.resizable(0,0)
            theory.title('Блок теории')
            theory.mainloop()
            
        ##Binds##
        ##ButtonRegion##
        #StartMenuButtons#
        Mbutton1=Button(self,text="Построение графика,\n без учёта сопротивления \n среды",width=20,height=3)
        Mbutton1.place(x=170,y=50)
        Mbutton2=Button(self,text="Решение задач",width=20,height=3)
        Mbutton2.place(x=170,y=205)
        Mbutton3=Button(self,text="Блок Теории",width=20,height=3,command=Theory)
        Mbutton4=Button(self,text="Построение графика,\n с учётом сопротивления \n среды",width=20,height=3)
        Mbutton5=Button(self,text="Выход",width=20,height=3,command=CloseProgramm)

        
        Mbutton4.place(x=170,y=105)
        Mbutton5.place(x=170,y=280)
        Mbutton1.bind('<Button-1>',Grafic)
        Mbutton2.bind('<Button-1>',Salvation)
        Mbutton4.bind('<Button-1>',GraficOUT)   
        
        Mbutton3.place(x=170,y=155)
class BuildGraphic(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        ##Labels##
        
        Blabel=Label(self, text="Построение графиков")
        
        Blabel1=Label(self, text="(Начальное положение по оси х,м) x0=")
        Blabel2=Label(self, text="(Начальное положение по оси y,м) y0=")
        Blabel3=Label(self, text="(Начальная скорость,м/с) V0=")
        Blabel4=Label(self, text="(Угол, под которым брошено тело, градусы) A=")
        Blabel5=Label(self)
        Blabel6=Label(self)
        Blabel7=Label(self)
        Blabel.place(x=200,y=0)
        
        Blabel1.place(x=47,y=40)
        Blabel2.place(x=47,y=60)
        Blabel3.place(x=97,y=80)
        Blabel4.place(x=0,y=100)

        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot()

        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        
        canvas.get_tk_widget().place(x=350,y=50)
 
        ##Entries##
        Entry1=Entry(self,width=7)
        Entry2=Entry(self,width=7)
        Entry3=Entry(self,width=7)
        Entry4=Entry(self,width=7)
        Entry1.place(x=270,y=40)
        Entry1.focus_set()
        Entry2.place(x=270,y=60)
        Entry3.place(x=270,y=80)
        Entry4.place(x=270,y=100)
        ##Buttons##
        def CloseProgramm():
            self.destroy()
        
        def Build():
            if Entry1.get()=="":
                 mb.showerror(
                    "Ошибка", 
                    "Поля не должны быть пустыми")
            elif Entry2.get()=="":
                 mb.showerror(
                    "Ошибка", 
                    "Поля не должны быть пустыми")
            elif Entry3.get()=="":
                 mb.showerror(
                    "Ошибка", 
                    "Поля не должны быть пустыми")
            elif Entry4.get()=="":
                 mb.showerror(
                    "Ошибка", 
                    "Поля не должны быть пустыми")
            else:
                x0=float(Entry1.get())
                y0=float(Entry2.get())
                v0=float(Entry3.get())
                a=radians(float(Entry4.get()))
                g=10
                T=(sqrt((v0**2*sin(a)**2)+(2*g*y0))+v0*sin(a))/g
                L=v0*cos(a)*T
                Hmax=y0+(v0**2*sin(a)**2/(2*g))
                
                t=np.arange(0,T,T/500)
                x = x0 + v0*cos(a)*t
                y = y0 + v0*sin(a)*t - g*t**2/2
                fig = plt.Figure(figsize = (5, 5), 
                 dpi = 100)     
                def init():
                    line.set_data([], [])
                    return line,
                def animate(i):
                    line.set_data(x[:i], y[:i])
                    return line,
               
                Blabel5.place(x=10,y=120)
                Blabel6.place(x=10,y=140)
                Blabel7.place(x=10,y=160)
                Blabel5.config(text="(Дальность полёта, м) L="+str(float('{:.3f}'.format(L))))
                Blabel6.config(text="(Высота подъёма, м) Hmax="+str(float('{:.3f}'.format(Hmax))))
                Blabel7.config(text="(Полное время полёта, с) T="+str(float('{:.3f}'.format(T))))

                canvas = FigureCanvasTkAgg(fig, self)
                canvas.get_tk_widget().place(x=350,y=50)
                ax = fig.add_subplot(111)
                ax.set_title('Траектория тела')
                ax.set_xlabel('Дальность')
                ax.set_ylabel('Высота')
                line, = ax.plot(x,y)
                anim = FuncAnimation(fig, animate, init_func=init,
                    frames=1000, interval=10, blit=True)
        def Build1(x,y):

            fig = plt.Figure(figsize = (5, 5), 
                 dpi = 100)
            def init():
                line.set_data([], [])
                return line,
            def animate(i):
                line.set_data(x[:i], y[:i])
                return line,
            canvas = FigureCanvasTkAgg(fig, self)
            canvas.get_tk_widget().place(x=350,y=50)
            ax = fig.add_subplot(111)
            ax.set_title('Траектория тела')
            ax.set_xlabel('Дальность')
            ax.set_ylabel('Высота') 
            line, = ax.plot(x,y)
            anim = FuncAnimation(fig, animate, init_func=init,
                frames=1000, interval=10, blit=True)
            Blabel5.place_forget()
            Blabel6.place_forget()
            Blabel7.place_forget()
        def ReadTXT(filename1):
            f=open(filename1,"r")
            com = f.readline()
            nums=f.readline().split()    
            f_type1='standart\n'
            if com==f_type1:  
                Entry1.delete('0', 'end')
                Entry2.delete('0', 'end')
                Entry3.delete('0', 'end')
                Entry4.delete('0', 'end')
                Entry1.insert(0,nums[0])
                Entry2.insert(0,nums[1])
                Entry3.insert(0,nums[2])
                Entry4.insert(0,nums[3])
            else:
                    mb.showerror(
                    "Ошибка", 
                    "Неверный файл")
            f.close()
        def WriteTXT(filename):
            f=open(filename,"w")
            f_type1='standart\n'
            f.write(f_type1)
            x0=float(Entry1.get())
            y0=float(Entry2.get())
            v0=float(Entry3.get())
            a=float(Entry4.get())
            f.write(str(x0)+" "+str(y0)+" "+str(v0)+ " "+str(a))
            f.close()    

        def ReadNPZ(npzname):
            Entry1.delete('0', 'end')
            Entry2.delete('0', 'end')
            Entry3.delete('0', 'end')
            Entry4.delete('0', 'end')
            npa=np.load(npzname)
            x=npa['x1']
            y=npa['y1']

            Build1(x,y)
        def WriteNPZ(npzname):
            x0=float(Entry1.get())
            y0=float(Entry2.get())
            v0=float(Entry3.get())
            a=radians(float(Entry4.get()))
            g=10
            L=v0*cos(a)*(v0*sin(a)/g + sqrt(v0**2*sin(a)**2/g**2 + 2*y0/g))
            T=(sqrt((v0**2*sin(a)**2)+(2*g*y0))+v0*sin(a))/g
            t=np.arange(0,T,T/500)
            x = x0 + v0*cos(a)*t
            y = y0 + v0*sin(a)*t - g*t**2/2
            np.savez(npzname,x1=x,y1=y)
        def Open():
            file_name = fd.askopenfilename(
                 filetypes=(("TXT files", "*.txt"),
                   ("NPZ files", "*.npz")))
            
            if Path(file_name).suffix==".txt":
                ReadTXT(file_name)
            elif Path(file_name).suffix==".npz":
                ReadNPZ(file_name)
        def Save():
            
            file_name = fd.asksaveasfilename(defaultextension="*",
                   filetypes=(("TXT files", "*.txt"),
                   ("NPZ files", "*.npz")),
                   )
            defaultextension="*"
            if Path(file_name).suffix==".txt":
                WriteTXT(file_name)
            elif Path(file_name).suffix==".npz":
                WriteNPZ(file_name)

        BButton=Button(self,text="Построить",width=20,height=2,command=Build)
        BButton.place(x=100,y=200)
        BButton1=Button(self,text="Открыть",width=20,height=2,command=Open)
        BButton1.place(x=100,y=240)
        BButton2=Button(self,text="Сохранить",width=20,height=2,command=Save)
        BButton2.place(x=100,y=280)   
        Mbutton5=Button(self,text="Выход",width=20,height=2,command=CloseProgramm)
        Mbutton5.place(x=100,y=320)
class BuildGraphicOUT(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        ##Labels##
        
        Blabel=Label(self, text="Построение графиков")
     
        Blabel1=Label(self, text="(Начальная координата по оси x, м) x0=")
        Blabel2=Label(self, text="(Начальная координата по оси y, м) y0=")
        Blabel3=Label(self, text="(Начальная скорость, м/с) V0=")
        Blabel4=Label(self, text="(Угол, под которым брошено тело, градусы) A=")
        Blabel8=Label(self, text="(Коэффициент сопротивления среды(K>0)) K=")
        Blabel9=Label(self, text="(Масса тела, кг) M=")
        Blabel5=Label(self)
        Blabel6=Label(self)
        Blabel7=Label(self)
        Blabel.place(x=200,y=0)
        
        Blabel1.place(x=45,y=40)
        Blabel2.place(x=45,y=60)
        Blabel3.place(x=95,y=80)
        Blabel4.place(x=0,y=100)
        Blabel8.place(x=10,y=120)
        Blabel9.place(x=158,y=140)
        f = Figure(figsize=(5,5), dpi=100)
        a = f.add_subplot(111)
        a.plot()

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().place(x=350,y=50)
        ##Entries##
        Entry1=Entry(self,width=7)
        Entry2=Entry(self,width=7)
        Entry3=Entry(self,width=7)
        Entry4=Entry(self,width=7)
        Entry5=Entry(self,width=7)
        Entry6=Entry(self,width=7)
        Entry1.place(x=270,y=40)
        Entry1.focus_set()
        Entry2.place(x=270,y=60)
        Entry3.place(x=270,y=80)
        Entry4.place(x=270,y=100)
        Entry5.place(x=270,y=120)
        Entry6.place(x=270,y=140)
        ##Buttons##
        def CloseProgramm():
            self.destroy()
        def Build():
            if Entry1.get()=="":
                 mb.showerror(
                    "Ошибка", 
                    "Поля не должны быть пустыми")
            elif Entry2.get()=="":
                 mb.showerror(
                    "Ошибка", 
                    "Поля не должны быть пустыми")
            elif Entry3.get()=="":
                 mb.showerror(
                    "Ошибка", 
                    "Поля не должны быть пустыми")
            elif Entry4.get()=="":
                 mb.showerror(
                    "Ошибка", 
                    "Поля не должны быть пустыми")
            elif Entry5.get()=="":
                mb.showerror(
                    "Ошибка", 
                    "Поля не должны быть пустыми")
            elif Entry6.get()=="":
                mb.showerror(
                    "Ошибка", 
                    "Поля не должны быть пустыми")
            else:
                x0=float(Entry1.get())
                y0=float(Entry2.get())
                v0=float(Entry3.get())
                a=radians(float(Entry4.get()))
                k=float(Entry5.get())
                m=float(Entry6.get())
                v0X=v0*cos(a)
                v0Y=v0*sin(a)
                g=10
                ##Про L и Hmax пока забудем##
                
                
                T=(sqrt((v0**2*sin(a)**2)+(2*g*y0))+v0*sin(a))/g
              
                yX = y0+ m/k*((v0Y+m*g/k)*(1-np.exp(-k*T/m))-g*T)
                while yX>0:
                    T=1.1*T
                    yX = y0+ m/k*((v0Y+m*g/k)*(1-np.exp(-k*T/m))-g*T)
                        
                t=np.arange(0,T,T/500)
                x = x0+ v0X*m/k*(1-np.exp(-k*t/m))
                y = y0+ m/k*((v0Y+m*g/k)*(1-np.exp(-k*t/m))-g*t)
                for i in range (len(y)-1,0,-1):
                    if(y[i]>0):
                        k=i
                        break
                t=t[:k]
                x=x[:k]
                y=y[:k]
                L=x[-1]-x0
                Hmax=max(y)
                T=t[-1]
                fig = plt.Figure(figsize = (5, 5), 
                 dpi = 100)
 
                
                def init():
                    line.set_data([], [])
                    return line,
                def animate(i):
                    line.set_data(x[:i], y[:i])
                    return line,
               
                Blabel5.place(x=147,y=160)
                Blabel6.place(x=128,y=180)
                Blabel7.place(x=125,y=200)
                Blabel5.config(text="(Дальность полёта, м) L="+str(float('{:.3f}'.format(L))))
                Blabel6.config(text="(Высота подъёма, м) Hmax="+str(float('{:.3f}'.format(Hmax))))
                Blabel7.config(text="(Полное время полёта, с) T="+str(float('{:.3f}'.format(T))))
                canvas = FigureCanvasTkAgg(fig, self)
                canvas.get_tk_widget().place(x=350,y=50)
                ax = fig.add_subplot(111)
                ax.set_title('Траектория тела')
                ax.set_xlabel('Дальность')
                ax.set_ylabel('Высота')
                line, = ax.plot(x,y)
                anim = FuncAnimation(fig, animate, init_func=init,
                    frames=1000, interval=10, blit=True)
        def Build1(x,y):
            fig = plt.Figure(figsize = (5, 5), 
                 dpi = 100) 
            def init():
                line.set_data([], [])
                return line,
            def animate(i):
                line.set_data(x[:i], y[:i])
                return line,
               
            

            canvas = FigureCanvasTkAgg(fig, self)
            canvas.get_tk_widget().place(x=350,y=50)
            ax = fig.add_subplot(111)
            ax.set_title('Траектория тела')
            ax.set_xlabel('Дальность')
            ax.set_ylabel('Высота')
            line, = ax.plot(x,y)
            anim = FuncAnimation(fig, animate, init_func=init,
                frames=1000, interval=10, blit=True)
            Blabel5.place_forget()
            Blabel6.place_forget()
            Blabel7.place_forget()
            
        def ReadTXT(filename1):
            f=open(filename1,"r")
            com = f.readline()
            nums=f.readline().split()    
            f_type1='extended\n'
            if com==f_type1:  
                Entry1.delete('0', 'end')
                Entry2.delete('0', 'end')
                Entry3.delete('0', 'end')
                Entry4.delete('0', 'end')
                Entry5.delete('0', 'end')
                Entry6.delete('0', 'end')
                Entry1.insert(0,nums[0])
                Entry2.insert(0,nums[1])
                Entry3.insert(0,nums[2])
                Entry4.insert(0,nums[3])
                Entry5.insert(0,nums[4])
                Entry6.insert(0,nums[5])
            else:
                    mb.showerror(
                    "Ошибка", 
                    "Неверный файл")
            f.close()
        def WriteTXT(filename):
            f=open(filename,"w")
            f_type1='extended\n'
            f.write(f_type1)
            x0=float(Entry1.get())
            y0=float(Entry2.get())
            v0=float(Entry3.get())
            a=float(Entry4.get())
            k=float(Entry5.get())
            m=float(Entry6.get())
            f.write(str(x0)+" "+str(y0)+" "+str(v0)+ " "+str(a)+" "+str(k)+" "+str(m))
            f.close()    

        def ReadNPZ(npzname):
            Entry1.delete('0', 'end')
            Entry2.delete('0', 'end')
            Entry3.delete('0', 'end')
            Entry4.delete('0', 'end')
            Entry5.delete('0', 'end')
            Entry6.delete('0', 'end')
            npa=np.load(npzname)
            x=npa['x1']
            y=npa['y1']
            Build1(x,y)
        def WriteNPZ(npzname):
            x0=float(Entry1.get())
            y0=float(Entry2.get())
            v0=float(Entry3.get())
            a=radians(float(Entry4.get()))
            k=float(Entry5.get())
            m=float(Entry6.get())
            ##ПОМЕНЯТЬ ФОРМУЛЫ##
            v0X=v0*cos(a)
            v0Y=v0*sin(a)
            g=10
            
            T=(sqrt((v0**2*sin(a)**2)+(2*g*y0))+v0*sin(a))/g
            t=np.arange(0,T,T/500)
            x = x0+ v0X*m/k*(1-np.exp(-k*t/m))
            y = y0+ m/k*((v0Y+m*g/k)*(1-np.exp(-k*t/m))-g*t)
            np.savez(npzname,x1=x,y1=y)
        def Open():
            file_name = fd.askopenfilename(
                 filetypes=(("TXT files", "*.txt"),
                   ("NPZ files", "*.npz")))
            
            if Path(file_name).suffix==".txt":
                ReadTXT(file_name)
            elif Path(file_name).suffix==".npz":
                ReadNPZ(file_name)
        def Save():
            
            file_name = fd.asksaveasfilename(defaultextension="*",
                   filetypes=(("TXT files", "*.txt"),
                   ("NPZ files", "*.npz")),
                   )
            defaultextension="*"
            if Path(file_name).suffix==".txt":
                WriteTXT(file_name)
            elif Path(file_name).suffix==".npz":
                WriteNPZ(file_name)

        BButton=Button(self,text="Построить",width=20,height=2,command=Build)
        BButton.place(x=100,y=220)
        BButton1=Button(self,text="Открыть",width=20,height=2,command=Open)
        BButton1.place(x=100,y=260)
        BButton2=Button(self,text="Сохранить",width=20,height=2,command=Save)
        BButton2.place(x=100,y=300) 
        Mbutton5=Button(self,text="Выход",width=20,height=2,command=CloseProgramm)
        Mbutton5.place(x=100,y=340)
class Solve(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        ##Labels##
        Slabel=Label(self,text="Решение задач")
        Slabel1=Label(self,text="(Полное время полёта, с) T=")
        Slabel2=Label(self,text="(Высота подъёма, м) Hmax=")
        Slabel3=Label(self,text="(Угол, под которым брошено тело, градусы) A=")
        Slabel4=Label(self,text="(Дальность полёта, м) Lmax=")
        Slabel5=Label(self,text="(Начальная координата по оси x, м) x0=")
        Slabel6=Label(self,text="(Начальная координата по оси y, м) y0=")
        Slabel.place(x=200,y=0)
        Slabel1.place(x=127,y=50)
        Slabel2.place(x=130,y=70)
        Slabel3.place(x=20,y=90)
        Slabel4.place(x=125,y=110)
        Slabel5.place(x=65,y=130)
        Slabel6.place(x=65,y=150)
        ##Entries##
        entry1=Entry(self)
        entry2=Entry(self)
        entry3=Entry(self)
        entry4=Entry(self)
        entry5=Entry(self)
        entry6=Entry(self)

        entry1.place(x=290,y=50)
        entry1.focus_set()
        entry2.place(x=290,y=70)
        entry3.place(x=290,y=90)
        entry4.place(x=290,y=110)
        entry5.place(x=290,y=130)
        entry6.place(x=290,y=150)

        ##Buttons##
        
        ##Functions##
        ##TODO: поменять формулы##
        def CloseProgramm():
            self.destroy()
        def Solve1(T,Hmax,A,x0,y0):
            g=10
            A=radians(A)
            l=sqrt(2*g*(Hmax-y0))*T/tan(A)
            entry4.insert(0,str(float('{:.3f}'.format(l))))

        def Solve2(T,Hmax,l,x0,y0):
            g=10
            A=atan((T*sqrt(2*g*(Hmax-y0)))/l)
            entry3.insert(0,str(float('{:.3f}'.format(degrees(A)))))

        def Solve3(T,A,l,x0,y0):
            g=10
            a=radians(A)
            v0=l/(cos(a)*T)
            Hmax=y0+(v0**2*sin(a)**2/(2*g))
            entry2.insert(0,str(float('{:.3f}'.format(Hmax))))

        def Solve4(Hmax,A,l,x0,y0):
            g=10
            A=radians(A)
            T=l*tan(A)/sqrt(2*g*(Hmax-y0))
            entry1.insert(0,str(float('{:.3f}'.format(T))))
            
        def Solvation():
            entrlist = [entry1,entry2,entry3,entry4,entry5,entry6]
            k=0
            for i in entrlist:
                if i.get()=="":
                    k+=1
            if k>1:
                mb.showerror(
                    "Ошибка", 
                    "Пустым может быть только 1 поле")
            
            else:
                if(entry1.get()==""):
                    Solve4(float(entry2.get()),float(entry3.get()),float(entry4.get()),float(entry5.get()),float(entry6.get()))
                elif(entry2.get()==""):
                    Solve3(float(entry1.get()),float(entry3.get()),float(entry4.get()),float(entry5.get()),float(entry6.get()))
                elif(entry3.get()==""):
                    Solve2(float(entry1.get()),float(entry2.get()),float(entry4.get()),float(entry5.get()),float(entry6.get()))
                elif(entry4.get()==""):
                    Solve1(float(entry1.get()),float(entry2.get()),float(entry3.get()),float(entry5.get()),float(entry6.get()))
        ##Binds##
        SButton=Button(self,text="Решить",width=20,height=2,command=Solvation)
        SButton.place(x=150,y=240)
        Mbutton5=Button(self,text="Выход",width=20,height=2,command=CloseProgramm)
        Mbutton5.place(x=150,y=280)
class TheoryBox(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        
        def Openbrowser1():
            webbrowser.open('https://uchebnik.mos.ru/catalogue/material_view/books/25119', new=2)
        def Openbrowser2():
            webbrowser.open('https://www.eduspb.com/node/1669', new=2)
        def Openbrowser3():
            webbrowser.open('https://glebgrenkin.blogspot.com/2014/03/blog-post.html', new=2)
        tLabel1=Label(self,text="В данном окне содержатся ссылки на всю необходимую для ознакомления информацию,\n связанную с траекторией тела брошенного под углом к горизонту \n (для перехода на сайт нажмите на кнопку)")
        tLabel1.place(x=40,y=10)
        tButton1=Button(self,text="Учебник физики 10 класс",width=40,height=3, command=Openbrowser1)
        tButton1.place(x=150,y=60)
        tButton2=Button(self,text="Статья посвящённая траектории тела,\n брошенного под углом к горизонту",width=40,height=3, command=Openbrowser2)
        tButton2.place(x=150,y=120)
        tButton3=Button(self,text="Статья посвящённая траектории тела,\n брошенного под углом к горизонту,\n с учётом сопротивления воздуха",width=40,height=3, command=Openbrowser3)
        tButton3.place(x=150,y=180)
menu=Menu()
menu.geometry("500x500")
menu.resizable(0,0)
menu.title("Главное меню")
menu.mainloop()
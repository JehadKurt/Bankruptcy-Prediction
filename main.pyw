import os

import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image


root= Tk()
root.title('Selection Of model for Classification')
root.geometry('400x450')
icon = PhotoImage(file="images/python.png")
root.iconphoto(False,icon)

root.configure()

bg = ImageTk.PhotoImage(file= "images/2.png")
my_Canvas= Canvas(root,width= 400,height = 500)
my_Canvas.pack(fill="both",expand = True)
my_Canvas.create_image(0,0,image=bg,anchor = "nw")

#def resizer(e):
#    global new,bg1, res_bg
    #open our Image
#    bg1 = Image.open("2.png")
#    res_bg = bg1.resize(e.width,e.height),Image.BILINEAR
#    new = ImageTk.PhotoImage(res_bg)
#    my_Canvas.create_image(0, 0, image=new,anchor="nw")



#background_image = tk.PhotoImage(file='a.png')
#background_label = tk.Label(root, image=background_image)
#background_label.place(relwidth=1, relheight=1)

#my_Canvas.crate_text(200,250,text = "welcome",font= 10)


def SVMC():
    os.startfile("SVM.pyw")  #or (r"C:\Users\JEHAD-PC\PycharmProjects\FiverProjectWork\SVM.pyw")

def LogReg():
    os.startfile("LogisticReg.pyw",operation="open") # or (C:\Users\JEHAD-PC\PycharmProjects\FiverProjectWork/LogisticReg.pyw)

def DecTree():
    os.startfile("DecisionTree.pyw",operation="open") # or (r"C:\Users\JEHAD-PC\PycharmProjects\FiverProjectWork\DecisionTree.pyw)






#button = tk.Button(frame, text="Show Accuracy", font="system", command=lambda:LR())
#button.place(relx=0.1, relheight=0.4, relwidth=0.9)
button1= tk.Button(root,text='Logistic Regression',font="System",activebackground="black",command=LogReg,activeforeground="red",bg= "green")
button1.place(relx=0.3,rely= 0.5, relheight=0.05, relwidth=0.425)
button2 = tk.Button(root,text='DecisionTree Classifier',font="System",activebackground="black",command=DecTree,activeforeground="blue",bg ="red")
button2.place(relx=0.3,rely= 0.6, relheight=0.05, relwidth=0.425)
button3= tk.Button(root,text='SVM Classifier',font="System",activebackground="black",command=SVMC,activeforeground="pink",bg= "blue")
button3.place(relx=0.3,rely= 0.7, relheight=0.05, relwidth=0.425)

#Button(root,text='Logistic Regression',font="System",activebackground="black",command=LogReg,activeforeground="red",bg= "green").place(x=150,y=130)
#Button(root,text='DecisionTree Classifier',font="System",activebackground="black",command=DecCls,activeforeground="blue",bg ="red").place(x=150,y=190)
#Button(root,text='SVM Classifier',font="System",activebackground="black",command=SVMCls,activeforeground="pink",bg= "blue").place(x=160,y=250)





label1 =Label(root,text= "Click on The Requried Model to See  \n the Page of Accuracy the Model  ",font= 50, bg= "darkblue")
label1.place(relx=0.15, rely=0.1,relheight=0.1, relwidth=0.7)


#Label(root,text="Regression",font="System").place(x=150,y=75)
#Label(root,text="Clustering",font="System").place(x=350,y=75)
label2 = Label(root,text="Classification Models Are Are Given Bellow",font="System" , bg="darkblue")
label2.place(relx=0.15,rely= 0.2, relheight=0.1, relwidth=0.7)

#Button(root,text='Best Classifier',activebackground="black",command=Best_Class,activeforeground="white").place(x=150,y=390)
#Button(root,text='Best Regressor',activebackground="black",command=Best_Reg,activeforeground="white").place(x=400,y=390)




#root.bind('<Configure>',resizer)
root.mainloop()

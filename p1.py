from tkinter import  *
root = Tk()
root.geometry("1920x1080")
root.title("Button program")
root.config(background="#FA706D")
photo = PhotoImage(file="C:\\Users\\hp\\Documents\\tkinter\\painting.png")
lab = Label(root,image= photo)
lab.place(x=200,y=300)
head = Label(root,text="ART GALLERY",font=("Bahnschrift SemiBold",50),fg="white",bg="#204863",padx=800,pady=50)
head.pack()
para = Label(root,text=" Modern art: art of a style marked by a significant departure from traditional styles and values, in particular that created between the late 19th and the late 20th centuries.",
             font=("monospace",13,),
             bg="#FA706D",
             fg="white",
             )
para.place(x=50,y=245)





root.mainloop()
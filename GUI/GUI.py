from Tkinter import *

# -------- Variables --------
"""
master = tkinter window
Title = Title for GUI
"""
# ------- Functions --------
# -- Done Button 1
# this is for after getting x and y range
def doneGrid():
    global mess
    
    if (len(ent_x.get()) != 0 and len(ent_dx.get()) != 0 and len(ent_y.get()) != 0 and len(ent_dy.get()) !=0 ):
        file_obj.write("x-range= " + ent_x.get() + "\n")
        file_obj.write("dx= " + ent_dx.get() + "\n")
        file_obj.write("y-range= " + ent_y.get() + "\n")
        file_obj.write("dy= " + ent_dy.get() + "\n")
        
        # Removing everything
        x_range.destroy()
        ent_x.destroy()
        
        dx.destroy()
        ent_dx.destroy()
        
        y_range.destroy()
        ent_y.destroy()
        
        dy.destroy()
        ent_dy.destroy()
        
        done.destroy()
        exit_btn.destroy()
        mess.destroy()
        
        # Running next step
        shape_inputs()
    else:
        # message about filling entries
        mess = Label(master, text="All entries need values.")
        mess.grid(row=9,columnspan=6)

# --- Getting geometric shapes
def shape_inputs():
    # -- Variables
    global canvas_height, canvas_width, grid1, geo_shape, circle_btn, line_btn, rec_btn, pnt_btn, exit_btn
    
    # Dimensions and creating layer
    canvas_width = 500
    canvas_height = 500
    grid1 = Canvas(master,width = canvas_width,height=canvas_height,background="white")
    grid1.grid(row=1,rowspan=7,column=0,columnspan=5)

    # Geometric shapes 
    geo_shape = Label(master, text="Geometric Shapes", anchor = "center", font = ("Times",18))
    geo_shape.grid(row=1,column=5,columnspan=2)
    
    # Circle
    circle_btn = Button(master, text="Circle",command=circle)
    circle_btn.grid(row=2, column=5,columnspan=2)
    
    # Line
    line_btn = Button(master, text="Line")
    line_btn.grid(row=3, column=5,columnspan=2)

    # Rectangle
    rec_btn = Button(master, text="Rectangle")
    rec_btn.grid(row=4, column=5, columnspan=2)

    # Point
    pnt_btn = Button(master, text="Point")
    pnt_btn.grid(row=5, column=5, columnspan=2)
    
    # move exit button
    exit_btn.destroy()
    exit_btn = Button(master, text="Exit", command=master.destroy)
    exit_btn.grid(row=6, column=5,columnspan=2)

# --- Circle function
def circle():
    # -- Variables
    global circle_label, c_r,ent_r, centre, ent_centre1,ent_centre2, c_pot, ent_pot, exit_btn
    
    # remove previous buttons
    geo_shape.destroy()
    circle_btn.destroy()
    line_btn.destroy()
    rec_btn.destroy()
    pnt_btn.destroy()

    # Circle Label
    circle_label = Label(master, text="Circle", anchor = "center", font = ("Times",18))
    circle_label.grid(row=1,column=5,columnspan=2)
 
    # Circle Radius
    c_r = Label(master, text="Radius")
    c_r.grid(row=2,column=5)
    ent_r = Entry(master)
    ent_r.grid(row=2,column=6)

    # Circle Centre
    centre = Label(master, text="Centre Coordinates")
    centre.grid(row=3, column=5,columnspan=2)
    ent_centre1 = Entry(master)
    ent_centre1.grid(row=4, column=5)
    ent_centre2 = Entry(master)
    ent_centre2.grid(row=4, column=6)

    # Potential
    c_pot = Label(master, text="Potential (0 if GND)")
    c_pot.grid(row=5, column=5)
    ent_pot = Entry(master)
    ent_pot.grid(row=5,column=6)

    # Empty space
    mess = Label(master)
    mess.grid(row=6,columnspan=2)
    
    # Done button
    done = Button(master, text="Done")
    done.grid(row=7,column=5)
    
    # move exit button
    exit_btn.destroy()
    exit_btn = Button(master, text="Exit", command=master.destroy)
    exit_btn.grid(row=7, column=6)

# ----------------- Program -------------------
# --- File
file_obj = open("conditions.txt","w")

# Top
master = Tk()
    
# Title
Title = Label(master, text = "Electrostatics", anchor = "center", font = ("Times",30), width = 11)
Title.grid(columnspan=6)

# ----- Getting grid size -----
# x-range
x_range = Label(master, text = "x-range ( -x to x )")
x_range.grid(row=1,columnspan=6)
ent_x = Entry(master)
ent_x.grid(row=2,columnspan=6)

# x-step size
dx = Label(master, text = "Step Size in x")
dx.grid(row=3,columnspan=6)
ent_dx = Entry(master)
ent_dx.grid(row=4, columnspan=6)

# y-range
y_range = Label(master, text = "y-range ( -y to y )")
y_range.grid(row=5,columnspan=6)
ent_y = Entry(master)
ent_y.grid(row=6,columnspan=6)

# y-step size
dy = Label(master, text = "Step Size in y")
dy.grid(row=7,columnspan=6)
ent_dy = Entry(master)
ent_dy.grid(row=8, columnspan=6)

# Empty space
mess = Label(master)
mess.grid(row=9,rowspan=2,columnspan=6)

# Done button
done = Button(master, text = "Done", command=doneGrid)
done.grid(row=11,column=0,columnspan=3)

# Exit button
exit_btn = Button(master, text="Exit", command=master.destroy)
exit_btn.grid(row=11,column=3,columnspan=3)

# Run it
master.mainloop()

# Close file
file_obj.close()

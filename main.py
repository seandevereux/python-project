from customtkinter import *
from functools import partial
from PIL import Image

set_appearance_mode("System")  # Modes: system (default), light, dark
set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = CTk()  # create CTk window like you do with the Tk window
app.geometry("800x400")
app.resizable(False, False)
app.iconbitmap("logoSmall.ico")
app.title("Tamper - Login")


def switchDashboardView(inp, m):
    dialogue = inp

    homeFrame = CTkFrame(master=m, width=900, height=820, corner_radius=20)
    homeFrame.place(relx= 0.61, rely=0.5, anchor=CENTER)
    
    dashFrame = CTkFrame(master=m, width=900, height=820, corner_radius=20)
    dashFrame.place(relx= 0.61, rely=0.5, anchor=CENTER)

    settingsFrame = CTkFrame(master=m, width=900, height=820, corner_radius=20)
    match dialogue:
        case "home":
            settingsFrame.place_forget()
            dashFrame.place_forget()
            homeFrame.place(relx= 0.61, rely=0.5, anchor=CENTER)
            welcome = CTkLabel(master=homeFrame,text="Hey, Welcome to the Home")
            welcome.place(relx=.5, rely=0.5, anchor=CENTER)
        case "dashboard":
            settingsFrame.place_forget()
            homeFrame.place_forget()
            dashFrame.place(relx= 0.61, rely=0.5, anchor=CENTER)
            welcome = CTkLabel(master=dashFrame,text="Hey, Welcome to the dashboard")
            welcome.place(relx=.5, rely=0.5, anchor=CENTER)
        case "settings":
            #show settings hide other ui options
            homeFrame.place_forget()
            dashFrame.place_forget()
            settingsFrame.place(relx= 0.61, rely=0.5, anchor=CENTER)
            welcome = CTkLabel(master=settingsFrame,text="Hey, Welcome to the settings")
            welcome.place(relx=.5, rely=0.5, anchor=CENTER)
        case "logout":
            print("logout code")
            
def openDashboard():
    dashboardWindow = CTk()
    dashboardWindow.geometry("1200x840")
    dashboardWindow.resizable(False, False)
    dashboardWindow.iconbitmap("logoSmall.ico")
    dashboardWindow.title("Tamper - Dashboard")
    
    switchDashboardView("home", dashboardWindow)

    listFrame = CTkFrame(master=dashboardWindow, width=300, height=820, corner_radius=20)
    listFrame.place(relx= 0.1, rely=0.5, anchor=CENTER)
    
    homeButton = CTkButton(master=listFrame, text="Home",corner_radius=0, width=200, height=75, command=partial(switchDashboardView,"home", dashboardWindow))
    homeButton.place(relx=.55, rely=.1, anchor=CENTER)

    dashboardButton = CTkButton(master=listFrame, text="Dashboard",corner_radius=0, width=200, height=75, command=partial(switchDashboardView,"dashboard", dashboardWindow))
    dashboardButton.place(relx=.55, rely=.2, anchor=CENTER)

    settingsButton = CTkButton(master=listFrame, text="Settings",corner_radius=0, width=200, height=75, command=partial(switchDashboardView,"settings", dashboardWindow))
    settingsButton.place(relx=.55, rely=.3, anchor=CENTER)

    logoutButton = CTkButton(master=listFrame, text="Log out",corner_radius=0, width=200, height=100, command=partial(switchDashboardView,"logout", dashboardWindow))
    logoutButton.place(relx=.55, rely=.9, anchor=CENTER)

    # Add widgets and configure the new window as needed
    
    # Make sure to call the new window's mainloop
    center_window(dashboardWindow,1200, 840)
    dashboardWindow.mainloop()

#just makes the application centered on startup
def center_window(window, width=800, height=400):
    # get screen width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

login_image = CTkImage(dark_image=Image.open("background1.png"), size=(400,400))
logo_image = CTkImage(dark_image=Image.open("logoText.png"), size=(250,75))

def button_function(x):
    if x == "Login":
        app.destroy()
        openDashboard()
    elif x == "Settings":
        print("not home")
    else:
        print("chicken")

#this label displays the image

loginFrame = CTkFrame(master=app, width=300, height=250, corner_radius=20)
loginFrame.place(relx=.75, rely=0.60, anchor=CENTER)

lab = CTkLabel(master=app,image=login_image,text="")
lab.grid(row=0,column=0)

logo = CTkLabel(master=app,image=logo_image,text="")
logo.place(relx=.75, rely=0.15, anchor=CENTER)

#entry fields
nameEntry = CTkEntry(app, placeholder_text="Username", corner_radius=0, width=200)
nameEntry.place(relx=.75, rely=0.4, anchor=CENTER)

passEntry = CTkEntry(app, placeholder_text="Password", corner_radius=0, show="*", width=200)
passEntry.place(relx=.75, rely=0.5, anchor=CENTER)

# Use CTkButton instead of tkinter Button
loginButton = CTkButton(master=app, text="Login", command=partial(button_function,"Login"), corner_radius=0,width=200)
loginButton.place(relx=.75, rely=0.7, anchor=CENTER)

passButton = CTkButton(master=app, text="Register", command=partial(button_function,"Data"), corner_radius=0, width=200)
passButton.place(relx=.75, rely=0.8, anchor=CENTER)

rememberMeCheckBox = CTkCheckBox(master=loginFrame, text="Remember me?")
rememberMeCheckBox.place(relx=.37, rely=0.5, anchor=CENTER)


center_window(app, app.winfo_width(), app.winfo_height())
app.mainloop()
import os
import customtkinter as ctk
from tkinter import messagebox

current_dir=os.path.dirname(os.path.abspath(__file__))
icon_path = os.path.join(current_dir,"10481311.ico")



ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.title("BMI")
app.iconbitmap(icon_path)
app.geometry("400x350+700+150")

# Function for "ورود" button
def login():
    global text_label , text_label1, weight_entry,height_entry,confrim_Button
    # Create and display the label when the button is clicked
    text_label = ctk.CTkLabel(app, text="وزن شما:",
                              text_color="white",
                              font=("arial", 21, "bold"))
    text_label.place(x=15, y=10)  # Place label at the specified position
    weight_entry = ctk.CTkEntry(app, width=100, height=30, 
                                font=("arial", 18),
                                corner_radius=20,
                                fg_color="#0F3460",
                                border_width=2.8,
                                border_color="#16213E",
                                )
    weight_entry.place(x=90, y=10)  # Positioned next to the label
    text_label1 = ctk.CTkLabel(app, text="قد شما:",
                              text_color="white",
                              font=("arial", 21, "bold"))
    text_label1.place(x=205 , y=10)
    height_entry = ctk.CTkEntry(app,width=115, height=30, 
                                font=("arial", 18),
                                corner_radius=20,
                                fg_color="#0F3460",
                                border_width=2.8,
                                border_color="#16213E",
                                )
    height_entry.place(x = 265 , y=10)

    confrim_Button = ctk.CTkButton(app , text="ثبت",
                             fg_color="#0F3460", 
                             hover_color="#533483", 
                             text_color="white", 
                             corner_radius=100,
                             border_width=3.8,
                             border_color="#16213E",
                             font=("arial", 21, "bold"),
                             height=60,
                             width=150,
                             command=confrim)
    confrim_Button.place(x=125 , y=80)

    Button_vorod.destroy()  # Optionally remove the "ورود" button after click
    Button_khorog.destroy() # Optionally remove the "خروج" button after click
# Function for "خروج" button
def logout():
    app.quit()  # Close the application
def confrim():
    weight = weight_entry.get().strip()
    height = height_entry.get().strip()
    if not weight or not height:
        messagebox.showerror("خطا", "لطفاً مقدار وزن و قد را وارد کنید!")
        return
    try:
        weight = float(weight)
        height = float(height)/100
        if weight <= 0 or height <= 0:
            raise ValueError 
    except ValueError:
        messagebox.showerror("خطا", "لطفاً مقدار وزن و قد را به‌درستی وارد کنید!")
        return

    bmi = weight/(height**2)


    text_label.destroy()
    text_label1.destroy()
    weight_entry.destroy()
    height_entry.destroy()
    confrim_Button.destroy()
    result_text_label = ctk.CTkLabel(app, text="نتیجه:",
                              text_color="white",
                              font=("arial", 21, "bold"))
    result_text_label.place(x=10 , y=10)
    

    bmi_label = ctk.CTkLabel(app , text=f" شاخص توده بدنی شما: {bmi:.2f}",
                             text_color="#0F3460",
                             font=("arial",21,"bold"))
    bmi_label.place(x=90 , y=10)


    if bmi < 18.5:
        status = "کمبود وزن"
        advice = "برای افزایش وزن، غذاهای مغذی با پروتئین و کربوهیدرات بالا مصرف کنید. ورزش‌های قدرتی انجام دهید."
    elif 18.5 <= bmi < 24.9:
        status = "وزن نرمال"
        advice = "وضعیت وزنی شما مناسب است. تغذیه سالم داشته باشید و فعالیت بدنی منظم را ادامه دهید."
    elif 25 <= bmi < 29.9:
        status = "اضافه وزن"
        advice = "برای کاهش وزن، از مصرف غذاهای پرچرب و شیرینی پرهیز کنید. ورزش منظم انجام دهید."
    else:
        status = "چاقی"
        advice = "برای کاهش وزن، رژیم غذایی سالم و کم‌کالری را دنبال کنید و ورزش‌های هوازی انجام دهید."

    # نمایش وضعیت BMI
    status_label = ctk.CTkLabel(app, text=f"وضعیت: {status}",
                                text_color="#533483",
                                font=("arial", 21, "bold"))
    status_label.place(x=140, y=40)

    messagebox.showinfo(f"وضعیت: {status}", advice)

    exit_button = ctk.CTkButton(app, text="خروج", 
                              fg_color="#0F3460", 
                              hover_color="#533483", 
                              text_color="white", 
                              corner_radius=100,
                              border_width=3.8,
                              border_color="#16213E",
                              font=("arial", 21, "bold"),
                              height=60,
                              width=150,
                              command=Logout_1)
    exit_button.place(x=125 , y=80)

    # # نمایش توصیه‌های پزشکی
    # advice_label = ctk.CTkLabel(app, text=f"توصیه: {advice}",
    #                             text_color="yellow",
    #                             wraplength=350,  # محدود کردن طول متن برای خوانایی بهتر
    #                             font=("arial", 18, "bold"),
    #                             justify="right")  # تراز متن به راست برای فارسی
    # advice_label.place(x=25, y=140)
def Logout_1():
    app.quit()
# Create the "ورود" button (Top-Left)
Button_vorod = ctk.CTkButton(app, text="ورود", 
                             fg_color="#0F3460", 
                             hover_color="#533483", 
                             text_color="white", 
                             corner_radius=100,
                             border_width=3.8,
                             border_color="#16213E",
                             font=("arial", 21, "bold"),
                             height=60,
                             width=150,
                             command=login)

Button_vorod.place(x=35, y=50)  # Positioned at top-left

# Create the "خروج" button (Top-Right)
Button_khorog = ctk.CTkButton(app, text="خروج", 
                              fg_color="#0F3460", 
                              hover_color="#533483", 
                              text_color="white", 
                              corner_radius=100,
                              border_width=3.8,
                              border_color="#16213E",
                              font=("arial", 21, "bold"),
                              height=60,
                              width=150,
                              command=logout)

Button_khorog.place(x=220, y=50)  # Positioned at top-right

app.mainloop()

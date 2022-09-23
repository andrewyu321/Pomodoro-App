from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check = "✔"
time = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    global time
    window.after_cancel(time)
    count_down(0)
    reps = 0
    check.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    canvas.configure(canvas, bg=YELLOW)
    window.config(bg=YELLOW)
    timer.config(bg=YELLOW)
    check.config(bg=YELLOW)
    start.config(bg=YELLOW)
    reset.config(bg=YELLOW)
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if len(str(count_sec)) == 1:
        count_sec = f"0{str(count_sec)}"
    if len(str(count_min)) == 1:
        count_min = f"0{str(count_min)}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global time
        time = window.after(100, count_down, count - 1)
    else:
        canvas.configure(canvas, bg=PINK)
        window.config(bg=PINK)
        timer.config(bg=PINK)
        check.config(bg=PINK)
        start.config(bg=PINK)
        reset.config(bg=PINK)
        mark = ""
        for x in range(math.floor(reps / 2)):
            mark += "✔"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=PINK)
#window.after(1000, )




canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#timer
timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=PINK)
timer.grid(column=1, row=0)

#start button
start = Button(text="Start", font=(FONT_NAME, 20,), command=start_timer, bg=PINK, fg=GREEN, borderwidth=0)
start.grid(column=0, row=2)

#Reset Button
reset = Button(text="Reset", font=(FONT_NAME, 20,), command=reset_timer, bg=PINK, fg=GREEN, borderwidth=0)
reset.grid(column=2, row=2)

#Check Mark
check = Label(text="", fg=GREEN, font=(FONT_NAME, 15), bg=PINK, borderwidth=0)
check.grid(column=1, row=3)



window.mainloop()
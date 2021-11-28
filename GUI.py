
import tkinter as tk
from tkinter import Button, font
from tkinter.constants import BOTTOM, GROOVE, LEFT, RIGHT
from tkinter import messagebox


class MainWindow :
    
    def __init__(self, title : str):
        
        self.screen = tk.Tk()
        self.height = self.screen.winfo_screenheight()
        self.width  = self.screen.winfo_screenwidth()
                
        self.screen.geometry(f"{int(self.width // 1.5)}x{int(self.height // 1.5)}")
        
        label_title = tk.Label(self.screen, text="Les tours d'Hanoï")
        label_title.config(font = ("Calibri", 24, "underline"))
        label_title.pack()
        
        self.tower_canvas = tk.Canvas(self.screen, height = int(self.height // 1.8), width = int(self.width) // 1.8, bd = 10, background = 'Ivory')
        self.tower_canvas.pack(side=LEFT)
        
        exit_button = tk.Button(self.screen, text = "Exit", background='red', command=lambda:self.screen.destroy())
        exit_button.pack(side=RIGHT,padx=10)
        
        play_button = tk.Button(self.screen, text = "Play", background='green', command=lambda:self.launch_game())
        play_button.pack(side=RIGHT)
        
        self.value = tk.StringVar()
        self.value.set("0")
        self.saisie = tk.Entry(self.screen,textvariable=self.value, width=5, justify='center', bd=3)
        self.saisie.pack(side=RIGHT)
     
    def launch_game(self):
        self.tower_list = Tower.draw(self.tower_canvas)
        self.disk_list = Disk.initialize(self.tower_canvas, self.tower_list, int(self.saisie.get()))
        print(self.disk_list)
    
    
class Tower :
    
    @staticmethod
    def draw(container : tk.Canvas):
        height = container.winfo_reqheight()
        width = container.winfo_reqwidth()
        
        distant = width / 4
        tower_size = height - 50
        start_size = height * 0.10
  
        first = container.create_rectangle(distant - 10, start_size, distant + 10, tower_size)  
        second = container.create_rectangle((distant * 2) - 10, start_size, (distant * 2) + 10, tower_size) 
        third = container.create_rectangle((distant * 3) - 10, start_size, (distant * 3) + 10, tower_size) 
           
        return [first, second, third]
    
    @staticmethod
    def clear(container : tk.Canvas):
        container.delete('all')
    
class Disk :
    
    @staticmethod
    def initialize(container : tk.Canvas, stake_list : list, nb_disk : int) :
        
        if nb_disk > 8 :
            messagebox.showerror(f"Error", f"For a better experience, the use of {nb_disk} disk is deprecated")
            return 
        
        height = container.winfo_reqheight()
        width = container.winfo_reqwidth()
        
        disk_height_list = []
        disk_width_list = []
        distant = width / 4
        start = 80
        disk_height = 70
        height_dif = 70 
        
        for element in range(nb_disk):
            disk = container.create_rectangle(distant - start , height - height_dif, distant + start, height - height_dif + 20, fill ='brown')
            
            start -= 10 
            disk_height -= 10  
            height_dif += 20
            
            disk_height_list.append(height - height_dif + 20)            
               
        return disk_height_list
    
    def read_from_config(self, config_list : list):
        for i in range(len(config_list)):
            if i == 0 :
                return 
    
   
    

            
main = MainWindow("Les tours d'hanoï")
main.screen.mainloop()
import tkinter as tk
from tkinter import messagebox

class TowerOfHanoi:
    def __init__(self, root, num_disks=3):
        self.root = root
        self.root.title("Tower of Hanoi")
        
        self.num_disks = num_disks
        self.towers = [[i for i in range(num_disks, 0, -1)], [], []]
        
        self.canvas = tk.Canvas(self.root, bg="white", width=600, height=400)
        self.canvas.pack(padx=10, pady=10)
        
        self.draw_towers()
        
        self.source_tower = None
        
        self.canvas.bind("<Button-1>", self.on_click)

    def draw_towers(self):
        self.canvas.delete("all")
        
        for i in range(3):
            x = 100 + i * 200
            self.canvas.create_rectangle(x - 10, 350, x + 10, 50, fill="black")
            
            for j, disk in enumerate(self.towers[i]):
                self.draw_disk(disk, x, 350 - j * 30)

    def draw_disk(self, size, x, y):
        self.canvas.create_rectangle(x - size * 15, y, x + size * 15, y - 20, fill="blue", tags=f"disk{size}")

    def on_click(self, event):
        tower_clicked = event.x // 200
        if not 0 <= tower_clicked <= 2:
            return
        
        if self.source_tower is None:
            if self.towers[tower_clicked]:
                self.source_tower = tower_clicked
        else:
            disk = self.towers[self.source_tower][-1]
            if not self.towers[tower_clicked] or disk < self.towers[tower_clicked][-1]:
                self.towers[tower_clicked].append(self.towers[self.source_tower].pop())
                self.source_tower = None
                self.draw_towers()
                
                if len(self.towers[2]) == self.num_disks:
                    messagebox.showinfo("Congratulations!", "You solved the puzzle!")
                    self.root.quit()
            else:
                messagebox.showwarning("Invalid Move", "You can't place a larger disk on top of a smaller one.")
                self.source_tower = None

if __name__ == "__main__":
    root = tk.Tk()
    game = TowerOfHanoi(root, num_disks=3)
    root.mainloop()

import tkinter as tk
from tkinter import ttk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = {
            "Important and Urgent": [],
            "Important not Urgent": [],
            "Urgent not important": [],
            "Not Urgent Nor Important": []
        }

        self.root.configure(bg="gray")

        top_strip = tk.Canvas(self.root, bg="aqua", height=10)
        top_strip.pack(fill=tk.X)

        input_frame = ttk.Frame(self.root, padding=10)
        input_frame.pack(fill=tk.X)

        self.input_var = tk.StringVar()

        input_container = ttk.Frame(input_frame)
        input_container.pack(fill=tk.X)

        
        self.input_entry = ttk.Entry(input_container, textvariable=self.input_var, font=("Helvetica", 14), justify="center")
        self.input_entry.pack(fill=tk.BOTH, padx=5, pady=(10, 20))  

        self.input_entry.insert(tk.END, "Enter your task here...")
        self.input_entry.bind("<FocusIn>", self.on_entry_focus_in)
        self.input_entry.bind("<FocusOut>", self.on_entry_focus_out)

        self.priority_var = tk.StringVar(value="Important and Urgent")

        priority_label = ttk.Label(input_frame, text="Select Priority:", font=("Helvetica", 14))
        priority_label.pack(pady=5)

        priorities = ["Important and Urgent", "Important not Urgent", "Urgent not important", "Not Urgent Nor Important"]
        priority_combobox = ttk.Combobox(input_frame, textvariable=self.priority_var, values=priorities, font=("Helvetica", 14), state="readonly", justify="center")
        priority_combobox.pack(pady=5)

        add_button = ttk.Button(input_frame, text="Add Task", command=self.add_task, width=15, style="Bold.TButton")
        add_button.pack(pady=10)

        self.style = ttk.Style()
        self.style.configure("Bold.TButton", font=("Helvetica", 14, "bold"))

        lists_frame = ttk.Frame(self.root, padding=10)
        lists_frame.pack(fill=tk.BOTH, expand=True)

        self.create_task_lists(lists_frame)

        bottom_strip = tk.Canvas(self.root, bg="aqua", height=10)
        bottom_strip.pack(fill=tk.X)

        
        buttons_frame = ttk.Frame(self.root, style="DarkGray.TFrame")
        buttons_frame.pack(side=tk.BOTTOM, fill=tk.X)

        
        complete_button = ttk.Button(buttons_frame, text="Mark as Complete", command=self.mark_selected_as_complete, width=15, style="Bold.TButton")
        complete_button.pack(pady=5)

        
        delete_button = ttk.Button(buttons_frame, text="Delete", command=self.delete_selected_tasks, width=15, style="Bold.TButton")
        delete_button.pack(pady=5)

        
        self.style.configure("DarkGray.TFrame", background="dark gray")

    def create_task_lists(self, parent):
        for priority, color in [("Important and Urgent", "light green"), ("Important not Urgent", "orange"), ("Urgent not important", "red"), ("Not Urgent Nor Important", "yellow")]:
            list_frame = ttk.Frame(parent, padding=5)
            list_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

            label = tk.Label(list_frame, text=priority, font=("Helvetica", 14), bg=color)
            label.pack(fill=tk.BOTH, pady=(5, 0))

            listbox = tk.Listbox(list_frame, selectbackground="gray", selectborderwidth=0, selectmode=tk.MULTIPLE, font=("Helvetica", 14))
            listbox.pack(fill=tk.BOTH, expand=True)
            self.tasks[priority].append(listbox)

    def add_task(self):
        task = self.input_var.get()
        priority = self.priority_var.get()

        if task and task != "Enter your task here...":
            listbox = self.tasks[priority][0]
            listbox.insert(tk.END, task)
            self.input_var.set("Enter your task here...")

    def on_entry_focus_in(self, event):
        if self.input_var.get() == "Enter your task here...":
            self.input_var.set("")

    def on_entry_focus_out(self, event):
        if not self.input_var.get():
            self.input_var.set("Enter your task here...")

    def delete_selected_tasks(self):
        for priority in self.tasks:
            listbox = self.tasks[priority][0]
            selected_indices = listbox.curselection()
            for index in reversed(selected_indices):
                listbox.delete(index)

    def mark_selected_as_complete(self):
        for priority in self.tasks:
            listbox = self.tasks[priority][0]
            selected_indices = listbox.curselection()
            for index in selected_indices:
                task = listbox.get(index)
                if "✓" not in task:
                    listbox.delete(index)
                    listbox.insert(index, "✓ " + task)

def main():
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

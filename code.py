import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataVisualizationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Visualization Tool")

        self.data_points = []

        # Create input frame
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=10)

        self.x_label = tk.Label(self.input_frame, text="X:")
        self.x_label.grid(row=0, column=0)
        self.x_entry = tk.Entry(self.input_frame, width=10)
        self.x_entry.grid(row=0, column=1)

        self.y_label = tk.Label(self.input_frame, text="Y:")
        self.y_label.grid(row=0, column=2)
        self.y_entry = tk.Entry(self.input_frame, width=10)
        self.y_entry.grid(row=0, column=3)

        self.add_button = tk.Button(self.input_frame, text="Add Point", command=self.add_point)
        self.add_button.grid(row=0, column=4, padx=10)

        self.plot_type_label = tk.Label(self.input_frame, text="Plot Type:")
        self.plot_type_label.grid(row=0, column=5)

        self.plot_type = tk.StringVar(value="Scatter")
        self.plot_type_menu = ttk.Combobox(self.input_frame, textvariable=self.plot_type, values=["Scatter", "Line", "Bar"])
        self.plot_type_menu.grid(row=0, column=6, padx=10)

        self.plot_button = tk.Button(self.input_frame, text="Plot", command=self.plot_data)
        self.plot_button.grid(row=0, column=7, padx=10)

        self.clear_button = tk.Button(self.input_frame, text="Clear", command=self.clear_data)
        self.clear_button.grid(row=0, column=8, padx=10)

        # Create plot frame
        self.plot_frame = tk.Frame(self.root)
        self.plot_frame.pack(pady=10)

        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.plot_frame)
        self.canvas.get_tk_widget().pack()

    def add_point(self):
        try:
            x = float(self.x_entry.get())
            y = float(self.y_entry.get())
            self.data_points.append((x, y))
            self.x_entry.delete(0, tk.END)
            self.y_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Data point added successfully!")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for X and Y.")

    def plot_data(self):
        if not self.data_points:
            messagebox.showwarning("No Data", "No data points to plot.")
            return

        self.ax.clear()
        x_values, y_values = zip(*self.data_points)
        plot_type = self.plot_type.get()

        if plot_type == "Scatter":
            self.ax.scatter(x_values, y_values)
            self.ax.set_title("Scatter Plot of Data Points")
        elif plot_type == "Line":
            self.ax.plot(x_values, y_values)
            self.ax.set_title("Line Plot of Data Points")
        elif plot_type == "Bar":
            self.ax.bar(x_values, y_values)
            self.ax.set_title("Bar Plot of Data Points")

        self.ax.set_xlabel("X")
        self.ax.set_ylabel("Y")
        self.canvas.draw()

    def clear_data(self):
        self.data_points.clear()
        self.ax.clear()
        self.canvas.draw()
        messagebox.showinfo("Cleared", "All data points cleared.")

# Initialize Tkinter root window
root = tk.Tk()
app = DataVisualizationApp(root)

# Run the Tkinter event loop
root.mainloop()

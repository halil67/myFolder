import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3

class Appointment:
    def __init__(self, title, date, time, repeat, status="Planned"):
        self.title = title
        self.date = date
        self.time = time
        self.repeat = repeat
        self.status = status

class AppointmentManager:
    def __init__(self, db_filename):
        self.db_filename = db_filename
        self.conn = sqlite3.connect(self.db_filename)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute(
                '''CREATE TABLE IF NOT EXISTS appointments (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    date TEXT,
                    time TEXT,
                    repeat TEXT,
                    status TEXT
                )'''
            )

    def add_appointment(self, title, date, time, repeat):
        with self.conn:
            self.conn.execute(
                '''INSERT INTO appointments (title, date, time, repeat, status)
                VALUES (?, ?, ?, ?, ?)''',
                (title, date, time, repeat, "Planned")
            )

    def list_appointments(self):
        with self.conn:
            cursor = self.conn.execute(
                '''SELECT id, title, date, time, repeat, status FROM appointments'''
            )
            return cursor.fetchall()

    def update_appointment_status(self, appointment_id, status):
        with self.conn:
            self.conn.execute(
                '''UPDATE appointments SET status = ? WHERE id = ?''',
                (status, appointment_id)
            )

class AppointmentApp:
    def __init__(self, root):
        self.manager = AppointmentManager('appointments.db')
        
        self.root = root
        self.root.title("Randevu Planlayıcı")

        self.title_label = tk.Label(root, text="Başlık")
        self.title_label.grid(row=0, column=0)
        self.title_entry = tk.Entry(root)
        self.title_entry.grid(row=0, column=1)

        self.date_label = tk.Label(root, text="Tarih")
        self.date_label.grid(row=1, column=0)
        self.date_entry = DateEntry(root, date_pattern='yyyy-mm-dd')
        self.date_entry.grid(row=1, column=1)

        self.time_label = tk.Label(root, text="Saat")
        self.time_label.grid(row=2, column=0)
        
        self.time_combobox = ttk.Combobox(root, values=[f"{hour:02}:00" for hour in range(24)])
        self.time_combobox.grid(row=2, column=1)
        self.time_combobox.set("09:00")

        self.repeat_label = tk.Label(root, text="Tekrar")
        self.repeat_label.grid(row=3, column=0)
        
        self.repeat_combobox = ttk.Combobox(root, values=["Yok", "Günlük", "Haftalık", "Aylık"])
        self.repeat_combobox.grid(row=3, column=1)
        self.repeat_combobox.set("Yok")

        self.add_button = tk.Button(root, text="Randevu Ekle", command=self.add_appointment)
        self.add_button.grid(row=4, column=0, columnspan=2)

        self.list_button = tk.Button(root, text="Randevuları Listele", command=self.list_appointments)
        self.list_button.grid(row=5, column=0, columnspan=2)

        self.appointments_listbox = tk.Listbox(root, height=10, width=50)
        self.appointments_listbox.grid(row=6, column=0, columnspan=2)
        self.appointments_listbox.bind('<<ListboxSelect>>', self.on_appointment_select)

        self.status_label = tk.Label(root, text="Randevu Durumu Güncelle")
        self.status_label.grid(row=7, column=0, columnspan=2)

        self.status_combobox = ttk.Combobox(root, values=["Planned", "Completed", "Cancelled"])
        self.status_combobox.grid(row=8, column=0, columnspan=2)
        self.status_combobox.set("Planned")

        self.update_status_button = tk.Button(root, text="Durumu Güncelle", command=self.update_appointment_status)
        self.update_status_button.grid(row=9, column=0, columnspan=2)

    def add_appointment(self):
        title = self.title_entry.get()
        date = self.date_entry.get()
        time = self.time_combobox.get()
        repeat = self.repeat_combobox.get()

        if not title or not date or not time or not repeat:
            messagebox.showwarning("Eksik bilgi", "Lütfen tüm alanları doldurun.")
            return

        self.manager.add_appointment(title, date, time, repeat)
        messagebox.showinfo("Başarılı", f"Randevu eklendi: {title} on {date} at {time}, Repeat: {repeat}")

        self.title_entry.delete(0, tk.END)
        self.date_entry.set_date('')
        self.time_combobox.set("09:00")
        self.repeat_combobox.set("Yok")

    def list_appointments(self):
        appointments = self.manager.list_appointments()
        self.appointments_listbox.delete(0, tk.END)

        if not appointments:
            self.appointments_listbox.insert(tk.END, "Henüz eklenmiş bir randevu yok.")
            return

        for idx, appointment in enumerate(appointments):
            self.appointments_listbox.insert(
                tk.END, 
                f"{appointment[0]}. {appointment[1]} on {appointment[2]} at {appointment[3]} - Repeat: {appointment[4]} - Status: {appointment[5]}"
            )

    def on_appointment_select(self, event):
        try:
            selected_index = self.appointments_listbox.curselection()[0]
            self.selected_appointment_index = selected_index
        except IndexError:
            return

    def update_appointment_status(self):
        try:
            selected_appointment = self.appointments_listbox.get(self.selected_appointment_index)
            appointment_id = int(selected_appointment.split(".")[0])
            status = self.status_combobox.get()
            self.manager.update_appointment_status(appointment_id, status)
            messagebox.showinfo("Başarılı", "Randevu durumu güncellendi.")
            self.list_appointments()
        except AttributeError:
            messagebox.showwarning("Hata", "Lütfen bir randevu seçin.")
        except IndexError:
            messagebox.showwarning("Hata", "Geçersiz randevu numarası.")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentApp(root)
    root.mainloop()

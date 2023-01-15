import tkinter as tk
import time
from datetime import datetime
import paramiko

class App:
    def __init__(self, master):
        self.master = master
        self.is_running = False  # zmienna flagowa do start/stop funkcji
        self.is_power_on = False
        self.temp_calc = 0 
        self.temp_info = '20'
        self.rinse_calc = 0
        self.rinse_info = '1'
        self.spin_calc = 0
        self.spin_info = '0'
        self.option_calc = 0
        self.option_info = 'PS'
        self.temp_time_simulatior = 5
        self.rinse_time_simulatior = 5
        self.spin_time_simulatior = 0
        self.option_time_simulatior = 5
        self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
        print(f'Całościowy czas {self.all_time_simulation}')
        self.running = False
        self.block_simulator = False
        self.approve_adres_ip = ''
        
        # tworzenie ramki lewej
        self.left_frame = tk.LabelFrame(master, width=200, height=200,  highlightthickness=3, borderwidth=2)
        self.left_frame.pack(side='left', fill='both', expand=True)
        
        # tworzenie ramki prawej
        self.right_frame = tk.LabelFrame(master, width=200, height=200, highlightthickness=3, borderwidth=2)
        self.right_frame.pack(side='left', fill='both', expand=True)

        # tworzenie ramki górnej lewej
        self.top_left_frame = tk.Frame(self.left_frame, width=200, height=100, highlightthickness=3, borderwidth=2)
        self.top_left_frame.pack(side='top', fill='both', expand=True)

        # tworzenie ramki środkowej lewej
        self.middle_left_frame = tk.Frame(self.left_frame, width=200, height=50, highlightthickness=3, borderwidth=2)
        self.middle_left_frame.pack(side='top', fill='both', expand=True)

        # tworzenie ramki dolnej lewej
        self.bottom_left_frame = tk.Frame(self.left_frame, width=200, height=50, highlightthickness=3, borderwidth=2)
        self.bottom_left_frame.pack(side='top', fill='both', expand=True)

        # tworzenie etykiety w ramce górnej lewej
        self.time_label = tk.Label(self.top_left_frame, text="0:00:00", font=("Arial",48))
        self.time_label.pack()
        self.info_label = tk.Label(self.top_left_frame, text="---------------", font=("Arial",30))
        self.info_label.pack()

        self.temperatur_frame = tk.LabelFrame(self.middle_left_frame, width=200, height=50, highlightthickness=3, borderwidth=2)
        self.temperatur_frame.grid(row=0, column=0)
        # tworzenie etykiety w ramce środkowej lewej
        self.label20 = tk.Label(self.temperatur_frame, text='20')
        self.label20.grid(row=4, column=0)
        self.led_20 = tk.Canvas(self.temperatur_frame, width=20, height=20)
        self.led_20.grid(row=4, column=1, sticky="W")
        self.led_20.create_oval(5, 5, 15, 15, fill="red")
        self.label30 = tk.Label(self.temperatur_frame, text='30')
        self.label30.grid(row=3, column=0)
        self.led_30 = tk.Canvas(self.temperatur_frame, width=20, height=20)
        self.led_30.grid(row=3, column=1, sticky="W")
        self.led_30.create_oval(5, 5, 15, 15, fill="red")
        self.label40 = tk.Label(self.temperatur_frame, text='40')
        self.label40.grid(row=2, column=0)
        self.led_40 = tk.Canvas(self.temperatur_frame, width=20, height=20)
        self.led_40.grid(row=2, column=1, sticky="W")
        self.led_40.create_oval(5, 5, 15, 15, fill="red")
        self.label60 = tk.Label(self.temperatur_frame, text='60')
        self.label60.grid(row=1, column=0)
        self.led_60 = tk.Canvas(self.temperatur_frame, width=20, height=20)
        self.led_60.grid(row=1, column=1, sticky="W")
        self.led_60.create_oval(5, 5, 15, 15, fill="red")
        self.label90 = tk.Label(self.temperatur_frame, text='90')
        self.label90.grid(row=0, column=0)
        self.led_90 = tk.Canvas(self.temperatur_frame, width=20, height=20)
        self.led_90.grid(row=0, column=1, sticky="W")
        self.led_90.create_oval(5, 5, 15, 15, fill="red")
        self.temp_button_frame = tk.LabelFrame(self.middle_left_frame, width=200, height=50, highlightthickness=3, borderwidth=2)
        self.temp_button_frame.grid(row=5, column=0)        
        self.buttonTemp = tk.Button(self.temp_button_frame, text='Temp.', command=self.temp)
        self.buttonTemp.pack(fill='both', expand=True)
        
        self.rinse_frame = tk.LabelFrame(self.middle_left_frame, width=200, height=50, highlightthickness=3, borderwidth=2)
        self.rinse_frame.grid(row=0, column=1)
        self.label_rinse1 = tk.Label(self.rinse_frame, text='1')
        self.label_rinse1.grid(row=4, column=0)
        self.led_rinse1 = tk.Canvas(self.rinse_frame, width=20, height=20)
        self.led_rinse1.grid(row=4, column=1, sticky="W")
        self.led_rinse1.create_oval(5, 5, 15, 15, fill="red")
        self.label_rinse2 = tk.Label(self.rinse_frame, text='2')
        self.label_rinse2.grid(row=3, column=0)
        self.led_rinse2 = tk.Canvas(self.rinse_frame, width=20, height=20)
        self.led_rinse2.grid(row=3, column=1, sticky="W")
        self.led_rinse2.create_oval(5, 5, 15, 15, fill="red")
        self.label_rinse3 = tk.Label(self.rinse_frame, text='3')
        self.label_rinse3.grid(row=2, column=0)
        self.led_rinse3 = tk.Canvas(self.rinse_frame, width=20, height=20)
        self.led_rinse3.grid(row=2, column=1, sticky="W")
        self.led_rinse3.create_oval(5, 5, 15, 15, fill="red")
        self.label_rinse4 = tk.Label(self.rinse_frame, text='4')
        self.label_rinse4.grid(row=1, column=0)
        self.led_rinse4 = tk.Canvas(self.rinse_frame, width=20, height=20)
        self.led_rinse4.grid(row=1, column=1, sticky="W")
        self.led_rinse4.create_oval(5, 5, 15, 15, fill="red")
        self.label_rinse5 = tk.Label(self.rinse_frame, text='5')
        self.label_rinse5.grid(row=0, column=0)
        self.led_rinse5 = tk.Canvas(self.rinse_frame, width=20, height=20)
        self.led_rinse5.grid(row=0, column=1, sticky="W")
        self.led_rinse5.create_oval(5, 5, 15, 15, fill="red")
        self.rinse_button_frame = tk.LabelFrame(self.middle_left_frame, width=200, height=50, highlightthickness=3, borderwidth=2)
        self.rinse_button_frame.grid(row=5, column=1)        
        self.buttonRinse = tk.Button(self.rinse_button_frame, text=' Rinse', command=self.rinse)
        self.buttonRinse.pack(fill='both', expand=True)
        
        self.spin_frame = tk.LabelFrame(self.middle_left_frame, width=200, height=50, highlightthickness=3, borderwidth=2)
        self.spin_frame.grid(row=0, column=2)
        self.label_spin0 = tk.Label(self.spin_frame, text='0')
        self.label_spin0.grid(row=4, column=0)
        self.led_spin0 = tk.Canvas(self.spin_frame, width=20, height=20)
        self.led_spin0.grid(row=4, column=1, sticky="W")
        self.led_spin0.create_oval(5, 5, 15, 15, fill="red")
        self.label_spin400 = tk.Label(self.spin_frame, text='400')
        self.label_spin400.grid(row=3, column=0)
        self.led_spin400 = tk.Canvas(self.spin_frame, width=20, height=20)
        self.led_spin400.grid(row=3, column=1, sticky="W")
        self.led_spin400.create_oval(5, 5, 15, 15, fill="red")
        self.label_spin800 = tk.Label(self.spin_frame, text='800')
        self.label_spin800.grid(row=2, column=0)
        self.led_spin800 = tk.Canvas(self.spin_frame, width=20, height=20)
        self.led_spin800.grid(row=2, column=1, sticky="W")
        self.led_spin800.create_oval(5, 5, 15, 15, fill="red")
        self.label_spin1200 = tk.Label(self.spin_frame, text='1200')
        self.label_spin1200.grid(row=1, column=0)
        self.led_spin1200 = tk.Canvas(self.spin_frame, width=20, height=20)
        self.led_spin1200.grid(row=1, column=1, sticky="W")
        self.led_spin1200.create_oval(5, 5, 15, 15, fill="red")
        self.label_spin1400 = tk.Label(self.spin_frame, text='1400')
        self.label_spin1400.grid(row=0, column=0)
        self.led_spin1400 = tk.Canvas(self.spin_frame, width=20, height=20)
        self.led_spin1400.grid(row=0, column=1, sticky="W")
        self.led_spin1400.create_oval(5, 5, 15, 15, fill="red")
        self.spin_button_frame = tk.LabelFrame(self.middle_left_frame, width=200, height=50, highlightthickness=3, borderwidth=2)
        self.spin_button_frame.grid(row=5, column=2)        
        self.button_spin = tk.Button(self.spin_button_frame, text='    Spin   ', command=self.spin)
        self.button_spin.pack(fill='both', expand=True)

        self.option_frame = tk.LabelFrame(self.middle_left_frame, width=200, height=50, highlightthickness=3, borderwidth=2)
        self.option_frame.grid(row=0, column=3)
        self.label_option1 = tk.Label(self.option_frame, text='PS')
        self.label_option1.grid(row=4, column=0)
        self.led_option1 = tk.Canvas(self.option_frame, width=20, height=20)
        self.led_option1.grid(row=4, column=1, sticky="W")
        self.led_option1.create_oval(5, 5, 15, 15, fill="red")
        self.label_option2 = tk.Label(self.option_frame, text='PW')
        self.label_option2.grid(row=3, column=0)
        self.led_option2 = tk.Canvas(self.option_frame, width=20, height=20)
        self.led_option2.grid(row=3, column=1, sticky="W")
        self.led_option2.create_oval(5, 5, 15, 15, fill="red")
        self.label_option3 = tk.Label(self.option_frame, text='PTK')
        self.label_option3.grid(row=2, column=0)
        self.led_option3 = tk.Canvas(self.option_frame, width=20, height=20)
        self.led_option3.grid(row=2, column=1, sticky="W")
        self.led_option3.create_oval(5, 5, 15, 15, fill="red")
        self.label_option4 = tk.Label(self.option_frame, text='PUMZ')
        self.label_option4.grid(row=1, column=0)
        self.led_option4 = tk.Canvas(self.option_frame, width=20, height=20)
        self.led_option4.grid(row=1, column=1, sticky="W")
        self.led_option4.create_oval(5, 5, 15, 15, fill="red")
        self.label_option5 = tk.Label(self.option_frame, text='PR')
        self.label_option5.grid(row=0, column=0)
        self.led_option5 = tk.Canvas(self.option_frame, width=20, height=20)
        self.led_option5.grid(row=0, column=1, sticky="W")
        self.led_option5.create_oval(5, 5, 15, 15, fill="red")
        self.option_button_frame = tk.LabelFrame(self.middle_left_frame, width=200, height=50, highlightthickness=3, borderwidth=2)
        self.option_button_frame.grid(row=5, column=3)        
        self.button_option = tk.Button(self.option_button_frame, text='  Option  ', command=self.option)
        self.button_option.pack(fill='both', expand=True)
        self.label_option_Info = tk.Label(self.left_frame, text='PS - Pranie Skrócone \nPW - Pranie Wstępne\nPTK - Pranie Tkanin Syntetycznych\nPUMZ - Pranie Ubrań Mocno Zabrudzonych\nPR - Pranie Ręczne')
        self.label_option_Info.pack()


        # tworzenie przycisków w ramce prawej
        self.button_power = tk.Button(self.right_frame, text='  Włącz  ', command=self.power_on_off)
        self.button_power.grid(row=0, column=0)
        self.check_status_power = tk.Canvas(self.right_frame, width=20, height=20)
        self.check_status_power.grid(row=0, column=1, sticky="W")
        self.check_status_power.create_oval(5, 5, 15, 15, fill="red")
        
        self.button_start_stop = tk.Button(self.right_frame, text='   Start    ', command=self.start_stop)
        self.button_start_stop.grid(row=1, column=0)
        self.check_status_start = tk.Canvas(self.right_frame, width=20, height=20)
        self.check_status_start.grid(row=1, column=1, sticky="W")
        self.check_status_start.create_oval(5, 5, 15, 15, fill="red")
    
        self.sending_data_main_frame = tk.LabelFrame(master, width=200, height=200, highlightthickness=3, borderwidth=2)
        self.sending_data_main_frame.pack(side='right', fill='both', expand=True)
        self.connection_frame = tk.LabelFrame(self.sending_data_main_frame, width=200, height=200, highlightthickness=3, borderwidth=2)
        self.connection_frame.grid(row=0,column=0)
        self.data_con_frame = tk.LabelFrame(self.sending_data_main_frame, width=200, height=200, highlightthickness=3, borderwidth=2)
        self.data_con_frame.grid(row=1,column=0)
        
        self.label_connection_info = tk.Label(self.connection_frame, text='Połączenie się z Jednostką Kontrolną')
        self.label_connection_info.grid(row=0,column=0)
        def limit_entry_3(string):
            # Zwraca True, jeśli długość string jest mniejsza niż 3
            if all(c.isnumeric() for c in string):
                return len(string) <= 3 
            return False
            
        self.connection_ip_frame = tk.Frame(self.connection_frame,highlightthickness=3, borderwidth=2)
        self.connection_ip_frame.grid(row=2,column=0)
        self.label_ip_info = tk.Label(self.connection_frame, text='Podaj Adres IP')
        self.label_ip_info.grid(row=1, column=0)        
        self.entry_ip_address1 = tk.Entry(self.connection_ip_frame, width = 3, validate="key", validatecommand=(root.register(limit_entry_3), "%P"))
        self.entry_ip_address1.grid(row=1,column=0)
        self.label_ip_dot1 = tk.Label(self.connection_ip_frame, text='.')
        self.label_ip_dot1.grid(row=1, column=1)   
        self.entry_ip_address2 = tk.Entry(self.connection_ip_frame, width = 3, validate="key", validatecommand=(root.register(limit_entry_3), "%P"))
        self.entry_ip_address2.grid(row=1,column=2)
        self.label_ip_dot2 = tk.Label(self.connection_ip_frame, text='.')
        self.label_ip_dot2.grid(row=1, column=3)  
        self.entry_ip_address3 = tk.Entry(self.connection_ip_frame, width = 3, validate="key", validatecommand=(root.register(limit_entry_3), "%P"))
        self.entry_ip_address3.grid(row=1,column=4)
        self.label_ip_dot3 = tk.Label(self.connection_ip_frame, text='.')
        self.label_ip_dot3.grid(row=1, column=5)  
        self.entry_ip_address4 = tk.Entry(self.connection_ip_frame, width = 3, validate="key", validatecommand=(root.register(limit_entry_3), "%P"))
        self.entry_ip_address4.grid(row=1,column=6)
        
        self.data_ip_frame = tk.Frame(self.connection_frame,highlightthickness=3, borderwidth=2)
        self.data_ip_frame.grid(row=3,column=0)
        self.label_ip_user = tk.Label(self.data_ip_frame, text='Username:')
        self.label_ip_user.grid(row=0, column=0)  
        self.entry_user_ip = tk.Entry(self.data_ip_frame, width = 15, validate="key")
        self.entry_user_ip.grid(row=0, column=1)
        self.label_ip_password = tk.Label(self.data_ip_frame, text='Password:')
        self.label_ip_password.grid(row=1, column=0)  
        self.entry_password_ip = tk.Entry(self.data_ip_frame, width = 15, validate="key")
        self.entry_password_ip.grid(row=1, column=1)
        self.button_approve_ip = tk.Button(self.connection_frame, text='Approve IP Data', command=self.approve_ip)
        self.button_approve_ip.grid(row=4,column=0)
        self.label_approve_ip = tk.Label(self.connection_frame, text='Nie zatwierdzono IP')
        self.label_approve_ip.grid(row=5,column=0)
        
        
        self.button_ip_try_connection = tk.Button(self.connection_frame, text='Spróbuj Nawiązać Połączenie', command=self.try_connection_ip)
        self.button_ip_try_connection.grid(row=6,column=0)
        self.label_ip_try_connection = tk.Label(self.connection_frame, text='Nie Wykonano Próby')
        self.label_ip_try_connection.grid(row=7,column=0)        
        self.led_ip_try_connection = tk.Canvas(self.connection_frame, width=20, height=20)
        self.led_ip_try_connection.grid(row=6, column=1, sticky="W")
        self.led_ip_try_connection.create_oval(5, 5, 15, 15, fill="red")
        self.button_ip_disconnection = tk.Button(self.connection_frame, text='Rozłącz', command=self.disconnec_ip)
        self.button_ip_disconnection.grid(row=8,column=0)
       
        self.label_sending_data_info = tk.Label(self.data_con_frame, text='Ramka do informacji co wysłano')
        self.label_sending_data_info.grid(row=0, column=0)
    
    def end_sim(self):
            print("Wyłączono Zasilanie")
            self.temp_calc = 0
            self.is_power_on = False
            self.is_running = False
            self.button_power.configure(text="  Włącz  ")
            self.check_status_power.destroy()
            self.check_status_power = tk.Canvas(self.right_frame, width=20, height=20)
            self.check_status_power.grid(row=0, column=1, sticky="W")
            self.check_status_power.create_oval(5, 5, 15, 15, fill="red")
            self.led_creator(20, self.temperatur_frame, 4, 1, "red")
            self.led_creator(30, self.temperatur_frame, 3, 1, "red")
            self.led_creator(40, self.temperatur_frame, 2, 1, "red")
            self.led_creator(60, self.temperatur_frame, 1, 1, "red")
            self.led_creator(90, self.temperatur_frame, 0, 1, "red")
            self.led_creator('rinse1', self.rinse_frame, 4, 1, "red")
            self.led_creator('rinse2', self.rinse_frame, 3, 1, "red")
            self.led_creator('rinse3', self.rinse_frame, 2, 1, "red")
            self.led_creator('rinse4', self.rinse_frame, 1, 1, "red")
            self.led_creator('rinse5', self.rinse_frame, 0, 1, "red")
            self.led_creator('spin0', self.spin_frame, 4, 1, "red")
            self.led_creator('spin400', self.spin_frame, 3, 1, "red")
            self.led_creator('spin800', self.spin_frame, 2, 1, "red")
            self.led_creator('spin1200', self.spin_frame, 1, 1, "red")
            self.led_creator('spin1400', self.spin_frame, 0, 1, "red")
            self.led_creator('option1', self.option_frame, 4, 1, "red")
            self.led_creator('option2', self.option_frame, 3, 1, "red")
            self.led_creator('option3', self.option_frame, 2, 1, "red")
            self.led_creator('option4', self.option_frame, 1, 1, "red")
            self.led_creator('option5', self.option_frame, 0, 1, "red")
            self.button_start_stop.configure(text="   Start    ")
            self.check_status_start.destroy()
            self.check_status_start = tk.Canvas(self.right_frame, width=20, height=20)
            self.check_status_start.grid(row=1, column=1, sticky="W")
            self.check_status_start.create_oval(5, 5, 15, 15, fill="red")
            self.time_label.configure(text="0:00:00")
            self.info_label.configure(text="---------------")
            self.temp_calc = 0 
            self.temp_info = '20'
            self.rinse_calc = 0
            self.rinse_info = '1'
            self.spin_calc = 0
            self.spin_info = '0'
            self.option_calc = 0
            self.option_info = 'PS'
            self.temp_time_simulatior = 5
            self.rinse_time_simulatior = 5
            self.spin_time_simulatior = 0
            self.option_time_simulatior = 5
            self.block_simulator = False
            self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
        
                    
    def sim_time(self):
        self.block_simulator = True
        if self.is_running and self.all_time_simulation>0:
            self.all_time_simulation -= 1
            self.time_label.configure(text=self.get_time_string())
            self.top_left_frame.after(1000, self.sim_time)
            print(self.all_time_simulation)
            self.info_label.configure(text="Program w toku")
        elif self.is_running and self.all_time_simulation <= 0 and self.all_time_simulation >= -3: 
            self.all_time_simulation -= 1
            self.info_label.configure(text="Koniec Programu")
            print(self.all_time_simulation)
            self.top_left_frame.after(1000, self.sim_time)
        elif self.is_running and self.all_time_simulation <= -4 and self.all_time_simulation >= -9:
            self.all_time_simulation -= 1
            print(self.all_time_simulation)
            self.info_label.configure(text="Wyłączenie urządzenia")
            self.top_left_frame.after(1000, self.sim_time)
            
        elif self.is_running and self.all_time_simulation >= -10:
            print(self.all_time_simulation)
            self.end_sim()
        else: 
            print(self.all_time_simulation)
                
        
    def start_stop(self):
        if not self.is_running and self.is_power_on:  # jeśli funkcja nie jest uruchomiona
            # tutaj możesz dodać kod, który ma się wykonać po kliknięciu przycisku
            print('Start')
            print(f'Program {self.is_running}')
            self.button_start_stop.configure(text="   Stop    ")
            self.is_running = True  # zmiana stanu zmiennej flagowej
            self.check_status_start.destroy()
            self.check_status_start = tk.Canvas(self.right_frame, width=20, height=20)
            self.check_status_start.grid(row=1, column=1, sticky="W")
            self.check_status_start.create_oval(5, 5, 15, 15, fill="light green")
            button_start_stop = self.button_start_stop.config('text')[-1]
            if button_start_stop == "  Wznów ":
                current_time = datetime.now()
                time_log = current_time.strftime("%Y-%m-%d %H:%M:%S")
                time_log2 = current_time.strftime("%Y%m%d")
                data = f'{time_log} Wznowiono Program \n'
                with open(f'log/logs{time_log2}.txt', "a",encoding="utf-8") as file:
                    file.write(data)
            else:
                current_time = datetime.now()
                time_log = current_time.strftime("%Y-%m-%d %H:%M:%S")
                time_log2 = current_time.strftime("%Y%m%d")
                data = f'{time_log} Wystartowano Program\nOption: {self.option_info}\nTemp: {self.temp_info}\nRinse: {self.rinse_info}\nSpin: {self.spin_info}\nMisja Potrwa: {self.all_time_simulation}\n'
                with open(f'log/logs{time_log2}.txt', "a",encoding="utf-8") as file:
                    file.write(data)
            self.sim_time()
            
            
        elif self.is_running and self.is_power_on:
            print('Stop')
            print(f'Program {self.is_running}')
            
            self.button_start_stop.configure(text="  Wznów ")
            current_time = datetime.now()
            time_log = current_time.strftime("%Y-%m-%d %H:%M:%S")
            time_log2 = current_time.strftime("%Y%m%d")
            data = f'{time_log} Zastopowano Program \n'
            with open(f'log/logs{time_log2}.txt', "a",encoding="utf-8") as file:
                file.write(data)
            self.is_running = False  # zmiana stanu zmiennej flagowej
            self.check_status_start.destroy()
            self.check_status_start = tk.Canvas(self.right_frame, width=20, height=20)
            self.check_status_start.grid(row=1, column=1, sticky="W")
            self.check_status_start.create_oval(5, 5, 15, 15, fill="orange")
            
        elif not self.is_running and self.is_power_on:
            print("Wznów")
            print(f'Program {self.is_running}')
            current_time = datetime.now()
            time_log = current_time.strftime("%Y-%m-%d %H:%M:%S")
            time_log2 = current_time.strftime("%Y%m%d")
            data = f'{time_log} Wznowiono Program\n '
            with open(f'log/logs{time_log2}.txt', "a",encoding="utf-8") as file:
                file.write(data)
            
            self.check_status_start.destroy()
            self.check_status_start = tk.Canvas(self.right_frame, width=20, height=20)
            self.check_status_start.grid(row=1, column=1, sticky="W")
            self.check_status_start.create_oval(5, 5, 15, 15, fill="light green")
        else:
            print("Nie włączono urządzenia")
            

    def power_on_off(self):
        if not self.is_power_on:
            current_time = datetime.now()
            time_log = current_time.strftime("%Y-%m-%d %H:%M:%S")
            time_log2 = current_time.strftime("%Y%m%d")
            data = f'{time_log} Włączono Urządzenie\n'
            with open(f'log/logs{time_log2}.txt', "a",encoding="utf-8") as file:
                file.write(data)
            self.is_power_on = True
            self.button_power.configure(text=" Wyłącz  ")
            self.check_status_power.destroy()
            self.check_status_power = tk.Canvas(self.right_frame, width=20, height=20)
            self.check_status_power.grid(row=0, column=1, sticky="W")
            self.check_status_power.create_oval(5, 5, 15, 15, fill="light green")
            self.led_creator(20, self.temperatur_frame, 4, 1, "light green")
            self.led_creator('rinse1', self.rinse_frame, 4, 1, "light green")
            self.led_creator('spin0', self.spin_frame, 4, 1, "light green")
            self.led_creator('option1', self.option_frame, 4, 1, "light green")
            self.time_label.configure(text=self.get_time_string())
        else:
            current_time = datetime.now()
            time_log = current_time.strftime("%Y-%m-%d %H:%M:%S")
            time_log2 = current_time.strftime("%Y%m%d")
            data = f'{time_log} Wyłączono Urządzenie\n'
            with open(f'log/logs{time_log2}.txt', "a",encoding="utf-8") as file:
                file.write(data)
            self.end_sim()
        
    def led_creator(self, name, frame, l_row, l_column, l_color):    
        led_name = f'led_{name}'
        led = getattr(self, led_name)
        try:
            led.destroy()
        except:
            print("Nie ma ledów do usunięcia")
       
        led = tk.Canvas(frame, width=20, height=20)
        led.grid(row=l_row, column=l_column, sticky="W")
        led.create_oval(5, 5, 15, 15, fill=l_color)
        setattr(self, led_name, led)

    def temp(self):
        if self.is_power_on and not self.is_running and not self.block_simulator:
            self.temp_calc +=1
            print(f'LED Temp. {self.temp_calc}')
            if self.temp_calc == 5:
                self.temp_calc = 0
                self.led_creator(90, self.temperatur_frame, 0, 1, "red")
                self.temp_info = '20'
                print("Reset Cyklu")
            if self.temp_calc == 0:
                self.led_creator(20, self.temperatur_frame, 4, 1, "light green")
                self.temp_info = '20'
            if self.temp_calc == 1:
                self.led_creator(20, self.temperatur_frame, 4, 1, "red")
                self.led_creator(30, self.temperatur_frame, 3, 1, "light green")
                self.temp_info = '30'
            if self.temp_calc == 2:
                self.led_creator(30, self.temperatur_frame, 3, 1, "red")
                self.led_creator(40, self.temperatur_frame, 2, 1, "light green")
                self.temp_info = '40'
            if self.temp_calc == 3:
                self.led_creator(40, self.temperatur_frame, 2, 1, "red")
                self.led_creator(60, self.temperatur_frame, 1, 1, "light green")
                self.temp_info = '60'
            if self.temp_calc == 4:
                self.led_creator(60, self.temperatur_frame, 1, 1, "red")
                self.led_creator(90, self.temperatur_frame, 0, 1, "light green")
                self.temp_info = '90'
                
    def rinse(self):
        if self.is_power_on and not self.is_running and not self.block_simulator:
            self.rinse_calc +=1
            print(f'LED Rinse {self.rinse_calc}')
            self.rinse_time_simulatior = 5
            print(f'Czas Rinse {self.rinse_time_simulatior}')
            self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
            print(f'Całościowy czas {self.all_time_simulation}')
            if self.rinse_calc == 5:
                self.rinse_calc = 0
                self.rinse_info = '0'
                self.led_creator('rinse5', self.rinse_frame, 0, 1, "red")
                self.rinse_time_simulatior = 5
                print(f'Czas Rinse {self.rinse_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.time_label.configure(text=self.get_time_string())
                print("Reset Cyklu")
            if self.rinse_calc == 0:
                self.rinse_time_simulatior = 5
                self.rinse_info = '1'
                print(f'Czas Rinse {self.rinse_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('rinse1', self.rinse_frame, 4, 1, "light green")
                self.time_label.configure(text=self.get_time_string())
            if self.rinse_calc == 1:
                self.rinse_time_simulatior = 10
                self.rinse_info = '2'
                print(f'Czas Rinse {self.rinse_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('rinse1', self.rinse_frame, 4, 1, "red")
                self.led_creator('rinse2', self.rinse_frame, 3, 1, "light green")
                self.time_label.configure(text=self.get_time_string())
            if self.rinse_calc == 2:
                self.rinse_time_simulatior = 15
                self.rinse_info = '3'
                print(f'Czas Rinse {self.rinse_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('rinse2', self.rinse_frame, 3, 1, "red")
                self.led_creator('rinse3', self.rinse_frame, 2, 1, "light green")
                self.time_label.configure(text=self.get_time_string())
            if self.rinse_calc == 3:
                self.rinse_time_simulatior = 20
                self.rinse_info = '4'
                print(f'Czas Rinse {self.rinse_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('rinse3', self.rinse_frame, 2, 1, "red")
                self.led_creator('rinse4', self.rinse_frame, 1, 1, "light green")
                self.time_label.configure(text=self.get_time_string())
            if self.rinse_calc == 4:
                self.rinse_time_simulatior = 25
                self.rinse_info = '5'
                print(f'Czas Rinse {self.rinse_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('rinse4', self.rinse_frame, 1, 1, "red")
                self.led_creator('rinse5', self.rinse_frame, 0, 1, "light green")    
                self.time_label.configure(text=self.get_time_string())
                
    def spin(self):
        if self.is_power_on and not self.is_running and not self.block_simulator: 
            self.spin_calc +=1
            print(f'LED Spin {self.spin_calc}')
            self.spin_time_simulatior = 0
            print(f'Czas Spin {self.spin_time_simulatior}')
            self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
            print(f'Całościowy czas {self.all_time_simulation}')
            if self.spin_calc == 5:
                self.spin_calc = 0
                self.spin_time_simulatior = 0
                self.spin_info = '0'
                print(f'Czas Spin {self.spin_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('spin1400', self.spin_frame, 0, 1, "red")
                self.time_label.configure(text=self.get_time_string())
                print("Reset Cyklu")
            if self.spin_calc == 0:
                self.spin_time_simulatior = 10
                self.spin_info = '0'
                print(f'Czas Spin {self.spin_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('spin0', self.spin_frame, 4, 1, "light green")
                self.time_label.configure(text=self.get_time_string())
            if self.spin_calc == 1:
                self.spin_time_simulatior = 15
                self.spin_info = '400'
                print(f'Czas Spin {self.spin_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('spin0', self.spin_frame, 4, 1, "red")
                self.led_creator('spin400', self.spin_frame, 3, 1, "light green")
                self.time_label.configure(text=self.get_time_string())
            if self.spin_calc == 2:
                self.spin_time_simulatior = 20
                self.spin_info = '800'
                print(f'Czas Spin {self.spin_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('spin400', self.spin_frame, 3, 1, "red")
                self.led_creator('spin800', self.spin_frame, 2, 1, "light green")
                self.time_label.configure(text=self.get_time_string())
            if self.spin_calc == 3:
                self.spin_time_simulatior = 25
                self.spin_info = '1200'
                print(f'Czas Spin {self.spin_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('spin800', self.spin_frame, 2, 1, "red")
                self.led_creator('spin1200', self.spin_frame, 1, 1, "light green")
                self.time_label.configure(text=self.get_time_string())
            if self.spin_calc == 4:
                self.spin_time_simulatior = 30
                self.spin_info = '1400'
                print(f'Czas Spin {self.spin_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('spin1200', self.spin_frame, 1, 1, "red")
                self.led_creator('spin1400', self.spin_frame, 0, 1, "light green")    
                self.time_label.configure(text=self.get_time_string())
                
    def option(self):
        if self.is_power_on and not self.is_running and not self.block_simulator:
            self.option_calc +=1
            print(f'LED Option {self.option_calc}')
            self.option_time_simulatior = 5
            print(f'Czas Option {self.option_time_simulatior}')
            self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
            print(f'Całościowy czas {self.all_time_simulation}')
            if self.option_calc == 5:
                self.option_calc = 0
                self.option_info = 'PS'
                self.led_creator('option5', self.option_frame, 0, 1, "red")
                self.option_time_simulatior = 5
                print(f'Czas Option {self.option_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.time_label.configure(text=self.get_time_string())
                print("Reset Cyklu")
            if self.option_calc == 0:
                self.option_info = 'PS'
                self.option_time_simulatior = 5
                print(f'Czas Option {self.option_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('option1', self.option_frame, 4, 1, "light green")
                self.time_label.configure(text=self.get_time_string())
            if self.option_calc == 1:
                self.option_time_simulatior = 10
                self.option_info = 'PW'
                print(f'Czas Option {self.option_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('option1', self.option_frame, 4, 1, "red")
                self.led_creator('option2', self.option_frame, 3, 1, "light green")
                self.time_label.configure(text=self.get_time_string())
            if self.option_calc == 2:
                self.option_time_simulatior = 15
                self.option_info = 'PTK'
                print(f'Czas Option {self.option_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('option2', self.option_frame, 3, 1, "red")
                self.led_creator('option3', self.option_frame, 2, 1, "light green")
                self.time_label.configure(text=self.get_time_string())
            if self.option_calc == 3:
                self.option_time_simulatior = 20
                self.option_info = 'PUMZ'
                print(f'Czas Option {self.option_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('option3', self.option_frame, 2, 1, "red")
                self.led_creator('option4', self.option_frame, 1, 1, "light green")
                self.time_label.configure(text=self.get_time_string())
            if self.option_calc == 4:
                self.option_time_simulatior = 25
                self.option_info = 'PR'
                print(f'Czas Option {self.option_time_simulatior}')
                self.all_time_simulation = self.option_time_simulatior + self.spin_time_simulatior + self.rinse_time_simulatior + self.temp_time_simulatior
                print(f'Całościowy czas {self.all_time_simulation}')
                self.led_creator('option4', self.option_frame, 1, 1, "red")
                self.led_creator('option5', self.option_frame, 0, 1, "light green")    
                self.time_label.configure(text=self.get_time_string())
                
                
    def get_time_string(self):
        minutes, seconds = divmod(self.all_time_simulation, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:d}:{minutes:02d}:{seconds:02d}"               
                
    def approve_ip(self):
        if self.entry_ip_address1.get() and self.entry_ip_address2.get() and self.entry_ip_address3.get() and self.entry_ip_address4.get() and self.entry_user_ip.get() and self.entry_password_ip.get():
            self.approve_adres_ip = self.entry_ip_address1.get() + '.' + self.entry_ip_address2.get() + '.' + self.entry_ip_address3.get() + '.' + self.entry_ip_address4.get()
            self.user_info = self.entry_user_ip.get()
            self.password_info = self.entry_password_ip.get()
            self.led_creator('ip_try_connection', self.connection_frame, 6, 1, "orange")
            print(f'Zatwierdzony adres IP: {self.approve_adres_ip}\nUser: {self.user_info}\nPassword: {self.password_info} ')    
            self.label_approve_ip.configure(text=f'Zatwierdzono: {self.approve_adres_ip}\nUser: {self.user_info}\nPassword: {self.password_info}')
        else:
            print("Niepoprawny adres IP")
            self.label_approve_ip.configure(text='Niepoprawne Dane')
            
    def try_connection_ip(self):
        print("Test")
        
        
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(hostname=f'{self.approve_adres_ip}', username=f'{self.user_info}', password=f'{self.password_info}')
                # Nawiązanie połączenia
            #client.connect('adres_IP', username='nazwa_użytkownika', password='hasło')

            # Wysłanie komendy
            stdin, stdout, stderr = self.client.exec_command("echo 'Test Wysyłki' >> /tmp/testwysyłki.txt")
            print("Komenda została wysłana.")
            self.led_creator('ip_try_connection', self.connection_frame, 6, 1, "light green")
            self.label_ip_try_connection.configure(text='Przesył danych możliwy')
            #self.client.close()
        except Exception as e:
            self.led_creator('ip_try_connection', self.connection_frame, 6, 1, "red")
            self.label_ip_try_connection.configure(text='Niemożliwe nawiązanie połaczenia')
            print("Nie można nawiązać połączenia: " + str(e))
            self.client.close()
            
    def disconnec_ip(self):
        print("Rozłączenie")
        stdin, stdout, stderr = self.client.exec_command("echo 'Rozłączenie Wysyłki' >> /tmp/testwysyłki.txt")
        self.led_creator('ip_try_connection', self.connection_frame, 6, 1, "red")
        self.label_ip_try_connection.configure(text='Rozłączono')
        self.client.close()
        

           
           
           
           

root = tk.Tk()
app = App(root)
root.mainloop()

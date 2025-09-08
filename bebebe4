import customtkinter
import tkinter
import tkinter.messagebox
import os
import datetime

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Калькулятор прибутку v4.4 (оновлений прогноз)")
        self.geometry("870x980") 

        self.initial_empty_bottle_prices = {
            "10 мл": 11.10,
            "5 мл": 3.60,
            "3 мл": 6.20
        }
        self.bottle_types_ordered = ["10 мл", "5 мл", "3 мл"]

        # --- Tkinter Змінні ---
        self.var_total_cost_liquid_purchase = tkinter.StringVar()
        self.var_total_volume_liquid_purchase = tkinter.StringVar()
        self.var_cost_per_ml_liquid = tkinter.StringVar(value="0.00 грн/мл")
        self.calculator_display_var = tkinter.StringVar()
        self.calculator_expression = ""
        
        self.vars_bottle_quantities = {
            vol: tkinter.StringVar(value="0") for vol in self.bottle_types_ordered
        }
        self.vars_empty_bottle_prices = {
            vol: tkinter.StringVar(value=f"{self.initial_empty_bottle_prices[vol]:.2f}") for vol in self.bottle_types_ordered
        }
        
        self.var_has_specific_leftovers = tkinter.BooleanVar(value=False)
        self.var_specific_leftover_ml = tkinter.StringVar(value="0")

        # --- Трейси ---
        self.var_total_cost_liquid_purchase.trace_add("write", self.update_cost_per_ml_display)
        self.var_total_volume_liquid_purchase.trace_add("write", self.update_cost_per_ml_display)

        # --- Головний фрейм ---
        main_frame = customtkinter.CTkFrame(self)
        main_frame.pack(pady=15, padx=15, fill="both", expand=True)

        # === Блок 1: Закупівля Рідкого Парфуму (Стиль: лейбл над полем) ===
        frame_liquid_purchase = customtkinter.CTkFrame(main_frame)
        frame_liquid_purchase.pack(pady=10, padx=10, fill="x")
        
        label_title1 = customtkinter.CTkLabel(frame_liquid_purchase, text="1. Закупівля Рідкого Парфуму", font=customtkinter.CTkFont(size=16, weight="bold"))
        label_title1.pack(pady=(10, 15))

        customtkinter.CTkLabel(frame_liquid_purchase, text="Загальна вартість закупівлі всієї рідини (грн):", anchor="w").pack(fill="x", padx=20, pady=(0,2))
        customtkinter.CTkEntry(frame_liquid_purchase, placeholder_text="наприклад, 990", textvariable=self.var_total_cost_liquid_purchase).pack(fill="x", padx=20, pady=(0,10))
        
        customtkinter.CTkLabel(frame_liquid_purchase, text="Загальний об'єм закупленої рідини (мл):", anchor="w").pack(fill="x", padx=20, pady=(0,2))
        customtkinter.CTkEntry(frame_liquid_purchase, placeholder_text="наприклад, 100", textvariable=self.var_total_volume_liquid_purchase).pack(fill="x", padx=20, pady=(0,10))
        
        frame_lp_cost_per_ml = customtkinter.CTkFrame(frame_liquid_purchase, fg_color="transparent")
        frame_lp_cost_per_ml.pack(fill="x", padx=20, pady=(5,10))
        customtkinter.CTkLabel(frame_lp_cost_per_ml, text="Розрахункова собівартість 1 мл рідини:", anchor="w").pack(side="left")
        customtkinter.CTkLabel(frame_lp_cost_per_ml, textvariable=self.var_cost_per_ml_liquid, font=customtkinter.CTkFont(size=18, weight="bold"), text_color=("#3B8ED0", "#36719F"), anchor="e").pack(side="right", fill="x", expand=True)

        # --- Контейнер для блоку 2 та калькулятора ---
        frame_middle_section = customtkinter.CTkFrame(main_frame, fg_color="transparent")
        frame_middle_section.pack(pady=10, padx=0, fill="x", expand=True)

        # === Блок 2: Формування Партії для Продажу (ліворуч) ===
        frame_batch_formation = customtkinter.CTkFrame(frame_middle_section)
        frame_batch_formation.pack(side="left", pady=0, padx=(10,5), fill="both", expand=True)
        
        label_title2 = customtkinter.CTkLabel(frame_batch_formation, text="2. Формування Партії для Продажу", font=customtkinter.CTkFont(size=16, weight="bold"))
        label_title2.pack(pady=(10,15))

        customtkinter.CTkLabel(frame_batch_formation, text="Бажана ціна продажу за 1 мл рідини (грн):", anchor="w").pack(fill="x", padx=20, pady=(0,2))
        self.entry_sell_price_per_ml = customtkinter.CTkEntry(frame_batch_formation, placeholder_text="17.00")
        self.entry_sell_price_per_ml.pack(fill="x", padx=20, pady=(0,15))

        customtkinter.CTkLabel(frame_batch_formation, text="Склад поточної партії:", font=customtkinter.CTkFont(size=14), anchor="w").pack(fill="x", padx=20, pady=(0,5))
        
        bottles_details_container = customtkinter.CTkFrame(frame_batch_formation, fg_color="transparent")
        bottles_details_container.pack(fill="x", padx=15)

        for bottle_type in self.bottle_types_ordered:
            frame_bottle_entry_row = customtkinter.CTkFrame(bottles_details_container, fg_color="transparent")
            frame_bottle_entry_row.pack(fill="x", pady=3)
            
            left_part_frame = customtkinter.CTkFrame(frame_bottle_entry_row, fg_color="transparent")
            left_part_frame.pack(side="left", expand=True, fill="x")
            customtkinter.CTkLabel(left_part_frame, text=f"{bottle_type}:", width=60, anchor="w").pack(side="left")
            customtkinter.CTkLabel(left_part_frame, text="К-ть:", width=40, anchor="w").pack(side="left", padx=(5,0))
            customtkinter.CTkEntry(left_part_frame, textvariable=self.vars_bottle_quantities[bottle_type], width=55).pack(side="left", padx=(2,5))
            
            right_part_frame = customtkinter.CTkFrame(frame_bottle_entry_row, fg_color="transparent")
            right_part_frame.pack(side="right")
            customtkinter.CTkEntry(right_part_frame, textvariable=self.vars_empty_bottle_prices[bottle_type], width=65, justify="right").pack(side="left", padx=(2,0))
            customtkinter.CTkLabel(right_part_frame, text=":Ціна", width=50, anchor="w").pack(side="left", padx=(2,0))
        
        customtkinter.CTkLabel(frame_batch_formation, text="Додаткові загальні витрати на цю партію (грн):", anchor="w").pack(fill="x", padx=20, pady=(15,2))
        self.entry_additional_batch_expenses = customtkinter.CTkEntry(frame_batch_formation, placeholder_text="50.00")
        self.entry_additional_batch_expenses.pack(fill="x", padx=20, pady=(0,10))
        
        self.frame_specific_leftovers_container = customtkinter.CTkFrame(frame_batch_formation, fg_color="transparent")
        self.frame_specific_leftovers_container.pack(pady=(5,10), padx=20, fill="x", anchor="w")

        self.checkbox_specific_leftovers = customtkinter.CTkCheckBox(
            self.frame_specific_leftovers_container, 
            text="Врахувати вартість додаткових нереалізованих\nзалишків/втрат рідини ?",
            variable=self.var_has_specific_leftovers,
            font=customtkinter.CTkFont(size=12),
            command=self.toggle_specific_leftovers_amount_field_visibility
        )
        self.checkbox_specific_leftovers.pack(pady=(0,5), anchor="w")

        self.frame_specific_leftovers_amount_entry = customtkinter.CTkFrame(self.frame_specific_leftovers_container, fg_color="transparent")
        self.label_specific_leftover_ml = customtkinter.CTkLabel(self.frame_specific_leftovers_amount_entry, text="Об'єм залишків/втрат (мл):", anchor="w")
        self.entry_specific_leftover_ml = customtkinter.CTkEntry(self.frame_specific_leftovers_amount_entry, textvariable=self.var_specific_leftover_ml, placeholder_text="напр., 23", width=120)
        self.toggle_specific_leftovers_amount_field_visibility()
        
        self.potential_income_button = customtkinter.CTkButton(
            frame_batch_formation, 
            text="Прогноз прибутку від рідини", # Змінив назву кнопки
            command=self.show_potential_max_profit_from_liquid, # Нова функція
            font=customtkinter.CTkFont(size=13)
        )
        self.potential_income_button.pack(pady=(10,0), padx=20, fill="x")

        # === Вбудований калькулятор (праворуч) ===
        frame_calculator = customtkinter.CTkFrame(frame_middle_section)
        frame_calculator.pack(side="right", pady=0, padx=(5,10), fill="y", expand=False) 
        
        label_calculator_title = customtkinter.CTkLabel(frame_calculator, text="Калькулятор", font=customtkinter.CTkFont(size=16, weight="bold"))
        label_calculator_title.pack(pady=(10,5), padx=5)
        entry_calculator_display = customtkinter.CTkEntry(frame_calculator, textvariable=self.calculator_display_var, font=customtkinter.CTkFont(size=16), justify="right", state="readonly", height=35) 
        entry_calculator_display.pack(pady=5, padx=5, fill="x")
        buttons_frame = customtkinter.CTkFrame(frame_calculator, fg_color="transparent")
        buttons_frame.pack(pady=5, padx=5, fill="both", expand=True) 
        button_specs = [ 
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('C', 3, 2), ('+', 3, 3),
            ('=', 4, 0, 4) 
        ]
        for i in range(4): buttons_frame.columnconfigure(i, weight=1, minsize=45) 
        for i in range(5): buttons_frame.rowconfigure(i, weight=1, minsize=35) 
        for (text, row, col, *span) in button_specs:
            colspan = span[0] if span else 1
            button = customtkinter.CTkButton(buttons_frame, text=text, font=customtkinter.CTkFont(size=14), command=lambda t=text: self.on_calculator_button_press(t), corner_radius=5)
            button.grid(row=row, column=col, columnspan=colspan, padx=2, pady=2, sticky="nsew")

        # === Блок 3: Розрахунок та результат ===
        self.calculate_button = customtkinter.CTkButton(main_frame, text="Розрахувати Прибуток Партії", command=self.calculate_profit_for_batch, font=customtkinter.CTkFont(size=16, weight="bold"), height=40)
        self.calculate_button.pack(pady=(20, 5), padx=10, fill="x")
        
        self.final_result_label = customtkinter.CTkLabel(main_frame, text="", font=customtkinter.CTkFont(size=26, weight="bold"))
        self.final_result_label.pack(pady=(5,10), padx=10)
        
        self.result_textbox = customtkinter.CTkTextbox(main_frame, height=280, font=customtkinter.CTkFont(size=13))
        self.result_textbox.pack(pady=(0,5), padx=10, fill="both", expand=True)
        self.result_textbox.configure(state="disabled")

    def toggle_specific_leftovers_amount_field_visibility(self, *args):
        if self.var_has_specific_leftovers.get():
            self.frame_specific_leftovers_amount_entry.pack(fill="x", pady=(0,5), padx=0, after=self.checkbox_specific_leftovers)
            self.label_specific_leftover_ml.pack(side="left", padx=(20,5)) 
            self.entry_specific_leftover_ml.pack(side="left", fill="x", expand=True)
        else:
            self.frame_specific_leftovers_amount_entry.pack_forget()
            self.var_specific_leftover_ml.set("0")

    def get_float(self, value_str, default_if_empty=0.0):
        if not value_str: return default_if_empty
        try:
            return float(value_str.replace(',', '.'))
        except ValueError:
            return default_if_empty 
        
    def update_cost_per_ml_display(self, *args):
        try:
            total_cost = self.get_float(self.var_total_cost_liquid_purchase.get())
            total_volume = self.get_float(self.var_total_volume_liquid_purchase.get())
            if total_volume > 0:
                cost_per_ml = total_cost / total_volume
                self.var_cost_per_ml_liquid.set(f"{cost_per_ml:.2f} грн/мл")
            else:
                self.var_cost_per_ml_liquid.set("0.00 грн/мл")
        except (ValueError, TypeError, ZeroDivisionError):
            self.var_cost_per_ml_liquid.set("Помилка вводу")

    def on_calculator_button_press(self, char):
        if char == 'C':
            self.calculator_expression = ""
            self.calculator_display_var.set("")
        elif char == '=':
            try:
                safe_expression = "".join(c for c in self.calculator_expression if c in "0123456789.+-*/()")
                if not safe_expression:
                    self.calculator_display_var.set("Помилка")
                    return
                result = eval(safe_expression)
                self.calculator_display_var.set(str(round(result, 4))) 
                self.calculator_expression = str(result) 
            except Exception:
                self.calculator_display_var.set("Помилка")
                self.calculator_expression = ""
        else:
            if self.calculator_display_var.get() == "Помилка": 
                self.calculator_expression = ""
            self.calculator_expression += str(char)
            self.calculator_display_var.set(self.calculator_expression)
    
    def show_potential_max_profit_from_liquid(self): # Перейменовано функцію
        try:
            total_volume_purchased = self.get_float(self.var_total_volume_liquid_purchase.get())
            total_cost_liquid_purchase_val = self.get_float(self.var_total_cost_liquid_purchase.get()) # Отримуємо вартість закупівлі
            
            sell_price_per_ml = self.get_float(self.entry_sell_price_per_ml.get())
            additional_expenses = self.get_float(self.entry_additional_batch_expenses.get())

            if total_volume_purchased <= 0:
                tkinter.messagebox.showerror("Помилка даних", "Будь ласка, введіть коректний загальний об'єм закупленої рідини (Блок 1).")
                return
            if sell_price_per_ml <= 0:
                tkinter.messagebox.showerror("Помилка даних", "Будь ласка, введіть коректну бажану ціну продажу за 1 мл (Блок 2).")
                return
            
            potential_gross_revenue = total_volume_purchased * sell_price_per_ml
            # Новий розрахунок: Валовий дохід - Вартість закупівлі рідини - Додаткові витрати
            potential_max_profit = potential_gross_revenue - total_cost_liquid_purchase_val - additional_expenses

            message_title = "Прогноз максимального прибутку від рідини"
            message_text = (
                f"Розрахунок потенційного максимального прибутку від усієї закупленої рідини:\n\n"
                f"Загальний об'єм закупленої рідини: {total_volume_purchased:.2f} мл\n"
                f"Бажана ціна продажу за 1 мл: {sell_price_per_ml:.2f} грн\n"
                f"Потенційний валовий дохід від рідини: {potential_gross_revenue:.2f} грн\n\n"
                f"Мінус вартість закупівлі всієї рідини: {total_cost_liquid_purchase_val:.2f} грн\n"
                f"Мінус додаткові загальні витрати: {additional_expenses:.2f} грн\n"
                f"--------------------------------------------------\n"
                f"ПРОГНОЗОВАНИЙ ЧИСТИЙ ПРИБУТОК: {potential_max_profit:.2f} грн\n\n"
                f"Цей розрахунок враховує собівартість закупленої рідини та додаткові витрати, але не враховує вартість порожніх флаконів."
            )
            tkinter.messagebox.showinfo(message_title, message_text)

        except ValueError: # Це вже обробляється get_float, але для загальної безпеки
            tkinter.messagebox.showerror("Помилка даних", "Будь ласка, перевірте коректність введених числових даних для прогнозу.")
        except Exception as e:
            tkinter.messagebox.showerror("Невідома помилка", f"Сталася помилка при розрахунку прогнозу: {e}")


    def calculate_profit_for_batch(self):
        self.result_textbox.configure(state="normal")
        self.result_textbox.delete("1.0", "end")
        self.final_result_label.configure(text="") 

        try:
            cost_per_ml_liquid_str_parts = self.var_cost_per_ml_liquid.get().split()
            if not cost_per_ml_liquid_str_parts or cost_per_ml_liquid_str_parts[0] == "Помилка":
                 raise ValueError("Собівартість рідини не розрахована. Перевірте дані у Блоці 1.")
            calculated_cost_per_ml_liquid = self.get_float(cost_per_ml_liquid_str_parts[0])
            if calculated_cost_per_ml_liquid < 0: 
                raise ValueError("Собівартість рідини (Блок 1) не може бути від'ємною.")
            
            total_liquid_purchase_cost = self.get_float(self.var_total_cost_liquid_purchase.get())
            total_liquid_purchase_volume = self.get_float(self.var_total_volume_liquid_purchase.get())
            if total_liquid_purchase_volume <=0 and calculated_cost_per_ml_liquid > 0:
                 pass 
            elif total_liquid_purchase_volume <=0 and total_liquid_purchase_cost > 0 : 
                 raise ValueError("Загальний об'єм закупленої рідини (Блок 1) має бути > 0, якщо вказана вартість закупівлі.")

            desired_sell_price_per_ml = self.get_float(self.entry_sell_price_per_ml.get())
            if desired_sell_price_per_ml <= 0:
                raise ValueError("Вкажіть бажану ціну продажу за 1 мл (більше нуля).")

            total_liquid_in_batch_ml = 0
            total_empty_bottles_cost_in_batch = 0
            total_revenue_from_batch = 0
            batch_composition_details = []
            any_bottles_in_batch = False

            for bottle_type in self.bottle_types_ordered:
                quantity = int(self.get_float(self.vars_bottle_quantities[bottle_type].get()))
                empty_bottle_price = self.get_float(self.vars_empty_bottle_prices[bottle_type].get())

                if quantity < 0: raise ValueError(f"Кількість флаконів {bottle_type} не може бути від'ємною.")
                if empty_bottle_price < 0: raise ValueError(f"Ціна порожнього флакону {bottle_type} не може бути від'ємною.")
                
                if quantity > 0: any_bottles_in_batch = True
                
                bottle_volume_ml = int(bottle_type.split()[0])
                total_liquid_in_batch_ml += quantity * bottle_volume_ml
                total_empty_bottles_cost_in_batch += quantity * empty_bottle_price
                total_revenue_from_batch += quantity * bottle_volume_ml * desired_sell_price_per_ml
                if quantity > 0:
                    batch_composition_details.append(f"   • {bottle_type}: {quantity} шт. (ціна пор. {empty_bottle_price:.2f} грн/шт)")

            if not any_bottles_in_batch: 
                if not (self.var_has_specific_leftovers.get() and self.get_float(self.var_specific_leftover_ml.get()) > 0):
                    raise ValueError("Не вказано жодного флакону для поточної партії або об'єму для списання.")

            additional_batch_expenses = self.get_float(self.entry_additional_batch_expenses.get())
            if additional_batch_expenses < 0:
                raise ValueError("Додаткові витрати на партію не можуть бути від'ємними.")

            cost_of_liquid_for_this_batch = total_liquid_in_batch_ml * calculated_cost_per_ml_liquid
            if total_liquid_in_batch_ml > total_liquid_purchase_volume and total_liquid_purchase_volume > 0:
                 self.result_textbox.insert("end", f"⚠️ Увага: Об'єм рідини в партії ({total_liquid_in_batch_ml} мл) перевищує закуплений об'єм ({total_liquid_purchase_volume} мл).\nСобівартість рідини розрахована на основі ціни за мл, але фактично у вас не вистачає закупленої рідини.\n\n")
            
            cost_of_specific_leftovers = 0
            specific_leftover_ml_for_report = 0
            if self.var_has_specific_leftovers.get():
                specific_leftover_ml = self.get_float(self.var_specific_leftover_ml.get())
                specific_leftover_ml_for_report = specific_leftover_ml
                if specific_leftover_ml < 0:
                    raise ValueError("Об'єм додаткових залишків/втрат не може бути від'ємним.")
                if specific_leftover_ml > 0 and calculated_cost_per_ml_liquid == 0 and total_liquid_purchase_cost > 0 and total_liquid_purchase_volume == 0 :
                     raise ValueError("Неможливо розрахувати вартість залишків: об'єм закупівлі (Блок 1) = 0, але вказана вартість закупівлі. Вкажіть об'єм закупівлі.")
                elif specific_leftover_ml > 0 and calculated_cost_per_ml_liquid == 0 and total_liquid_purchase_cost == 0:
                     cost_of_specific_leftovers = 0
                else:
                     cost_of_specific_leftovers = specific_leftover_ml * calculated_cost_per_ml_liquid
                
            total_expenses_for_batch = cost_of_liquid_for_this_batch + cost_of_specific_leftovers + total_empty_bottles_cost_in_batch + additional_batch_expenses
            net_profit_for_batch = total_revenue_from_batch - total_expenses_for_batch
            
            potential_revenue_from_all_liquid = 0
            if total_liquid_purchase_volume > 0 :
                potential_revenue_from_all_liquid = total_liquid_purchase_volume * desired_sell_price_per_ml

            profit_text_label = f"Чистий прибуток: {net_profit_for_batch:.2f} грн"
            loss_text_label = f"Чистий збиток: {abs(net_profit_for_batch):.2f} грн"
            neutral_text_label = "Результат партії: 0.00 грн"
            profit_color, loss_color, neutral_color = "green", "red", customtkinter.ThemeManager.theme["CTkLabel"]["text_color"]

            if net_profit_for_batch > 0: self.final_result_label.configure(text=profit_text_label, text_color=profit_color)
            elif net_profit_for_batch < 0: self.final_result_label.configure(text=loss_text_label, text_color=loss_color)
            else: self.final_result_label.configure(text=neutral_text_label, text_color=neutral_color)

            report = ["📊 ФІНАНСОВИЙ АНАЛІЗ ПОТОЧНОЇ ПАРТІЇ 📊", "--------------------------------------------", "Склад партії:"]
            if batch_composition_details: report.extend(batch_composition_details)
            elif not (self.var_has_specific_leftovers.get() and specific_leftover_ml_for_report > 0):
                 report.append("   (Не вказано жодного флакону для продажу)")

            report.append(f"Загальний об'єм рідини у флаконах партії: {total_liquid_in_batch_ml:.2f} мл")
            report.append(f"Собівартість 1 мл рідини (з Блоку 1): {calculated_cost_per_ml_liquid:.2f} грн/мл")
            report.append(f"Бажана ціна продажу 1 мл рідини: {desired_sell_price_per_ml:.2f} грн/мл")
            report.append("--------------------------------------------\n")
            report.append(f"💰 ЗАГАЛЬНИЙ ДОХІД від цієї партії: {total_revenue_from_batch:.2f} грн\n")
            report.append(f"📉 ЗАГАЛЬНІ ВИТРАТИ на цю партію: {total_expenses_for_batch:.2f} грн")
            report.append(f"   • Вартість рідини для флаконів ЦІЄЇ партії ({total_liquid_in_batch_ml:.2f} мл): {cost_of_liquid_for_this_batch:.2f} грн")
            if self.var_has_specific_leftovers.get() and specific_leftover_ml_for_report > 0: 
                report.append(f"   • Вартість списаних залишків/втрат ({specific_leftover_ml_for_report:.2f} мл): {cost_of_specific_leftovers:.2f} грн")
            report.append(f"   • Вартість порожніх флаконів для партії: {total_empty_bottles_cost_in_batch:.2f} грн")
            report.append(f"   • Додаткові витрати на партію: {additional_batch_expenses:.2f} грн\n")
            report.append("--------------------------------------------")
            report.append(f"🏆 РЕЗУЛЬТАТ ЦІЄЇ ПАРТІЇ: {net_profit_for_batch:.2f} грн")
            report.append("--------------------------------------------\n")
            if total_liquid_purchase_volume > 0:
                report.append(f"💡 Потенційний макс. дохід від ВСІЄЇ закупленої рідини ({total_liquid_purchase_volume:.2f} мл по {desired_sell_price_per_ml:.2f} грн/мл, без ін. витрат): {potential_revenue_from_all_liquid:.2f} грн")
            
            self.result_textbox.insert("1.0", "\n".join(report))

        except (ValueError, TypeError) as e:
            self.final_result_label.configure(text="Помилка в даних!", text_color="red")
            self.result_textbox.insert("1.0", f"⚠️ Помилка: {e}\n\nПеревірте введені дані.")
        except ZeroDivisionError: 
             self.final_result_label.configure(text="Помилка розрахунку!", text_color="red")
             self.result_textbox.insert("1.0", f"⚠️ Помилка: Ділення на нуль.")
        except Exception as e:
            self.final_result_label.configure(text="Непередбачена помилка!", text_color="red")
            self.result_textbox.insert("1.0", f"⚠️ Сталася непередбачена помилка: {e}")
        finally:
            self.result_textbox.configure(state="disabled")

if __name__ == "__main__":
    app = App()
    app.mainloop()


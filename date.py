from datetime import datetime

def start():
    print("Это калькулятор возраста.")
    print("Введите вашу дату рождения в формате ДД-ММ-ГГГГ:")
    
    birth_date = input()
    birth_date = datetime.strptime(birth_date, "%d-%m-%Y").date()
    today_date = datetime.today().date()
    age = today_date - birth_date
    age_years = age.days // 365
    age_months = (age.days % 365) // 30
    age_days = (age.days % 365) % 30
    
    print("Тебе", age_years, "лет", age_months, "месяцев", age_days, "дней")

start()

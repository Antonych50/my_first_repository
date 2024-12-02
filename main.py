import tkinter as tk
from tkinter import ttk

# Функция для извлечения данных из выделенной строки
def get_selected_item():
    selected_item = tree.selection()[0]
    # Получаем идентификатор выделенной строки
    values = tree.item(selected_item, "values")
    #Извлекаем данные строки
    print("Выделенная строка содержит:", values[2])

# Создаем главное окно
root = tk.Tk()
root.title("Пример использования ttk.Treeview")
# Функция для извлечения данных из выделенной строки
frm = tk.Frame()
tree = ttk.Treeview(root, columns=("Имя", "Возраст", "Профессия"), show="headings")
tree.grid(row=0, column=0, sticky='s')
tree.grid_configure()
# Определяем заголовки столбцов
tree.heading("Имя", text="Имя")
#tree.heading("Возраст", text="Возраст")
#tree.heading("Профессия", text="Профессия")

# Определяем ширину столбцов
tree.column("Имя", width=100)
tree.column("Возраст", width=50)
tree.column("Профессия", width=150)

# Добавляем данные в таблицу
data = [
    ("Алексей", 30, "Инженер"),
    ("Мария", 25, "Дизайнер"),
    ("Иван", 40, "Менеджер"),
    ("Анна", 35, "Маркетолог")
]
for item in data:
    tree.insert("", tk.END, values=item)
tree.insert("", 1, values=("Варвара", 2, "котёнок"))
# Добавляем скроллбар
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
tree.configure(yscrollcommand=scrollbar.set)

# Кнопка для вызова функции
button = tk.Button(root, text="Показать данные выделенной строки", command=get_selected_item)
button.grid(row=1, column=0, pady=10)
print(button.configure().keys(), '\n')
print(dir(button))
print(set(button.configure().keys()) - set(frm.configure().keys()))
# Запускаем основное событие
root.mainloop()


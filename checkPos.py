import pyautogui
import time

print("Переместите курсор на нужную клетку.")
time.sleep(5)  # У вас будет 5 секунд, чтобы переместить курсор

# Получение координат текущей позиции курсора
x, y = pyautogui.position()
print(f"Координаты клетки: x={x}, y={y}")

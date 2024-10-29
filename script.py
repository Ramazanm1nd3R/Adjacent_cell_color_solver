import pyautogui
import time
import cv2
import numpy as np
from PIL import ImageGrab

# Координаты клеток и кнопки "Reset"
cell_positions = [
    (778, 573), (823, 573), (864, 573), (914, 573),
    (956, 573), (1012, 573), (1061, 573), (1097, 573),
    (1139, 573), (1191, 573), (1238, 573), (1281, 573),
    (1331, 573), (1379, 573), (1420, 573), (1469, 573),
    (1519, 573), (1563, 573)
]
reset_position = (1171, 670)

# Функция для захвата цвета клетки по её координатам
def get_cell_color(x, y):
    screen = ImageGrab.grab(bbox=(x, y, x + 10, y + 10))
    screen_np = np.array(screen)
    color = cv2.cvtColor(screen_np, cv2.COLOR_BGR2RGB)
    
    avg_color = color.mean(axis=0).mean(axis=0)
    if avg_color[0] < 100 and avg_color[1] < 100 and avg_color[2] < 100:
        return "black"
    elif avg_color[0] > 200 and avg_color[1] > 200 and avg_color[2] > 200:
        return "white"
    else:
        return "gray"

# Функция для клика по клетке и получения её цвета
def click_and_get_color(index):
    x, y = cell_positions[index]
    pyautogui.click(x, y)
    time.sleep(0.5)  # Пауза для обновления экрана после щелчка
    color = get_cell_color(x, y)
    
    if color == "gray":
        print(f"Gray cell detected at {index}. Resetting and trying a new strategy...")
        pyautogui.click(reset_position)  # Нажимаем на "Reset"
        time.sleep(1)  # Пауза для обновления
        return "reset"
    
    return color

# Функция проверки смежных клеток для заданной стратегии
def check_adjacent_cells(check_indices, strategy_name):
    print(f"Trying {strategy_name}...")
    for idx in check_indices:
        color1 = click_and_get_color(idx)
        
        if color1 == "reset":
            return False  # Остановка текущей стратегии
        
        if idx < len(cell_positions) - 2:
            color2 = click_and_get_color(idx + 1)
            if color2 == "reset":
                return False
            
            print(f"Checking cells {idx} and {idx + 1}: Color1 = {color1}, Color2 = {color2}")
            
            if color1 != color2:
                print(f"Found different colors at cells {idx} and {idx + 1} using {strategy_name}")
                return True  # Успешное решение найдено

    print(f"{strategy_name} did not find a solution. Resetting...")
    return False

# Стратегии поиска
def central_check_strategy():
    check_indices = [8, 7, 9, 6, 10]
    return check_adjacent_cells(check_indices, "Central Check Strategy")

def mixed_check_strategy():
    check_indices = [1, 16, 4, 13, 7, 10]
    return check_adjacent_cells(check_indices, "Mixed Check Strategy")

def sequential_check_strategy():
    check_indices = list(range(1, len(cell_positions) - 1))
    return check_adjacent_cells(check_indices, "Sequential Check Strategy")

def outer_inner_check_strategy():
    check_indices = [1, 16, 2, 15, 3, 14, 4, 13]
    return check_adjacent_cells(check_indices, "Outer to Inner Check Strategy")

def random_check_strategy():
    check_indices = [3, 8, 12, 15, 4, 9, 13, 2, 14, 7]
    return check_adjacent_cells(check_indices, "Random Check Strategy")

def alternating_check_strategy():
    check_indices = [1, 3, 5, 7, 9, 11, 13, 15]
    return check_adjacent_cells(check_indices, "Alternating Check Strategy")

def reverse_sequential_check_strategy():
    check_indices = list(range(len(cell_positions) - 2, 0, -1))
    return check_adjacent_cells(check_indices, "Reverse Sequential Check Strategy")

def inner_outer_check_strategy():
    check_indices = [9, 8, 10, 7, 11, 6, 12, 5]
    return check_adjacent_cells(check_indices, "Inner to Outer Check Strategy")

def opposite_ends_check_strategy():
    check_indices = [1, 16, 2, 15, 3, 14, 4, 13]
    return check_adjacent_cells(check_indices, "Opposite Ends Check Strategy")

def corner_focus_check_strategy():
    check_indices = [1, 16, 2, 15, 4, 13]
    return check_adjacent_cells(check_indices, "Corner Focus Check Strategy")

def alternate_outer_inner_check_strategy():
    check_indices = [1, 16, 8, 9, 2, 15, 7, 10]
    return check_adjacent_cells(check_indices, "Alternate Outer to Inner Strategy")

def check_every_third_strategy():
    check_indices = [1, 4, 7, 10, 13, 16]
    return check_adjacent_cells(check_indices, "Check Every Third Strategy")

def zigzag_check_strategy():
    check_indices = [1, 16, 3, 14, 5, 12, 7, 10]
    return check_adjacent_cells(check_indices, "Zigzag Check Strategy")

def near_middle_check_strategy():
    check_indices = [7, 8, 9, 10, 11]
    return check_adjacent_cells(check_indices, "Near Middle Check Strategy")

def random_reverse_check_strategy():
    check_indices = [7, 14, 3, 10, 5, 12, 4, 15, 2, 16]
    return check_adjacent_cells(check_indices, "Random Reverse Check Strategy")

def alternating_inner_check_strategy():
    check_indices = [8, 10, 7, 9, 11]
    return check_adjacent_cells(check_indices, "Alternating Inner Check Strategy")

def expanding_outwards_check_strategy():
    check_indices = [9, 8, 10, 7, 11, 6, 12]
    return check_adjacent_cells(check_indices, "Expanding Outwards Check Strategy")

def adjacent_edge_check_strategy():
    check_indices = [1, 2, 15, 16]
    return check_adjacent_cells(check_indices, "Adjacent Edge Check Strategy")

def split_half_check_strategy():
    check_indices = [1, 9, 8, 16, 7]
    return check_adjacent_cells(check_indices, "Split Half Check Strategy")

def focus_on_outer_check_strategy():
    check_indices = [2, 15, 3, 14]
    return check_adjacent_cells(check_indices, "Focus on Outer Check Strategy")

# Основная функция для перебора стратегий
def find_adjacent_diff_color():
    strategies = [
        central_check_strategy,
        mixed_check_strategy,
        sequential_check_strategy,
        outer_inner_check_strategy,
        random_check_strategy,
        alternating_check_strategy,
        reverse_sequential_check_strategy,
        inner_outer_check_strategy,
        opposite_ends_check_strategy,
        corner_focus_check_strategy,
        alternate_outer_inner_check_strategy,
        check_every_third_strategy,
        zigzag_check_strategy,
        near_middle_check_strategy,
        random_reverse_check_strategy,
        alternating_inner_check_strategy,
        expanding_outwards_check_strategy,
        adjacent_edge_check_strategy,
        split_half_check_strategy,
        focus_on_outer_check_strategy
    ]
    
    for strategy in strategies:
        result = strategy()
        if result:
            return  # Решение найдено, завершаем
    
        # Если стратегия не нашла решение, нажимаем "Reset" и пробуем следующую
        pyautogui.click(reset_position)
        time.sleep(1)  # Пауза для перезагрузки интерфейса

    print("All strategies failed to find a solution.")

# Запуск основной функции
find_adjacent_diff_color()

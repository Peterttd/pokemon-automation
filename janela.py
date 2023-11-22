import pygetwindow as gw

# Lista todos os títulos de janelas abertas
windows = gw.getAllTitles()

# Imprime os nomes das janelas
for window in windows:
    print(window)
print('Ведіть ціле число')

signal_intensity = int(input())

if signal_intensity >= 95:
    signal_level = "Насичення фотоприймача"
elif signal_intensity >= 60:
    signal_level = "Сильний сигнал"
elif signal_intensity >= 20:
    signal_level = "Робочий діапазон"
else:
    signal_level = "Слабкий сигнал"

mode = "Потрібна увага" if signal_intensity < 20 or signal_intensity >= 95 else "Звичайний режим"

print(f"Рівень: {signal_level}")
print(f"Режим: {mode}")
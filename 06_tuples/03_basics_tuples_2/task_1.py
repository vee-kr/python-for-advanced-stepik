poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
new_data = list(poet_data)
new_data[-1] = "Москва"
poet_data = tuple(new_data)
print(poet_data)
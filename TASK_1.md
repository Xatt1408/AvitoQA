### *Задание 1.* ###

#### Изучить скриншот, найти имеющиеся баги на странице, задать приоритет  ####


|  №  | Описание | Ожидаемый результат | Фактический результат |  Приоритет |
|-------------|-------------|-------------|-----------------|-----------|
| 1   | Ошибка в лого сайта     | Avito   |  Awito  | high |
| 2   |  Лишняя марка телефона     | Только Samsung     | Дополнительно выдает Iphone  | medium |
| 3   |  Телефоны с разным объемом памяти     | Только 512гб    | Имееются телефоны с 256гб | low | 
| 4   |  Разные цвета телефонов | Выбран только 1 цвет | Показывает телефоны разных цветов | medium | 
| 5  |  Телефоны неправильной ценовой категории | Выдаст телефоны < 50000 | Показывает телефоны > 50000| medium |
| 6 | Неправильная сортировка | Сначала выдает смартфоны из Москвы| В фильтре по Москве встречаются смартфоны, регион которых не указан. | low |
| 7 | Опечатка в названии метро | Сокол 5 мин | Eсть возможность вписать то, чего не существует - "Соколдо" | medium |

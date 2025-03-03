# SLP_1S_2.2-2.5
## Описание и назначение проекта
Проект содержит в себе программу для вычисления факториала 
введённого числа, написанную для учебной (ознакомительной) практики.
Кейс-задачи 2.2 и 2.5 - кодовая база и документация, включая, но не 
ограничиваясь данным файлом, комментариями к коду, строками 
документации и аннотациями типов.

### Постановка задачи на кодовую базу
Напишите программу, которая запрашивает у пользователя ввод 
положительного целого числа:

- Реализуйте функцию, которая вычисляет факториал введенного числа.
- Выведите на экран результат вычисления факториала.
- Обеспечьте обработку возможных ошибок, таких как ввод пользователем нечисловых данных или отрицательного числа.
- Добавьте оптимизацию для работы с большими числами, используя библиотеку math для работы с факториалами.

### Постановка задачи на документацию
Проведите анализ и подробно опишите выполненную кейс-задачу, 
по следующим критериям:

- **Цель:** Создать программу, которая получает от пользователя положительное целое число и проверяет корректность ввода.
- **Основные функции:** Запрос ввода числа у пользователя. Проверка, что введенное значение является положительным целым числом. Вывод сообщения об ошибке в случае некорректного ввода. Повторный запрос ввода в случае ошибки.
- **Интерфейс:** Консольный ввод/вывод. Сообщение с просьбой ввести положительное целое число. Сообщение об ошибке, если введенное значение некорректно.
- **Алгоритм:** Запрашивать у пользователя ввод числа. Проверять, что введенное значение является положительным целым числом. Если введенное значение некорректно, выводить сообщение об ошибке и запрашивать ввод повторно. Если ввод корректен, завершать выполнение программы или использовать введенное значение в дальнейшем.
- **Валидация и обработка исключений:** Проверка, что введенное значение действительно является числом. Обработка исключений для случайного ввода нечисловых данных (например, строки, специальные символы). Проверка на допустимость числа (например, отрицательные значения или ноль).
- **Пользовательский опыт:** Понятные и информативные сообщения об ошибках. Возможность повторного ввода без завершения программы в случае ошибки.
- **Производительность:** Оптимизация обработки ввода для больших объемов данных или частых запросов.
- **Расширяемость:** Возможность добавления дополнительных проверок (например, диапазон чисел, минимальное и максимальное значения).
- **Документация и тестирование:** Документация по коду и описание логики работы программы. Написание тестов для проверки корректности работы программы с различными вводами (например, положительные целые числа, нули, отрицательные значения, текст).
- **Дополнительные требования:** Валидация ввода (например, проверка, что значение положительное и является целым числом). Обработка исключений (например, случай неверного формата ввода).
## Работа с программой
Данная программа поставляется "как есть", в виде проекта в репозитории.
Для запуска потребуется установленная IDE и интерпретатор Python версии
не ниже 3.11. Десктопной версии не предусмотрено по условиям задачи.
### Порядок работы
Интерфейс приложения консольный, после запуска пользователю будет 
вежливо, но настойчиво предложено ввести целое положительное число, 
факториал планируется вычислить. (Напоминаем, что n!, при n = 0, n = 1
будет равен 1). Введённое значение будет проверено на принадлежность
к целым положительным числам, т.е., на возможность приведения
к типу `int` после ввода. После запуска программы у пользователя 
есть пять попыток на корректный ввод значения, в противном случае
программа завершит работу. Если все проверки пройдены - программа
вычислит и выведет факториал **n!**, где n - число, введённое 
пользователем.

В случае, если пользователь просит вычислить факториал числа равного
или превосходящего 1000 - программа запросит подтверждение действия
и попросит ввести да или нет, перед продолжением работы. Если
пользователь откажется - программа прекратит работу и отдаст в 
консоль соответствующий статус. Этот предохранитель реализован для
случаев когда программа запускается на слабых машинах и может 
повредить аппаратную составляющую ЭВМ.
## Архитектура
Проект структурирован таким образом, чтобы можно было переиспользовать
интерфейсы ввода/вывода с последующим расширением функциональной 
составляющей. Для этого файл запуска выделен в корне проекта, а 
приложения любых типов, ввиду небольшого размера проекта - выделены
в директорию `/applications` и разбиты на модули. На данный момент
таких модулей с приложениями всего три.
### Описание компонентов
>`user_interface.py`
>>Cодержит в себе функции ввода/вывода значений, форматирования 
> сообщений и всего, что пользователь видит на экране.

>`factorial.py`
>>Непосредственно калькулятор факториала числа, основанный на `math`
> Также содержит в себе проверку на величину введённого значения и 
> вызов дисклеймера сложного вычисления

>`checkers.py`
>>Содержит в себе любые проверки любого рода с достаточной для выноса
> в отдельный момент сложностью логики. 

Данная структура может быть и не оправдана объёмом проекта, однако 
никто не застрахован от его расширения в будущем. Раз уж структура
существует - давайте её придерживаться до следующего рефакторинга. 

`!` Примечание: Весь проект построен на стандартных библиотеках и 
встроенных методах. При смене этой парадигмы, коль скоро она будет
изменена - потребуется собрать `requirements.txt`, который не 
реализован в репозитории сейчас. Будьте внимательны.

## Тестирование
В данном пункте привожу ручные сценарии и чек-листы, автоматическое
модульное тестирование - не реализовано, ввиду небольшого объема кодовой базы.

### Тестирование счастливого пути
1. Запустить программу 
2. Проверить корректность приветственного сообщения 
3. Ввести целое положительное число:`7`
4. Проверить сообщение об окончании вычислений 
5. Проверить, что на экран выведено значение факториала
### Тестирование критического пути
1. Запустить программу 
2. Проверить корректность приветственного сообщения 
3. Ввести целое отрицательное число:`-2`
4. Проверить, что программа вернулась ко вводу 
5. Проверить сообщение об ошибке 
6. Ввести строку:`duck`
7. Повторить шаги `4-5`
8. Ввести целое положительное число больше `1000`
9. Проверить сообщение о сложности вычислений
10. Ввести значение отличающееся от инструкции: `lf`
11. Проверить сообщение о нераспознанной команде
12. Подтвердить выполнение, введя `да`
13. Проверить сообщение об окончании вычислений
14. Проверить, что на экран выведено значение факториала
### Исключения и прерывания
#### Проверка пользовательского ввода
1. Запустить программу 
2. Проверить корректность приветственного сообщения 
3. Ввести целое отрицательное число:-2 
4. Проверить, что программа вернулась ко вводу 
5. Проверить сообщение об ошибке 
6. Ввести строку:duck
7. Повторить шаги 4-5
8. Выполнить ещё 3 ввода некорректных значений:
9. `-9, moose, пустой ввод
10. Проверить что программа завершила работу с ошибкой`

#### Дисклеймер сложных вычислений
1. Запустить программу 
2. Проверить корректность приветственного сообщения 
3. Ввести целое положительное число больше `1000`
4. Проверить сообщение о сложности вычислений
5. Запросить отказ выполнения, введя `нет`
6. Проверить что программа завершила работу с ошибкой`








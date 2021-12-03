# Clock and calendar Add-on for NVDA (Додаток годинника й календаря для NVDA) #

* Автори: Hrvoje Katić, Abdel and NVDA contributors
* Завантажити [стабільну версію][1]
* Завантажити [версію в розробці][2]
* Сумісність з NVDA: 2019.3 і пізніші

Цей додаток надає розширені функції годинника, будильника та календаря для
NVDA.

Ви можете налаштувати NVDA для озвучування часу й дати у форматах, відмінних
від тих, які початково надає Windows. Крім того, можна дізнатися поточний
день, номер тижня і кількість днів, що залишилися до кінця поточного року, а
також налаштувати автоматичне сповіщення часу на заданий інтервал. У додатку
також є вбудовані функції секундоміра, таймера і будильника, які дозволяють
розраховувати час виконання завдань, таких як копіювання файлів,
встановлення програм або приготування їжі.

Примітки:

* коли ви оновлюєте додаток, під час процесу встановлення майстер визначає,
  чи стара конфігурація сумісна з новою, і пропонує виправити її перед
  встановленням, тоді вам просто потрібно  натиснути кнопку «Гаразд» для
  підтвердження.
* У Windows 10 і новіших версіях можна використовувати програму «Будильники
  та годинники», щоб керувати секундоміром і таймером.

## Основні команди

* NVDA+F12: повідомляє поточний час
* NVDA+F12 натисніть двічі швидко: промовляє поточну дату
* NVDA+F12 натисніть тричі швидко: промовляє поточний день, номер тижня, рік
  і дні, що залишилися до кінця року
* NVDA+Shift+F12: ввести багаторівневу команду годинника

## Непризначені команди

Ці команди початково не призначені; якщо ви хочете їх призначити,
скористайтеся діалогом «Жести вводу», щоб додати власні команди. Для цього
відкрийте меню NVDA, Параметри, потім Жести вводу. Відкрийте категорію
«Годинник», потім знайдіть непризначені команди у списку нижче та виберіть
«Додати», а потім введіть жест, який ви хочете використовувати.

* Повідомити Час, що минув і залишився до наступного будильника. Подвійне
  швидке натискання цього жесту скасує будильник.
* Зупинити відтворення сигналу будильника.
* Відкрити діалог нагадування розкладу.

## Багаторівневі команди

Щоб використовувати багаторівневі команди, натисніть NVDA+Shift+F12, потім
одну з нижченаведених клавіш:

* S: запускає, скидає або зупиняє секундомір
* R: Скидає секундомір на 0 без перезапуску
* A: показує час, що минув і залишився до наступного сигналу будильника
* T: відкриває діалог розкладу будильника.
* C: скасовує наступний будильник
* Пробіл: промовляє поточний секундомір або зворотний відлік таймера
* p: якщо сигнал будильника надто довгий, дозволяє його зупинити
* H: список усіх багаторівневих команд (довідка)

## Налаштування й використання

Щоб налаштувати функції годинника, відкрийте меню NVDA, Параметри, потім
Налаштування та налаштуйте такі параметри в категорії Годинника:

* Формат відображення часу та дати: використовуйте ці поля зі списком, щоб
  налаштувати, як NVDA оголошуватиме час і дату, коли ви швидко натискаєте
  NVDA+F12 один раз або двічі відповідно.
* Інтервал: виберіть інтервал озвучування часу з цього списку (вимкнено,
  кожні 10 хвилин, 15 хвилин, 30 хвилин або щогодини).
* Промовляння часу (якщо інтервал не вимкнено): виберіть між голосом і
  звуком, лише звуком або лише голосом.
* Звук сигналу годинника (якщо інтервал не вимкнено): виберіть звук сигналу
  годинника.
* Тихі години (якщо інтервал не вимкнено): установіть цей прапорець, щоб
  налаштувати діапазон тихих годин, коли автоматичне сповіщення часу не
  відбуватиметься.
* Формат часу тихих годин (якщо ввімкнено режим тихих годин): виберіть, як
  відображатимуться параметри тихого часу (12-годинний або 24-годинний
  формат).
* Час початку та закінчення тихого режиму: виберіть діапазон годин і хвилин
  для тихого режиму з комбінованого списку годин і хвилин.

Щоб запланувати будильник, відкрийте меню NVDA, Інструменти, потім виберіть
Запланувати будильник. Зміст діалогу включає:

* Тривалість будильника в: виберіть тривалість будильника/таймера в годинах,
  хвилинах та секундах.
* Тривалість: введіть тривалість будильника у вказаних вище одиницях.
* Звук будильника: виберіть звук будильника, який повинен відтворюватись.
* Кнопки зупинки та паузи: зупинка або пауза тривалого звукового сигналу.

Натисніть «Гаразд» і почуєте вибрану тривалість будильника.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=cac

[2]: https://addons.nvda-project.org/files/get.php?file=cac-dev
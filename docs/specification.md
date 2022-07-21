# Техническое задание

# 1 Цель проекта
Разработать программу для просмотра фото, которые находятся на компьютере локально. При этом нужно иметь возможность отмечать предметы на фото. Отметки хранятся внутри файла изображения. Это нужно для групповых фото и для фото, где важно отметить части изображения. Программа может проанализировать отметки внутри папки и показать их в инспекторе тегов.

# 2 Описание
В программе есть следующие панели:
- Левая панель:
	- Файловый браузер (Файлы)
	- Инспектор тегов (Теги)
- Центральная панель (панель просмотра и панель инструментов по работе с фото)
- Правая панель
	- Инспектор свойств изображения (Свойства изображения)
	- Инспектор тегов изображения (Теги изображения)
- Нижняя панель 

### 2.1 Функционал
#### Просмотр фото
Если открыть программу в папке, то в файловом браузере отобразятся миниатюры фотографий в папке, а также другие папки.
Также можно вызвать программу применительно к конкретному файлу. В этом случае файл отобразится в окне просмотра, а в файловом браузере появится папка, в которой этот файл лежит.
Открытый файл подсвечен в файловом браузере.
Фото на панели просмотра отображается на белом фоне.
При помощи панели инструментов можно повернуть изображение (что сохранится в свойствах фото), перейти к следующей и предыдущей картинке.
В режиме работы с тегам подсвечиваются имеющиеся на изображении теги.
В инспекторе свойств изображения прописаны EXIF свойства изображения:
- дата фото
- имя фото
- локация
- текущие теги

В инспекторе тегов изображения показаны теги текущего изображения.

В инспекторе тегов отображаются теги директории.

Каждая кнопка продублирована горячей клавишей.

#### Отметка участков изображений
В режиме работы с тегами можно обвести прямоугольником участок изображения и присвоить ему тег. При наборе имени тега предлагаются теги, которые имеются в текущей директории.
После ввода имени тега, он сразу сохранятся в файл.
В инспекторе свойств и в инспекторе тегов можно переименовать тег двойным щелчком мыши.

#### Работа с тегами
В инспекторе тегов можно пометить тег как фильтр для файлового менеджера.

## 2.2 Дизайн
Нравится светлый notion-like стиль. Использование emoji.
Логотип:😶‍🌫️ 
Название: Peeker

## 2.3 Стек
Прототип на https://streamlit.io/
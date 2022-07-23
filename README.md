# 😶‍🌫️ Peeker
Программа для просмотра фото, и выделения предметов. Отметки хранятся внутри файла изображения в метаданных.

Программа читает и прописывает теги в EXIF-поле `image_description`. Так его сразу видно и в других программах.
В этом случае значение поля будет следующим:

```json
{
    "description": "Tags for Peeker software. Contact `rahmaevao@gmail.com` for details",
    "version": "0.1.0",
    "tags": {
        "name": "Some tag name",
        "id": "Some tag id",
        "x": 0.1,
        "y": 0.4,
        "w": 0.05,
        "h": 0.05
    }
}
```
## Как запустить?

```bash
python peeker.py <path_to_file>
```
def get_cats_info(path):
    cats = []

    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                cat_id, name, age = line.strip().split(",")

                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": age
                }

                cats.append(cat_info)

        return cats

    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []


cats_info = get_cats_info("cats_file.txt")

for cat in cats_info:
    print(f"ID: {cat['id']}, Name: {cat['name']}, Age: {cat['age']}")
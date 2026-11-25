import sqlite3

conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

print("=" * 60)
print("6. ВСЕ ЗАПИСИ ИЗ БАЗЫ ДАННЫХ (SELECT * FROM sales):")
print("=" * 60)
cursor.execute("SELECT * FROM sales")
for row in cursor.fetchall():
    print(row)

print("\n" + "=" * 60)
print("7. САМОСТОЯТЕЛЬНЫЕ ЗАДАНИЯ:")
print("=" * 60)

print("\n--- Задание 3: Товары дороже 20 000 тенге ---")
cursor.execute("SELECT product, category, price FROM sales WHERE price > 20000")
for row in cursor.fetchall():
    print(f"Товар: {row[0]:<25} | Категория: {row[1]:<12} | Цена: {row[2]} ₸")

target_category = "Техника"
print(f"\n--- Задание 4: Товары категории '{target_category}' ---")
cursor.execute("SELECT product, price, quantity, sale_date FROM sales WHERE category = ?", (target_category,))
for row in cursor.fetchall():
    print(f"Товар: {row[0]:<20} | Цена: {row[1]} ₸ | Кол-во: {row[2]} | Дата: {row[3]}")

print("\n--- Задание 5: Товары, отсортированные по убыванию цены ---")
cursor.execute("SELECT product, category, price FROM sales ORDER BY price DESC")
for row in cursor.fetchall():
    print(f"{row[0]:<25} ({row[1]}): {row[2]} ₸")

print("\n--- Задание 6: Количество записей в таблице ---")
cursor.execute("SELECT COUNT(*) FROM sales")
total_count = cursor.fetchone()[0]
print(f"Всего записей в таблице sales: {total_count}")
cursor.execute("SELECT DISTINCT category FROM sales")
categories = [r[0] for r in cursor.fetchall()]
print(f"Категории товаров ({len(categories)} шт.): {', '.join(categories)}")

conn.close()

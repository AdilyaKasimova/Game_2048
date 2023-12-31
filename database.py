import sqlite3

bd = sqlite3.connect("2048.sqlite")  # работает как open

cur = bd.cursor()  # создание курсора
cur.execute("""
create table if not exists RECORDS (
    name text, 
    score integer 
)""")


def insert_result(name, score):
    cur.execute("""
        insert into RECORDS values (?,?)
    """, (name, score))
    bd.commit()


def get_best_3():
    cur.execute("""
    SELECT name gamer, max(score) score from RECORDS	 -- вывод (отображение) таблицы (скрытое ROWID)
    GROUP by name -- у каждого игрока сохраняем только его максимальное значение
    ORDER by score DESC	-- сортируем по элементу score по убыванию
    limit 3 -- оставляет три верхних значения (формирует топ-3)
    """)
    return cur.fetchall()

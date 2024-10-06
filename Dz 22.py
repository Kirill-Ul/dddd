import psycopg2

conn = psycopg2.connect(
    dbname='northwind',
    user='postgres',
    password='kirill',
    host='localhost',
    port=5432
)

# cur = conn.cursor()
#
# cur.execute('''SELECT ship_country, SUM(freight) sum_freight
#                FROM orders
#                WHERE ship_region IS NOT NULL
#                GROUP BY ship_country
#                HAVING SUM(freight) > 2750
#                ORDER BY sum_freight DESC''')
#
# rows = cur.fetchall()
#
# for row in rows:
#     print(*row)
#
# cur.close()
# conn.close()
#
# cur = conn.cursor()
# try:
#     cur.execute('''INSERT INTO territories(territory_id, territory_description, region_id)
#                VALUES(601372, 'Andreewo', 2)''')
#     conn.commit()
# except Exception as e:
#     conn.rollback()
#     print(f'Ошибка {e}')
#
# cur.close()
# conn.close()



cur = conn.cursor()

cur.execute('''SELECT state_id, state_name
               FROM us_states''')

rows = cur.fetchall()
print('Выберите название штата из предложенных')
for row in rows:
    print(f'[{row[0]}] {row[1]}')


id = int(input('Введите ID: '))
capital = input('Введите название города : ')
country = input('Введите страну : ')
location = input('Укажите расположение: ')


try:
    cur.execute('''INSERT INTO us_states( state_id, state_name, state_abbr, state_region )
               VALUES(%s, %s, %s, %s)''',(id, capital, country, location))
    conn.commit()
except Exception as e:
    conn.rollback()
    print(f'Ошибка {e}')

cur.close()
conn.close()
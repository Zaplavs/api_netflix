import json
import sqlite3






def get_title_movie(title):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT `title`, `country`, `release_year`, `listed_in`, `description` "
                       "FROM netflix "
                       f"WHERE `title`='{title}' "
                       f"ORDER BY `date_added` DESC")
        result = cursor.fetchall()
        res = result[0]
        answer = {"title": res[0],
                  "country": res[1],
                  "release_year": res[2],
                  "genre": res[3],
                  "description":res[4]}
        answer = json.dumps(answer)
        return answer

def get_year_between(year1, year2):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT `title`, `release_year` "
                       "FROM netflix "
                       f"WHERE `title` BETWEEN {year1} AND {year2} "
                       f"LIMIT 100")
        result = cursor.fetchall()
        answer = []
        for movie in result:
            ans = {"title":movie[0],
                   "release_year":movie[1],}
            answer.append(ans)
        answer = json.dumps(answer)
        return answer

def get_rating(rat):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT `title`, `rating`, `description` "
                       "FROM netflix "
                       f"WHERE `rating` IN {rat} ")
        result = cursor.fetchall()
        answer = []
        for movie in result:
            ans = {"title": movie[0],
                   "rating": movie[1],
                   "description": movie[2]}
            answer.append(ans)
        answer = json.dumps(answer)
        return answer

def get_genre(genre):
    with sqlite3.connect("netflix.db") as connection:
        cursor = connection.cursor()
        print(genre)
        cursor.execute("SELECT `title`, `description` "
                       "FROM netflix "
                       f"WHERE `listed_in` LIKE '%{genre}%' "
                       f"ORDER BY `date_added` DESC "
                       f"LIMIT 10")
        result = cursor.fetchall()
        answer = []
        for movie in result:
            ans = {"title": movie[0],
                   "description": movie[1]}
            answer.append(ans)
        answer = json.dumps(answer)
        return answer

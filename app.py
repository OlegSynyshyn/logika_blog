from flask import Flask, render_template
from db_scripts import DBManager

app = Flask(__name__)  # Створюємо веб–додаток Flask
db = DBManager("blog.db")

@app.route("/")  # Вказуємо url-адресу для виклику функції
def index():
    categories = db.get_categories()
    print(categories)
    return render_template("index.html", categories=categories)  # html-сторінка, що повертається у браузер


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)  # Запускаємо веб-сервер з цього файлу в режимі налагодження

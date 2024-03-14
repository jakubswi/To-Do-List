from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
Bootstrap5(app)

list_of_tasks = {}


@app.route('/', methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        list_of_tasks[request.form['task']] = [request.form['description'], '#67C6E3', False]
        return render_template("index.html", tasks=list_of_tasks)
    return render_template("index.html", tasks=list_of_tasks)


@app.route('/delete', methods=["GET", "POST"])
def delete():
    done_tasks = request.form.getlist('task done')
    for task in done_tasks:
        list_of_tasks[task][2] = True
    return redirect(url_for('main_page'))


@app.route('/change_color/<task>/<color>')
def change_color(task, color):
    list_of_tasks[task][1] = color
    return redirect(url_for('main_page'))


@app.route('/restore/<task>')
def restore(task):
    list_of_tasks[task][2] = False
    return redirect(url_for('main_page'))


if __name__ == "__main__":
    app.run(debug=False)

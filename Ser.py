import sqlite3
from bottle import route, run, debug, template, request


@route('/skill_test_base/<id>')
def show_curs(id):
    conn = sqlite3.connect('skill.db')
    c = conn.cursor()
    c.execute("SELECT id,Profession,Description,Price FROM skillbox WHERE id=?", (id,))
    result = c.fetchall()
    c.close()
    output = template('make_table', result=result)
    return output


@route('/add_row', method=['GET', 'POST']) 
def create_curs():
    if request.POST.save:

        prof = request.POST.Profession.strip()
        descrip = request.POST.Description.strip()
        pr = request.POST.Price.strip()

        conn = sqlite3.connect('skill.db')
        c = conn.cursor()

        c.execute("INSERT INTO skillbox (Profession,Description, Price, Time) VALUES (?,?,?,?)", (prof, descrip, pr, 1))
        new_id = c.lastrowid
        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id

    else:
        return template('new_task')


@route('/add_info/<no:int>', method=['GET', 'POST'])
def update_curs(no):
    if request.GET.save:
        prof = request.GET.Profession.strip()
        descrip = request.GET.Description.strip()
        pr = request.GET.Price.strip()

        if descrip == 'open':
            prof = input()
            descrip = input()
            pr = input()

        conn = sqlite3.connect('skill.db')
        c = conn.cursor()
        c.execute("UPDATE skillbox SET Profession = ?, Description = ?, Price = ? WHERE id LIKE ?", (prof, descrip, pr, no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' % no
    else:
        conn = sqlite3.connect('skill.db')
        c = conn.cursor()
        c.execute("SELECT Profession, Description, Price FROM skillbox WHERE id LIKE ?", (str(no),))
        cur_data = c.fetchone()

        return template('edit_price', old=cur_data, no=no)


@route('/delete_row/<id>')
def delete_curs(id):
    conn = sqlite3.connect('skill.db')
    c = conn.cursor()
    result = c.fetchall()
    c.execute("DELETE FROM skillbox WHERE id = ?", (id,))
    conn.commit()
    c.close()
    output = template('delete_table', rows=result)
    return output


debug(True)
run(realoder=True)

from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)
app.secret_key = "secret123"


# ---------------- DATABASE CONNECTION ----------------
def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('home.html')


# ---------------- ABOUT ----------------
@app.route('/about')
def about():
    return render_template('about.html')


# ---------------- GALLERY ----------------
@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


# ---------------- BOOKING ----------------
@app.route('/booking', methods=['GET', 'POST'])
def booking():

    decor_image = request.args.get('decor_image')
    package_price = request.args.get('package_price', 0)

    success_message = None

    if request.method == 'POST':

        decor_image = request.form.get('decor_image')
        package_price = request.form.get('package_price')

        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        email = request.form['email']
        event_type = request.form['event_type']
        event_date = request.form['event_date']
        message = request.form['message']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO bookings
        (name, phone, address, email, event_type, event_date, message, decor_image, package_price)
        VALUES (?,?,?,?,?,?,?,?,?)
        """, (name, phone, address, email, event_type, event_date, message, decor_image, package_price))

        conn.commit()
        conn.close()

        success_message = "🎉 Booking Successful! Thank you for booking with us."

    return render_template('bookings.html',
                           decor_image=decor_image,
                           package_price=package_price,
                           success_message=success_message)


# ---------------- CONTACT ----------------
@app.route('/contact', methods=['GET', 'POST'])
def contact():

    if request.method == 'POST':

        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']

        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO contact_us (name, email, phone, message)
        VALUES (?,?,?,?)
        """, (name, email, phone, message))

        conn.commit()
        conn.close()

        flash("Message sent successfully ✅")
        return redirect(url_for('contact'))

    return render_template('contact.html')


# ---------------- ADMIN LOGIN ----------------
@app.route('/admin', methods=['GET', 'POST'])
def admin_login():

    if request.method == 'POST':

        password = request.form['password']

        if password == "1234":
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Wrong password ❌")

    return render_template('admin_login.html')


# ---------------- ADMIN DASHBOARD ----------------
@app.route('/admin_dashboard')
def admin_dashboard():

    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    conn = get_db_connection()
    cursor = conn.cursor()

    bookings = cursor.execute(
        "SELECT * FROM bookings ORDER BY id DESC").fetchall()

    contacts = cursor.execute(
        "SELECT * FROM contact_us ORDER BY id DESC").fetchall()

    conn.close()

    return render_template('dashboard.html',
                           bookings=bookings,
                           contacts=contacts)


# ---------------- CONFIRM BOOKING ----------------
@app.route('/admin/confirm_booking/<int:booking_id>')
def confirm_booking(booking_id):

    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE bookings SET status='Confirmed' WHERE id=?", (booking_id,))

    conn.commit()
    conn.close()

    flash("Booking confirmed ✅")
    return redirect(url_for('admin_dashboard'))


# ---------------- DELETE BOOKING ----------------
@app.route('/admin/delete_booking/<int:booking_id>')
def delete_booking(booking_id):

    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM bookings WHERE id=?", (booking_id,))

    conn.commit()
    conn.close()

    flash("Booking deleted ✅")
    return redirect(url_for('admin_dashboard'))


# ---------------- DELETE CONTACT ----------------
@app.route('/admin/delete_contact/<int:contact_id>')
def delete_contact(contact_id):

    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM contact_us WHERE id=?", (contact_id,))

    conn.commit()
    conn.close()

    flash("Contact message deleted ✅")
    return redirect(url_for('admin_dashboard'))


# ---------------- ADMIN LOGOUT ----------------
@app.route('/admin/logout')
def admin_logout():

    session.clear()
    return redirect(url_for('admin_login'))


# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, request, jsonify, render_template, redirect, flash
from flask_cors import CORS
import mysql.connector
import datetime

app = Flask(__name__)
app.secret_key = "abc123"
CORS(app)

# ======================
# DATABASE
# ======================
def db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Helia183@",
        database="foodshop1"
    )

# ======================
# PAGES
# ======================
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")

@app.route("/login")
def login_page():
    return render_template("login.html")

@app.route("/register")
def register_page():
    return render_template("register.html")

@app.route("/orders")
def orders_page():
    return render_template("orders.html")

@app.route("/checkout")
def checkout_page():
    return render_template("checkout.html")

@app.route("/user")
def user():
    return render_template("user.html")

@app.route("/admin")
def admin():
    return render_template("admin.html")

# ======================
# AUTH API
# ======================
@app.route("/api/register", methods=["POST"])
def register():
    try:
        data = request.json if request.is_json else request.form

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return jsonify(success=False, message="Thiếu dữ liệu")

        c = db()
        cur = c.cursor()

        cur.execute("""
            INSERT INTO nguoi_dung (HoTen, Email, MatKhau, VaiTro)
            VALUES (%s, %s, %s, %s)
        """, (name, email, password, "user"))

        c.commit()
        c.close()

        return jsonify(success=True)

    except mysql.connector.errors.IntegrityError:
        return jsonify(success=False, message="Email đã tồn tại")

    except Exception as e:
        return jsonify(success=False, message=str(e))


@app.route("/api/login", methods=["POST"])
def login():
    data = request.json if request.is_json else request.form

    c = db()
    cur = c.cursor(dictionary=True)

    cur.execute("""
        SELECT MaNguoiDung, HoTen, Email, VaiTro
        FROM nguoi_dung
        WHERE Email=%s AND MatKhau=%s
    """, (data.get("email"), data.get("password")))

    user = cur.fetchone()
    c.close()

    return jsonify(user=user)

# ======================
# ORDER API
# ======================
@app.route("/api/order", methods=["POST"])
def create_order():
    data = request.json
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")

    c = db()
    cur = c.cursor()

    cur.execute("""
        INSERT INTO orders (user_id, total, status, created_at)
        VALUES (%s, %s, %s, %s)
    """, (data["userId"], data["total"], "Đang xử lý", now))

    order_id = cur.lastrowid

    for i in data["items"]:
        cur.execute("""
            INSERT INTO order_items (order_id, name, price, qty)
            VALUES (%s, %s, %s, %s)
        """, (order_id, i["name"], i["price"], i["qty"]))

    c.commit()
    c.close()

    return jsonify(success=True)

@app.route("/api/orders/<int:user_id>")
def get_orders(user_id):
    c = db()
    cur = c.cursor()

    cur.execute("""
        SELECT id, total, status, created_at
        FROM orders
        WHERE user_id=%s
    """, (user_id,))

    orders = cur.fetchall()
    c.close()

    return jsonify(orders)

# ======================
# USER ACTION
# ======================
@app.route("/user-action", methods=["POST"])
def user_action():
    action = request.form.get("action")

    if action == "edit":
        return redirect("/user/edit")

    if action == "logout":
        return redirect("/")

    return redirect("/user")

@app.route("/user/edit", methods=["GET", "POST"])
def edit_user():
    if request.method == "POST":
        flash("✅ Cập nhật thông tin thành công!")
        return redirect("/user")

    return render_template("edit_user.html")

# ======================
# RUN
# ======================
if __name__ == "__main__":
    app.run(debug=True)

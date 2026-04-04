from flask import Flask, render_template, request, redirect, flash, session
import yaml
from function import add_expense, calculate_total, get_all_expenses, delete_expense_by_index, get_category_totals

app = Flask(__name__)
app.secret_key = "yash_smart_secure_key" 

def load_config():
    with open('config.yaml', 'r') as file:
        return yaml.safe_load(file)

# --- LOGIN & LOGOUT ROUTES ---
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.form.get('phone')
        otp = request.form.get('otp')
        
        
        if otp == "1234":
            session['user'] = phone
            flash("Successfully Logged In!", "success")
            return redirect('/')
        else:
            flash("Invalid OTP! Try 1234", "danger")
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

# --- DASHBOARD ROUTE ---
@app.route('/')
def index():
    if 'user' not in session:
        return redirect('/login')
        
    config = load_config()
    total = calculate_total()
    all_expenses = get_all_expenses()
    cat_data = get_category_totals()
    
    labels = list(cat_data.keys())
    values = list(cat_data.values())
    
    return render_template('index.html', 
                           total=total, 
                           currency=config['currency'], 
                           categories=config['categories'], 
                           expenses=all_expenses,
                           labels=labels,
                           values=values)

@app.route('/add', methods=['POST'])
def add():
    if 'user' not in session: return redirect('/login')
    amount = request.form.get('amount')
    category = request.form.get('category')
    note = request.form.get('note')
    if amount:
        add_expense(amount, category, note)
        flash("✅ Expense Saved!", "success")
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if 'user' not in session: return redirect('/login')
    delete_expense_by_index(index)
    flash("🗑️ Expense Deleted!", "danger")
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
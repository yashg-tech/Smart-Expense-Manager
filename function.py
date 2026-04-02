import datetime

# 1. Expense ko file mein save karne ka function
def add_expense(amount, category, note):
    import datetime
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Ensure karo ki amount khali na ho aur sahi format mein ho
    try:
        amount_val = float(amount)
    except:
        amount_val = 0.0

    # Format: Date, Amount, Category, Note
    data = f"{date}, {amount_val}, {category}, {note}\n"
    
    with open("expenses.txt", "a") as file:
        file.write(data)
    print("\n✅ Expense saved successfully!")

def get_all_expenses():
    expenses_list = []
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.split(",")
                if len(parts) >= 4:
                    # Ek dictionary bana rahe hain har expense ke liye
                    expense = {
                        'date': parts[0].strip(),
                        'amount': parts[1].strip(),
                        'category': parts[2].strip(),
                        'note': parts[3].strip()
                    }
                    expenses_list.append(expense)
        return expenses_list
    except FileNotFoundError:
        return []
def calculate_total():
    total = 0.0
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.split(",")
                if len(parts) >= 2:
                    # Yahan parts likhna zaroori hai
                    amount_str = parts[1].strip()
                    total += float(amount_str)
        return total
    except FileNotFoundError:
        return 0.0
    except Exception as e:
        print(f"Error reading file: {e}")
        return 0.0
def delete_expense_by_index(index_to_delete):
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
        
        # Reverse list handle karne ke liye index sahi karna
        # Kyunki hum website pe reverse dikha rahe hain [::-1]
        actual_index = len(lines) - 1 - index_to_delete
        
        if 0 <= actual_index < len(lines):
            del lines[actual_index]
            
        with open("expenses.txt", "w") as file:
            file.writelines(lines)
        return True
    except:
        return False

def get_category_totals():
    totals = {}
    try:
        with open("expenses.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                parts = line.split(",")
                if len(parts) >= 3:
                    cat = parts.strip()
                    amt = float(parts.strip())
                    # Dictionary mein category wise sum karna
                    totals[cat] = totals.get(cat, 0) + amt
        return totals # Example: {'Food': 500, 'Travel': 200}
    except:
        return {}            
      
 
import yaml
from function import add_expense, view_expenses, calculate_total 

def load_config():
    try:
        with open('config.yaml', 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:    
        return {'currency': 'INR', 'categories': ['Food', 'Travel', 'Others']}

def main():
    config = load_config()
    print(f"\n--- Welcome to Smart Expense Manager ({config['currency']}) ---")
    
    while True:
        print("\n" + "="*30)
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Spending")
        print("4. Exit")
        print("="*30)
        
        choice = input("\nChoose an option: ")
        
        if choice == '1':
            try:
                amount = float(input("Enter Amount: "))
                print(f"Available Categories: {', '.join(config['categories'])}")
                category = input("Enter Category: ")
                note = input("Enter a small note: ")
                
                add_expense(amount, category, note)
            except ValueError:
                print("\n❌ Error: Please enter a valid number for the amount!")
            
        elif choice == '2':
            view_expenses()
            
        elif choice == '3':
            total = calculate_total()
            print(f"\n💰 Your Total Spending so far: {config['currency']} {total}")
            
        elif choice == '4':
            print("\nExiting... Have a great day!")
            break
            
        else:
            print("\n❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
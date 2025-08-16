import csv
from datetime import datetime
import os

expense='expense.csv'
def initalize_file():
    if not os.path.exists(expense):
        with open (expense,'w',newline='') as file:
            writer=csv.writer(file)
            writer.writerow(['date','category','description','amount'])
def add_expense ():
    date=input("enter in yyyy-mm-dd or leave blank if today : ")
    if not date:
        date=datetime.today().strftime('%Y-%m-%d')

    category=input("enter category")
    description=input("enter description")
    amount =input ("enter amount")    
    with open(expense,'a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([date,category,description,amount])
        print ("expense added")

def view_expense ():
    if not os.path.exists(expense):
        print ("no expense")
    with open (expense,'r') as file:
        reader=csv.reader(file)
        next (reader)
        print("\n📋 All Expenses:\n")
        for idx,row in enumerate (reader,start=1):
            date, category ,description,amount=row
            print(f"{idx}.Date: {date}")
            print(f"category: {category}")
            print(f"desciption: {description}")
            print(f"amount: {amount}")
def main():
    initalize_file()
    while True: 
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()

        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expense()
        elif choice == '3':
            print("👋 Exiting. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose 1, 2, or 3.")



if __name__=='__main__':
    main()

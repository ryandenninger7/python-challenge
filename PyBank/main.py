import os
import csv

file_path = "Resources/budget_data.csv"
PyBank_results = "PyBank_results.txt"

with open(file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',')
    header_row = next(csv_reader)  # Skip the header row

    total_months = 0
    total = 0
    previous_value = None
    amount_of_changes = 0
    total_change = 0
    greatest_dec = 0
    greatest_inc = 0
    inc_month = ""
    dec_month = ""
    for row in csv_reader:
        total_months += 1
        try:
            value = int(row[1])
            total += value
            
            if previous_value is not None:
                change = value - previous_value
                total_change += change
                amount_of_changes += 1
                if change > greatest_inc:
                    inc_month = row[0]
                    greatest_inc = change
                if change < greatest_dec:
                    greatest_dec = change
                    dec_month = row[0]

            previous_value = value
        except (ValueError, IndexError):
            continue
    avg_change = round(total_change / amount_of_changes, 2)
    print(f"Financial Analysis")
    print(f"----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {inc_month} (${greatest_inc})")
    print(f"Greatest Decrease in Profits: {dec_month} (${greatest_dec})")
    
    with open(PyBank_results, 'w') as output_file:
        output_file.write("Financial Analysis\n")
        output_file.write(f"----------------------------\n")
        output_file.write(f"Total Months: {total_months}\n")
        output_file.write(f"Total: ${total}\n")
        output_file.write(f"Average Change: ${avg_change}\n")
        output_file.write(f"Greatest Increase in Profits: {inc_month} (${greatest_inc})\n")
        output_file.write(f"Greatest Decrease in Profits: {dec_month} (${greatest_dec})\n")
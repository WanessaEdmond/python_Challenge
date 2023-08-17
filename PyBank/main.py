import csv
with open('/Users/wedmo/OneDrive/Documents/Class/python_Challenge/PyBank/Resources/budget_data.csv') as csv_file:
    csv_read = csv.reader(csv_file, delimiter=',')
    headers = next(csv_read) # skip header line
 
    #for rows in csv_read:
    total = 0
    row_count=0
    changes = []
    previous_row = None
    max_profit = 0
    max_profit_date = ''
    min_profit = 0
    min_profit_date = ''
    previous_profit = 0

    for row in csv_read:
        profit = int(row[1])
        if profit - previous_profit > max_profit:
            max_profit = profit - previous_profit
            max_profit_date = row[0]
        if profit - previous_profit < min_profit:
            min_profit = profit - previous_profit
            min_profit_date = row[0]
        previous_profit = profit

        row_count +=1
        total += int(row[1])
        if previous_row is not None:
            change = int(row[1]) - int(previous_row[1])
            changes.append(change)
        previous_row = row
    average_change = sum(changes) / len(changes)
        
    
print(f'The total number of months included in the dataset is {row_count}.')
print(f'The net total amount of "Profit/Losses" over the entire period is {total}.')
print(f'The average of the changes in "Profit/Losses" over the entire period is {average_change}.')
print(f'The greatest increase in profits was on {max_profit_date} with an amount of ${max_profit}.')
print(f'The greatest decrease in profits was on {min_profit_date} with an amount of ${min_profit}.')


with open('analysis.txt', 'w') as txt_file:
    txt_file.write('Financial Analysis\n')
    txt_file.write('----------------------------\n')
    txt_file.write(f'Total Months: {row_count}\n')
    txt_file.write(f'Total: ${total}\n')
    txt_file.write(f'Average Change: ${average_change:.2f}\n')
    txt_file.write(f'Greatest Increase in Profits: {max_profit_date} (${max_profit})\n')
    txt_file.write(f'Greatest Decrease in Profits: {min_profit_date} (${min_profit})\n')

print('The analysis has been exported to analysis.txt.')
import os
import csv

months=[]
profit_loss=[]
Average_changes=[]

budget_csv=os.path.join('budget_data.csv')


with open(budget_csv, newline="") as csvfile:
    budget_reader = csv.reader(csvfile, delimiter=",")

    next (budget_reader)  #skip the heading

    for row in budget_reader:

        months.append(row[0])
        profit_loss.append(float(row[1]))

    for i in range(len(profit_loss)):
        ac=profit_loss[i]-profit_loss[i-1]
        Average_changes.append(ac)

Average_changes[0]=0
Count=len(Average_changes)-1
sum(Average_changes)/Count

total_months=(len(months))
net_amount= sum(profit_loss)
avg_change= sum(Average_changes)/Count

#Greatest Increase in Profits
max_profit=max(Average_changes)
index_max=Average_changes.index(max_profit)
max_month= months[index_max]

#Greatest Decrease in Profits
min_profit=min(Average_changes)
index_min=Average_changes.index(min_profit)
min_month= months[index_min]


financial_analysis = (f'''Financial Analysis
----------------------------------
Total Months: {total_months}
Total: ${net_amount:.2f}
Average Change: {avg_change:.2f}
Greatest Increase in Profits: {max_month} ${max_profit:.2f}
Greatest Decrease in Profits: {min_month} ${min_profit:.2f}''')

print(financial_analysis)

#Create a .txt file containing the same analysis in the print out
analysis = open('financial_analysis.txt', 'w')

analysis.write(financial_analysis)

analysis.close()



salesRevenue = input("Sales Revenue: ")
cogs = input("Cost of Goods Sold: ")
opExpense = input("Operating Expenses: ")

salesMargin = (salesRevenue - cogs - opExpense) * 1.0 / salesRevenue

print "Sales Margin = " + str(salesMargin * 100) + "%"

investedCapital = input("Invested Capital: ")

capitalTurnover = 1.0 * salesRevenue / investedCapital

print "Capital Turnover = " + str(capitalTurnover)

roi = salesMargin * capitalTurnover

print "Return on Investment = " + str(roi * 100) + "%"

# targetROI = input("Target ROI for the next year: ")
# 
# print "Note that this is assuming Sales Revenue and Average Invested Capital remain constant"
# 
# maxExpense = salesRevenue - (targetROI * investedCapital)
# 
# print "Maximum expense allowable in order to achieve an ROI of at least " + str(targetROI * 100) + "% is " + str(maxExpense)
# 
# newSalesMargin = (salesRevenue - maxExpense) * 1.0 / salesRevenue
# 
# print "New Sales Margin would therefore be: " + str(newSalesMargin*100) + "%"

# 6000000
# 3300000
# 2400000
# 3000000
# margin = 5%
# turnover = 2
# return on investment = 10%
# target return on investment = 15%
# max expense = 5550000
# new margin = 7.5%

#Residual Income
#profit - (capital * imputed interest rate)
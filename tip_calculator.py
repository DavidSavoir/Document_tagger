from optparse import OptionParser

parser = OptionParser()

parser.add_option("-m", "--meal", dest="cost_meal", help="meal cost")
parser.add_option("-t", "--tax", dest="cost_tax", help="tax cost")
parser.add_option("-p", "--tip", dest="cost_tip", help="tip cost",default="0")

(options, args) = parser.parse_args() 

if not (options.cost_meal or options.cost_tax): 
    parser.error("You need to provide the cost of your meal or tax")

#print "The first argument is '{}'.".format(options.first_arg)
#print "The second argument is '{}'.".format(options.second_arg)


meal = float(options.cost_meal)
tax = (float(options.cost_tax))/100
tip = (float(options.cost_tip))/100

tax_value = meal*tax
meal_with_tax = meal + tax_value
tip_value = tip*meal
total = meal_with_tax + tip_value

print "The base cost of your meal was %.2f" % meal_with_tax
print "The dollar value of the tax on the meal is: %.2f" % tax_value
print "The dollar value of the tip they'll need you to pay %.2f" % tip_value
print "Grand total is %.2f" % total

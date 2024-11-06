number_of_bottles_at_most_1L=int(input("Number of bottles at most 1 litre:"))
number_of_bottles_more_than_1L=int(input("Number of bottles more than 1 litre:"))


deposit_for_bottle_1=0.1*number_of_bottles_at_most_1L
deposit_for_bottle_2=0.25*number_of_bottles_more_than_1L
total_refund=deposit_for_bottle_1+deposit_for_bottle_2
#print("Total amount to be refuded is $",round(total_refund))
print("Total amount to be refuded is $",round(total_refund,1))
 

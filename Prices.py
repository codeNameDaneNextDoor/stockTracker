#initialize the count variable to 0
#initialize the sum variable to 0

count = 0
sum = 0

#input full_name
#input the min_price and convert it to float

name = input('What is your name?:')
minPrice = float(input("What is the minimum price?:"))

#create a list of prices example: price_list = []
priceList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#for price in price_list
for i in priceList :
    #add current price to sum
    sum += i
    #if price > min_price
    if i > minPrice :
        count += 1
        #increment count by 1        
#output "Hello",name,"the minimum price is ",min_price
#output "There are ",count,"prices greater than the minimum price"
#output "The total price is ",sum
print ('Hello',name,',the minimum price is', minPrice, '\nThere are' , count, 'prices greater than the minimum price.\nThe total price is', sum) 
login_user="Hassan test user"
wait_time = 5
product_price = 150
cart_price = 2000
Company_URL = "[www.tgs.com/dashboard](https://www.tgs.com/dashboard)"
user_age = 18
entered_promo = "summer20"
is_payment_successful = False


print("usename:",login_user)
print("wait_time:",wait_time)

# Testing
Actual_promo = "Hassan20"
minimum_required_age = 16
actual_company_URL = "[www.tgs.com/dashboard](https://www.tgs.com/dashboard)"
expected_price = 150
expected_cart_total = 2500
actual_price = product_price
actual_cart_total = 2000
actual_cart_total = cart_price
print("price verification test  passed:?",expected_price==actual_price)
print("cart_price verification test  passed:?",expected_cart_total==actual_cart_total)
print("URL verification test passed :?", actual_company_URL == Company_URL)
minimum_required_age = 16
print("check Required Age Test : ?", user_age>minimum_required_age)
print("Promo Test:?",Actual_promo == entered_promo )
print("check_payment_test:?", is_payment_successful == False)





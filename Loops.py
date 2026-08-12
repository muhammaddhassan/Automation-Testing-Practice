test_URLS = ["login_page","home_page","cart_page"]
for URL in test_URLS:
     print("Testing URLS:",URL)

wait_time = 0
max_wait = 5
while wait_time < max_wait:
     print("wait time to load button...seconds:", wait_time)

     wait_time += 1
print("Timeout Reached")

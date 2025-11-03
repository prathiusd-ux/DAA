import random
import time

secret_pin = f"{random.randint(0,9999):}"
print("generated otp:", secret_pin)

initial_timestamp = time.time()
guess_counter = 0

for current_number in range(10000):
    check_string = f"{current_number:04d}"
    guess_counter += 1
    
    if check_string == secret_pin:
        final_timestamp = time.time()
        print("otp found:", check_string)
        print("total attempts:", guess_counter)
        print("time taken:", round(final_timestamp - initial_timestamp, 4), "seconds")
        break
else:
    print("otp not found")
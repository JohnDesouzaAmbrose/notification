import time
from win11toast import toast

# Define the notification function
def show_notification():
    toast("Time to take a break!")

# Loop to show notification every 20 minutes
while True:
    show_notification()
    time.sleep(2)  # Sleep for 20 minutes (1200 seconds)

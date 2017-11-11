import time
from sms import sendSMS
from camera import takePhoto

def main():
    try:
        while True:
            sendSMS("This is Brooklyn", "+16463715825")
            time.sleep(2)
    except KeyboardInterrupt:
        print("Quitting Application")

if __name__ == "__main__":
    main()
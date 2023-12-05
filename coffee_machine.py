import paho.mqtt.client as mqtt
import time
from random import random, randint
import json

THINGSBOARD_HOST = "demo.thingsboard.io"
DEVICE_ACCESS_TOKEN = "7tZs7Otx4j5FIe9tqqmU"
TOPIC = "v1/devices/me/telemetry"
SLEEP_TIME = 3
COFFEE_PRICE = 1000
START_MONEY = 2000
sensor_data = {'coffee_cost': COFFEE_PRICE, 'money_left': START_MONEY, 'has_enough_money': True}
    
client = mqtt.Client()
client.username_pw_set(DEVICE_ACCESS_TOKEN, "")
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()
client.publish(TOPIC, json.dumps(sensor_data))
print("Start money is {} Ft and a coffee costs {} Ft".format(START_MONEY, COFFEE_PRICE))

try:
    while True:

        options = int(input("Options: (1: Buy coffee, 2: Pay in money, 3: Check my balance): "))

        match options: 
            case 1:
                if sensor_data["money_left"] - COFFEE_PRICE >= 0: 
                    sensor_data["money_left"] -= COFFEE_PRICE
                    if sensor_data["money_left"] < COFFEE_PRICE: 
                        sensor_data["has_enough_money"] = False
                    print("Coffee bought ", sensor_data)
                    time.sleep(SLEEP_TIME)
                else: 
                    print("Not enough money")
                    sensor_data["has_enough_money"] = False

                client.publish(TOPIC, json.dumps(sensor_data))

            case 2:
                money = int(input("How much do you want to pay in? (Ft) "))
                print("You paid in {} Ft".format(money))
                sensor_data["money_left"] += money
                if sensor_data["money_left"] >= COFFEE_PRICE: 
                    sensor_data["has_enough_money"] = True
                client.publish(TOPIC, json.dumps(sensor_data))

            case 3:
                print("You have {} Ft".format(sensor_data["money_left"]))

except KeyboardInterrupt:
    pass

except ValueError:
    print("Invalid value given, program ends.")

client.loop_stop()
client.disconnect()

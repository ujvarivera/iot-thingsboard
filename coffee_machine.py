import paho.mqtt.client as mqtt
import time
from random import random, randint
import json

THINGSBOARD_HOST = "demo.thingsboard.io"
DEVICE_ACCESS_TOKEN = "7tZs7Otx4j5FIe9tqqmU"
SLEEP_TIME = 3
COFFEE_PRICE = 500
START_MONEY = 2000
sensor_data = {'coffee_cost': COFFEE_PRICE, 'money_left': START_MONEY, 'has_enough_money': True}
    
client = mqtt.Client()
client.username_pw_set(DEVICE_ACCESS_TOKEN, "")
client.connect(THINGSBOARD_HOST, 1883, 60)
client.loop_start()
client.publish("v1/devices/me/telemetry", json.dumps(sensor_data))
print("Start money: {}, and a coffee costs {}".format(START_MONEY, COFFEE_PRICE))

try:
    while True:
        coffee_bought = int(input("Buy coffee (1: yes, 0: no): "))
        if (coffee_bought == 1):
            if (sensor_data["has_enough_money"] == True and sensor_data["money_left"] - COFFEE_PRICE >= 0): 
                sensor_data["money_left"] = sensor_data["money_left"] - COFFEE_PRICE
                if(sensor_data["money_left"] == 0): sensor_data["has_enough_money"] = False
                client.publish("v1/devices/me/telemetry", json.dumps(sensor_data))
                print("Coffee bought ", sensor_data)
                time.sleep(SLEEP_TIME)
            else: 
                print("Not enough money")
                sensor_data["has_enough_money"] = False
                client.publish("v1/devices/me/telemetry", json.dumps(sensor_data))
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()

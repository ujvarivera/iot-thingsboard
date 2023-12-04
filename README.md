# Coffee Machine in Thingsboard

The python code sends data to Thingsboard, like how much money do you have, whether enough to buy a coffee and the current cost of the coffee.

If you start the python script, you can do the following:

![options](pics/options.png)

- Buy a coffee (only if you have enough money)
- Pay in money (to buy more coffee in the future)

## Created Dashboard in Thingsboard

On the created dashboard, you can see your current money what's left, whether it is enough to buy a coffee and the current cost of the coffee. Also, you can see alerts, which indicating if you want to buy coffee but don't have enough money.

![dashboard](pics/dashboard.png)

## How to run

- Create a device in your thingsboard.
- In the python code, change the THINGSBOARD_HOST and the DEVICE_ACCESS_TOKEN constants.
- Create the alarm and the dashboard in thingsboard.
- Run the python code in your terminal: 
`python coffee_machine.py`

### Create the alarm

1. Create a new rule chain

It will send an alarm if you have not enough money to buy a coffee.

![alarm_rule_chain](pics/alarm_rule_chain.png)

The script:

![alarm_script](pics/alarm_script.png)

2. Change the root rule chain

Attach the new, alarm rule chain at the end of the root rule chain.

![root_rule_chain](pics/root_rule_chain.png)


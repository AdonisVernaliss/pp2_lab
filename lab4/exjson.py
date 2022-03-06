import json

with open('sample-data.json', 'r') as f:
    response = f.read()
data = json.loads(response)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for i in range(len(data["imdata"])):
    dn = data['imdata'][i]['l1PhysIf']['attributes']['dn']
    descr = data['imdata'][i]['l1PhysIf']['attributes']['descr']
    speed = data['imdata'][i]['l1PhysIf']['attributes']['speed']
    mtu = data['imdata'][i]['l1PhysIf']['attributes']['mtu']
    print("{:<49}{:<23}{:<7}".format(dn, descr, speed), mtu)

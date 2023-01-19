new_item = {'type':'item', 'color':'undefined', 'material':'unknown'}
item_dict = [new_item for item in range(100)]

for i in range(20):
    if item_dict.copy()[i]['color'] == 'undefined':
        item_dict[i]['color'] = 'blue'

for i in range(20):
    if item_dict.copy()[i]['type'] == 'item':
        item_dict[i]['type'] = 'soccer_ball'

for i in range(20):
    if item_dict.copy()[i]['material'] == 'unknown':
        item_dict[i]['material'] = 'rubber'

for i in range(20):
    if item_dict.copy()[i]['type'] == 'soccer ball':
        item_dict[i]['price'] = 20   

print(item_dict[0:1])
from flowlogs_reader import FlowLogsReader
import json

flow_log_reader = FlowLogsReader('flowlogs-analize')

# print(dir(flow_log_reader))



values_json = [event.to_dict() for event in list(flow_log_reader)]



#must covert datetime values into strings otherwise unable to use json dumps
for value in values_json:
    if value.get('start'):
        value['start'] = value['start'].strftime('%m/%d/%Y')
    if value.get('end'):
        value['end'] = value['end'].strftime('%m/%d/%Y')


interfaces = set()

for value in values_json:
  
    interfaces.add(value.get('interface_id'))

interface_list = list(interfaces)

#######################
frequency_accept = {}
frequency_deny = {}


for i in interface_list:
    for value in values_json:
        if value.get('interface_id') == i: #if the interface id from our set exists in a dictionary from the main json data
            if value.get('action') == 'REJECT':
                if i in frequency_deny:
                    frequency_deny[i] += 1
                else: 
                    frequency_deny[i] = 1

            if value.get('action') == 'ACCEPT':
                if i in frequency_accept:
                    frequency_accept[i] += 1
                else: 
                    frequency_accept[i] = 1


accept_list = []

deny_list = []

#the data needs to be modified by adding another key which is needed for the x axis in the react chart
for key,value in frequency_accept.items():
    new = {}
    new['interface_id'] = key 
    new['count'] = value 
    accept_list.append(new)

for key,value in frequency_deny.items():
    new = {}
    new['interface_id'] = key 
    new['count'] = value 
    deny_list.append(new)

print(accept_list)
print(deny_list)
                

   



# print(interfaces)





with open('server/flowlog_data.json', 'w') as ink:
    ink.write(json.dumps(values_json))

with open('server/accepted.json', 'w') as ink:
    ink.write(json.dumps(accept_list))

with open('server/denied.json', 'w') as ink:
    ink.write(json.dumps(deny_list))


# #get total count of Accepts and associate with interface
# #get total cound Rejects 

# #need to get a list of all unique interfaces
# #for each interface need to check if it's a reject or 

# #get total count of accepts in interval 

# #get unique time 
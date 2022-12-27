from flowlogs_reader import FlowLogsReader
import json
import functools

flow_log_reader = FlowLogsReader('flowlogs-analize')

values_json = [event.to_dict() for event in list(flow_log_reader)]

#must covert datetime values into strings otherwise unable to use json dumps
for value in values_json:
    if value.get('start'):
        value['start'] = value['start'].strftime('%m/%d/%Y')
    if value.get('end'):
        value['end'] = value['end'].strftime('%m/%d/%Y')

interfaces = set()  #use set because it automatically parses uniqe values from list 

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


sum_accept = [sum.get('count') for sum in accept_list]
sum_deny = [sum.get('count') for sum in deny_list]

                
single_metric_accept = functools.reduce(lambda a, b: a + b, sum_accept) #a and b are paramaters for the lambda 
single_metric_deny = functools.reduce(lambda a, b: a + b, sum_deny ) 
   
print(single_metric_accept)
print(single_metric_deny)


with open('server/flowlog_data.json', 'w') as ink:
    ink.write(json.dumps(values_json))

with open('server/accepted.json', 'w') as ink:
    ink.write(json.dumps(accept_list))

with open('server/denied.json', 'w') as ink:
    ink.write(json.dumps(deny_list))

with open('server/single_metric_accept.json', 'w') as ink:
    ink.write(json.dumps(single_metric_accept))

with open('server/single_metric_deny.json', 'w') as ink:
    ink.write(json.dumps(single_metric_deny))


from datadog import initialize, api
import time

options = {
    'api_key': '5e13414b657f878dbc9170d2cb5a6cc0',
    'app_key': '698b7f0309d617a6797aee1e37109a2d6cca5252'
}

initialize(**options)

now = int(time.time())
query = 'docker.cpu.system{*}by{host}'
response =  api.Metric.query(start=now - 3600, end=now, query=query)
mylist = (response['series'])
for i in mylist:
    print mylist[0]['pointlist'][i]['numeric_value']
    print mylist[0]['scope'][i]
    print mylist[0]['display_name'][i]

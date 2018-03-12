from datadog import initialize, api

options = {
    'api_key': '5e13414b657f878dbc9170d2cb5a6cc0',
    'app_key': 'd604ff0f5cfc468c69d01cfe6c967c55a8043379'
}

initialize(**options);
dash={};
dash = api.Monitor.get(3921940);
#print dash;
monitorname = dash['name']
print "Name of the monitor is " + monitorname;
createdate = dash['created'];
print "Created date of the monitor is " + createdate;
modifydate = dash['modified'];
print "modified date of the monitor is " + modifydate;
Author = dash['creator'];
print "Author of the monitor is " + str(Author)
rule = dash['query'];
print "Query of the monitor is " + str(rule)

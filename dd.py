from datadog import initialize, api

options = {
    'api_key': '5e13414b657f878dbc9170d2cb5a6cc0',
    'app_key': 'd604ff0f5cfc468c69d01cfe6c967c55a8043379'
}

initialize(**options)
dash={};
dash = api.Screenboard.get(47874)
print dash;
creationdate = dash['created'];
Boardname = dash['board_title'];
author = dash['created_by']['name'];

print "Creation Date of the dashboard is : " + creationdate;
print "Title of the dashboard is : " + Boardname;
print "Author of dashboard : " + author;

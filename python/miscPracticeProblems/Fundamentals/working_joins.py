line_data = {'key': 'customer', 'label': 'Customer', 'line_type': 'text', 'actions_on': [], 'actions_off': [], 'description': 'Do something here.'}

actions_off = ""
actions_on = ""

if line_data['actions_off']:
    actions_off = ", -".join(line_data['actions_off'])
    actions_off = f"-{actions_off}"

if line_data['actions_on']:
    actions_on = ", ".join(line_data['actions_on'])

if len(actions_off) > 0:
    actions = f"{actions_off}, {actions_on}"
else:
    actions = f"{actions_on}" 

print(actions)
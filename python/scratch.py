admins = [
    ("""Scott White""", "scott.white@huvrdata.com"),
    ("""Jeff Sheffield""", "jeff.sheffield@huvrdata.com"),
    ("""Nick Fang""", "nick.fang@huvrdata.com"),
    ("""Julia Guimiot""", "julia.guimiot@huvrdata.com"),
    ("""Sean Hong""", "sean.hong@huvrdata.com"),
    ("""Saul Feliz""", "saul.feliz@huvrdata.com"),
    ("""Steve Hatch""", "steve.hatch@huvrdata.com"),
    ("""William Wigfield""", "william.wigfield@huvrdata.com"),
]

# admin_emails = []
# for admin in admins:
#     admin_emails.append(admin[1])

admin_emails = [admin[1] for admin in admins]
print(admin_emails)

response = {
  'asset_condition': [],
  'owner': [{
    'id': 85,
    'name': 'Gallegos LLC',
    'parent': None,
    'created_on': '2021-03-30T21:51:55.143538Z',
    'updated_on': '2021-03-30T21:51:55.143809Z',
    'role': 'OWNER',
    'description': None,
    'is_active': True,
    'labels': []
  }, {
    'id': 86,
    'name': 'Brady, Moran and Jones',
    'parent': None,
    'created_on': '2021-03-30T21:51:55.147546Z',
    'updated_on': '2021-03-30T21:51:55.147827Z',
    'role': 'OWNER',
    'description': None,
    'is_active': True,
    'labels': []
  }, {
    'id': 87,
    'name': 'Sutton and Sons',
    'parent': None,
    'created_on': '2021-03-30T21:51:55.161450Z',
    'updated_on': '2021-03-30T21:51:55.161733Z',
    'role': 'OWNER',
    'description': None,
    'is_active': True,
    'labels': []
  }],
  'asset_type': [{
    'id': 62,
    'name': 'Kevin Manors',
    'manufacturer': 'Hurst-Kelly',
    'model': None,
    'track_asset_condition': True,
    'created_on': '2021-03-30T21:51:55.149755Z',
    'updated_on': '2021-03-30T21:51:55.150004Z',
    'is_active': True,
    'deactivated_on': None,
    'icon_url': '/api-static/images/markers/pin-blue-11.png'
  }, {
    'id': 63,
    'name': 'Alexander Views',
    'manufacturer': 'Weber, Gallagher and Johnson',
    'model': None,
    'track_asset_condition': True,
    'created_on': '2021-03-30T21:51:55.153235Z',
    'updated_on': '2021-03-30T21:51:55.153557Z',
    'is_active': True,
    'deactivated_on': None,
    'icon_url': '/api-static/images/markers/pin-blue-11.png'
  }, {
    'id': 64,
    'name': 'Walker Plains',
    'manufacturer': 'Lucas PLC',
    'model': None,
    'track_asset_condition': True,
    'created_on': '2021-03-30T21:51:55.157169Z',
    'updated_on': '2021-03-30T21:51:55.158022Z',
    'is_active': True,
    'deactivated_on': None,
    'icon_url': '/api-static/images/markers/pin-blue-11.png'
  }],
  'parent': [],
  'count': 3
}

def get_owners(response):
	for owner in response["owner"]:
		print(owner["id"])
	print(response["count"])

get_owners(response)
import geojson
import dataparse as p


def create_map(data_file):
	"""Creates a GeoJSON file."""

	# Define a type of GeoJSON
	geo_map = {"type": "FeatureCollection"}
	# Define list to collect each point to graph
	item_list = []

	# Iterate over our data to create GeoJSON doc
	for index, line in enumerate(data_file):
		# Skip any zero coordinates
		if line['X'] == '0' or line['Y'] == '0':
			continue
		# New dict for every iteration
		data = {}
		# Assign line items to json fields
		data['type'] = 'Feature'
		data['id'] = index
		data['properties'] = {'title': line['Category'],
		                      'description': line['Descript'],
		                      'date': line['Date']}
		data['geometry'] = {'type': 'Point',
		                    'coordinates': (line['X'], line['Y'])}
		# Add data dict to our itemlist
		item_list.append(data)

	# for each point in our item list we add a point to dict
	for point in item_list:
		geo_map.setdefault('features', []).append(point)
	# write a file, upload to gist.github.com
	with open('file_sf.geojson', 'w') as f:
		f.write(geojson.dumps(geo_map))


def main():
	data = p.parse(p.my_file, p.delimiter)
	return create_map(data)


if __name__ == '__main__':
	main()

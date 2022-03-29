import requests

def get_weather_desc_and_temp():
	api_key = "{sign up for an api key at api.openweathermap.org}" #removed for github share
	city = "York"
	country = "GB"

	request_url = "http://api.openweathermap.org/data/2.5/weather?q="+city+","+country+"&appid="+api_key+"&units=metric"

	request = requests.get(request_url)
	json = request.json()

	description = json.get("weather")[0].get("description")
	temp_min = json.get("main").get("temp_min")
	temp_max = json.get("main").get("temp_max")
	
	return {'description': description,
			'temp_min': temp_min,
			'temp_max': temp_max}

def main():
	weather_dict = get_weather_desc_and_temp()
	#print the results
	print("Today's forecast is", weather_dict.get('description'))
	print("Today's minimum temperature is", weather_dict.get('temp_min'))
	print("Today's maximum temperature is", weather_dict.get('temp_max'))
	#print(json)

main()
#  Pass the data back to the main.py file, so that you can print the data from main.py
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
# print(sheet_data)

#sheet_data = data_manager.get_destination_data()



if sheet_data[0]["iataCode"] == "":
    city_names = [row["city"] for row in sheet_data]
    print(city_names)
    codes = flight_search.get_destination_code(city_names)
    data_manager.update_destination_code(codes)
    sheet_data = data_manager.get_destination_data()
    # print(f"sheet_data:\n {sheet_data}")

tom = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tom,
        to_time=six_months_from_today
    )

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_msg(
            message= f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}"
        )

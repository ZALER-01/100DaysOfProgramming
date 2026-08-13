capitals = {
    "Bihar":"Patna",
    "india":"New Delhi",
    "Maharashtra":"Mumbai"
}

# travel_log = {
#     "Bihar":["Muzaffarpur" , "Hajipur", "Samastipur"],
#     "india":["Bihar", "UP","Hyderabad"],
#     "Maharashtra":["Pune","Chinchwad"]
# }

# print(travel_log["Bihar"][0])

nested_list = ["A","B","c",["D","E"]]
print(nested_list[3][1])

travel_log = {
    "Bihar":{
        "NumOfTimesVisited":8 ,
        "CitiesVisited":{"Muzaffarpur","Gaya","Purnia","Sitamadhi"}
    },
    "india":{
        "NumOfTimesVisited":10 ,
        "CitiesVisited":{"Pune","Banglore","Gurugram","Hyderabad"}
    }
}
print(travel_log["Bihar"]["NumOfTimesVisited"])
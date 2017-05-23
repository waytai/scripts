var start_time = new ISODate('2016-01-23T16:00:00Z');
var end_time = new ISODate('2016-04-20T16:00:00Z');
print(start_time);  
print(end_time);  
db.mqtt_event.remove({"sendat":{"$gte":start_time,"$lte":end_time}})




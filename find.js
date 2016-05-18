db.mqtt_event.find({"sendat":{"$gt":new Date("2016-05-18 13:00:00")}}).sort({"sendat":-1}).limit(100).forEach( function(cap){
    print(cap.sendat, cap.productid,cap.deviceid,cap.payload)
})


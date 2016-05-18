db.mqtt_event.find().sort({"sendat":-1}).limit(100).forEach( function(cap){
    print(cap.sendat.toISOString(), cap.productid,cap.deviceid,cap.payload)
})


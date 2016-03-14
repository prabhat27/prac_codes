var gcm = require('node-gcm');
var request = require("request");

var header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/27.0',
              'content-type': 'application/json'
             }
             
send_notif = function(notifMessage, registrationIds, callback){

    var API_KEY = 'AIzaSyDz8oxSPkf6E66vCPS3XhcTq9DEMTaVssg' //API key that Google gave you when you registered for the Google Cloud Messaging service
    var sender = new gcm.Sender(API_KEY);        
    var message = new gcm.Message({
        priority: 'high',
    })

    message.addNotification({
        title: 'Test Message',
        body: notifMessage,
        icon: 'ic_launcher',
        // click_action: "Dashboard"
    });

    sender.sendNoRetry(message, registrationIds, function (err, result) {
        if(err) callback(false, 304, "Error while sending Notif !");
        else    callback(true, 200, "Message sent !");
    });

}


var registrationIds = ['APA91bEPa0lIbtyTcpRqgkX7be_7rBJUXrTvc4BN4-oTTqw_5gkwxCfjKHFEV_Z9Ha9MtGZWuplnscV2BYDwJiteEqpwpgiQWVe-bN4iiGk-RM_MJpms99iQ8MWforaFvjFyAp5mXKcU']
var message = "hello world !"

send_notif(message, registrationIds, function(status, code, msg){
    console.log(msg);
})
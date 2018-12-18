
    const myChannel = "myIOT";


    // $(function(argument) {
    //   $('[type="checkbox"]').bootstrapSwitch();
	//   $.fn.bootstrapSwitch.defaults.labelWidth = 400;
    // });

	// $('input').on('switchChange.bootstrapSwitch', function (event, state) {
    //     console.log("EVENT>>>" , this.id, state);
    //     var btnStatus = new Object();
    //     //btnStatus[this.id] = $(this).data(state ? 'onText' : 'offText');
    //     btnStatus[this.id] = state;
    //     console.log(btnStatus);

    //     var event = new Object();
    //     event.event = btnStatus;
    //     //sendEvent(this.id + "-" + value);
    //     publishUpdate(event, myChannel);
    // })

  var alive_second = 0;
  var heartbeat_rate = 5000;
console.log("I am connected!");
  function keep_alive(){
    var request = new XMLHttpRequest();
    request.onreadystatechange = function(){
      if(this.readyState === 4){
            if (this.status === 200) {
              if (this.responseText !== null) {
                var date = new Date();
                alive_second = date.getTime();
                var keep_alive_data=this.responseText;
                console.log(keep_alive_data)
                }
            }
        }
    };
    var val = 50;
    // request.open("POST","/web/", true);
    // request.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    // request.send(val);
    setTimeout('keep_alive()', heartbeat_rate);
   }

  function time(){
            var d = new Date();
            var current_sec = d.getTime();
            if (current_sec - alive_second > heartbeat_rate + 1000){
               document.getElementById("Connection_id").innerHTML = " Dead";
            } else {
               document.getElementById("Connection_id").innerHTML = " Alive";
            }
    setTimeout('time()',1000);
   }

    pubnub = new PubNub({
      publish_key: 'pub-c-09074860-0d78-4dce-90de-ad5efe037e74',
      subscribe_key: 'sub-c-25e6eef0-f44e-11e8-b4b3-36001c7c3431'

    });


    pubnub.addListener({
        status: function(statusEvent) {
            if (statusEvent.category === "PNConnectedCategory") {
                //publishSampleMessage();
            }
        },
        message: function(message) {
        var msg = message.message;
        
        console.log(JSON.stringify(msg));
        console.log(typeof(msg));
        var csrftoken = Cookies.get('csrftoken');
        console.log("csrf: "+ csrftoken);
        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }
        $.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });
        
        $.ajax({
            type: "POST",
            url: "/web/",
            data: {'id':msg},
            dataType: "json",
        //     headers: {
        //         'X-CSRF-Token': csrftoken 
        //    },
            success: function(data){
                console.log("success");
            },
            error: function(res,e){
                alert("Something Went Wrong");
            }
        });
        
        if (msg.event){
            $("#motion_id").text(msg.event["motion"]);

         }
        },

        presence: function(presenceEvent) {
            // handle presence
        }
    })

    pubnub.subscribe({
        channels: [myChannel]
    });


	function publishUpdate(data, channel) {
	  pubnub.publish({
		channel: channel,
		message: data
	  },
      function (status, response) {
        if (status.error) {
            console.log(status)
        } else {
            console.log("message Published w/ timetoken", response.timetoken)
        }
       }
	  );

	}
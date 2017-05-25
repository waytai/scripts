function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

$('input[name="my-checkbox"]').on('switchChange.bootstrapSwitch', function(event, state) {
    console.log(this); // DOM element
    var td_node = $(this).parent().parent().parent()
    var t_start_one = td_node.children().eq(0).text()
    var t_end_one= td_node.children().eq(1).text()
    var bright_one = td_node.children().eq(2).text()

    var t_start_two = td_node.children().eq(3).text()
    var t_end_two = td_node.children().eq(4).text()
    var bright_two = td_node.children().eq(5).text()

    var t_start_three = td_node.children().eq(6).text()
    var t_end_three = td_node.children().eq(7).text()
    var bright_three = td_node.children().eq(8).text()
    var turn_off_time = td_node.children().eq(9).text()
  

    console.log(t_start_one); // DOM element
    console.log(t_end_one); // DOM element
    console.log(bright_one); // DOM element

    console.log(t_start_two); // DOM element
    console.log(t_end_two); // DOM element
    console.log(bright_two); // DOM element

    console.log(t_start_three); // DOM element
    console.log(t_end_three); // DOM element
    console.log(bright_three); // DOM element
    console.log(turn_off_time); // DOM element

    console.log(state); // true | false
    if (state)
    {
        console.log("state is true");
        $.ajax({
            type: "post",
            dataType: "json",
            url: '/downlink/downlinkcmd/',
            beforeSend: function(jqXHR, settings){
                jqXHR.setRequestHeader("x-csrftoken", csrftoken);

            },
            data: {dev_eui:"1234"},
            success: function (data) {
                    console.log(data);
                    }
                }
            );
    }
    else
    {
        console.log("state is false");
    }
});


$(document).ready( function() {
    $('html').ajaxSend(function(event, xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    });

    $("form").submit( function() {
        var username = $("#id_username").val();
        var message =  $("#id_message").val();
        var html = '<li><h5>' +username+ '</h5><p>' +message+ '</p></li>';
        if (username && message) {
            $.ajax({
                type: 'POST',
                url: '/ajax/request/send/',
                data: {
                    username: username,
                    message: message
                },
                beforeSend:function() {
                    $(".loader").show();
                },
                success:function(data){
                    $(".loader").hide();
                    $(".items").append(html);
                }
            });
        }
        return false;
    });
});
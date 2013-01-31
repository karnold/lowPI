var app = {
    // Application Constructor
    initialize: function() {
        this.bindEvents();
    },
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
    },
    // deviceready Event Handler
    //
    // The scope of 'this' is the event. In order to call the 'receivedEvent'
    // function, we must explicity call 'app.receivedEvent(...);'
    onDeviceReady: function() {
        app.receivedEvent('deviceready');
    },
    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    }
};

app.initialize();

(function($) {
    $(document).ready(function() {
        var racer = false;

        $('.switch').click(function(e) {
            e.preventDefault();

            if (racer) return;

            racer = true;

            $.ajax({
                url: 'http://192.168.1.108',
                type: 'POST',
                dataType: 'json',
                data: {
                    switch: $(this).data('switch'),
                },  
                success: function(data) {
                    racer = false;
                    console.log('success');
                },  
                error: function(e) {
                    racer = false;
                    console.log('error');
                }   
            }); 
        }); 
    }); 
})(jQuery);

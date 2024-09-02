$(document).ready(function() {
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) { /* Adjust 100 to the scroll position where you want to change the nav */
            $('.navbar').addClass('transparent-nav');
        } else {
            $('.navbar').removeClass('transparent-nav');
        }
    });
}); 
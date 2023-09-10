$(document).ready(function () {
    $('.parent').click(function (event) {
        if ($(event.target).hasClass('arrow')) {
            // Toggle content when the arrow is clicked
            $(this).find('.content').slideToggle();
            $(this).find('.arrow').toggleClass('rotate');
        } else if ($(event.target).hasClass('parent')) {
            // Toggle content when the parent div is clicked
            $(this).find('.content').slideToggle();
            $(this).find('.arrow').toggleClass('rotate');
        }
    });
});

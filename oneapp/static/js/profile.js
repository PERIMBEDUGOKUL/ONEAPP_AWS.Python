$('.dpy-btn').click(function(){
    $('.sidebar .aws .dpy-show').toggleClass("show"); 
    $('.sidebar .aws .first').toggleClass("rotate");
  });
// $('.sidebar .aws .aws-active').click(function(){
//      $(this).addClass("active").siblings().removeClass("active");
// });

// $(document).ready(function() {
//   $(".container").click(function() {
//       $(".content", this).slideToggle();
//       $(".arrow", this).toggleClass("rotate");
//   });
// });


// $(document).ready(function () {
//   $('.parent').click(function (event) {
//       if ($(event.target).hasClass('arrow')) {
//           // Toggle content when the arrow is clicked
//           $(this).find('.content').slideToggle();
//           $(this).find('.arrow').toggleClass('rotate');
//       } else if ($(event.target).hasClass('parent')) {
//           // Toggle content when the parent div is clicked
//           $(this).find('.content').slideToggle();
//           $(this).find('.arrow').toggleClass('rotate');
//       }
//   });
// });
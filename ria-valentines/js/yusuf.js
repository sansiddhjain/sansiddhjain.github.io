var orj = $('.left .page-inner').outerHeight();

$('.left .page-inner').on('keydown', function() {
  if ( !$(this).hasClass("full") ) {
    var divs = $(this).find("div"),
        heights = 0;

    console.log(heights);

    divs.each(function(i) {
      heights = heights + $(this).outerHeight();
      console.log(heights);
    });

    if (heights > orj) {
      $(".right .page-inner").focus();
      $(this).addClass("full");
    }
  }
});

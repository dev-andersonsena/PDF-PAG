$(function() {
	$(".closeburger").click( function() {
		$(".container").toggleClass("open");
	});

  // CodePen Dashboard animation
  window.setTimeout(autoopen, 700);
});

function autoopen() {
  $(".container").addClass("open");
  window.setTimeout(autoclose, 1500);
}

function autoclose() {
  $(".container").removeClass("open");
}

	
	

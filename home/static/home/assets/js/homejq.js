// dropdown
$('.ui.dropdown').dropdown();

// sidebar
$('.menubar-icon').click(function(){
	sidebar('toggle')
});

// checkbox
$('.ui.checkbox').checkbox();

// accordion
$('.ui.accordion').accordion();

// modal
$('.feedback-btn').click(function(){ $('.ui.feedback').modal('show')});
$('.del-ac').click(function(){ $('.ui.delete').modal('show')});

// shape flipping 
$('#menu-item').hover(function(){
	$('.shape').shape('flip down')
});
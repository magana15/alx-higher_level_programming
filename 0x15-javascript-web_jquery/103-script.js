$(document).ready(function(){
  
  function translate(){
  const langcode = $('#language_code').val();
  const url = `https://hellosalut.stefanbohacek.dev/?lang=${langcode}`;
  
$.get(url, function(data){
  $('#hello').text(data.hello);
});}
$('#btn_translate').click(translate)
$('#language_code').keypress(function(event){
  if (event.which===13){translate();}
})
});



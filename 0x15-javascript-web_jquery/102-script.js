$(document).ready(function(){
  $('#btn_translate').click(function(){
  const langcode = $('#language_code').val();
  const url = `https://hellosalut.stefanbohacek.dev/?lang=${langcode}`;
  
$.get(url, function(data){
  $('#hello').text(data.hello);
});
});
});





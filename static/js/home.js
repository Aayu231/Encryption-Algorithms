$(document).ready(function() {
  $('#caesar-form').on('submit', function(event) {
    $('#caesar-output').text("Encrypting your message...").show();
    $.ajax({
       data : {
          plaintext : $('#caesar-plaintext').val(),
          key: $('#caesar-key').val(),
              },
          type : 'POST',
          url : '/encrypt/caesar/'
         })
     .done(function(data) {
       console.log(data.cipher);
      $('#caesar-table').show();
       $('#caesar-output').text(data.cipher).show();
   });
   event.preventDefault();
   });

   $('#mult-form').on('submit', function(event) {
    $('#mult-output').text("Encrypting your message...").show();
    $.ajax({
       data : {
          plaintext : $('#mult-plaintext').val(),
          key: $('#mult-key').val(),
              },
          type : 'POST',
          url : '/encrypt/multiplicative/'
         })
     .done(function(data) {
       console.log(data.cipher);
      $('#mult-table').show();
       $('#mult-output').text(data.cipher).show();
   });
   event.preventDefault();
   });
});



//Copy to clipboard script
function myFunction(value) {
  console.log(value);
    str = document.getElementById(value).innerHTML;
    const el = document.createElement('textarea');
    el.value = str;
    document.body.appendChild(el);
    el.select();
    document.execCommand('copy');
    document.body.removeChild(el);
    alert('Copied the text : ' + el.value);
};
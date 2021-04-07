$(document).ready(function() {
    $('#caesar-form').on('submit', function(event) {
      $('#caesar-output').text("Decrypting your message...").show();
      $.ajax({
         data : {
            cipher : $('#caesar-ciphertext').val(),
            key: $('#caesar-key').val(),
                },
            type : 'POST',
            url : '/decrypt/caesar/'
           })
       .done(function(data) {
         console.log(data.plaintext);
        $('#caesar-table').show();
         $('#caesar-output').text(data.plaintext).show();
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
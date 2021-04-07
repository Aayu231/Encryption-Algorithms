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

   $('#affine-form').on('submit', function(event) {
    $('#affine-output').text("Encrypting your message...").show();
    $.ajax({
       data : {
          plaintext : $('#affine-plaintext').val(),
          affine_key1: $('#affine_key1').val(),
          affine_key2: $('#affine_key2').val(),
              },
          type : 'POST',
          url : '/encrypt/affine/'
         })
     .done(function(data) {
       console.log(data.cipher);
      $('#affine-table').show();
       $('#affine-output').text(data.cipher).show();
   });
   event.preventDefault();
   });

   $('#autokey-form').on('submit', function(event) {
    $('#autokey-output').text("Encrypting your message...").show();
    $.ajax({
       data : {
          plaintext : $('#autokey-plaintext').val(),
          key: $('#autokey-key').val(),
              },
          type : 'POST',
          url : '/encrypt/autokey/'
         })
     .done(function(data) {
       console.log(data.cipher);
      $('#autokey-table').show();
       $('#autokey-output').text(data.cipher).show();
   });
   event.preventDefault();
   });


   $('#vigenere-form').on('submit', function(event) {
    $('#vigenere-output').text("Encrypting your message...").show();
    // console.log($('#vigenere_plaintext').val(), $('#vigenere_keyword').val());
    $.ajax({
       data : {
          plaintext : $('#vigenere_plaintext').val(),
          key: $('#vigenere_keyword').val(),
              },
          type : 'POST',
          url : '/encrypt/vigenere/'
         })
     .done(function(data) {
       console.log(data.cipher);
      $('#vigenere-table').show();
       $('#vigenere-output').text(data.cipher).show();
   });
   event.preventDefault();
   });
   
   $('#playfair-form').on('submit', function(event) {
    $('#playfair-output').text("Encrypting your message...").show();
    $.ajax({
       data : {
          plaintext : $('#playfair_plaintext').val(),
          key: $('#playfair_keyword').val(),
              },
          type : 'POST',
          url : '/encrypt/playfair/'
         })
     .done(function(data) {
      $('#playfair-table').show();
      $('#playfair-message').text(data.msg);
      $('#playfair-keymatrix1').text(data.key_matrix[0]);
      $('#playfair-keymatrix2').text(data.key_matrix[1]);
      $('#playfair-keymatrix3').text(data.key_matrix[2]);
      $('#playfair-keymatrix4').text(data.key_matrix[3]);
      $('#playfair-keymatrix5').text(data.key_matrix[4]);
       $('#playfair-output').text(data.cipher).show();
   });
   event.preventDefault();
   });


   $('#keylesstrans-form').on('submit', function(event) {
    $('#keylesstrans-output').text("Encrypting your message...").show();
    $.ajax({
       data : {
          plaintext : $('#keylesstrans_plaintext').val(),
          block: $('#keylesstrans_block').val(),
              },
          type : 'POST',
          url : '/encrypt/keylesstrans/'
         })
     .done(function(data) {
      $('#keylesstrans-table').show();
      $('#keylesstrans-message').text(data.msg);
       $('#keylesstrans-output').text(data.cipher).show();
   });
   event.preventDefault();
   });
   
   $('#coltrans-form').on('submit', function(event) {
       $('#coltrans-error').hide();
    $('#coltrans-output').text("Encrypting your message...").show();
    $.ajax({
       data : {
          plaintext : $('#coltrans_plaintext').val(),
          key: $('#coltrans_key').val(),
              },
          type : 'POST',
          url : '/encrypt/coltrans/'
         })
     .done(function(data) {
         if (data.code == 200){
      $('#coltrans-table').show();
      $('#coltrans-message').text(data.msg);
       $('#coltrans-output').text(data.cipher).show(); 
    }else{
        $('#coltrans-error').text(data.error).show();
        $('#coltrans-table').hide();
    }
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
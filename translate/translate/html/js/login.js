$(function(){
  $("#submit").on('click', function(){
  var params = {'email': $('#email').val(), 'password':$('#password').val()};
  var deferred = new $.Deferred();
   $.ajax({
       type: 'POST',
       url: 'login',
       data: params,
       dataType: 'json'
   }).done(function (result) {
          location.href = result.query;
   }).fail(function () {
      alert('failed!!!');
   }).always(function () {
       deferred.resolve();
   });
   return deferred;
  });
})

$(function(){
  $("#submit").on('click', function(){
      var params = {'japanese': $('#japanese').val(), 'english':$('#english').val()};
      var deferred = new $.Deferred();
      $.ajax({
           type: 'POST',
           url: 'register',
           data: params,
           dataType: 'json'
      }).done(function (result) {  //引数resultにdefault.pyからreturnされた値が入る
              alert(result);
      }).fail(function () {
          alert('failed!!!');
      }).always(function () {
           deferred.resolve();
      });
      return deferred;
  });
})
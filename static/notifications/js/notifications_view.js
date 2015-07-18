$(document).ready(function() {
  $('.panel-primary').on('click', function(e) {
    var notid = $(this).attr('data-notid');
    me = $(this);
    $.get('/notifications/read/', {notification_id: notid}, function(data) {
      me.find('#more_details').toggle();
      me.find('#less_details').toggle();
      me.find('.panel-body').toggle();
      me.find('.new').remove();
      $('#num_nots').html(data);
      me.removeClass('panel-primary');
      me.addClass('panel-default');
    });
    e.preventDefault();
  });

  $('.panel-default').on('click', function(e) {
    $(this).find('#more_details').toggle();
    $(this).find('#less_details').toggle();
    $(this).find('.panel-body').toggle();
    e.preventDefault();
  });
});

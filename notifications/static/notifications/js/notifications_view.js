$(document).ready(function() {
  $('.panel-body').hide();
  $('.panel-primary').on('click', function(e) {
    e.preventDefault();
    var notid = $(this).attr('data-notid');
    var me = $(this);
    $.get('/notifications/read/', {notification_id: notid}, function(data) {
      $('#num_nots').html(data);
      me.find('.new').remove();
      me.removeClass('panel-primary');
      me.addClass('panel-default');
    });
  });

  $('.panel').on('click', function(e) {
    e.preventDefault();
    $(this).find('.glyphicon-chevron-down').toggle();
    $(this).find('.glyphicon-chevron-right').toggle();
    $(this).find('.more_details').toggle();
    $(this).find('.less_details').toggle();
    $(this).find('.panel-body').toggle();
  });
});

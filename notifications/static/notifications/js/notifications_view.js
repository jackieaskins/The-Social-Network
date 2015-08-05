$(document).ready(function() {
  $('.panel-body').hide();

  $('.panel-primary').on('click', '.panel-heading', function() {
    var new_panel = $(this).parent();
    var notid = $(this).parent().attr('data-notid');
    $.get('/notifications/read/', {notification_id: notid}, function(data) {
      $('#num_nots').html(data);
      new_panel.find('.new').remove();
      new_panel.removeClass('panel-primary');
      new_panel.addClass('panel-default');
      new_panel.find('.glyphicon-chevron-down').toggle();
      new_panel.find('.glyphicon-chevron-right').toggle();
      new_panel.find('.more_details').toggle();
      new_panel.find('.less_details').toggle();
      new_panel.find('.panel-body').toggle();
    });
    return false;
  });

  $('.panel-default').on('click', '.panel-heading', function() {
    var panel = $(this).parent();
    panel.find('.glyphicon-chevron-down').toggle();
    panel.find('.glyphicon-chevron-right').toggle();
    panel.find('.more_details').toggle();
    panel.find('.less_details').toggle();
    panel.find('.panel-body').toggle();
    return false;
  });
});

$(document).ready(function() {
  $('.status_post').on('click', '#comment', function() {
    var comment_box = $(this).parent().find('#comment_box');
    comment_box.toggle();
  });
});

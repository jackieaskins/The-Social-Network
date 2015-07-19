$(document).ready(function() {
  $('.comment_box').hide();
  $('.status_post').on('click', '#comment', function(e) {
    e.preventDefault();
    var comment_box = $(this).parent().find('.comment_box');
    comment_box.toggle();
  });
});

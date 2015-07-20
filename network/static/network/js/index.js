$(document).ready(function() {
  $('.comment_box').hide();
  $('.status_post').on('click', '#comment', function(e) {
    e.preventDefault();
    var comment_box = $(this).parent().find('.comment_box');
    comment_box.toggle();
  });

  $('.new_post').on('keyup', remove_errors);
  $('.new_comment').on('keyup', remove_errors);

  $('.comment_box').on('submit', function(e) {
    e.preventDefault();
    me = $(this);
    $.ajax({
      type: me.attr('method'),
      url: me.attr('action'),
      data: me.serialize(),

      success: function(data) {
        var error_div = me.find('#div_id_text');
        if (data.indexOf('error_1_id_text') != -1) {
          error_div.addClass('has-error');
          if(error_div.find('.controls p').length === 0) {
            error_div.find('.controls').append(data);
          }
        } else {
          me.find('#new_comment').val('');
          me.parent().find('.post_comments').html(data);
          error_div.removeClass('has-error');
          error_div.find('.controls p').remove();
        }
      },

      error: function(data) {

        console.log('Uh oh!');
      }
    });
  });

  function remove_errors() {
    me = $(this);
    var error_div = me.closest('#div_id_text');
    error_div.removeClass('has-error');
    error_div.find('.controls p').remove();
  }
});

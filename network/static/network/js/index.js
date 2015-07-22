$(document).ready(function() {
  $('.comment_box').hide();

  $('.show_comment_box').on('click', function() {
    $(this).parent().find('.comment_box').toggle();
    return false;
  });

  $('#new_post').on('keyup', remove_errors);
  $('.new_comment').on('keyup', remove_errors);

  $('.like_post').on('submit', function() {
    var me = $(this);
    var button = me.find('button');
    var span = me.find('.glyphicon');
    $.ajax({
      type: me.attr('method'),
      url: me.attr('action'),
      data: me.serialize(),

      success: function(data) {
        me.parent().find('.post_likes').html(data);
        if(span.hasClass('glyphicon-thumbs-down')) {
          button.text('');
          button.prepend('<span class="glyphicon glyphicon-thumbs-up"></span> Like');
        } else {
          button.text('');
          button.prepend('<span class="glyphicon glyphicon-thumbs-down"></span> Unlike');
        }
      }
    });
    return false;
  });

  $('.like_comment').on('submit', function() {
    var me = $(this);
    var button = me.find('button');
    $.ajax({
      type: me.attr('method'),
      url: me.attr('action'),
      data: me.serialize(),

      success: function(data) {
        me.parent().find('.comment_likes').html(data);
        if(button.text().indexOf('Unlike') != -1) {
          console.log('WOOOO');
          button.text('Like');
        } else {
          button.text('Unlike');
        }
      }
    });
    return false;
  });

  $('.comment_box').on('submit', function() {
    var me = $(this);
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
          me.find('.new_comment').val('');
          me.parent().find('.post_comments').html(data);
          error_div.removeClass('has-error');
          error_div.find('.controls p').remove();
        }
      }
    });
    return false;
  });

  $('#post_box').on('submit', function() {
    var me = $(this);
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
          location.reload();
        }
      }
    });
    return false;
  });

  function remove_errors() {
    var me = $(this);
    var error_div = me.closest('#div_id_text');
    error_div.removeClass('has-error');
    error_div.find('.controls p').remove();
  }
});

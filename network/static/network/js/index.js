$(document).ready(function() {
  $('.comment_box').hide();

  // Show the comment form
  $('.show_comment_box').click(function() {
    $(this).parent().find('.comment_box').toggle();
    return false;
  });

  // Shorten posts
  $('.post_text').each(function(){
    var me = $(this);
    var max_length = 325;

    if(me.html().length > max_length) {
      var short_content = $(this).html().substr(0, max_length);
      var long_content = $(this).html().substr(max_length);

      me.html(short_content +
        '<a href="#" class="read_more"><br/>Read More</a>' +
        '<span class="more_text" style="display:none;">' + long_content + '</span>'
      );

      me.find('a.read_more').click(function() {
        $(this).hide();
        $(this).parents('.post_text').find('.more_text').toggle();
        return false;
      });
    }
  });
  $('.comment_text').each(function(){
    var me = $(this);
    var max_length = 125;

    if(me.html().length > max_length) {
      var short_content = $(this).html().substr(0, max_length);
      var long_content = $(this).html().substr(max_length);

      me.html(short_content +
        '<a href="#" class="read_more"><br/>Read More<br /></a>' +
        '<span class="more_text" style="display:none;">' + long_content + '</span>'
      );

      me.find('a.read_more').click(function() {
        $(this).hide();
        $(this).parents('.comment_text').find('.more_text').toggle();
        return false;
      });
    }
  });

  // Post and comment popover settings
  $('.post_popover').popover({
    placement: 'right',
    html: 'true',
    container: 'body',
    trigger: 'focus',
    title: '<button type="button" class="close"><span aria-hidden="true">&times;</span></button>' +
           '<h6>This post is liked by...</h6>',
    content: function() {
      return $(this).parent().find('.post_popover_content').html();
    }
  });
  $('.comment_popover').popover({
    placement: 'right',
    html: 'true',
    container: 'body',
    trigger: 'focus',
    title: '<button type="button" class="close"><span aria-hidden="true">&times;</span></button>' +
           '<h6>This comment is liked by...</h6>',
    content: function() {
      return $(this).parent().find('.comment_popover_content').html();
    }
  });

  // Post and comment like buttons
  $('.like_post').submit(function() {
    var me = $(this);
    var button = me.find('button');
    var span = me.find('.glyphicon');
    $.ajax({
      type: me.attr('method'),
      url: me.attr('action'),
      data: me.serialize(),

      success: function(data) {
        $('#post_likes_' + data).load(' #post_likes_' + data, function() {
          $(this).children().unwrap();
        });
        $('#post_popover_content_' + data).load(' #post_popover_content_' + data, function() {
          $(this).children().unwrap();
        });
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
  $('.like_comment').submit(function() {
    var me = $(this);
    var button = me.find('button');
    $.ajax({
      type: me.attr('method'),
      url: me.attr('action'),
      data: me.serialize(),

      success: function(data) {
        $('#comment_likes_' + data).load(' #comment_likes_' + data, function() {
          $(this).children().unwrap();
        });
        $('#comment_popover_content_' + data).load(' #comment_popover_content_' + data, function() {
          $(this).children().unwrap();
        });
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

  // Make comments and posts
  $('.comment_box').submit(function() {
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
  $('#post_box').submit(function() {
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

  // Remove any form errors when typing
  $('#new_post').keyup(remove_errors);
  $('.new_comment').keyup(remove_errors);

  function remove_errors() {
    var me = $(this);
    var error_div = me.closest('#div_id_text');
    error_div.removeClass('has-error');
    error_div.find('.controls p').remove();
  }
});

// General Page Validation

$(document).ready(function(){
$('#save_general').click(function(){

if ($("#app_name1").val() == '' ){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please enter App Name</p>');
$("#app_name1").addClass('val_error_highlight');
return false;
}
if ($("#app_id_portal").val() == '' ){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please enter App ID created by the system</p>');
$("#app_id_portal").addClass('val_error_highlight');
return false;
}
if ($("#ios_app_id").val() == '' ){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please enter the ID set in the Apple Dev account for the app</p>');
$("#ios_app_id").addClass('val_error_highlight');
return false;
}
if ($("#facebook_id").val() == '' ){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please enter the ID Facebook generates when you create an app in their system</p>');
$("#facebook_id").addClass('val_error_highlight');
return false;
}
if ($("#portal_app").val() == '' ){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please determine which Portal App is linked to the build</p>');
$("#portal_app").addClass('val_error_highlight');
return false;
}
if ($("#sharing:checked").length == 0){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please choose if you would like to have the sharing option enabled</p>');
$("#sharing_label").addClass('val_error_highlight');
$("#sharing_label2").addClass('val_error_highlight');
return false;
}
if ($("#share_text").val() == '' ){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please enter the tag line that will show when shared</p>');
$("#share_text").addClass('val_error_highlight');
return false;
}
if ($("#platform:checked").length == 0){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please select which platform you would like to publish on</p>');
$("#platform_label").addClass('val_error_highlight');
$("#platform_label2").addClass('val_error_highlight');
return false;
}
if ($("#registration:checked").length == 0){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please choose if you would like to register your app</p>');
$("#registration_label").addClass('val_error_highlight');
$("#registration_label2").addClass('val_error_highlight');
return false;
}
if ($("#multi_lang:checked").length == 0){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please choose if you would like your app to be multi lingual</p>');
$("#multi_label").addClass('val_error_highlight');
$("#multi_label2").addClass('val_error_highlight');
return false;
}
if ($("#preview_pages:checked").length == 0){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please choose if you would like to preview your pages</p>');
$("#preview_label").addClass('val_error_highlight');
$("#preview_label2").addClass('val_error_highlight');
return false;
}
if ($("#toc:checked").length == 0){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please choose if you would like to have a table of contents</p>');
$("#toc_label").addClass('val_error_highlight');
$("#toc_label2").addClass('val_error_highlight');
return false;
}
if ($("#advertising:checked").length == 0){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please choose if you want to support banner ads in your app</p>');
$("#advertising_label").addClass('val_error_highlight');
$("#advertising_label2").addClass('val_error_highlight');
$("#advertising_label3").addClass('val_error_highlight');
return false;
}
if ($("#color_themes_enable:checked").length == 0){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please choose if you would like to enable color themes</p>');
$("#color_themes_enable_label").addClass('val_error_highlight');
$("#color_themes_enable_label2").addClass('val_error_highlight');
return false;
}
if ($("#push_notification:checked").length == 0){
$('.validation_msg').slideDown().html('<h4>Error While Saving</h4><p id="error">Please choose if you would like to enable push notifications</p>');
$("#push_notification_label").addClass('val_error_highlight');
$("#push_notification_label2").addClass('val_error_highlight');
return false;
}


else{
    $('.validation_msg').slideDown().html('<h4 class="val_success">Save Successfull</h4><p id="error">Your information was successfully saved</p>');
return true;
}
});
});

$( ".val_close" ).click(function() {
  $('.validation_container').addClass( "hidden" );
  setTimeout(function() {
      $("#app_name1").removeClass('val_error_highlight');
      $("#app_id_portal").removeClass('val_error_highlight');
      $("#sharing_label").removeClass('val_error_highlight');
      $("#sharing_label2").removeClass('val_error_highlight');
      $("#ios_app_id").removeClass('val_error_highlight');
      $("#facebook_id").removeClass('val_error_highlight');
      $("#portal_app").removeClass('val_error_highlight');
      $("#share_text").removeClass('val_error_highlight');
      $("#platform_label").removeClass('val_error_highlight');
      $("#platform_label2").removeClass('val_error_highlight');
      $("#registration_label").removeClass('val_error_highlight');
      $("#registration_label2").removeClass('val_error_highlight');
      $("#multi_label").removeClass('val_error_highlight');
      $("#multi_label2").removeClass('val_error_highlight');
      $("#preview_label").removeClass('val_error_highlight');
      $("#preview_label2").removeClass('val_error_highlight');
      $("#toc_label").removeClass('val_error_highlight');
      $("#toc_label2").removeClass('val_error_highlight');
      $("#advertising_label").removeClass('val_error_highlight');
      $("#advertising_label2").removeClass('val_error_highlight');
      $("#advertising_label3").removeClass('val_error_highlight');
      $("#color_themes_enable_label").removeClass('val_error_highlight');
      $("#color_themes_enable_label2").removeClass('val_error_highlight');
      $("#push_notification_label").removeClass('val_error_highlight');
      $("#push_notification_label2").removeClass('val_error_highlight');
}, 2000);
});


function save_success() {
    $('.validation_container').removeClass( "hidden" );
};

$('.text-input').blur(function()
{
      if( !this.value == '' ) {
            $(this).addClass('input-sel');
      }
      else{
        $(this).removeClass('input-sel');
      }
});

$(function() {
    var $radioButtons = $('input[type="radio"]');
    $radioButtons.click(function() {
        $radioButtons.each(function() {
            $(this).parent().toggleClass('input-sel', this.checked);
        });
    });
});

$(function() {
    var $radioButtons = $('input[type="checkbox"]');
    $radioButtons.click(function() {
        $radioButtons.each(function() {
            $(this).parent().toggleClass('input-sel', this.checked);
        });
    });
});

$('.test-build-history').click(function() {
    $('.test-build-history-container').toggleClass( "hidden" );
    $('.test-build-history').toggleClass( "input-sel" );
    if($('.test-build-history-container').hasClass('hidden')) {
        $('.test-build-history').text('See Build History');
    }
    else{
        $('.test-build-history').text('Hide Build History');
    }
});

$('.submit-build-history').click(function() {
    $('.submit-build-history-container').toggleClass( "hidden" );
    $('.submit-build-history').toggleClass( "input-sel" );
    if($('.submit-build-history-container').hasClass('hidden')) {
        $('.submit-build-history').text('See Build History');
    }
    else{
        $('.submit-build-history').text('Hide Build History');
    }
});

$( ".col-box1" ).click(function() {
  $( ".col-box1" ).empty();
});

$( ".col-box2" ).click(function() {
  $( ".col-box2" ).empty();
});

$( ".col-box3" ).click(function() {
  $( ".col-box3" ).empty();
});

$( ".col-box4" ).click(function() {
  $( ".col-box4" ).empty();
});

$( ".col-box5" ).click(function() {
  $( ".col-box5" ).empty();
});

$( ".col-box6" ).click(function() {
  $( ".col-box6" ).empty();
});





$(document).ready(function() {
    if($('#general-ios').hasClass('active')) {
        $( '#general-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#general-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
}
if($('#general-android').hasClass('active')) {
        $( '#general-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#general-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
}
$('#general-android').click(function() {
        $( '#general-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#general-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
})
$('#general-ios').click(function() {
        $( '#general-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#general-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
})

});

$(document).ready(function() {
    if($('#publisher-info-ios').hasClass('active')) {
        $( '#publisher-info-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#publisher-info-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
}
if($('#publisher-info-android').hasClass('active')) {
        $( '#publisher-info-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#publisher-info-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
}
$('#publisher-info-android').click(function() {
        $( '#publisher-info-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#publisher-info-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
})
$('#publisher-info-ios').click(function() {
        $( '#publisher-info-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#publisher-info-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
})

});

$(document).ready(function() {
    if($('#design-ios').hasClass('active')) {
        $( '#design-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#design-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
}
if($('#design-android').hasClass('active')) {
        $( '#design-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#design-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
}
$('#design-android').click(function() {
        $( '#design-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#design-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
})
$('#design-ios').click(function() {
        $( '#design-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#design-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
})

});

$(document).ready(function() {
    if($('#platform-specifics-ios').hasClass('active')) {
        $( '#platform-specifics-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#platform-specifics-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
}
if($('#platform-specifics-android').hasClass('active')) {
        $( '#platform-specifics-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#platform-specifics-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
}
$('#platform-specifics-android').click(function() {
        $( '#platform-specifics-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#platform-specifics-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
})
$('#platform-specifics-ios').click(function() {
        $( '#platform-specifics-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#platform-specifics-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
})

});

$(document).ready(function() {
    if($('#build-app-ios').hasClass('active')) {
        $( '#build-app-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#build-app-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
}
if($('#build-app-android').hasClass('active')) {
        $( '#build-app-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#build-app-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
}
$('#build-app-android').click(function() {
        $( '#build-app-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#build-app-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
})
$('#build-app-ios').click(function() {
        $( '#build-app-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#build-app-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
})

});

$(document).ready(function() {
    if($('#store-general-ios').hasClass('active')) {
        $( '#store-general-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#store-general-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
}
if($('#store-general-android').hasClass('active')) {
        $( '#store-general-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#store-general-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
}
$('#store-general-android').click(function() {
        $( '#store-general-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#store-general-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
})
$('#store-general-ios').click(function() {
        $( '#store-general-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#store-general-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
})

});

$(document).ready(function() {
    if($('#store-artwork-ios').hasClass('active')) {
        $( '#store-artwork-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#store-artwork-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
}
if($('#store-artwork-android').hasClass('active')) {
        $( '#store-artwork-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#store-artwork-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
}
$('#store-artwork-android').click(function() {
        $( '#store-artwork-ios-icon' ).css( "background", "url('../img/ico_ios_inactive.png')" );
        $( '#store-artwork-android-icon' ).css( "background", "url('../img/ico_android_active.png')" );
})
$('#store-artwork-ios').click(function() {
        $( '#store-artwork-ios-icon' ).css( "background", "url('../img/ico_ios_active.png')" );
        $( '#store-artwork-android-icon' ).css( "background", "url('../img/ico_android_inactive.png')" );
})

});

$(document).ready(function() {
  $('[data-toggle=offcanvas]').click(function() {
    $('.row-offcanvas').toggleClass('active');
  });
});

function readURL(input) {
if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
        $('#multi-up1')
            .attr('src', e.target.result)
            .width(150)
            .height(200);
    };

    reader.readAsDataURL(input.files[0]);
}
}

function readURL2(input) {
if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
        $('#multi-up2')
            .attr('src', e.target.result)
            .width(150)
            .height(200);
    };

    reader.readAsDataURL(input.files[0]);
}
}

function readURL3(input) {
if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
        $('#multi-up3')
            .attr('src', e.target.result)
            .width(150)
            .height(200);
    };

    reader.readAsDataURL(input.files[0]);
}
}

function readURL4(input) {
if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
        $('#multi-up4')
            .attr('src', e.target.result)
            .width(150)
            .height(200);
    };

    reader.readAsDataURL(input.files[0]);
}
}

function readURL5(input) {
if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
        $('#multi-up5')
            .attr('src', e.target.result)
            .width(150)
            .height(200);
    };

    reader.readAsDataURL(input.files[0]);
}
}

function readURL6(input) {
if (input.files && input.files[0]) {
    var reader = new FileReader();

    reader.onload = function (e) {
        $('#multi-up6')
            .attr('src', e.target.result)
            .width(150)
            .height(200);
    };

    reader.readAsDataURL(input.files[0]);
}
}

$(document).ready(function() {
   $('.color-box').colpick({
        colorScheme:'light',
        layout:'rgbhex',
        color:'ff8800',
        onSubmit:function(hsb,hex,rgb,el) {
            $(el).css('background-color', '#'+hex);
            $(el).colpickHide();
        }
    })
});


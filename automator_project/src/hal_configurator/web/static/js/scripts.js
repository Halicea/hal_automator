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


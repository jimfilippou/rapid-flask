/*
    Name: Slider
    Plugin Url: https://github.com/umkka/carousel
    Author: Umkka 
    Author Url: http://umkka.net  
    Year: 2016
*/

jQuery.fn.rbtSlider = function(opt){
        return this.each(function() {
            var slider = $(this);
            if (opt.height) slider.css('height', opt.height);
            slider.find('.slItem').first().addClass('active');
            if (opt.dots) {
                var count = slider.find('.slItem').length;
                slider.append(
                    $('<div/>', {
                        class: 'slDots',
                        html: $('<div/>', {
                            class: 'slDotsSingle active'
                        })
                    })                                  
                );
                for (var i = 1; i < count; i++) {
                    slider.find('.slDotsSingle.active').clone().removeClass('active').appendTo($(this).find('.slDots'));    
                }
                slider.find('.slDotsSingle').on('click', function(){
                    curIndex = $(this).parents('.slDots').find('.active').removeClass('active').index() + 1;
                    index = $(this).addClass('active').index() + 1;
                    if (index != curIndex) {
                        if (index > curIndex) nav('next', index);
                        else nav('prev', index);
                    }
                });
            }
            if (opt.arrows) {
                slider.append(
                    $('<div/>', {
                        class: 'ctrlPrev',
                        html: '&lsaquo;'
                    }).on('click', function(){
                        nav('prev');
                    })
                ).append(
                    $('<div/>', {
                        class: 'ctrlNext',
                        html: '&rsaquo;'
                    }).on('click', function(){
                        nav('next');
                    })
                );
            }
            if (opt.auto) {
                var time = setInterval(function(){nav('next')}, opt.auto * 1000);
                slider.on('mouseover', function() {
                    clearInterval(time);
                }).on('mouseleave', function() {
                    time = setInterval(function(){nav('next')}, opt.auto * 1000);
                });
            }

            function nav(side, index) {
                if (index) {
                    nextItem = slider.find('.slItem').eq(index - 1);
                } else {
                    if (side == 'prev') {
                        if (slider.find('.slItem.active').prev().length) nextItem = slider.find('.slItem.active').prev();  
                        else nextItem = slider.find('.slItem').last();
                    } else {
                        if (slider.find('.slItem.active').next().length) nextItem = slider.find('.slItem.active').next();
                        else nextItem = slider.find('.slItem').first();
                    }    
                    slider.find('.slDots > .active').removeClass('active').parent().find('.slDotsSingle').eq(nextItem.index()).addClass('active');
                }
                nextItem.addClass(side + 'Item').delay(50).queue(function(){
                    slider.find('.slItems > .active').addClass(side).delay(700).queue(function(){
                        $(this).removeClass(side +' active').dequeue();
                    });

                    $(this).addClass(side).delay(700).queue(function(){
                        $(this).removeClass(side + ' ' + side + 'Item').addClass('active').clearQueue();
                    });

                    $(this).dequeue();
                });
            }
        });
    };

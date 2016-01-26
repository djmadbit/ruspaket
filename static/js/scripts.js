$(document).ready(function() { 
	$('.popup_shadow').hide(); //убираем тень 	
	timer();
	var page = $('input[name="page"]').val().match(/(?:\/)(.{1})(?:\/.*)$/i); //берем ссылку на страницу из поля input[name='page']
	if(page == 'a')	{
		var prefix = ''; //если страница /a/ то префикс не нужен
	} else {
		if(page != null)
			var prefix = '../a/'; //если /b/ или /c/ и т.д.
		else
			var prefix = 'a/'; //если целевая (в корне)
	}
	
	
	$('.button').click(function() {
		$('body').find('form:not(this)').children('label').removeClass('red'); //удаление всех сообщение об ошибке(валидатора)
		var page = $('input[name="page"]').val(); //берем ссылку на страницу из поля input[name='page']

		var url ='/create_order/'; //если /a/ или /b/

		var answer = checkForm($(this).parent().get(0)); //ответ от валидатора
		if(answer != false)
		{
			var $form = $(this).parent(),
				name =     $('input[name="name"]', $form).val(),
				phone =    $('input[name="phone"]', $form).val(),
				email =    $('input[name="email"]', $form).val(),
				ques =     $('textarea[name="ques"]', $form).val(),
				sbt =      $('input[type="button"]', $form).attr("name"),
				submit =   $('input[name='+sbt+']', $form).val(),
				type =   $('input[name="type"]', $form).val();
			var ref =      $('input[name="referer"]').val();
			var desc =      $('input[name="desc"]').val();
			var formname = $('input[name="formname"]',$form).val();
			$.ajax({
				type: "POST",
				url: url,
				dataType: "json",
				data: "type="+type+"&name="+name+"&phone="+phone+"&"+sbt+"="+submit+"&email="+email+"&ques="+ques+"&formname="+formname+"&desc="+desc+"&page="+page, //добавить параметр +"&имя"+имя_переменной
				success:function(response)
				{
					if(response.status=='success'){
						popup_out();
		            	popup('spasibo');
					}
					else alert('Что-то полшло не так, попробуйте еще раз...')
				}
			});
		}
	});
	
	var top = (window.outerHeight - 250 - 180) / 2 + 'px'; // (не обязательно)     центрируем блок "Спасибо за заявку" на целевой странице. 250 - сумма высоты header и footer, 180 - высота блока "Спасибо за заявку"
	$('.target').css('top', top);


	var Android = navigator.userAgent.search(/Android/i);
	var iPhone = navigator.userAgent.search(/iPhone/i);
	var iPad = navigator.userAgent.search(/iPad/i);
	if(Android != -1 || iPhone != -1 || iPad != -1) {
		$('html').css('width', window.innerWidth + 'px'); //фикс для мобильных телефонов
	} else {
		$(".scroll").each(function () { // анимация по скролу(используйте этот) достаточно добавить анимируемому блоку класс 'scroll' а css анимацию писать так: '.animated.класс_блока'
			var block = $(this);
			$(window).scroll(function() {
				var top = block.offset().top;
				var bottom = block.height()+top;
				top = top - $(window).height();
				var scroll_top = $(this).scrollTop();
				if ((scroll_top > top) && (scroll_top < bottom)) {
					if (!block.hasClass("animated")) {
						block.addClass("animated");
					}
				} else {
					block.removeClass("animated");
				}
			});
		});
		$('head').append('<link rel="stylesheet" href="/static/css/animation.css" />'); //подключение файла animation.css если не мобильник
	}

	//script dlya vibora tovara

	$(".product").click(function(){
	    var image = $(this).children().filter(".image").html();
	    var h3 = $(this).children().filter(".h3").html();
	    var description = $(this).children().filter(".description").html();
	    var price = $(this).children().filter(".price").html();


	    $(".show-product").children().filter(".image").html(image);
	    $(".show-product").children().filter(".h3").html(h3);
	    $(".show-product").children().filter(".description").html(description);
	    $(".show-product").children().filter(".price").html(price);
	});
	
});


jQuery(document).ready(function () {
    jQuery(function () {
        jQuery.mask.definitions["1"] = "[01234569]";
        jQuery("input[name=phone]").mask("+7 (199) 999-9999", {
            placeholder: " "
        });
    });
});

/*
	Masked Input plugin for jQuery
	Copyright (c) 2007-2013 Josh Bush (digitalbush.com)
	Licensed under the MIT license (http://digitalbush.com/projects/masked-input-plugin/#license)
	Version: 1.3.1
*/
(function(e){function t(){var e=document.createElement("input"),t="onpaste";return e.setAttribute(t,""),"function"==typeof e[t]?"paste":"input"}var n,a=t()+".mask",r=navigator.userAgent,i=/iphone/i.test(r),o=/android/i.test(r);e.mask={definitions:{9:"[0-9]",a:"[A-Za-z]","*":"[A-Za-z0-9]"},dataName:"rawMaskFn",placeholder:"_"},e.fn.extend({caret:function(e,t){var n;if(0!==this.length&&!this.is(":hidden"))return"number"==typeof e?(t="number"==typeof t?t:e,this.each(function(){this.setSelectionRange?this.setSelectionRange(e,t):this.createTextRange&&(n=this.createTextRange(),n.collapse(!0),n.moveEnd("character",t),n.moveStart("character",e),n.select())})):(this[0].setSelectionRange?(e=this[0].selectionStart,t=this[0].selectionEnd):document.selection&&document.selection.createRange&&(n=document.selection.createRange(),e=0-n.duplicate().moveStart("character",-1e5),t=e+n.text.length),{begin:e,end:t})},unmask:function(){return this.trigger("unmask")},mask:function(t,r){var c,l,s,u,f,h;return!t&&this.length>0?(c=e(this[0]),c.data(e.mask.dataName)()):(r=e.extend({placeholder:e.mask.placeholder,completed:null},r),l=e.mask.definitions,s=[],u=h=t.length,f=null,e.each(t.split(""),function(e,t){"?"==t?(h--,u=e):l[t]?(s.push(RegExp(l[t])),null===f&&(f=s.length-1)):s.push(null)}),this.trigger("unmask").each(function(){function c(e){for(;h>++e&&!s[e];);return e}function d(e){for(;--e>=0&&!s[e];);return e}function m(e,t){var n,a;if(!(0>e)){for(n=e,a=c(t);h>n;n++)if(s[n]){if(!(h>a&&s[n].test(R[a])))break;R[n]=R[a],R[a]=r.placeholder,a=c(a)}b(),x.caret(Math.max(f,e))}}function p(e){var t,n,a,i;for(t=e,n=r.placeholder;h>t;t++)if(s[t]){if(a=c(t),i=R[t],R[t]=n,!(h>a&&s[a].test(i)))break;n=i}}function g(e){var t,n,a,r=e.which;8===r||46===r||i&&127===r?(t=x.caret(),n=t.begin,a=t.end,0===a-n&&(n=46!==r?d(n):a=c(n-1),a=46===r?c(a):a),k(n,a),m(n,a-1),e.preventDefault()):27==r&&(x.val(S),x.caret(0,y()),e.preventDefault())}function v(t){var n,a,i,l=t.which,u=x.caret();t.ctrlKey||t.altKey||t.metaKey||32>l||l&&(0!==u.end-u.begin&&(k(u.begin,u.end),m(u.begin,u.end-1)),n=c(u.begin-1),h>n&&(a=String.fromCharCode(l),s[n].test(a)&&(p(n),R[n]=a,b(),i=c(n),o?setTimeout(e.proxy(e.fn.caret,x,i),0):x.caret(i),r.completed&&i>=h&&r.completed.call(x))),t.preventDefault())}function k(e,t){var n;for(n=e;t>n&&h>n;n++)s[n]&&(R[n]=r.placeholder)}function b(){x.val(R.join(""))}function y(e){var t,n,a=x.val(),i=-1;for(t=0,pos=0;h>t;t++)if(s[t]){for(R[t]=r.placeholder;pos++<a.length;)if(n=a.charAt(pos-1),s[t].test(n)){R[t]=n,i=t;break}if(pos>a.length)break}else R[t]===a.charAt(pos)&&t!==u&&(pos++,i=t);return e?b():u>i+1?(x.val(""),k(0,h)):(b(),x.val(x.val().substring(0,i+1))),u?t:f}var x=e(this),R=e.map(t.split(""),function(e){return"?"!=e?l[e]?r.placeholder:e:void 0}),S=x.val();x.data(e.mask.dataName,function(){return e.map(R,function(e,t){return s[t]&&e!=r.placeholder?e:null}).join("")}),x.attr("readonly")||x.one("unmask",function(){x.unbind(".mask").removeData(e.mask.dataName)}).bind("focus.mask",function(){clearTimeout(n);var e;S=x.val(),e=y(),n=setTimeout(function(){b(),e==t.length?x.caret(0,e):x.caret(e)},10)}).bind("blur.mask",function(){y(),x.val()!=S&&x.change()}).bind("keydown.mask",g).bind("keypress.mask",v).bind(a,function(){setTimeout(function(){var e=y(!0);x.caret(e),r.completed&&e==x.val().length&&r.completed.call(x)},0)}),y()}))}})})(jQuery);

$(window).resize(function(){
	var Mtop = -($('.activePopup').outerHeight() / 2) + 'px'; //центрируем всплывашки по вертикали (менять не нужно)
	var Mleft = -($('.activePopup').outerWidth() / 2) + 'px'; //центрируем всплывашки по горизонтали (менять не нужно)
	$('.activePopup').css({
		'margin-top' : Mtop,
		'margin-left' : Mleft,
		'left' : '50%',
		'top' : '50%'
 	});
	var targetTop = (window.outerHeight - 250 - 180) / 2 + 'px'; // (не обязательно)     центрируем блок "Спасибо за заявку" на целевой странице. 250 - сумма высоты header и footer, 180 - высота блока "Спасибо за заявку"
	$('.target').css('top', targetTop);
});

function timer() //в блоке таймера дописывайте содежрание блоков '00' !!!! тоесть <div class="day">00</div>
{
	var now = new Date();
	var newDate = new Date((now.getMonth()+1)+","+now.getDate()+","+now.getFullYear()+" 23:59:59");
	var totalRemains = (newDate.getTime()-now.getTime());
	if (totalRemains>1)
	{
		var Days = (parseInt(parseInt(totalRemains/1000)/(24*3600)));
		var Hours = (parseInt((parseInt(totalRemains/1000) - Days*24*3600)/3600));
		var Min = (parseInt(parseInt((parseInt(totalRemains/1000) - Days*24*3600) - Hours*3600)/60));
		var Sec = parseInt((parseInt(totalRemains/1000) - Days*24*3600) - Hours*3600) - Min*60;
		if (Sec<10){Sec="0"+Sec}
		if (Min<10){Min="0"+Min}
		if (Hours<10){Hours="0"+Hours}
		if (Days<10){Days="0"+Days}
		$(".day").each(function() { $(this).text(Days); });
		$(".hour").each(function() { $(this).text(Hours); });
		$(".min").each(function() { $(this).text(Min); });
		$(".sec").each(function() { $(this).text(Sec); });
		setTimeout(timer, 1000);
	}
}
function popup(id, form)
{
	$('.popup_shadow').show(); //показываем тень
	$('#'+id).addClass('activePopup'); //добавляем текущей всплывашке класс 'activePopup'
	var Mtop = -($('.activePopup').outerHeight() / 2) + 'px'; //центрируем всплывашки по вертикали (менять не нужно)
	var Mleft = -($('.activePopup').outerWidth() / 2) + 'px'; //центрируем всплывашки по горизонтали (менять не нужно)
	$('.activePopup').css({
		'margin-top' : Mtop,
		'margin-left' : Mleft,
		'left' : '50%',
		'top' : '50%'
 	});
	$('.activePopup').show(); //показываем всплывашку
	$('.formname').attr("value", form); //передаём название
}

function popup_two(id, form)
{
	$('.popup_shadow').show(); //показываем тень
	$('#'+id).addClass('activePopup'); //добавляем текущей всплывашке класс 'activePopup'
	var Mtop = -($('.activePopup').outerHeight() / 2) + 'px'; //центрируем всплывашки по вертикали (менять не нужно)
	var Mleft = -($('.activePopup').outerWidth() / 2) + 'px'; //центрируем всплывашки по горизонтали (менять не нужно)
	$('.activePopup').css({
		'margin-top' : Mtop,
		'margin-left' : Mleft,
		'left' : '50%',
		'top' : '50%'
 	});
	$('.activePopup').show(); //показываем всплывашку
	$('.formname').attr("value", form); //передаём название
}

function popup_out()
{
	$('.popup_shadow').hide(); //убираем тень
	$('.popup').hide(); //убираем всплывашку
	$('.popup').removeClass('activePopup'); //убираем у неё класс 'activePopup'
}
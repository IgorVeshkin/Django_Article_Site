var navbar_btn = document.querySelector(".mobile-nav-btn");
var side_panel = document.querySelector(".sidepanel-on-mobiles");
var navbar_exit_btn = document.querySelector(".mobile-sidebar-exit-btn");
var side_panel_sublayer = document.querySelector(".left-sidebar-for-mobiles");
var header = document.querySelector('.header');
var content_box = document.querySelector('.article_content');

var navbar_btn_pressed = false;
var current_timer = 0
var refreshIntervalId = '';

//var screen_size = document.querySelector('.screen-size');
//
//window.onresize = function() {
//    var width = window.innerWidth
//        || document.documentElement.clientWidth
//        || document.body.clientWidth;
//
//    screen_size.innerHTML = width;
//};


if(document.querySelector(".error-msg-box") != null) {

    var msg_box_error = document.querySelector('.error-msg-box');
    var msg_box_error_exit_btn = document.querySelector('.msg-exit-btn');

    msg_box_error_exit_btn.onclick = function() {
        msg_box_error.parentNode.removeChild(msg_box_error);
        //    msg_box_error.style.display = 'None';
}

}


//setInterval(timer, 50);

function timer() {
    current_timer += 0.05;

    if (current_timer>=0.25) {
        current_timer=0;

//        side_panel.style.position = "absolute";
////	    side_panel.style.display = "flex";
//        side_panel_sublayer.style.position = "sticky";
//	    side_panel_sublayer.style.left = "0px";
//	    side_panel_sublayer.style.right = "0px";
//	    side_panel.style.top = "70px";
//	    side_panel_sublayer.style.top = "70px";
//	    side_panel_sublayer.style.bottom = "0px";
//	    side_panel_sublayer.style.width = "270px";
//	    side_panel.style.width = "270px";
	    clearInterval(refreshIntervalId);


    }

}

navbar_btn.onclick = function () {
	if (navbar_btn_pressed == false) {
	    navbar_btn_pressed = true;
//	    refreshIntervalId = setInterval(timer, 50);
//	    side_panel.style.position = "absolute";
//	    side_panel.style.display = "flex";
//	    side_panel.style.display = "flex";
//        side_panel_sublayer.style.position = "sticky";

        side_panel.style.width = "270px";

        var body = document.body,
        html = document.documentElement;

        html.style.overflowY = 'hidden';


        side_panel.style.position = "absolute";
	    side_panel.style.marginLeft = "0px";

        var header = document.querySelector(".header");

//        alert(header.offsetTop);

        side_panel.style.top = `${header.offsetTop+70}px`;

        var win_h = document.body.scrollHeight;
        side_panel.style.minHeight = `${win_h-header.offsetTop-70}px`;

        refreshIntervalId = setInterval(timer, 50);

//        setTimeout(100 in ms );





//        console.log(header_rect.top, header_rect.right, header_rect.bottom, header_rect.left);

//        pos = findPos(header);
//        top = pos[1];
//        left = pos[0];
//        window.alert(top);

//	    side_panel_sublayer.style.left = "0px";
//	    side_panel_sublayer.style.right = "0px";
////	    side_panel_sublayer.style.top = "70px";
//	    side_panel_sublayer.style.bottom = "0px";
//	    side_panel_sublayer.style.width = "270px";


//        var window_height = Math.max(body.scrollHeight, body.offsetHeight, html.clientHeight, html.scrollHeight, html.offsetHeight);

//	    var header = document.querySelector(".header");
//        pos = findPos(header);
//        top = pos[1];
//        left = pos[0];

//        side_panel_sublayer.style.top = `${top}px`;


	}

}


navbar_exit_btn.onclick = function () {
	if (navbar_btn_pressed == true) {
	    navbar_btn_pressed = false;
	    side_panel.style.position = "absolute";
//	    side_panel.style.display = "flex";
	    side_panel.style.marginLeft = "-275px";

	    var body = document.body,
        html = document.documentElement;

        html.style.overflowY = 'scroll';
//        side_panel.style.filter = "blur(0)";
//        header.style.filter = "blur(0)";

	}

}

var TransitionIntervalId = "";

function transition_switcher() {
    side_panel.style.transitionDuration = "0.25s";
    clearInterval(TransitionIntervalId);
}

window.addEventListener("resize", hide_left_sidebar_for_mobiles);

function hide_left_sidebar_for_mobiles(){
    var width = window.innerWidth
	|| document.documentElement.clientWidth
	|| document.body.clientWidth;

	if (width >= 800) {
	    navbar_btn_pressed = false;
	    side_panel.style.position = "absolute";
	    side_panel.style.transitionDuration = "0s";
//	    side_panel.style.transition = "all 0s forwards";
	    side_panel.style.marginLeft = "-275px";
	    TransitionIntervalId = setInterval(transition_switcher, 250);

	    var body = document.body,
        html = document.documentElement;

        html.style.overflowY = 'scroll';
//	    side_panel.style.transitionDuration = "0.25s";
//	    side_panel.style.transition = "margin-left 0.25s linear";
//	    alert(width);

	}


};
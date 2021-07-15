
//REMOVE ON USE ---------------
window.onbeforeunload = function () {
	var scrollPos;
	if (typeof window.pageYOffset != 'undefined') {
		scrollPos = window.pageYOffset;
	}
	else if (typeof document.compatMode != 'undefined' && document.compatMode != 'BackCompat') {
		scrollPos = document.documentElement.scrollTop;
	}
	else if (typeof document.body != 'undefined') {
		scrollPos = document.body.scrollTop;
	}
	document.cookie = "scrollTop=" + scrollPos;
}
window.onload = function () {
	if (document.cookie.match(/scrollTop=([^;]+)(;|$)/) != null) {
		var arr = document.cookie.match(/scrollTop=([^;]+)(;|$)/);
		document.documentElement.scrollTop = parseInt(arr[1]);
		document.body.scrollTop = parseInt(arr[1]);
	}
}
// -------------------------


const animText = $("#description");

function fallDownText(animElem){
	let text = animElem.text();
	let textLen = text.replaceAll(/ /ig, "").length;
	animElem = setupTextFall(animElem)
	const delay = 45;
	const elems = animElem.find("span");

	elems.each((index, elem) => {
		setTimeout(() => {
			$(elem).addClass("showText");
			if (index+1 >= textLen){
				setTimeout(() => {clearAnim(animElem, text)}, textLen*delay);
			}
		}, delay * index)
	});
}


function clearAnim(animElem, text){
	animElem.css({"visibility": "visible"});
	animElem.html(text);
}


function setupTextFall(animElem) {
	let nc = "";
	const text = animElem.text();

	for (let i = 0; i < text.length; i++){
		let str = text.substr(i, 1);

		if (str != " ") {
			nc += '<span>' + str + '</span>';
		} else {
			nc += " ";
		} 
	}

	animElem.html(nc);
	return animElem;
}

document.onr
setTimeout(() => {fallDownText(animText)}, 100);
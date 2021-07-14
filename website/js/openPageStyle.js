const animText = $("#description");

console.log(animText.text())

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


setTimeout(() => {fallDownText(animText)}, 100);
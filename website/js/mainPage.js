const container = $("#container");

if (getCookie("colorTheme") == "false"){
	container.toggleClass("dark");
	container.toggleClass("light");
    $("#setThemeCheckBox")[0].checked = false;
}

$("#setThemeCheckBox")[0].addEventListener('change', e => {
	container.toggleClass("dark");
	container.toggleClass("light");
	setCookie("colorTheme", e.target.checked.toString(), 365);
}, false);


function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}

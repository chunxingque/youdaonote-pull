var tmp_cookie = '这里把上图Cookie属性的值丢进来'

function getCookies() {
    var cookies = tmp_cookie.split(';');
    var result = [];
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        var parts = cookie.split('=');
        var name = parts[0];
        var value = parts[1];
        if (name === 'YNOTE_CSTK' || name === 'YNOTE_LOGIN' || name === 'YNOTE_SESS') {
            result.push([name, value, '.note.youdao.com', '/']);
        }
    }
    return result;
}

function formatCookies(cookies) {
    return {
        cookies: cookies
    };
}

var cookies = getCookies();
var formattedCookies = formatCookies(cookies);
// 网站屏蔽了日志或者设置了console的日志级别，因此这里使用warn级别，可以正常打印
console.warn(JSON.stringify(formattedCookies, null, 2))

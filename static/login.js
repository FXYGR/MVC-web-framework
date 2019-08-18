var log = console.log.bind(console, new Date().toLocaleString())

var e = function (selector) {
    return document.querySelector(selector)
}

var messageResult = function (message) {
    var form = document.querySelector('#message-result')
    form.innerText = message
}

var checkUsername = function (username) {
    var first = username[0]
    var length = username.length
    var last = username[length - 1]
    var flag = true
    if (((length >= 2 && length <= 10)) && ((first >= 'a' && first <= 'z') || (first >= 'A' && first <= 'Z')) &&
        ((last >= 'a' && last <= 'z') || (last >= 'A' && last <= 'Z') || (last >= '0' && last <= '9'))){
        for (var i = 1; i < length - 1; i++) {
            var e = username[i]
            if (((e < 'a' && e > 'z') || (e < 'A' && e > 'Z')) && (e < '0' && e > '9') && e !== '_') {
                flag = false
                break
            }
        }
    }else {
        flag = false
    }
    if (flag === true) {
        return '检查合格'
    }else {
        return '用户名错误'
    }
}

var bindEvents = function () {
    var b = e('#username-button-login')
    b.addEventListener('click', function () {
        log('click')
        var input = e('#username-input-login')
        log(input)
        log(input.value)
        var username = input.value
        var message = checkUsername(username)
        log(message)
        messageResult(message)

        // ajax('POST', '/todo/ajax/add', data, function (json) {
        //     log('拿到ajax响应')
        //     var message = json.message
        //     alert(message)
        //     insertTodo(todoCell)
        // })
    })
}

var main = function () {
    bindEvents()
}

main()
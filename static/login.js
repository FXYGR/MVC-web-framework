var messageTemplate = function (message) {
    var form = e('#message-result')
    form.innerText = message
}

var bindEvents = function () {
    var b = e('#username-button-login')
    b.addEventListener('click', function () {
        log('click')
        var input = e('input')
        log(input)
        log(input.value)
        var username = input.value
        var data = {
            username: username,
        }
        log(data)

        ajax('POST', '/login/ajax/check_username', data, function (json) {
            log('拿到ajax响应')
            var message = json.message
            messageTemplate(message)
        })
    })
}

var main = function () {
    bindEvents()
}

main()
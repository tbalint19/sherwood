const Cookies = require('./cookies')

const createApiController = (controller) => {

  const URL = "/"
  const csrftoken = Cookies.get('csrftoken')

  const JSONtransfer = (req) => {
    // req.method => "POST"
    // req.destination => "someurl"
    // req.data => {value: 8}
    // req.action => {type: "SOMETHING_HAPPENED", whatIWantToPass: "someData"}
    const request = new XMLHttpRequest()
    request.open(req.method, URL + req.destination, true)
    if (req.method == "POST") {
      request.setRequestHeader("X-CSRFToken", csrftoken)
      request.setRequestHeader("Content-Type", "application/json;charset=UTF-8")
    }
    request.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        let action = req.action
        action.data = JSON.parse(this.responseText)
        controller.dispatch(action)
      }
    }
    if (req.method == "POST") {
      request.send(JSON.stringify(req.data))
    }
    if (req.method == "GET") {
      request.send()
    }
  }

  return JSONtransfer

}

export default createApiController

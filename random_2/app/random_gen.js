const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
    var random_num = Math.floor(Math.random(0) * 50);
    var ret_json = JSON.parse('{"val":'+random_num+'}');
    res.send(ret_json);
})

app.listen(port, () => console.log(`listening on container port ${port}`))
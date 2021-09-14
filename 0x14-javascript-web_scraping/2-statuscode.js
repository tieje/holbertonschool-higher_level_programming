#!/usr/local/bin/node
// #!/usr/bin/node
// request status code
const rq = require('request');
rq(process.argv[2], (err, response, body) => {
  console.log('code:', response.statusCode);
  if (err) {
    console.log(err);
  }
});

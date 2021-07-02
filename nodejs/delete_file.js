var fs = require('fs');

fs.unlink('mynewfile6.txt', function(err){
	if (err) throw err;
	console.log('File deleted!');
});

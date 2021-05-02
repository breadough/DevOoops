var fs = require('fs');

fs.writeFile('mynewfile3.txt', 'Hello, this is write file and this replaces the content of an existing file', function(err){
	if(err) throw err;
	console.log('Saved!');
});

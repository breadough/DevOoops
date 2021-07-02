var fs = require('fs');

fs.appendFile('mynewfile.txt', 'Hello this is a new file from using filesystem', function(err){
	if(err) throw err;
	console.log('Saved!');
});

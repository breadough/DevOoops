var fs = require('fs');

fs.appendFile('mynewfile6.txt', 'This is another text from 2nd execution!', function(err){
	if (err) throw err;
	console.log('Updated');
});

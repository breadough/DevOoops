var fs = require('fs');

fs.writeFile('mynewfile6.txt', 'Contents should be gone!', function (err){
	if (err) throw err;
	console.log('File Updated');
});

var express = require('express');
var nodeMailer = require('nodemailer');
var bodyParser = require('body-parser');
var rl = require('readline');
var fs = require('fs')
var path = require('path')
var app = express();
var port = process.env.PORT || 3000;

app.use(express.static('public'));
app.use(bodyParser.urlencoded({extended: true}));
app.use(bodyParser.json());
app.set('view engine', 'ejs');

app.get('/', function (req, res) {
   res.render('dashboard', {page_name: 'dashboard'});
})

app.get('/request', function (req, res) {
   res.render('contact', {page_name: 'contact'});
})

app.get('/archive/:year', function(req,res) {
   year = req.params.year;
   directoryPath = path.join(__dirname, 'public', 'archive', year);

   fs.readdir(directoryPath, function (err, files) {
      var subfolders = []
      //handling error
      if (err) {
          return console.log('Unable to scan directory: ' + err);
      } 
      //listing all files using forEach
      files.forEach(function (file) {
          // Do whatever you want to do with the file
          subfolders.push({fullPath: path.join('archive', year, file),name:file}); 
      });

      return res.render('archive_year', {page_name: 'archive-' + year, subfolders: subfolders, year: year});
  });
})

app.get('/archive/:year/:subfolder', function(req,res) {
   year = req.params.year;
   subfolder = req.params.subfolder;
   directoryPath = path.join(__dirname, 'public', 'archive', year, subfolder);

   fs.readdir(directoryPath, function (err, files) {
      var images = []
      //handling error
      if (err) {
          return console.log('Unable to scan directory: ' + err);
      } 
      //listing all files using forEach
      files.forEach(function (file) {
         if(path.extname(file) == '.png') {
            imageObj = {
               fullPath: "",
               name: "",
               title: "",
               desc: "",
            }
            imageObj.fullPath = path.join('archive', year, subfolder, file);
            imageObj.name = file;

            var textFileName = file.slice(0, -4) + '.txt';

            if(fs.existsSync(path.join(directoryPath, textFileName))) {
               var text = fs.readFileSync(path.join(directoryPath, textFileName));
               var textByLine = text.toString().split("\n")
               imageObj.title = textByLine[0];
               imageObj.desc = textByLine[1];
            }

            images.push(imageObj);
         }
      });

      return res.render('archive_subfolder', {page_name: 'archive-' + year, plots:images, year: year});
  });
})

app.post('/send-email', function (req, res) {
   let transporter = nodeMailer.createTransport({
       host: 'smtp.gmail.com',
       port: 465,
       secure: true,
       auth: {
           // should be replaced with real sender's account
           user: 'educationanalytica@gmail.com',
           pass: 'analyticaeducationsuperparola2029'
       }
   });

   if(isBlank(req.body.email) || isBlank(req.body.fname) || isBlank(req.body.lname) || isBlank(req.body.requestDetails)) {
      res.status(500).send({error: 'Please provide all required details!'}); 
      return;
   }

   let message = "<p>E-mail: " + req.body.email + "</p><br>"
   message += "<p>Name:" + req.body.fname + " " + req.body.lname + "</p><br>"
   message += "<p>Request:" + req.body.requestDetails + "</p><br>"

   let mailOptions = {
       // should be replaced with real recipient's account
       to: 'codrutlemeni@gmail.com',
       subject: "Education Analytica Statistics Request",
       html: message
   };

   transporter.sendMail(mailOptions, (error, info) => {
       if (error) {
           return console.log(error);
       }
       console.log('Message %s sent: %s', info.messageId, info.response);
   });

   res.status(200).send({msg: 'Success! Request has been sent.'});
 });

app.listen(port, function () {
   console.log("Example app listening on %s", port)
})

function isBlank(str) {
   return (!str || /^\s*$/.test(str));
}
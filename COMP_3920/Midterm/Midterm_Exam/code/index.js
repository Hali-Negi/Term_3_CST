const express = require('express');

const port = process.env.PORT || 3005;

const app = express();

app.set("view engine", "ejs");

app.use(express.urlencoded({extended: false}));


app.get('/', (req,res) => {
    res.render("home");
});

app.get('/surveyStart', (req,res) => {
	var missingFields = req.param.invalid;
	if (missingFields) {
		res.render("survey", {missingFields: 1});
	}
	else {
    	res.render("survey");
	}
});

app.post('/submitSurvey', (req,res) => {
	var phoneType = req.body.phoneType; 
	var email = req.body.email;


	if (!email || !phoneType) {
		res.redirect("/surveyStart?invalid=1");
		return;	
	}

	var phoneStats = {
		iphone: 57,
		android: 43
	};  //stats according to statista.com for Canada 2022 (https://www.statista.com/statistics/1190552/smartphone-market-share-canada/)

	var percent = 0;
	if (phoneType === "iphone") {
		percent = phoneStats.iphone;

	} else if (phoneType === "android") {
		percent = phoneStats.android;
	}

	res.render("surveyResults", {percent: percent, usersPhoneType: phoneType});
});


app.listen(port, () => {
	console.log("Node application listening on port "+port);
}); 
# Deploy4CustomApp
This custom app will be able to take in two parameters. The two parameters are Budget and Spend amount. The two parameters will be taken and it will calculate how much of the budget is left with Budget - Spend which are then fed into the Left variable. which will feed the input variables and the calculation result into a database. 

Ex Try: 

Windows: curl -X POST http://127.0.0.1:5000/SubBudge/new -d "{\"Budget\": \"2000\", \"Spent\": \"900\"}" -H 'Content-Type: application/json'


Mac: curl -X POST http://127.0.0.1:5000/SubBudge/new -d '{"Budget": "2000", "Spent": "900"}' -H 'Content-Type: application/json'

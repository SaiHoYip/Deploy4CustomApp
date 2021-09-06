# Deploy4CustomApp
This custom app will be able to take in two parameters. The two parameters are Budget and Spend amount. The two parameters will be taken and it will calculate how much of the budget is left with Budget - Spend which are then fed into the Left variable. which will feed the input variables and the calculation result into a database. 

Ex Try: 

Windows: curl -X POST http://127.0.0.1:5000/SubBudge/new -d "{\"Budget\": \"2000\", \"Spent\": \"900\"}" -H 'Content-Type: application/json'


Mac: curl -X POST http://127.0.0.1:5000/SubBudge/new -d '{"Budget": "2000", "Spent": "900"}' -H 'Content-Type: application/json'

Why I chose to do this:
  I chose to create a table that can take two values and do a simple subtraction simply because I wanted to see what I could do with what was given in the todo app. Doing so helped me to understand the application better and how I can get the front and backend to communicate with each other. The issue I ran into while approaching this app was that I was more of a backend person so I had to do some research on the frontend. 
  My application works by having the frontend act as a user interface while the backend acts as the logic. The frontend simply gets the needed data from the user and then once the submit button is hit the backend does the rest of the work. The backend will take the data supplied by the user in the frontend and make a calculation based on the two parameters then adjust the table and finally commits the changes.

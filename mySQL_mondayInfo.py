apikey = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE0MDk5OTY1OCwidWlkIjoyNzA5ODg5NiwiaWFkIjoiMjAyMi0wMS0xNVQxMTo0Nzo1MS4wMDBaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTA0MTgyNzYsInJnbiI6InVzZTEifQ.ae7AhCWsdxZ7Kseh3EYxzrd3e6u0HM6nmDDM1Gr3GWs"
apiUrl = "https://api.monday.com/v2"
headers = {"Authorization": apikey}
query = 'query {  boards(ids:1921968816)   {     items    { id      name       subitems       {         name        }       column_values(ids:[person,status,_____________,_____,__________])       {         text         title        value              }     }  } }'
data = {'query': query}

const express = require('express')
const app = express()
const cors = require('cors')
fs = require('fs');
app.use(cors())


app.use("/accept", (req, res) => {


    try {

        fs.readFile('accepted.json', 'utf8', (err, data) => {
            if (err) {
              console.error(err);
              return;
            }
            // console.log(data)
          res.send(data)
        
            // console.log(data);
          });
        
    } catch (error) {
        console.log(error)
    }
 
  
})



app.use("/denied", (req, res) => {

    
    try {

        fs.readFile('denied.json', 'utf8', (err, data) => {
            if (err) {
              console.error(err);
              return;
            }
            // console.log(data)
          res.send(data)
        
            // console.log(data);
          });
        
    } catch (error) {
        console.log(error)
    }
 
  
})





app.listen(888, () => {
    console.log("Server is running on port 888")
})
import './style.css';
const fs = require('fs')

function data_reader(){
  readFile('./message.txt', 'utf8', (err, jsonString) => {
      if (err) {
          console.log("File read failed:", err)
          return
      }
      console.log('File data:', jsonString)
  })
}
data_reader()


from flask import Flask, jsonify
app = Flask(__name__)



index = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <script src="https://www.gstatic.com/firebasejs/8.4.1/firebase-app.js"></script>
        <script src="https://www.gstatic.com/firebasejs/8.4.1/firebase-database.js"></script>
        <script src = "https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>



</head>
<body>

<style>
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'poppins', sans-serif;
    }

.container{

display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
width: 100%;
height: 100vh;
background: #2c3e50;

}

.bluecntainer{
    background: #004b96;
}
.greencntainer{
    background: #1d8800;
}


.btn{
    background: #797979;
    color: #fff;
    border: 0;
    outline: none;
    width: 100px;
    cursor: pointer;

    padding: 15px;
    border-radius: 30px;
    font-weight: 600;
    font-size: 24px;
}

.btn-on{
    background: #00850b;
}
.btn-off{
    background: #99000d;
}

.rowcontainer{
    background: white;
    display: flex;
    justify-content: space-between;
    flex-direction: row;
    padding: 8px 8px;
    width: 90%;
    max-width: 600px;
    border-radius: 40px;
    margin:6px;
}
.right{
    direction: right;
}
.devicename{
    font-size: 24px;
    font-family: Arial, Helvetica, sans-serif;
    padding: 12px 12px;
    font-weight:800;
    color: black;
    display: flex;
    align-items: center;
    justify-content: center;
}

</style>

    <div class="container" id="container">
  <a href="/h"><button type="button" class="btn">Click</button></a>
        <div class="rowcontainer">
             <div class="devicename">Living Room</div>
             <button type="button" class="btn" id="btn1" ><div id="btntxt1">.....</div></button>
        </div>
        <div class="rowcontainer">
            <div class="devicename">Kitchen</div>
            <button type="button" class="btn" id="btn2" ><div id="btntxt2">.....</div></button>
       </div>
       <div class="rowcontainer">
        <div class="devicename">Bedroom</div>
        <button type="button" class="btn" id="btn3" ><div id="btntxt3">.....</div></button>
   </div>
   <div class="rowcontainer">
    <div class="devicename">Washroom</div>
    <button type="button" class="btn" id="btn4" ><div id="btntxt4">.....</div></button>
</div>
<div class="rowcontainer">
    <div class="devicename">Ceiling Fan</div>
    <button type="button" class="btn" id="btn5" ><div id="btntxt5">.....</div></button>
</div>
<div class="rowcontainer">
    <div class="devicename">Main Gate</div>
    <button type="button" class="btn" id="btn6" ><div id="btntxt6">.....</div></button>
</div>


    </div>

    <script>
const firebaseConfig = {
  apiKey: "AIzaSyApeQ-R7i4usSU2kFz8iVv8ExcGFzZ6EdY",
  authDomain: "cloudatcorsit.firebaseapp.com",
  databaseURL: "https://cloudatcorsit-default-rtdb.firebaseio.com",
  projectId: "cloudatcorsit",
  storageBucket: "cloudatcorsit.appspot.com",
  messagingSenderId: "80425947877",
  appId: "1:80425947877:web:d7909554c9f870c2c83a0c",
  measurementId: "G-MELN0TRVGT"
};


firebase.initializeApp(firebaseConfig);

let cont = document.getElementById("container");
var btntxt1 = document.getElementById("btntxt1");
var btn1 = document.getElementById("btn1");
var btntxt2 = document.getElementById("btntxt2");
var btn2 = document.getElementById("btn2");
var btntxt3 = document.getElementById("btntxt3");
var btn3 = document.getElementById("btn3");
var btntxt4 = document.getElementById("btntxt4");
var btn4 = document.getElementById("btn4");
var btntxt5 = document.getElementById("btntxt5");
var btn5 = document.getElementById("btn5");
var btntxt6 = document.getElementById("btntxt6");
var btn6 = document.getElementById("btn6");


  var stat1;
  var stat2;
  var stat3;
  var stat4;
  var stat5;
  var stat6;

$(document).ready(function(){


var database = firebase.database();


database.ref("/status").once("value", function(snap){
  stat1 = snap.val().button1;
  stat2 = snap.val().button2;
  stat3 = snap.val().button3;
  stat4 = snap.val().button4;
  stat5 = snap.val().button5;
  stat6 = snap.val().button6;

if(stat1==1){
  btntxt1.innerHTML= "ON";
  btn1.classList.add("btn-on");
  btn1.classList.remove("btn-off");
}
else if(stat1==0){
  btntxt1.innerHTML= "OFF";
  btn1.classList.remove("btn-on");
  btn1.classList.add("btn-off");
}

if(stat2==1){
  btntxt2.innerHTML= "ON";
  btn2.classList.add("btn-on");
  btn2.classList.remove("btn-off");
}
else if(stat2==0){
  btntxt2.innerHTML= "OFF";
  btn2.classList.remove("btn-on");
  btn2.classList.add("btn-off");
}

if(stat3==1){
  btntxt3.innerHTML= "ON";
  btn3.classList.add("btn-on");
  btn3.classList.remove("btn-off");
}
else if(stat3==0){
  btntxt3.innerHTML= "OFF";
  btn3.classList.remove("btn-on");
  btn3.classList.add("btn-off");
}

if(stat4==1){
  btntxt4.innerHTML= "ON";
  btn4.classList.add("btn-on");
  btn4.classList.remove("btn-off");
}
else if(stat4==0){
  btntxt4.innerHTML= "OFF";
  btn4.classList.remove("btn-on");
  btn4.classList.add("btn-off");
}

if(stat5==1){
  btntxt5.innerHTML= "ON";
  btn5.classList.add("btn-on");
  btn5.classList.remove("btn-off");
}
else if(stat5==0){
  btntxt5.innerHTML= "OFF";
  btn5.classList.remove("btn-on");
  btn5.classList.add("btn-off");
}

if(stat6==1){
  btntxt6.innerHTML= "ON";
  btn6.classList.add("btn-on");
  btn6.classList.remove("btn-off");
}
else if(stat6==0){
  btntxt6.innerHTML= "OFF";
  btn6.classList.remove("btn-on");
  btn6.classList.add("btn-off");
}

});



  $("#btn1").click(function(){

    var firebaseRef1 = firebase.database().ref().child("status/button1");


    if(stat1==0){
       firebaseRef1.set("1");
        console.log("ON");
        btntxt1.innerHTML= "ON";
  btn1.classList.add("btn-on");
  btn1.classList.remove("btn-off");
        stat1=1;
    }
    else if(stat1==1){
       firebaseRef1.set("0");
        console.log("OFF");
        btntxt1.innerHTML= "OFF";
  btn1.classList.remove("btn-on");
  btn1.classList.add("btn-off");
        stat1=0;
    }

    })



    $("#btn2").click(function(){

      var firebaseRef2 = firebase.database().ref().child("status/button2");
    if(stat2==0){
       firebaseRef2.set("1");
        console.log("ON");
        btntxt2.innerHTML= "ON";
  btn2.classList.add("btn-on");
  btn2.classList.remove("btn-off");
        stat2=1;
    }
    else if(stat2==1){
       firebaseRef2.set("0");
        console.log("OFF");
        btntxt2.innerHTML= "OFF";
  btn2.classList.remove("btn-on");
  btn2.classList.add("btn-off");
        stat2=0;
    }
      })

      $("#btn3").click(function(){

        var firebaseRef3 = firebase.database().ref().child("status/button3");
      if(stat3==0){
         firebaseRef3.set("1");
          console.log("ON");
          btntxt3.innerHTML= "ON";
    btn3.classList.add("btn-on");
    btn3.classList.remove("btn-off");
          stat3=1;
      }
      else if(stat3==1){
         firebaseRef3.set("0");
          console.log("OFF");
          btntxt3.innerHTML= "OFF";
    btn3.classList.remove("btn-on");
    btn3.classList.add("btn-off");
          stat3=0;
      }
        })

        $("#btn4").click(function(){

          var firebaseRef4 = firebase.database().ref().child("status/button4");
        if(stat4==0){
           firebaseRef4.set("1");
            console.log("ON");
            btntxt4.innerHTML= "ON";
      btn4.classList.add("btn-on");
      btn4.classList.remove("btn-off");
            stat4=1;
        }
        else if(stat4==1){
           firebaseRef4.set("0");
            console.log("OFF");
            btntxt4.innerHTML= "OFF";
      btn4.classList.remove("btn-on");
      btn4.classList.add("btn-off");
            stat4=0;
        }
          })


          $("#btn5").click(function(){

            var firebaseRef5 = firebase.database().ref().child("status/button5");
          if(stat5==0){
             firebaseRef5.set("1");
              console.log("ON");
              btntxt5.innerHTML= "ON";
        btn5.classList.add("btn-on");
        btn5.classList.remove("btn-off");
              stat5=1;
          }
          else if(stat5==1){
             firebaseRef5.set("0");
              console.log("OFF");
              btntxt5.innerHTML= "OFF";
        btn5.classList.remove("btn-on");
        btn5.classList.add("btn-off");
              stat5=0;
          }
            })


            $("#btn6").click(function(){

              var firebaseRef6 = firebase.database().ref().child("status/button6");
            if(stat6==0){
               firebaseRef6.set("1");
                console.log("ON");
                btntxt6.innerHTML= "ON";
          btn6.classList.add("btn-on");
          btn6.classList.remove("btn-off");
                stat6=1;
            }
            else if(stat6==1){
               firebaseRef6.set("0");
                console.log("OFF");
                btntxt6.innerHTML= "OFF";
          btn6.classList.remove("btn-on");
          btn6.classList.add("btn-off");
                stat6=0;
            }
              })

  });


</script>
</body>
</html>"""


@app.route('/')
def home():
  return index


@app.route("/h")
def hello_world():
  return "<hr><center><h1>Namaste INDIA</h1></center><hr>"

@app.route("/hh")
def hello_worldd():
  return "Hello, World! Hello, World!"


if __name__ ==  "__main__":
    app.run(debug=True)
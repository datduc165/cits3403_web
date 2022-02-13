const ban = document.querySelector(".banner");
const slider = document.querySelector(".slider");
const tl = new TimelineMax();

tl.fromTo(ban,1.5,{width:"0%"},{width:"100%"})
.fromTo(slider, 0.8, {opacity:0.0},{opacity:1},"-=0.5");

/*--FUNCTION--*/
function ChangeBGColor() {
    var x;
    x = document.getElementById("BGcolor").value;
    document.querySelector("body").style.backgroundColor = x;
  }

  function ResetBGColor() {
    document.querySelector("body").style.backgroundColor = "";
  }

/*--AJAX-- */

  function load(url, cFunction) {
    var xhttp;
    xhttp=new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        cFunction(this);
      }
    };
    xhttp.open("GET", url, true);
    xhttp.send();
  }
  function change(xhttp) {
    document.getElementById("ajax_text").innerHTML = xhttp.responseText;
  }
 
//Temitope Akinwale
/* This my content file for my chrome extension
   Here I connect my extension to my model via a 
   HTTP request. My content file connects to my
   API which reads the prediction from my model
   and will cover up any text detected as a spoiler
   Naviagate to webpage -> predict text on webpage -> if spoiler detected -> black out the spoiler
*/

//Name of my extension
console.log("Spoiler BeGONE");

var paragraphs = document.getElementsByTagName('p') //get elements by paragraph tags 

for (elt of paragraphs) {
	//getting the inner and outer elements of the HTML code
    let inner = elt.innerHTML;
    let outer = elt.outerHTML;
    
    //creating xml http request
    let xhttp = new XMLHttpRequest();
    let p = elt
    //changing the request when the function is ready 
    xhttp.onreadystatechange = function() {
    	//checking that the server response is okay
        if (this.readyState == 4 && this.status == 200) {
        	//if model classifies text as spoiler 
            if(this.responseText == "False"){
                console.log(p)
                p.style['background-color'] = '#000000'; //black out the spoiler
            }
        }
    };
    
    xhttp.open("POST", "http://localhost:5000/predict", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("prediction=" + inner);
}





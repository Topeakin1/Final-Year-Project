console.log("Spoiler BeGONE");

var paragraphs = document.getElementsByTagName('p')

for (elt of paragraphs) {
    let inner = elt.innerHTML;
    let outer = elt.outerHTML;
    
    let xhttp = new XMLHttpRequest();
    let p = elt
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            if(this.responseText == "True"){
                console.log(p)
                p.style['background-color'] = '#000000';
            }
        }
    };
    
    xhttp.open("POST", "http://localhost:5000/predict", true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send("prediction=" + inner);
}





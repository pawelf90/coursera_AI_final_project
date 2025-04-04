let RunSentimentAnalysis = ()=>{
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onload = function() {
        document.getElementById("result").innerHTML = this.responseText;
    }
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze"+"="+textToAnalyze, true);
    xhttp.send();
}

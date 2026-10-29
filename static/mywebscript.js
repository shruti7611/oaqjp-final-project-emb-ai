
function RunSentimentAnalysis() {
    const textToAnalyze =
        document.getElementById("textToAnalyze").value;

    const output = document.getElementById("system_response");

    if (!textToAnalyze.trim()) {
        output.innerText = "Please enter some text.";
        return;
    }

    const xhttp = new XMLHttpRequest();

    xhttp.onreadystatechange = function () {
        if (this.readyState === 4) {
            output.innerText = this.responseText;
        }
    };

    xhttp.open(
        "GET",
        "/emotionDetector?textToAnalyze=" +
            encodeURIComponent(textToAnalyze),
        true
    );

    xhttp.send();
}

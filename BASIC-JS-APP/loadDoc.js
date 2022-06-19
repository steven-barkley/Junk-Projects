

function loadDoc() 
{
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            document.getElementById("example").innerHTML = 
            this.responseText;
        }
        else
            document.getElementById("example").innerHTML = "You aren't connecting to the server!"
    };
    xhttp.open("GET", "ajax_info.txt", true);
    xhttp.send();
}
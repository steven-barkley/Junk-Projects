function PromptUser() {
    var txt;
    var name = window.prompt("Enter your name");
    if (name != null || name == "") 
        {
            txt = "Hello " +  name;
        }

    document.getElementById("name").innerHTML = txt;
}
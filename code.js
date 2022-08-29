function resize()
{
    let width = window.innerWidth;
    if (width < 780)
    {
        document.getElementById("indem").classList.replace("flex-column","flex-row");
        document.getElementById("indem").classList.replace("justify-content-center","justify-content-around");
    }
    else
    {
        document.getElementById("indem").classList.replace("flex-row","flex-column");
        document.getElementById("indem").classList.replace("justify-content-around","justify-content-center");
    }
}
var count1 = 0;
window.addEventListener("resize",resize);
window.addEventListener("load",resize);

setInterval(function(){

    if (count1 == 0)
    {
        document.getElementById("indextext").innerHTML = "I am a Photographer!";
        count1 = 1;
    }
    else if (count1 == 1)
    {
        document.getElementById("indextext").innerHTML = "I am a Gamer!";
        count1 = 2;
    }
    else
    {
        document.getElementById("indextext").innerHTML = "I am a Developer!"
        count1 = 0;
    }
}, 3000);



function localStorageSave(){
    localStorage.setItem("my-local-key", "my-local-item-saved on click!!!!");
}

function spam(){
    for (let i = 0; i < 10000000; i++) {
        console.log("I did it!");
      }
}

function timealert(){
    var today = new Date();
    var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();

    alert(time)
}

function changebgc(){
    document.body.style.background = "linear-gradient(to top left, #24C6DC, #514A9D)"
}
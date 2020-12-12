
var json_data;

async function getData() {
    const response = await fetch("data.json");
    const data = await response.json();
    console.log(data)
    json_data = data;

}

getData();


function buttonClick() {

    var input_token = document.getElementById("input-element").value;

    var name = json_data[input_token].name;
    var match = json_data[input_token].match;
    var wish = json_data[input_token].wish;
    var img = json_data[input_token].img;

    document.getElementById("text-name").style.visibility = 'visible';
    document.getElementById("name").textContent = name;

    document.getElementById("text-match").style.visibility = 'visible';
    document.getElementById("match").textContent = match;

    document.getElementById("text-wish").style.visibility = 'visible';
    document.getElementById("wish").textContent =  wish;

    document.getElementById("image-sec").src = img;


};

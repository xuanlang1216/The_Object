function load(){
        var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function(){
        if (this.readyState === 4 && this.status === 200){
            var mapParams = getMapParam1(this.response);
            Plotly.plot('linechart', mapParams.data, mapParams.layout);
        }
    };
    xhttp.open("GET", "/linechart");
    xhttp.send();
}

function getMapParam1(xd){
var finaldata = {};

var Year_2016 = {
  x: xd["year"],
  y: xd["Rape"],
  mode: 'lines+markers'
};

var Year_2017 = {
  x: xd["year"],
  y: xd["Assault"],
  mode: 'lines+markers'
};

var data = [ Year_2016, Year_2017];

var layout = {
  "title":'Rape and Assault Rate (2016 - 2018)'
};
finaldata["data"] = data;
finaldata["layout"] = layout;
return finaldata;
}

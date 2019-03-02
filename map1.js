function loadmap(){
Plotly.setPlotConfig({ mapboxAccessToken: 'pk.eyJ1IjoiZ3VvemhlbmciLCJhIjoiY2pucnhvczIyMGQ3cTNrcGFkOXdqaDExcSJ9.iPsaWDQ9zuKp7egNkCyrMQ' });
var xhttp = new XMLHttpRequest();
xhttp.onreadystatechange = function(){
if (this.readyState === 4 && this.status === 200){
var mapParams = getMapParams(this.response);
var Chart = chart(this.response);
Plotly.plot('map', mapParams.data, mapParams.layout);
Plotly.newPlot('chart', Chart);
}
};
xhttp.open("GET", "/ticket");
xhttp.send();
}
function chart(abc){
var jdata=JSON.parse(abc);
var x=[];
var y=[];
for(var i of jdata){
if(i.length===11)
x.push(i);

}
var Rape = {
x: ['2008', '2009', '2010','2011', '2012', '2013','2014', '2015', '2016', '2017', '2018'],
y: [0,x[0][0],x[0][1],x[0][2],x[0][4],x[0][5],x[0][6],x[0][7],x[0][8],x[0][9],x[0][10],x[0][11],15],
mode: 'lines',
name:'Rape'
};
var Assault = {
x: ['2008', '2009', '2010','2011', '2012', '2013','2014', '2015', '2016', '2017', '2018'],
y: [0,x[1][0],x[1][1],x[1][2],x[1][4],x[1][5],x[1][6],x[1][7],x[1][8],x[1][9],x[1][10],x[1][11],15],
mode: 'lines+markers',
name:'Assault'
};
var data = [Rape, Assault ];

return data;
}
function setupMapData(abc){
var lat=[];
var lon=[];
var text=[];
for (var i of abc){
lat.push(i[0]);
lon.push(i[1]);
text.push(i[2]);
}
var data = [{
type:'scattermapbox',
lat:lat,
lon:lon,
mode:'markers',
marker: {
size:5,
color:"rgb(255,0,0)"
},
text:text
}];
return data;
}

function findCenter(abc){
var lat=[];
var lon=[];
for (var i of abc){
lat.push(i[0]);
lon.push(i[1]);
} 
var maxLat=Math.max(...lat);
var minLat=Math.min(...lat);
var maxLon=Math.max(...lon);
var minLon=Math.min(...lon);
var centerlat=(maxLat + minLat)/2
var centerlon=(maxLon+minLon)/2
return ([centerlat, centerlon])
}
function setupMapLayout(abc){
var x=findCenter(abc);
var layout = {
mapbox: {
style:"satellite-streets",
center: {
lat:x[0],
lon:x[1]
},
zoom:11
},
};
return layout;
}
function getMapParams(abc){
var jdata=JSON.parse(abc);
var x=[];
var y=[];
for(var i of jdata){
if(i.length ===3)
x.push(i);
}
var data=setupMapData(x);
var layout=setupMapLayout(x);
var obj={
data,
layout
};
return obj;
}
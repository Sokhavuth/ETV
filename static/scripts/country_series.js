//static/scritps/country_series.js
class Country_series{
  load_items(url){
    $('#load-more img').attr('src', '/static/images/loading.gif');
    $.get(url, function(data, status){
      if(status === "success"){
        country_series.listing_series(data)
      }else{
        alert('Fail to connect to server.');
      }
    });
  }
  listing_series(data){
    var html = '';
    for(var v=0; v<data['series'].length; v++){
      html += '<div class="series-wrapper">';
      html += `<a href="/series/${ data['series'][v][0] }"><img src="${ data['thumbs'][v] }" /></a>`;
      html += `<a class="series-title" href="/series/${ data['series'][v][0] }">${ data['series'][v][2] }</a>`;
      html += `</div>`;
    }
  
    $('#country-series').append(html);
    $('#load-more img').attr('src', '/static/images/arrow.png')
  }
}//end class

const country_series = new Country_series();
//static/scritps/country.js
class Country{
  load_items(url){
    $('#load-more img').attr('src', '/static/images/loading.gif');
    $.get(url, function(data, status){
      if(status === "success"){
        country.listing_movies(data)
      }else{
        alert('Fail to connect to server.');
      }
    });
  }
  listing_movies(data){
    var html = '';
    for(var v=0; v<data['movies'].length; v++){
      html += '<div class="movie-wrapper">';
      html += `<a href="/movie/${ data['movies'][v][0] }"><img src="${ data['thumbs'][v] }" /></a>`;
      html += `<a class="movie-title" href="/movie/${ data['movies'][v][0] }">${ data['movies'][v][3] }</a>`;
      html += `</div>`;
    }
  
    $('#country-movies').append(html);
    $('#load-more img').attr('src', '/static/images/arrow.png')
  }
}//end class

const country = new Country();
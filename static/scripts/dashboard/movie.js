//static/scritps/dashboard/movie.js
class Movie{
  load_items(url){
    $('#load-more img').attr('src', '/static/images/loading.gif');
    $.get(url, function(data, status){
      if(status === "success"){
        movie.listing_movies(data)
      }else{
        alert('Fail to connect to server.');
      }
    });
  }
  listing_movies(data){
    var html = '';
    for(var v=0; v<data['movies'].length; v++){
      html += '<li class="movie">';
      html += `<a class="thumbnail" href="/movie/${ data['movies'][v][0] }"><img src="${data['thumbs'][v]}" /></a>`;
      html += `<div class='title'>`;
      html += `<a href="/movie/${ data['movies'][v][0] }">${ data['movies'][v][3] }</a>`;
      html += `<div>${ data['movies'][v][4] }</div>`
      html += `<span>${ data['movies'][v][6] }</span>`;
      html += `</div>`;
      html += `<div class="crud">`;
      html += `<div class="user">${ data['movies'][v][8] }</div>`;
      html += `<a href='/dashboard/movie/delete/${ data["movies"][v][0] }'><img src="/static/images/delete.png" /></a>`;
      html += `<a href='/dashboard/movie/edit/${ data["movies"][v][0] }'><img src="/static/images/edit.png" /></a>`;
      html += `</div>`;
      html += `</li>`;
    }
  
    $('#item-listing').append(html);
    $('#load-more img').attr('src', '/static/images/load-more.png')
  }
}//end class

const movie = new Movie();
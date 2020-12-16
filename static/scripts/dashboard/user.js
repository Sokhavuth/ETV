//static/scritps/dashboard/user.js
class User{
  load_items(url){
    $('#load-more img').attr('src', '/static/images/loading.gif');
    $.get(url, function(data, status){
      if(status === "success"){
        user.listing_users(data)
      }else{
        alert('Fail to connect to server.');
      }
    });
  }
  listing_users(data){
    var html = '';
    for(var v=0; v<data['users'].length; v++){
      html += '<li class="user">';
      html += `<a class="thumbnail" href="/user/${ data['users'][v][0] }"><img src="${data['thumbs'][v]}" /></a>`;
      html += `<div class='title'>`;
      html += `<a href="/user/${ data['users'][v][0] }">${ data['users'][v][1] }</a>`;
      html += `<div>${ data['users'][v][4] }</div>`
      html += `<span>${ data['users'][v][6] }</span>`;
      html += `</div>`;
      html += `<div class="crud">`;
      html += `<div class="user">${ data['users'][v][8] }</div>`;
      html += `<a href='/dashboard/user/delete/${ data["users"][v][0] }'><img src="/static/images/delete.png" /></a>`;
      html += `<a href='/dashboard/user/edit/${ data["users"][v][0] }'><img src="/static/images/edit.png" /></a>`;
      html += `</div>`;
      html += `</li>`;
    }
  
    $('#item-listing').append(html);
    $('#load-more img').attr('src', '/static/images/load-more.png')
  }
}//end class

const user = new User();
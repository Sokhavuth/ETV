//static/scritps/dashboard/series.js
class Series{
  constructor(){
    this.list = [];
    this.playlist = [];
  }

  generatePlaylist(){
    var vidType = $('#data-entry select option:selected').text();
    var vidId = $('#data-entry #vid-id').val();
    this.list.push({type:vidType, id:vidId});
    var length = this.list.length;
    var lastIndex = length - 1;
    if(this.pl){
      length += (this.pl).length;
    }
    var inputs = '<a>'+length+'</a><input class="vid-type" type="text" value="'+this.list[lastIndex].type+'" />';
    inputs += '<input class="vid-id" type="text" value="'+this.list[lastIndex].id+'" />';
    $('#data-header').append(inputs);
    $('#data-entry #vid-id').val('');
  }

  getPlaylist(){
    var vidTypes = $('#data-header').children('input.vid-type');
    var vidIds = $('#data-header').children('input.vid-id');
    var playlist = [];
    for(var i=0; i<vidTypes.length; i++){
      playlist.push({type:vidTypes[i].value, id:vidIds[i].value})
    }
    this.playlist = playlist;
    $('#playlist').val(JSON.stringify(this.playlist));
    alert('ទិន្នន័យ​ត្រូវ​បាន​បញ្ចូល​ទៅ​ក្នុង​ទំរង់​បែបបទ។')
  }

  setPlaylist(playlist){
    if(!this.pl){
      var pl = JSON.parse(playlist);
      this.pl = pl;
    }else{
      var pl = this.pl;
    }
    var inputs = '<div>ភាគ</div><div>ប្រភេទ​វីដេអូ</div><div>អត្តសញ្ញាណ​វីដេអូ</div>';
    for(var i=0; i<pl.length; i++){
      inputs += `<a title="Delete" onclick="series.delete(${i})">`+(i+1)+'</a><input class="vid-type" type="text" value="'+pl[i].type+'" />';
      inputs += '<input class="vid-id" type="text" value="'+pl[i].id+'" />';
    }
    $('#data-header').html(inputs);
  }

  delete(id){
    (this.pl).splice(id,1);
    this.setPlaylist();
  }

  load_items(url){
    $('#load-more img').attr('src', '/static/images/loading.gif');
    $.get(url, function(data, status){
      if(status === "success"){
        series.listing_series(data)
      }else{
        alert('Fail to connect to server.');
      }
    });
  }

  listing_series(data){
    var html = '';
    for(var v=0; v<data['series'].length; v++){
      html += '<li class="series">';
      html += `<a class="thumbnail" href="/series/${ data['series'][v][0] }"><img src="${data['thumbs'][v]}" /></a>`;
      html += `<div class='title'>`;
      html += `<a href="/series/${ data['series'][v][0] }">${ data['series'][v][2] }</a>`;
      html += `<div><a href="/series/country/${ data['series'][v][3] }">${ data['series'][v][3] }</a></div>`
      html += `<span>${ data['series'][v][5] }</span>`;
      html += `</div>`;
      html += `<div class="crud">`;
      html += `<div class="user">${ data['series'][v][7] }</div>`;
      html += `<a href='/dashboard/series/edit/${ data["series"][v][0] }'><img src="/static/images/edit.png" /></a>`;
      html += `<a href='/dashboard/series/delete/${ data["series"][v][0] }'><img src="/static/images/delete.png" /></a>`;
      html += `</div>`;
      html += `</li>`;
    }
  
    $('#item-listing').append(html);
    $('#load-more img').attr('src', '/static/images/load-more.png')
  }
}//end class

const series = new Series();
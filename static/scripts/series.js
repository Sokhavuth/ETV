//static/scripts/series.js
class Series{
  setVideo(playlist=[], episode=0){
    if(!this.pl){
      var pl = JSON.parse(playlist);
      this.pl = pl;
      var index = pl.length - 1;
    }else{
      var pl = this.pl;
      var index = episode - 1;
      var activeElement = document.getElementById(this.active);
      var clickedElement = document.getElementById(`episode${episode}`);
      activeElement.className = 'episode-outer';
      clickedElement.className += ' active';
      this.active = `episode${episode}`;
    }

    if(pl[index].type === "YouTube"){
      var src = "https://www.youtube.com/embed/" + pl[index].id;
    }else if(pl[index].type === "Facebook"){
      var src = `https://www.facebook.com/watch/?v=${pl[index].id}`;
    }else if(pl[index].type === "Dailymotion"){
      var src = "https://www.dailymotion.com/embed/video/" + pl[index].id;
    }else if(pl[index].type === "Vimeo"){
      var src = "https://player.vimeo.com/video/" + pl[index].id;
    }else if(pl[index].type === "OKRU"){
      var src = "//ok.ru/videoembed/" + pl[index].id;
    }else if(pl[index].type === "YouTubePl"){
      var src = "https://www.youtube.com/embed/videoseries?list=" + pl[index].id;
    }

    if(pl[index].type !== 'Facebook'){
      var iframe = `<div style='position:relative;padding-top:56.25%;margin-top:20px;'>
      <iframe id="series-player" src="${src}" frameborder="0" allowfullscreen></iframe>
      </div>`;
    }else{
      var iframe = `<div class="fb-video" data-href="${src}" data-width="auto" data-show-captions="true"></div>`;
    }

    $('#series-wrapper').html(iframe);
    FB.XFBML.parse();
  }

  setEpisodes(playlist, ending){
    var pl = JSON.parse(playlist);
    var html = '';

    for(var i=pl.length-1; i>-1; i--){
      if(i==pl.length-1)
        html += `<div class="episode-outer active" id="episode${i+1}">`;
      else
        html += `<div class="episode-outer" id="episode${i+1}">`;

      html += `<div class="thumb"><a onclick="series.setVideo(undefined, ${i+1})"><img src="/static/images/playlist.jpg" /></a></div>`;
      if((ending === 'ចប់​ហើយ') && (i === pl.length-1))
        html += `<div class="episode"><a>ភាគ​ទី ${i+1} ចប់</a></div>`;
      else
        html += `<div class="episode"><a>ភាគ​ទី ${i+1}</a></div>`;

      html += `</div>`;
    }
    $('#episodes').html(html);
    this.active = `episode${pl.length}`;
  }
}//End of class

const series = new Series();
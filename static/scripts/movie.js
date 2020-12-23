//static/scripts/movie.js
class Movie{
  setVideo(videoId, vidType){
    
    if(vidType === "YouTube"){
      var src = "https://www.youtube.com/embed/" + videoId;
    }else if(vidType === "Facebook"){
      var src = `https://www.facebook.com/watch/?v=${videoId}`;
    }else if(vidType === "Dailymotion"){
      var src = "https://www.dailymotion.com/embed/video/" + videoId;
    }else if(vidType === "Vimeo"){
      var src = "https://player.vimeo.com/video/" + videoId;
    }else if(vidType === "OKRU"){
      var src = "//ok.ru/videoembed/" + videoId;
    }else if(vidType === "YouTubePl"){
      var src = "https://www.youtube.com/embed/videoseries?list=" + videoId;
    }

    if(vidType !== 'Facebook'){
      var iframe = `<div style='position:relative;padding-top:56.25%;margin-top:20px;'>
      <iframe id="video-player" src="${src}" frameborder="0" allowfullscreen></iframe>
      </div>`;
    }else{
      var iframe = `<div class="fb-video" data-href="${src}" data-width="auto" data-show-captions="true"></div>`;
    }

    $('#video-wrapper').html(iframe);
  }
}//End of class

const movie = new Movie();



$( document ).ready(function() {
    var images = ['../images/0.gif', '../images/1.gif', '../images/2.gif', '../images/3.gif', '../images/4.gif'];

    $('body').css({'background-image': 'url(static/images/' + images[Math.floor(Math.random() *      images.length)] + ')'});

    console.log(images[Math.floor(Math.random() *  images.length)])
});

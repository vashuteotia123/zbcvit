
$('.notification_icon').click(function(){
    var x=$('.notification_wrap>ul');
    //if(x.css('display')=='none'){x.fadeIn("slow");x.css('display','block');}
    //else{ x.fadeOut("slow"); x.css('display','none');}
    //x.toggle();*/
    x.fadeToggle("slow","linear");
})
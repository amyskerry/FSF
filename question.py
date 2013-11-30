#!/usr/bin/python

import cgitb, cgi, MySQLdb, ast
#import cgitb, cgi, ast
import cPickle as p
from random import randint, shuffle
from ast import literal_eval
from slist import subjects, keycodes
from dim import dimensions, dimlabels, dimInstruct, dimQuest
import config as cf
myform=cgi.FieldStorage()
cgitb.enable()
cursor = MySQLdb.connect(host="localhost",user="askerry",passwd="password",db="aesbehave").cursor()
print 'Content-type:text/html\n\n'


#cgitb.enable(display=0, logdir="/path/to/logdir")
print '''
<style type="text/css">
    body {
        font-family:verdana,arial,helvetica,sans-serif;
        font-size:100%;
    }
</style>
'''
#testing
theids=myform.keys()
moviedir='http://mindhive.mit.edu/saxe/FSF/stimfiles_dark/'
subjid = myform['subjid'].value
dimlabel=subjid[-5:-3]
runnum=subjid[5]
cbid=subjid[6]
moviename=moviedir+'r'+runnum+cbid+'.mp4'
#tempmov='http://mindhive.mit.edu/saxe/FSF/temp.mp4'
#print "%s" %moviename
dimindex=dimlabels.index(dimlabel)
dim=dimensions[dimindex]
dimQ=dimQuest[dimindex]
qindex=myform['qindex'].value
formindex=myform['rownum'].value
formindex=str(formindex)
qindex=int(qindex)+1
qindex=str(qindex)
keycode=myform['keycode'].value

if int(qindex)==1:
        #print "your id is correct <br>"
        #print "<p>these are the ids: %s </p>" %(theids)
        #print "<p>qindex: %s </p>" %(qindex)
       	sql='update FSF_rating set dimension ="'+dimlabel+'" where rownum="'+formindex+'"'
	cursor.execute(sql)
       	sql='update FSF_rating set counterbalance ="'+cbid+'" where rownum="'+formindex+'"'
	cursor.execute(sql)
       	sql='update FSF_rating set run ="'+runnum+'" where rownum="'+formindex+'"'
	cursor.execute(sql)
else:
	#print "row: %s" % formindex
	lastrating=myform['ratingvector'].value
        lasttiming=myform['timevector'].value
        lastresponse=myform['response'].value
        lastratinglist=lastrating.split('!!')
        lasttiminglist=lasttiming.split('!!')
       	ratingvar='rating1'
	timingvar='timing1'
	sql='update FSF_rating set ' +timingvar +' ="'+lasttiming+'" where rownum="'+formindex+'"'
       	cursor.execute(sql)
	sql='update FSF_rating set ' +ratingvar +' ="'+lastrating+'" where rownum="'+formindex+'"'
       	cursor.execute(sql)
### css setup
print '''
<script>
decreasekey=%(down)s;
increasekey=%(up)s
</script>''' % {'up':cf.upkey, 'down':cf.downkey}
print '''
<head><title>Research Study</title>
<body>
<link rel="shortcut icon" href="favicon.ico" type="image/x-icon" />
<style type="text/css" media="all">@import "css/drupalit.css";</style>
<style type="text/css" media="all">@import "css/content.css";</style>
<style type="text/css" media="all">@import "css/node.css";</style>
<style type="text/css" media="all">@import "css/defaults.css";</style>
<style type="text/css" media="all">@import "css/system.css";</style>
<style type="text/css" media="all">@import "css/userhttp://htmledit.squarefree.com/.css";</style>
<style type="text/css" media="all">@import "css/fieldgroup.css";</styl<style type="text/css" media="all">@import

"css/date.css";</style>
<style type="text/css" media="all">@import "css/acidfree.css";</style>
<style type="text/css" media="all">@import "css/style.css";</style>
<style type="text/css" media="all">
	.radioLeft{
text-align:left;
		display:inline-block;	
	}
	label {
margin-left: 10px;
		 margin-right: 15px;
	}
	</style>
	<script type="text/javascript">
function validate(thisform){
    if (!checkRadioArray(thisform.response)) {alert('Please enter your rating!');return false;}
    return true
}
function checkRadioArray(radioButtons){
    for (var i=0; i< radioButtons.length; i++) {
        if (radioButtons[i].checked) return true;
    }
    return false;
}
function myfunction(form){

if (document.getElementById('myvideo').ended==1){
        document.getElementById("contbutton").value='SUBMIT';
        document.getElementById("contbutton").type='submit';
        document.getElementById("contbutton").style.color='black';
        }

if (document.getElementById('myvideo').paused==0){
        //var lastinput = document.getElementById("textfield1").value;
        var evtobj=window.event? event : e //distinguish between IE's explicit event object (window.event) and Firefox's implicit.
        var unicode=evtobj.charCode? evtobj.charCode : evtobj.keyCode
        //use event key code rather than text value to get arrow keys
        if (unicode==increasekey) {if (currentpos<10) {currentpos=currentpos+1}}
        if (unicode==decreasekey) {if (currentpos>0) {currentpos=currentpos-1}}
	currval=range[currentpos]
	document.getElementById("textfield1").value="";
	trialvar=trialvar+'!'+currval;
	newtime=new Date().getTime() / 1000;
	newtime=newtime-start-gonetime;
	newtime=Math.round(newtime*100)/100
	newtime=String(newtime)
	newtime=newtime.substr(0,6)
	trialtime=trialtime+'!'+ newtime;
	currcolor='scalefiles/emph_color'+currval+'.png';
        currimage='colorimage'+currval;
	// seperate vectors to deal with certain browser's length issues
        document.getElementById("ratingvector1").value=trialvar.substr(0,500);
        document.getElementById("timevector1").value=trialtime.substr(0,500);
        document.getElementById("ratingvector2").value=trialvar.substr(500,500);
        document.getElementById("timevector2").value=trialtime.substr(500,500);
        document.getElementById("ratingvector3").value=trialvar.substr(1000,500);
        document.getElementById("timevector3").value=trialtime.substr(10000,500);
        document.getElementById("ratingvector4").value=trialvar.substr(1500);
        document.getElementById("timevector4").value=trialtime.substr(1500);


        document.getElementById("colorimage0").src='scalefiles/color0.png';
        document.getElementById("colorimage1").src='scalefiles/color1.png';
        document.getElementById("colorimage2").src='scalefiles/color2.png';
        document.getElementById("colorimage3").src='scalefiles/color3.png';
        document.getElementById("colorimage4").src='scalefiles/color4.png';
        document.getElementById("colorimage5").src='scalefiles/color5.png';
        document.getElementById("colorimage6").src='scalefiles/color6.png';
        document.getElementById("colorimage7").src='scalefiles/color7.png';
        document.getElementById("colorimage8").src='scalefiles/color8.png';
        document.getElementById("colorimage9").src='scalefiles/color9.png';
        document.getElementById("colorimage10").src='scalefiles/color10.png';
	document.getElementById(currimage).src=currcolor;
}
}
started=0;
function pausemyvideo(){
if (document.getElementById('myvideo').ended==1){
        document.getElementById("contbutton").value='SUBMIT';
        document.getElementById("contbutton").type='submit';
        document.getElementById("contbutton").style.color='black';
        }
if (document.getElementById('myvideo').paused==1){
	document.getElementById('myvideo').play();
	if (started==0){
	trialvar='0';
	trialtime='0';
	start=new Date().getTime() / 1000;
	currentpos=0;
	range=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];
	started=1;
	gonetime=0;
	}
	else {
        newtime=new Date().getTime() / 1000;
	newtime=Math.round(newtime*100)/100
        lapsedtime=newtime-start-pausetime
	gonetime=gonetime+lapsedtime
	newtime=newtime-start-gonetime
        newtime=String(newtime)
        newtime=newtime.substr(0,6)
        trialtime=trialtime+'!'+ newtime;
        trialvar=trialvar+'!PLAY';
	}
}
else {
	document.getElementById('myvideo').pause();
        newtime=new Date().getTime() / 1000;
        newtime=newtime-start-gonetime
        pausetime=newtime
	newtime=Math.round(newtime*100)/100
        newtime=String(newtime)
        newtime=newtime.substr(0,6)
        trialtime=trialtime+'!'+ newtime;
        trialvar=trialvar+'!PAUSE';
	}
}
function pausemyvideodef(){
if (document.getElementById('myvideo').ended==1){
        document.getElementById("contbutton").value='SUBMIT';
        document.getElementById("contbutton").type='submit';
        document.getElementById("contbutton").style.color='black';
        }
if (document.getElementById('myvideo').paused==0){
        document.getElementById('myvideo').pause();
        newtime=new Date().getTime() / 1000;
        newtime=newtime-start-gonetime
	newtime=Math.round(newtime*100)/100
        pausetime=newtime
	newtime=String(newtime)
        newtime=newtime.substr(0,6)
        trialtime=trialtime+'!'+ newtime;
        trialvar=trialvar+'!PAUSE';
}
}
</script>
</head>
'''
####end of setup
#moviename=moviedir+subjid[0:7]+'.mp4'
#print "%s" % moviename
if int(qindex)<1:
    nextscript='question.py'
else:
    nextscript='demographics.py'

#print "main loop"
print "<center>Rate the video for: <b>%s</b><br>" % (dim)
print "<br>%s<br>" % dimQ
print "<br>Remember to rate<b> all 4 clips</b>. Do not press Submit until the video has progressed through 4 clips. If the movie pauses, press the green button to continue."
print "<form name='thisform' action='%s' method='submit' onSubmit='return validate(thisform)'>" %nextscript
#print "<video width='512' height='384' id='myvideo' muted><source src=%s type='video/mp4'></video>" % (tempmov)
print "<video width='512' height='384' id='myvideo' muted><source src=%s type='video/mp4'></video>" % (moviename)
#print "<div id='video-overlay'> </div>"
print '''
<br>
<input type="text" id="textfield1" onClick='pausemyvideo()' onBlur='pausemyvideodef()' style='background-image: url("http://mindhive.mit.edu/saxe/FSF/startbutton.png");height:60px;width:199px;color:#32CD32;border:none' value="" onkeydown="myfunction(thisform)"><br>
<img id='colorimage0' alt='temp' src='scalefiles/emph_color0.png' width='40' height='30'><img id='colorimage1' alt='temp' src='scalefiles/color1.png' width='40' height='30'><img id='colorimage2' alt='temp' src='scalefiles/color2.png' width='40' height='30'><img id='colorimage3' alt='temp' src='scalefiles/color3.png' width='40' height='30'><img id='colorimage4' alt='temp' src='scalefiles/color4.png' width='40' height='30'><img id='colorimage5' alt='temp' src='scalefiles/color5.png' width='40' height='30'><img id='colorimage6' alt='temp' src='scalefiles/color6.png' width='40' height='30'><img id='colorimage7' alt='temp' src='scalefiles/color7.png' width='40' height='30'><img id='colorimage8' alt='temp' src='scalefiles/color8.png' width='40' height='30'><img id='colorimage9' alt='temp' src='scalefiles/color9.png' width='40' height='30'><img id='colorimage10' alt='temp' src='scalefiles/color10.png' width='40' height='30'>
'''
print '''
<div id="page_content" align="center">
<br><br>Were these clips familiar to you? Please check the boxes for clips you have seen before.<br>
<div class="radioLeft" align="center">
<br><input type="checkbox" name="clip1" value="seen"><label for="clip1">clip #1</label>
</div>
<div class="radioLeft" align="center">
<br><input type="checkbox" name="clip2" value="seen"><label for="clip2">clip #2</label>
</div>
<div class="radioLeft" align="center">
<br><input type="checkbox" name="clip3" value="seen"><label for="clip3">clip #3</label>
</div>
<div class="radioLeft" align="center">
<br><input type="checkbox" name="clip4" value="seen"><label for="clip4">clip #4</label>
</div>
<br><br>Please provide any comments on the clips (optional)<br>
<br>clip #1<input type="text" name="comment1" size=100 >
<br>clip #2<input type="text" name="comment2" size=100>
<br>clip #3<input type="text" name="comment3" size=100>
<br>clip #4<input type="text" name="comment4" size=100>
<br><br>
<input type="hidden" name="subjid" value="'''+subjid+'''">
<input type="hidden" name="ratingvector1" id="ratingvector1" size=300 value="rating">
<input type="hidden" name="ratingvector2" id="ratingvector2" size=300 value="rating">
<input type="hidden" name="ratingvector3" id="ratingvector3" size=300 value="rating">
<input type="hidden" name="ratingvector4" id="ratingvector4" size=300 value="rating">
<input type="hidden" name="timevector1" id="timevector1" size=300 value="timing">
<input type="hidden" name="timevector2" id="timevector2" size=300 value="timing">
<input type="hidden" name="timevector3" id="timevector3" size=300 value="timing">
<input type="hidden" name="timevector4" id="timevector4" size=300 value="timing">
<input type="hidden" name="keycode" value="'''+keycode+'''">
<input type="hidden" name="qindex" value="'''+qindex+'''">
<input type="hidden" name="rownum" value="'''+formindex+'''"> 	
<input type="button" name="contbutton" id="contbutton" value="SUBMIT" style="color:LightGray" /></center>
<br><br><br><br>
</form>
</div>
</body>
</html>
'''

#end 



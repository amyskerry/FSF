#!/usr/bin/python

import cgitb, cgi, MySQLdb, ast
#import cgitb, cgi, ast
import cPickle as p
from random import randint, shuffle
from ast import literal_eval
from slist import subjects, keycodes
from dim import dimensions, dimInstruct, dimlabels, dimQuest
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
playmovie='playtrial.mp4'
subjid = myform['subjid'].value
login = myform['enterlogin'].value
qindex=myform['qindex'].value
match=0
if subjid in subjects: 
	subjindex=subjects.index(subjid)
	match=1
	keycode=keycodes[subjindex]
else: 
	match=0
#print "theseare the keys %s" % theids
if match==0:	
	print "<center><br><br> OOPS:<br>"
	print "The subject ID you have provided is incorrect. Please return to the previous page and re-enter the subject ID provided on your Mechanical Turk start page."
else:
	dimlabel=subjid[-5:-3]
	i=dimlabels.index(dimlabel)
	dim=dimensions[i]
	diminst=dimInstruct[i]	
        #print "your id is correct <br>"
       	if login=="unlogged":
		#add the person to the database:  "insert" command for new rows
       		cursor.execute('insert into FSF_rating (subjid) values (%s)',str(subjid))
		login="logged";
      	formindex=cursor.execute("SELECT MAX(rownum) AS formindex FROM FSF_rating")
       	formindex = cursor.fetchone()
       	#print "<p> %s </p>" % (formindex)
       	thisvar=str(formindex)
       	thisvar=thisvar[1:-3]
       	formindex=thisvar
       	#print "<p> type: %s </p>" % thisvar
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
        function validate(myform){
            if (!checkRadioArray(myform.response)) {alert('Please enter your rating!');return false;}
            return true;
        }
        function checkRadioArray(radioButtons){
            for (var i=0; i< radioButtons.length; i++) {
                if (radioButtons[i].checked) return true;
            }
            return false;
        }
        trialvar='0';
	trialtime='0';
	start=new Date().getTime() / 1000;
	currentpos=0;
	range=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'];
	function myfunction(form){
        //var lastinput = document.getElementById("textfield1").value;
        var evtobj=window.event? event : e //distinguish between IE's explicit event object (window.event) and Firefox's implicit.
        var unicode=evtobj.charCode? evtobj.charCode : evtobj.keyCode
        //use event key code rather than text value to get arrow keys
        if (unicode==increasekey) {if (currentpos<10) {currentpos=currentpos+1}}
        if (unicode==decreasekey) {if (currentpos>0) {currentpos=currentpos-1}}
	currval=range[currentpos]
	document.getElementById("textfield1").value="";
	trialvar=trialvar+'!!'+currval;
	newtime=new Date().getTime() / 1000;
	newtime=newtime-start;
	newtime=String(newtime)
	newtime=newtime.substr(0,6)
	trialtime=trialtime+'!!'+ newtime;
	currcolor='scalefiles/emph_color'+currval+'.png';
	currimage='colorimage'+currval;
	document.getElementById("ratingvector").value=trialvar;
	document.getElementById("timevector").value=trialtime;
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
function pausemyvideo(){
if (document.getElementById('myvideo').paused==1)
        document.getElementById('myvideo').play();
else
        document.getElementById('myvideo').pause();
}

function pausemyvideodef(){
	document.getElementById('myvideo').pause();
}

        </script>
        </head>
        '''
        ####end of setup
	moviename=moviedir+playmovie
        #moviename=moviedir+'introtrial.mp4'
	#print "main loop"
        print "<center>In this task, you will use a scale like the one below to continuously rate videos. <br> You will use the right and left arrow keys to move around the scale. First, let's play with the scale.<br> <br><b>To begin, click the green box below and follow the instructions on the video.</b> <br><br>"
        print "<br><video id='myvideo' width='512' height='384'><source src=%s type='video/mp4'></video>" % (moviename)                
  	print '''
  	<form name="thisform" action="intro.py" method="post" onSubmit="return validate(thisform)">
  	<br><input type="text" id="textfield1"  onClick='pausemyvideo()' onBlur='pausemyvideodef()' style='background-image: url("http://mindhive.mit.edu/saxe/FSF/startbutton.png");height:60px;width:199px;color:#32CD32;border:none' value="" onkeydown="myfunction(thisform)"><br>
  	<img id='colorimage0' alt='temp' src='scalefiles/emph_color0.png' width='40' height='30'><img id='colorimage1' alt='temp' src='scalefiles/color1.png' width='40' height='30'><img id='colorimage2' alt='temp' src='scalefiles/color2.png' width='40' height='30'><img id='colorimage3' alt='temp' src='scalefiles/color3.png' width='40' height='30'><img id='colorimage4' alt='temp' src='scalefiles/color4.png' width='40' height='30'><img id='colorimage5' alt='temp' src='scalefiles/color5.png' width='40' height='30'><img id='colorimage6' alt='temp' src='scalefiles/color6.png' width='40' height='30'><img id='colorimage7' alt='temp' src='scalefiles/color7.png' width='40' height='30'><img id='colorimage8' alt='temp' src='scalefiles/color8.png' width='40' height='30'><img id='colorimage9' alt='temp' src='scalefiles/color9.png' width='40' height='30'><img id='colorimage10' alt='temp' src='scalefiles/color10.png' width='40' height='30'>
        '''
	
  	print '''
  	<div id="page_content" align="center">
        <div class="radioLeft" align="center">
	<br>
	<center>
        <input type="hidden" name="subjid" value="'''+subjid+'''">
        <input type="hidden" name="keycode" value="'''+keycode+'''">
        <input type="hidden" name="ratingvector" id="ratingvector" value="rating:">
	<input type="hidden" name="timevector" id="timevector" value="timing:">
	<input type="hidden" name="qindex" value="'''+qindex+'''">
	<input type="hidden" name="rownum" value="'''+formindex+'''"> 	
	<input type="hidden" name="tryagain" value='false'> 	
	<input type="hidden" name="enterlogin" value="'''+login+'''"> 	
        <input type="submit" value="Continue" />
        <br><br>
   	</form>
        </div>
        </body>
        </html>
        '''
        #end        







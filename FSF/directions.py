#!/usr/bin/python

import cgitb, cgi, MySQLdb, ast
#import cgitb, cgi, ast
import cPickle as p
from random import randint, shuffle
from ast import literal_eval
from slist import subjects, keycodes
from dim import dimensions, dimInstruct, dimlabels

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
subjid = myform['subjid'].value
dimlabel=subjid[-5:-3]
dimindex=dimlabels.index(dimlabel)
dim=dimensions[dimindex]
diminst=dimInstruct[dimindex]
qindex=myform['qindex'].value
formindex=myform['rownum'].value
qindex=int(qindex)
lastrating=myform['ratingvector'].value
lasttiming=myform['timevector'].value
lastresponse=myform['response'].value
lastratinglist=lastrating.split('!!')
lasttiminglist=lasttiming.split('!!')
keycode=myform['keycode'].value
tryagain=myform['tryagain'].value
#print "timing: %s" %lasttiminglist
#print "ratings %s" %lastratinglist
#print "%s" %lastresponse
#print "row %s" %formindex
testintro=0;
if lastresponse=='getit':
	for n in ['10', '9', '8', '6', '5']:
        	if n in lastratinglist:
			testintro=1
else: 
	testintro=0
if tryagain=='final':
	testintro=1
if tryagain=='true':
	formindex=str(formindex)
        qindex=str(qindex)
        if testintro:
		print "<br><center>Okay. Looks like you've got it!"
	else:
		print "<br><center>Okay. Looks like our task is still a bit confusing. Please do the best you can with the remaining videos."
        print "<form name='failform' action='directions.py' method='submit'>"
        print '''
        <input type="hidden" name="subjid" value="'''+subjid+'''">
        <input type="hidden" name="ratingvector" id="ratingvector" value="10">
        <input type="hidden" name="timevector" id="timevector" value="timing:">
        <input type="hidden" name="qindex" value="'''+qindex+'''">
        <input type="hidden" name="rownum" value="'''+formindex+'''">   
        <input type="hidden" name="keycode" value="'''+keycode+'''">
        <input type="hidden" name="response" value="'''+lastresponse+'''">
        <input type="hidden" name="tryagain" value="final">
        '''
        print "<br><br><input type='submit' value='Continue'>"
        print "</form>"
elif testintro==0:	
	formindex=str(formindex)
	qindex=str(qindex)
	rating='10'
	print "<br><center>Okay. Looks like we should practice this task a bit more. Click below to return to the practice page and try again. <br>Remember to click the green button and then use the arrow keys on your keyboard to move around on the scale."
	print "<form name='failform' action='intro.py' method='submit'>"
        print '''
	<input type="hidden" name="subjid" value="'''+subjid+'''">
        <input type="hidden" name="ratingvector" id="ratingvector" value="10">
        <input type="hidden" name="timevector" id="timevector" value="timing:">
        <input type="hidden" name="qindex" value="'''+qindex+'''">
        <input type="hidden" name="rownum" value="'''+formindex+'''">   
        <input type="hidden" name="keycode" value="'''+keycode+'''">
	<input type="hidden" name="tryagain" value="true">
	'''
	print "<br><br><input type='submit' value='Try Again'>"
	print "</form>"

else:
        #print "your id is correct <br>"
        #print "<p>these are the ids: %s </p>" %(theids)
        #print "<p>these are the qnums: %s </p>" %(qnums)
        #print "<p>qindex: %s </p>" %(qindex)
        qindex=str(qindex)
        #print "<p>these are the new qnums: %s </p>" %(qnumlist)
        
       	#add the person to the database:  "insert" command for new rows
	sql='update FSF_rating set introcheck ="'+lastresponse+'" where rownum="'+formindex+'"'
	cursor.execute(sql)
	sql='update FSF_rating set introrating ="'+lastrating+'" where rownum="'+formindex+'"'
	cursor.execute(sql)
	sql='update FSF_rating set introtiming ="'+lasttiming+'" where rownum="'+formindex+'"'
	cursor.execute(sql)
       	#print "<p> type: %s </p>" % thisvar
        ### css setup
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
            return true;
        }
        function checkRadioArray(radioButtons){
            for (var i=0; i< radioButtons.length; i++) {
                if (radioButtons[i].checked) return true;
            }
            return false;
        }
        </script>
        </head>
        '''
        ####end of setup
	nextscript='question.py'

       	#print "main loop"
       	print "<center><b><br><br>Directions:</b><br><br>"
	print "For the remaining videos, you will be continuously rating the extent to which the video currently involves <b>%s</b>. <br> " % (dim)
        print "<br>%s<br><br>" %diminst
	print "Remember, once you begin this task, you will need to rate the video continuously for roughy 10 minutes. There will be 4 clips joined together as a single movie. <br> <b>You can click the green button to start and pause the clip, and use the arrow keys to move around the scale.</b> <br><br> If you are ready to begin recording, press the button below."
	print "<form name='thisform' action='%s' method='submit' onSubmit='return validate(thisform)'>" %nextscript
	print '''
	<div id="page_content" align="center">
	<br>
        <input type="hidden" name="subjid" value="'''+subjid+'''">
        <input type="hidden" name="keycode" value="'''+keycode+'''">
        <input type="hidden" name="qindex" value="'''+qindex+'''">
        <input type="hidden" name="rownum" value="'''+formindex+'''"> 	
        <input type="submit" value="Continue" /></center>
        <br><br><br><br>
	</form>
        </div>
        </body>
        </html>
	'''
        
        
        
        #end


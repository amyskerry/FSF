#!/usr/bin/python

import cgitb, cgi, MySQLdb, ast
#import cgitb, cgi, ast
import cPickle as p
from random import randint, shuffle
from ast import literal_eval

myform=cgi.FieldStorage()
cgitb.enable()
cursor = MySQLdb.connect(host="localhost",user="askerry",passwd="password",db="aesbehave").cursor()
print 'Content-type:text/html\n\n'

print '''
<style type="text/css">
    body {
        font-family:verdana,arial,helvetica,sans-serif;
        font-size:100%;
    }
</style>
'''

#cgitb.enable(display=0, logdir="/path/to/logdir")
theids=myform.keys() 
subjid = myform['subjid'].value
qindex=myform['qindex'].value
keycode=myform['keycode'].value
qindex=int(qindex)
formindex=myform['rownum'].value
#print "<p>these are the ids: %s </p>" %(theids)
lastrating1=lastrating2=lastrating3=lastrating4=lasttiming1=lasttiming2=lasttiming3=lasttiming4=lastrating5=lastrating6=lastrating7=lastrating8=lastrating9=lastrating10=lasttiming5=lasttiming6=lasttiming7=lasttiming8=lasttiming9=lasttiming10=''
#omg so ghetto I'm sorry
try:
	lastrating1=myform['ratingvector1'].value
except: pass
try:
	lastrating2=myform['ratingvector2'].value
except: pass
try:
	lastrating3=myform['ratingvector3'].value
except: pass
try:	
	lastrating4=myform['ratingvector4'].value
except: pass
try:
	lasttiming1=myform['timevector1'].value
except: pass
try:
	lasttiming2=myform['timevector2'].value
except: pass
try:
	lasttiming3=myform['timevector3'].value
except: pass
try:	
	lasttiming4=myform['timevector4'].value
except: pass
try:
        lastrating5=myform['ratingvector5'].value
except: pass
try:
        lastrating6=myform['ratingvector6'].value
except: pass
try:
        lastrating7=myform['ratingvector7'].value
except: pass
try:
        lastrating8=myform['ratingvector8'].value
except: pass
try:
        lastrating9=myform['ratingvector9'].value
except: pass
try:
        lastrating10=myform['ratingvector10'].value
except: pass
try:
        lasttiming5=myform['timevector5'].value
except: pass
try:
        lasttiming6=myform['timevector6'].value
except: pass
try:
        lasttiming7=myform['timevector7'].value
except: pass
try:
        lasttiming8=myform['timevector8'].value
except: pass
try:
        lasttiming9=myform['timevector9'].value
except: pass
try:
        lasttiming10=myform['timevector10'].value
except: pass
try:
	lastrating=lastrating1+lastrating2+lastrating3+lastrating4+lastrating5+lastrating6+lastrating7+lastrating8+lastrating9+lastrating10
except: pass
try:
	lasttiming=lasttiming1+lasttiming2+lasttiming3+lasttiming4+lasttiming5+lasttiming6+lasttiming7+lasttiming8+lasttiming9+lasttiming10
except: pass
#print "%s" % lasttiming
#print "%s" % lastrating
clip1=clip2=clip3=clip4=comment1=comment2=comment3=comment4='0'
try:
	clip1=myform['clip1'].value
except: pass
try:
        clip2=myform['clip2'].value
except: pass
try:
        clip3=myform['clip3'].value
except: pass
try:
        clip4=myform['clip4'].value
except: pass
try:
        comment1=myform['comment1'].value
except: pass
try:
        comment2=myform['comment2'].value
except: pass
try:        
        comment3=myform['comment3'].value
except: pass
try:    
        comment4=myform['comment4'].value
except: pass

clipseen=clip1 +'!!' + clip2 + '!!' + clip3 +'!!' + clip4
clipcomments=comment1 +'!!'+ comment2+'!!'+ comment3+'!!'+ comment4
#print "%s" % clipseen
lastratinglist=lastrating.split('!!')
lasttiminglist=lasttiming.split('!!')
lastQ='1'
qvar='q1'
ratingvar='rating'+ lastQ
timingvar='timing' + lastQ
qvarseen=qvar+'seen'
qvarcomments=qvar+'comments'
sql='update FSF_rating set ' +qvarseen +' ="'+clipseen+'" where rownum="'+formindex+'"'
cursor.execute(sql)
sql='update FSF_rating set ' +qvarcomments +' ="'+clipcomments+'" where rownum="'+formindex+'"'
cursor.execute(sql)
sql='update FSF_rating set ' +timingvar +' ="'+lasttiming+'" where rownum="'+formindex+'"'
cursor.execute(sql)
sql='update FSF_rating set ' +ratingvar +' ="'+lastrating+'" where rownum="'+formindex+'"'
cursor.execute(sql)

### css setup
print '''
<head><title>Research Study: Demographics</title>

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
<style>
  .pagealign{
                text-align:left;
                margin-left:130px;margin-right:20px

        }	
  .demoalign{
        }
        label {
                 margin-left: 0px;
                 margin-right: 10px;
        }

</style>

<script type="text/javascript">
function validate(form){
    if (!checkTextField(form.gender)) {alert('Please enter your gender!');return false;}
    if (!checkTextField(form.age)) {alert('Please enter your age!');return false;}
    return true;
}
function checkRadioArray(radioButtons){
    for (var i=0; i< radioButtons.length; i++) {
        if (radioButtons[i].checked) return true;
    }
    return false;
}
function checkTextField(textField){
    if (textField.value!='') return true;
    return false;
}
</script>
</head>
'''
####end of setup

print '''
<div id="page_content" style="margin-right:160px;  margin-left: 160px;">
<br>
<p style="text-align:center"><font size="5"> Demographics </font></p>
<br>
<p style="text-align:center">Thank you for completing our study! We have a few quick follow up questions for you.</p>
<br>
<form name="myform" action="debrief.py" method="post" onSubmit="return validate(myform)">
<div class=pagealign> 
Please tell us where you are from.
<br>
<label for="city">City (optional): </label> <input type="text" name="city" size=30>
<br>
<label for="country" >Country (optional): </label><input type="text" name="country" size=30>
<br><br>
Please tell us about yourself.<br>
<label for="gender" >Gender: </label><input type="text" name="gender" size=30>
<br>
<label for="age">Age: </label><input type="text" name="age" size=30>
<br><br>
</table><br>
Do you have any comments, thoughts, or feedback about this study? 
<br><textarea name="thoughts" cols=80 rows=8> </textarea><br>
</div>
<br><br><br>
<center>
We very much appreciate you taking the time to do this study.<br>
When you click continue you will receive a code that allows you to <b> recieve your payment.<center>
<br><br>
<input type="hidden" name="subjid" value="'''+subjid+'''">
<input type="hidden" name="keycode" value="'''+keycode+'''"> 
<input type="hidden" name="rownum" value="'''+formindex+'''"> 
<input type="submit" value="Continue" /></center>
<br><br><br><br>
</form>
</div>
</body>
</html>
'''
#end

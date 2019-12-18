import os, re, string, tarfile, subprocess
path = os.getcwd()
def writeIndexHTML():
	f = open('index.html', 'w')
	htmlfile = """
<!DOCTYPE html>
<html>

<head>
	<title>Main Index</title>
	<style>
		body{
			font-family:monospace;
		}
		h2{
			text-align:center;
		}
		.linkButton{
			display: inline-block;
			border-radius: 4px;
			background-color: #FFFFFF;
			border: none;
			color: #000000;
			text-align: center;
			width:150px;
			font-size: 12px;
			padding: 10px 25px;
			transition: all 0.5s;
			cursor: pointer;
			margin: 5px;
		}
		.linkButton span{
			cursor: pointer;
			display: inline-block;
			position: relative;
			transition: 0.5s;
		}
		.linkButton span:after{
			content: '>>';
			position: absolute;
			opacity: 0;
			top: 0;
			right: -20px;
			transition:0.5s;
		}
		.linkButton:hover span{
			padding-right: 25px;
		}
		.linkButton:hover span:after{
			opacity: 1;
			right: 0;
		}
		#banner{
			top: 0px;
			left:0px;
			right:0px;
			width:100%;
			height:100%;
			z-index:-1;
		}
		.projectBanners{
			text-align: center;
			margin:20px;
			margin-left: 150px;
			margin-right: 150px;
			padding: 20px;
			border-radius:12px;
			box-shadow: 10px 10px 5px grey;
			color:black;
		}
	</style>
	
</head>

<body>
	<img id="banner" src="http://www.algocult.org/wp-content/uploads/2018/08/cropped-Web-Personalization-Humans-v.-Algorithms.png"/>
	<hr>
	<h1 align="center">My CSC344 Projects!<br>By Luis Estevez</h1>

	<div class="projectBanners" style="background-color:lightgrey" >
		<p style = "float: center; margin: 1px;"><img src="https://iq.opengenus.org/content/images/2019/07/TurigMachine.png" height="175px" width="400px"/><p>
		<h1>Assignment 1: Turing Machine</h1>
		<h3>My implementation of a Turing Machine in C.</h3>
		<i>Click here for more information: </i>
		<a href="../Assignment1/summary_main.c.html" class="linkButton" target="_blank"
		type="button"><span>C-site</span></a>
	</div>

	<div class="projectBanners" style="background-color:#FCFE3C" >
		<p style = "float: center; margin: 1px;"><img src="https://www.sanfoundry.com/wp-content/uploads/2016/09/plc-program-implement-various-logic-gates-01.png" height="175px" width = "400px"/><p>
		<h1>Assignment 2: Nor-Logic Converter</h1>
		<h3>My implementation of a Nor-Logic Converter in Clojure.</h3>
		<i>Click here for more information: </i>
		<a href="../Assignment2/summary_main.clj.html" class="linkButton" target="_blank"
		type="button"><span>Clojure-site</span></a>
	</div>

	<div class="projectBanners" style="background-color:#7AE171" >
		<p style = "float: center; margin: 1px;"><img src="https://cdn-images-1.medium.com/max/1400/1*QEDiKhSaOgi6W52S5QUHGg.png" height="175px" width="400px"/><p>
		<h1>Assignment 3: Pattern Matching</h1>
		<h3>My implementation of a pattern matcher using in Scala.</h3>
		<i>Click here for more information: </i>
		<a href="../Assignment3/summary_main.scala.html" class="linkButton" target="_blank"
		type="button"><span>Scala-site</span></a>
	</div>

	<div class="projectBanners" style="background-color:#F9C159" >
		<p style = "float: center; margin: 1px;"><img src="http://danielschlegel.org/wp/wp-content/uploads/2017/10/LaserProblem.png" height="175px" width="400px"//><p>
		<h1>Assignment 4: Laser Beams</h1>
		<h3>My implementation of a pattern matcher using in Prolog.</h3>
		<i>Click here for more information: </i>
		<a href = "../Assignment4/summary_main.pl.html" class="linkButton" target="_blank"
		type="button"><span>Prolog-site</span></a>
	</div>

	<div class="projectBanners" style="background-color:#71E1C7" >
		<p style = "float: center; margin: 1px;"><img src="https://miro.medium.com/max/3336/1*YMFKP8e6kR9cbM3IKXBtLw.png" height="150px" width="400px"/><p>
		<h1>Assignment 5: Project Summarizer</h1>
		<h3>My implementation of a pattern matcher using in Python.</h3>
		<i>Click here for more information: </i>
		<a href="../Assignment5/summary_main.py.html" class="linkButton"  target="_blank" 
		type="button"><span>Python-site</span></a>
	</div>
	<hr>

</body>

</html>
	 """
	f.write(htmlfile)
	f.close()

def summaryHTML(parentPath, prj):
	f = open(parentPath + '/summary_' + prj.name + '.html', 'w')
	out = subprocess.check_output(['wc', '-l', prj])
	numOfLines = int(re.search(r'\d+', str(out)).group())
	html = """
<!DOCTYPE html>
<html>
<head>
	<title>"""+ prj.name +"""</title>
	<style>
		body{
			font-family: monospace;
		}
		.projectInfo{
			margin: 20px;
			margin-left: 150px;
			margin-right: 150px;
			padding: 20px;
			border-radius:12px;
			box-shadow: 10px 10px 5px grey;
		}
	</style>
</head>
<body>
	<h1 align="center">"""+ prj.name +"""</h1>
	<hr>
	<div class="projectInfo" style="background-color:lightgrey; color:black">
		<p>Number of Lines:<i> """+ str(numOfLines) +"""</i></p>
		<p><a target="_blank" href='""" + prj.name + """'>Source Code</a></p>
		<p>List of Identifiers:<br>
"""	
	html = html + writeLists(prj)
	html = html + """
	</div>
</body>
</html>
"""
	f.write(html)

def writeLists(currPrj):
	lsOfId = parseList(currPrj)
	res = " "
	for ID in lsOfId:
		res = res + "<li>" + ID + "</li>"
	return res

def parseList(currPrj):
	res = list()
	f = open(currPrj.path, 'r')
	for line in f:
		line = line.lstrip()
		while line.startswith('//') or line.startswith(';') or line.startswith('#'):
			line = next(f)
			line = line.lstrip()

		if line.startswith('/*'):
			line = next(f)
			line = line.lstrip()			
			while not line.endswith('*/\n'):
				line = next(f)
				line = line.lstrip()
			line = next(f)
			line = line.lstrip()

		if line.startswith('%'):
			line = next(f)
			line = line.lstrip()
			while not line.endswith('.\n'):
				line = next(f)
				line = line.lstrip()
			line = next(f)
			line = line.lstrip()

		if line.startswith('"'):
			line = next(f)
			line = line.lstrip()
			while not line.endswith('"\n'):
				line = next(f)
				line = line.lstrip()
			line = next(f)
			line = line.lstrip()

		line = re.sub('(\)+.*(?=))', '', line)
		line = re.findall('(\s*[a-zA-Z]*\s*)',line)
		for wrd in line:
			wrd = re.sub('\s+','', wrd)
			if not res.__contains__(wrd) and wrd != '':
				res.append(wrd)
	res.sort()
	return res


def getProjects():
	projectList = [None] * 5
	prjPath = ' '
	with os.scandir(path + '/..') as itr:
		for entry in itr:
			if 'Assignment' in entry.name:
				prjPath = path + '/../' + entry.name
				with os.scandir(path + '/../' + entry.name) as itr:
					for e in itr:
						if e.name.startswith('main', 0, 4):
							if e.name.endswith('.c'):
								projectList[0] = e
								summaryHTML(prjPath, e)
							if e.name.endswith('.clj'):
								projectList[1] = e
								summaryHTML(prjPath, e)
							if e.name.endswith('.scala'):
								projectList[2] = e
								summaryHTML(prjPath, e)
							if e.name.endswith('.pl'):
								projectList[3] = e
								summaryHTML(prjPath, e)
							if e.name.endswith('.py'):
								projectList[4] = e
								summaryHTML(prjPath, e)
	return projectList

def getTar():
	tar = tarfile.open('CSC344Projects' + ".tar.xz", 'w|')
	with os.scandir(path  + '/..') as itr:
		for dir in itr:
			
			if dir.name.startswith('Assignment'):
				with os.scandir(dir) as d:
					for f in d:
						if f.name.startswith('main', 0, 4) or f.name.endswith('.html'):
							
							tar.add(f.path, dir.name + '/' + f.name)
		tar.close()

writeIndexHTML()
getProjects()
tar = getTar()
a = subprocess.Popen("echo 'This is the body' | mutt -s test -- lestevez@oswego.edu", shell = True)
a.communicate()

import time, MySQLdb, os, glob, pygal

while True:
	UTime = str(time.strftime("%M:%S", time.gmtime()))
	print UTime
	if UTime == "10:00":
		db = MySQLdb.connect(host="*Host*", user="*User*",passwd="*password*",db="*DataBase*")
		cur = db.cursor()
		query = ("SELECT Time, Date, Temp, CPUTemp FROM TBL_Temp ORDER BY ID DESC LIMIT 24;")
		cur.execute(query)
		ItemList =  cur.fetchall()
		cur.close()
		db.close()
		i = 0 
		lable = []
		CPUTemps = []
		AbTemps = []

		for i in range(len(ItemList)):  
			lable.append(ItemList[i][0] + " " + ItemList[i][1])
			CPUTemps.append(ItemList[i][3])
			AbTemps.append(ItemList[i][2])
	
		line_chart = pygal.Line(label_font_size=8,x_label_rotation=90)
		line_chart.title = 'RaspberyPi ambient temp and CPU Temp'
		line_chart.x_labels = reversed(lable)
		line_chart.y_labels = 0, 10, 20, 30, 40, 50, 60
		line_chart.add('CPU Temps', reversed(CPUTemps))
		line_chart.add('Ambient Temps', reversed(AbTemps))
		print "Rendering"
		line_chart.render_to_file('PiTemp.svg')
		print "Finsihed rendering"
		print str(time.strftime("%H:%M:%S", time.gmtime()))
		time.sleep(1800)
	else :
		time.sleep(1)

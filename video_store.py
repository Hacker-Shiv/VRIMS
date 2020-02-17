import csv
import sys
from tempfile import NamedTemporaryFile
import shutil
import datetime
d = datetime.datetime.now()
def add_vid():
	with open('video.csv','a+') as csvfile:
		columns = ['vid_id','vid_name','rating','quantity','chk_sts']
		writer = csv.DictWriter(csvfile,fieldnames = columns)
		vid_id = int(input("Enter ID : "))
		vide_name = input("Enter video name : ")
		with open('video.csv','r+') as csfile:
			reader=csv.DictReader(csfile)
			for row in reader:
				if row['vid_name'] == vide_name:
					print("Video Already exists.")
					return

		
		rating = int(input("Enter video rating : "))
		quantity = int(input("Enter quantity : "))
		chk_sts = input("Enter Video Status (T/F)")
		writer.writerow({'vid_id':vid_id,'vid_name':vide_name,'rating':rating,'quantity':quantity,'chk_sts':chk_sts})

		
		with open('store.csv','a+') as csvfile:
			pur_date= d.strftime("%d")
			pur_month= d.strftime("%m")
			pur_year = d.strftime("%Y")
			columns = ['vid_id','vid_name','rating','quantity','chk_sts']
			writer = csv.DictWriter(csvfile,fieldnames = columns)
			writer.writerow({'vid_id':vid_id,'vid_name':vide_name,'rating':rating,'quantity':quantity,'chk_sts':chk_sts})


def search_vid():
    with open('video.csv','r') as csvfile:
        name=input('Enter the video name to checkout : ')
        reader=csv.DictReader(csvfile)
        for row in reader:
            if row['vid_name'] == name:
                print('Name : ', row['vid_name'],'\n','Checkout : ', row['chk_sts'],'\n','Rating : ',row['rating'],'\n',)
def ret_vid():
    vd_name =input('Enter the name of the video you want to return : ')
    print("Video",vd_name,"returned successfully")

def update_vid():
    tempfile = NamedTemporaryFile(mode='w', delete=False)
    columns = ['vid_id','vid_name','rating','quantity']
    with open('video.csv', 'r+') as csvfile, tempfile:
        reader = csv.DictReader(csvfile)
        writer = csv.DictWriter(tempfile, fieldnames=columns)
        writer.writeheader()
        vide_name =input('Enter the name of the video you want to receive rating : ')
        for row in reader:
            if row['vid_name'] == vide_name:
            	print('---------------------------------------------')
            	print('|1.To update Name                           |')
            	print('---------------------------------------------')
            	print('|2.To update Rating                         |')
            	print('---------------------------------------------')
            	choice=int(input())
            	if(choice==1):
            		row['vid_name']=input("Enter the new name : ")

            	elif(choice==2):
            		row['rating']=int(input("Enter the new rating : "))
    
            row = {'vid_id':row['vid_id'],'vid_name':row['vid_name'],'rating':row['rating'],'quantity':row['quantity']}
            writer.writerow(row)
    shutil.move(tempfile.name, 'video.csv')
    print("Rating ",row['rating'], "has been mapped to the video ",vide_name)
	
def list_all():
	count = 0
	with open('video.csv','r') as csvfile:
		reader=csv.DictReader(csvfile)
		for row in reader:
			if int(row['vid_id']) >0:
				count+=1
				print(' ID : ', row['vid_id'],'\n',' Name : ', row['vid_name'],'\n','Rating : ',row['rating'],'\n',' Checkout : ', row['chk_sts'])   
	if count == 0:
		print("No Video exists.\n")			        
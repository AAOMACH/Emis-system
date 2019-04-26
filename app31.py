from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QFileDialog
import sqlite3
import datetime
import time
import csv

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np


####################################### Database class
conn = sqlite3.connect('Education.db')
c = conn.cursor()
conn.commit()

######################### DATABASE TABLES #######################################

def create_school_table():
    c.execute("CREATE TABLE IF NOT EXISTS school(Emis_no INTEGER PRIMARY KEY,school_name TEXT,school_type TEXT,sub_county TEXT,"
              "parish TEXT,village TEXT)")

def create_user_table():
    c.execute("CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY,first_name TEXT,last_name TEXT,user_name TEXT,"
              "passward TEXT)")

def create_teacher_table():
    c.execute('CREATE TABLE IF NOT EXISTS teacher(EmployeeNo INTEGER PRIMARY KEY, school TEXT,'
              'Emis_No INTEGER,school_type TEXT,sub_county TEXT,Qualification TEXT,expected_Date_of_retirement TEXT,name TEXT,'
              'Gender TEXT,Date_of_Birth TEXT,Marital_status TEXT,home_district TEXT, home_subcounty TEXT,'
              'home_parish TEXT, home_village TEXT,Next_of_kin TEXT,Title TEXT,'
              'confirmation_status TEXT,nin TEXT,supplier_no TEXT,tin TEXT,reg_no,datestamp TEXT,'
              'FOREIGN KEY(Emis_No) REFERENCES school(Emis_no))')

def create_enrollment_table():
    c.execute('CREATE TABLE IF NOT EXISTS enrollment(id2 INTEGER PRIMARY KEY,school_name TEXT,Emis_no INTEGER,school_type TEXT,'
              'village TEXT,parish TEXT,sub_county TEXT,category TEXT,ownership TEXT,p1male INTEGER,p1female INTEGER,p2male INTEGER,p2female INTEGER,'
              'p3male INTEGER,p3female INTEGER,p4male INTEGER,p4female INTEGER,p5male INTEGER,p5female INTEGER,p6male INTEGER,p6female INTEGER,'
              'p7male INTEGER,p7female INTEGER,maletotal INTEGER,femaletotal TEXT,datestamp TEXT,FOREIGN KEY(Emis_no) REFERENCES school(Emis_no))')

def create_senrollment_table():
    c.execute('CREATE TABLE IF NOT EXISTS secenrollment(id2 INTEGER PRIMARY KEY,school_name TEXT,Emis_no INTEGER,school_type TEXT,'
              'village TEXT,parish TEXT,sub_county TEXT,category TEXT,ownership TEXT,s1male INTEGER,s1female INTEGER,s2male INTEGER,s2female INTEGER,'
              's3male INTEGER,s3female INTEGER,s4male INTEGER,s4female INTEGER,s5male INTEGER,s5female INTEGER,s6male INTEGER,s6female INTEGER,'
              'maletotal INTEGER,femaletotal TEXT,datestamp TEXT,FOREIGN KEY(Emis_no) REFERENCES school(Emis_no))')

def create_teacher_qualifications_table():
    c.execute('CREATE TABLE IF NOT EXISTS qualifications(id3 INTEGER PRIMARY KEY,school_name TEXT,school_type TEXT,Emis_no INTEGER,'
              'village TEXT,parish TEXT,sub_county TEXT,'
              'category TEXT,ownership TEXT,no_p1teachers REAL,no_p2teachers REAL,no_p3teachers REAL,'
              'no_p4teachers REAL,no_p5teachers REAL,no_p6teachers REAL,no_p7teachers REAL,total REAL,'
              'licensed_m REAL,licensed_f REAL,certificate_m,certificate_f,m_deploma REAL, f_deploma REAL, m_bachelors, f_bachelors, m_masters REAL, f_master REAL,'
              'datestamp TEXT,FOREIGN KEY(Emis_no) REFERENCES school(Emis_no))')
    
def create_steacher_qualifications_table():
    c.execute('CREATE TABLE IF NOT EXISTS secqualifications(id3 INTEGER PRIMARY KEY,school_name TEXT,school_type TEXT,Emis_no INTEGER,'
              'village TEXT,parish TEXT,sub_county TEXT,'
              'category TEXT,ownership TEXT,no_s1teachers REAL,no_s2teachers REAL,no_s3teachers REAL,'
              'no_s4teachers REAL,no_s5teachers REAL,no_s6teachers REAL,total REAL,'
              'licensed_m REAL,licensed_f REAL,certificate_m,certificate_f,m_deploma REAL, f_deploma REAL, m_bachelors, f_bachelors, m_masters REAL, f_master REAL,'
              'datestamp TEXT,FOREIGN KEY(Emis_no) REFERENCES school(Emis_no))')
    
def create_school_facilities_table():
    c.execute('CREATE TABLE IF NOT EXISTS facilities(id4 INTEGER PRIMARY KEY,school_name TEXT,Emis_no INTEGER,school_type TEXT,'
              'village TEXT,parish TEXT,sub_county TEXT,'
              'category TEXT,ownership TEXT,library REAL,science_lab REAL,computer_lab REAL,'
              'kitchen REAL,staff_room REAL,administration_block REAL,dining_hall REAL,reliable_safe_water_supply REAL,'
              'stores REAL,workshop REAL,playground REAL,school_garden REAL,latrine REAL,no_of_stances REAL,'
              'handwashing_facility REAL,p1_desk REAL,p2_desk REAL,p3_desk REAL,p4_desk REAL,p5_desk REAL,'
              'p6_desk REAL,p7_desk REAL,datestamp TEXT,'
              'FOREIGN KEY(Emis_no) REFERENCES school(Emis_no))')

def create_school_sfacilities_table():
    c.execute('CREATE TABLE IF NOT EXISTS secfacilities(id4 INTEGER PRIMARY KEY,school_name TEXT,Emis_no INTEGER,school_type TEXT,'
              'village TEXT,parish TEXT,sub_county TEXT,'
              'category TEXT,ownership TEXT,library REAL,science_lab REAL,computer_lab REAL,'
              'kitchen REAL,staff_room REAL,administration_block REAL,dining_hall REAL,reliable_safe_water_supply REAL,'
              'stores REAL,workshop REAL,playground REAL,school_garden REAL,latrine REAL,no_of_stances REAL,'
              'handwashing_facility REAL,s1_desk REAL,s2_desk REAL,s3_desk REAL,s4_desk REAL,s5_desk REAL,'
              's6_desk REAL,datestamp TEXT,FOREIGN KEY(Emis_no) REFERENCES school(Emis_no))')
    
def create_classroom_table():
    c.execute('CREATE TABLE IF NOT EXISTS classroom(id4 INTEGER PRIMARY KEY,school_name TEXT,Emis_no INTEGER,school_type TEXT,'
              'village TEXT,parish TEXT,sub_county TEXT,'
              'category TEXT,ownership TEXT,p1_classroom REAL,p2_classroom REAL,p3_classroom REAL,'
              'p4_classroom REAL,p5_classroom REAL,p6_classroom REAL,p7_classroom REAL,'
              'total_classrooms,complete_permanent REAL,complete_temporary REAL,at_foundation REAL,at_window REAL,'
              'at_wallplate_and_above REAL,number_of_classes_without_structures REAL,datestamp TEXT,'
              'FOREIGN KEY(Emis_no) REFERENCES school(Emis_no))')

def create_sclassroom_table():
    c.execute('CREATE TABLE IF NOT EXISTS secclassroom(id4 INTEGER PRIMARY KEY,school_name TEXT,Emis_no INTEGER,school_type TEXT,'
              'village TEXT,parish TEXT,sub_county TEXT,'
              'category TEXT,ownership TEXT,s1_classroom REAL,s2_classroom REAL,s3_classroom REAL,'
              's4_classroom REAL,s5_classroom REAL,s6_classroom REAL,'
              'total_classrooms,complete_permanent REAL,complete_temporary REAL,at_foundation REAL,at_window REAL,'
              'at_wallplate_and_above REAL,number_of_classes_without_structures REAL,datestamp TEXT,'
              'FOREIGN KEY(Emis_no) REFERENCES school(Emis_no))')

def create_teacher_housing_table():
    c.execute('CREATE TABLE IF NOT EXISTS teacher_housing(id5 INTEGER PRIMARY KEY,school_name TEXT,Emis_no INTEGER,school_type TEXT,'
              'village TEXT,parish TEXT,sub_county TEXT,category TEXT,ownership TEXT,complete_permanent REAL,complete_temporary REAL,'
              'permanent_at_foundation REAL,permanent_at_window_level REAL,permanent_at_wallplate_and_above REAL,'
              'datestamp TEXT,FOREIGN KEY(Emis_no) REFERENCES school(Emis_no))')
    
def create_leave_table():
    c.execute("CREATE TABLE IF NOT EXISTS leave(id INTEGER PRIMARY KEY,empno INTEGER,name TEXT, school TEXT,schoo_type TEXT,details_of_leave TEXT,"
              "startdate TEXT, enddate TEXT,FOREIGN KEY(empno) REFERENCES teacher(EmployeeNo))")

def create_retired_table():
    c.execute('CREATE TABLE IF NOT EXISTS retired(EmployeeNo INTEGER PRIMARY KEY, school TEXT,'
              'Emis_No INTEGER,school_type TEXT,sub_county TEXT,Qualification TEXT,expected_Date_of_retirement TEXT,name TEXT,'
              'Gender TEXT,Date_of_Birth TEXT,Marital_status TEXT,home_district TEXT, home_subcounty TEXT,'
              'home_parish TEXT, home_village TEXT,Next_of_kin TEXT,Title TEXT,'
              'confirmation_status TEXT,nin TEXT,supplier_no TEXT,tin TEXT,reg_no,datestamp TEXT)')

def create_deceased_table():
    c.execute('CREATE TABLE IF NOT EXISTS deceased(EmployeeNo INTEGER PRIMARY KEY, school TEXT,'
              'Emis_No INTEGER,school_type TEXT,sub_county TEXT,Qualification TEXT,expected_Date_of_retirement TEXT,name TEXT,'
              'Gender TEXT,Date_of_Birth TEXT,Marital_status TEXT,home_district TEXT, home_subcounty TEXT,'
              'home_parish TEXT, home_village TEXT,Next_of_kin TEXT,Title TEXT,'
              'confirmation_status TEXT,nin TEXT,supplier_no TEXT,tin TEXT,reg_no,date_of_death TEXT)')
    
def create_absconded_table():
    c.execute('CREATE TABLE IF NOT EXISTS absconded(EmployeeNo INTEGER PRIMARY KEY, school TEXT,'
              'Emis_No INTEGER,school_type TEXT,sub_county TEXT,Qualification TEXT,expected_Date_of_retirement TEXT,name TEXT,'
              'Gender TEXT,Date_of_Birth TEXT,Marital_status TEXT,home_district TEXT, home_subcounty TEXT,'
              'home_parish TEXT, home_village TEXT,Next_of_kin TEXT,Title TEXT,'
              'confirmation_status TEXT,nin TEXT,supplier_no TEXT,tin TEXT,reg_no,date TEXT)')


#################################### CRUD functions ##################################################################
############### INSERT DATA
def insertschool(emis, name, subcounty, parish, village, schooltype):
    
    c.execute("INSERT INTO school(Emis_no,school_name,school_type,sub_county,parish,village) VALUES(?, ?, ?, ?, ?, ?)",(emis,name,schooltype,subcounty,parish,
                                                                                                                        village))
    conn.commit()

def insertteacher(empno, schooln, subcounty, quaification, name, gender, dob, marital, hdistrict, hsubcounty,
                  hparish, hvillage, nok, tital, confirmation, nin, supplier, tin,reg_no):

    x = 21915
    bd = datetime.datetime.strptime(dob,"%m/%d/%Y")
    eod = bd + datetime.timedelta(days = x)
    datestamp = datetime.datetime.today().year
    c.execute("SELECT * FROM school WHERE school_name = ?",(schooln,))
    for row in c.fetchall():
        emis1 = row[0]
        stype = row[2]
        
        c.execute("INSERT INTO teacher(EmployeeNo,school,Emis_No,school_type, sub_county, Qualification, expected_Date_of_retirement,"
                  "name, Gender, Date_of_Birth, Marital_status, home_district, home_subcounty, home_parish, home_village,"
                  "Next_of_kin, Title, confirmation_status, nin,"
                  "supplier_no, tin,reg_no,datestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (empno, schooln, emis1,stype, subcounty,quaification,eod,name,gender,
                                                                                                               dob,marital,hdistrict,hsubcounty,hparish,hvillage, nok,tital,
                                                                                                               confirmation,nin,supplier,tin,reg_no,datestamp))
        
        conn.commit()

def insertenrollment(school, category, owership, p1m, p1f, p2m, p2f, p3m, p3f, p4m, p4f, p5m, p5f, p6m, p6f, p7m, p7f):

    c.execute("SELECT * FROM school WHERE school_name = ?",(school,))
    datestamp = datetime.datetime.today().year
           
    for row in c.fetchall():
        
        emis2 = row[0]
        village = row[5]
        parish = row[4]
        subcounty = row[3]
        stype = row[2]
        mtotal = p1m + p2m + p3m + p4m + p5m + p6m + p7m
        ftotal = p1f + p2f + p3f + p4f + p5f + p6f + p7f

        c.execute("INSERT INTO enrollment(school_name,Emis_no,school_type,village,parish,sub_county,category,ownership,p1male,p1female,p2male,p2female,p3male,"
                  "p3female,p4male,p4female,p5male,p5female,p6male,p6female,p7male,"
                  "p7female,maletotal,femaletotal,datestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school, emis2, stype,village, parish,subcounty,category,
                                                                                                                         owership, p1m, p1f, p2m, p2f, p3m, p3f, p4m,
                                                                                                                         p4f,p5m, p5f, p6m, p6f, p7m, p7f, mtotal,
                                                                                                                         ftotal,datestamp))
        conn.commit()

def insertsecenrollment(school, category, owership, s1m, s1f, s2m, s2f, s3m, s3f, s4m, s4f, s5m, s5f, s6m, s6f):

    c.execute("SELECT * FROM school WHERE school_name = ?",(school,))
    datestamp = datetime.datetime.today().year
           
    for row in c.fetchall():
        
        emis2 = row[0]
        village = row[5]
        parish = row[4]
        subcounty = row[3]
        stype = row[2]
        mtotal = s1m + s2m + s3m + s4m + s5m + s6m
        ftotal = s1f + s2f + s3f + s4f + s5f + s6f

        c.execute("INSERT INTO secenrollment(school_name,Emis_no,school_type,village,parish,sub_county,category,ownership,s1male,s1female,s2male,s2female,s3male,"
                  "s3female,s4male,s4female,s5male,s5female,s6male,s6female,"
                  "maletotal,femaletotal,datestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school, emis2, stype,village, parish,subcounty,category,
                                                                                                            owership, s1m, s1f, s2m, s2f, s3m, s3f, s4m,
                                                                                                            s4f,s5m, s5f, s6m, s6f, mtotal,ftotal,datestamp))
        conn.commit()

def teacherqualification(school, category, ownership, p1teachers, p2teachers, p3teachers, p4teachers,p5teachers,p6teachers,
                         p7teachers, mlicenced, flicenced, mcertificate, fcertificate, mdeploma, fdeploma, mbachelors,fbachelors,
                         mmasters, fmasters):

    c.execute("SELECT * FROM school WHERE school_name = ?",(school,))
    datestamp = datetime.datetime.today().year
    for row in c.fetchall():
        emis3 = row[0]
        village = row[5]
        parish = row[4]
        subcounty = row[3]
        stype = row[2]

        total = p1teachers + p2teachers + p3teachers + p4teachers + p5teachers + p6teachers + p7teachers

        c.execute("INSERT INTO qualifications(school_name,Emis_no,school_type,village,parish,sub_county, category, ownership, no_p1teachers,"
                  " no_p2teachers, no_p3teachers, no_p4teachers, no_p5teachers, no_p6teachers, no_p7teachers,total,"
                  "licensed_m,licensed_f,certificate_m,certificate_f,m_deploma,f_deploma,m_bachelors,f_bachelors,m_masters,"
                  "f_master,datestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school, emis3, stype, village, parish,subcounty,category, ownership,
                                                                                                       p1teachers, p2teachers, p3teachers, p4teachers,
                                                                                                       p5teachers, p6teachers, p7teachers, total, mlicenced,
                                                                                                       flicenced,mcertificate,fcertificate, mdeploma, fdeploma,
                                                                                                       mbachelors, fbachelors, mmasters, fmasters, datestamp))
        conn.commit()
        
def teachersecqualification(school, category, ownership, s1teachers, s2teachers, s3teachers, s4teachers,s5teachers,s6teachers,
                            mlicenced, flicenced, mcertificate, fcertificate, mdeploma, fdeploma, mbachelors,fbachelors,mmasters, fmasters):

    c.execute("SELECT * FROM school WHERE school_name = ?",(school,))
    datestamp = datetime.datetime.today().year
    for row in c.fetchall():
        emis3 = row[0]
        village = row[5]
        parish = row[4]
        subcounty = row[3]
        stype = row[2]

        total = s1teachers + s2teachers + s3teachers + s4teachers + s5teachers + s6teachers

        c.execute("INSERT INTO secqualifications(school_name,Emis_no,school_type,village,parish,sub_county,category, ownership, no_s1teachers,"
                  " no_s2teachers, no_s3teachers, no_s4teachers, no_s5teachers, no_s6teachers,total,"
                  "licensed_m,licensed_f,certificate_m,certificate_f,m_deploma,f_deploma,m_bachelors,f_bachelors,m_masters,"
                  "f_master,datestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school, emis3, stype, village, parish,subcounty, category, ownership,
                                                                                                     s1teachers, s2teachers, s3teachers, s4teachers,
                                                                                                     s5teachers, s6teachers, total, mlicenced,
                                                                                                     flicenced,mcertificate,fcertificate, mdeploma, fdeploma,
                                                                                                     mbachelors, fbachelors, mmasters, fmasters, datestamp))
        
        conn.commit()
        
def facilities(school, category, ownership, library, sciencelab, complab, kitchen, staffroom,adminblock, dininghall,
               watersupply, stores, workshop, playground, garden, latrine, stances, handwashing, p1desk, p2desk, p3desk,
               p4desk,p5desk,p6desk,p7desk):
    
    c.execute("SELECT * FROM school WHERE school_name = ?",(school,))
    datestamp = datetime.datetime.today().year
    for row in c.fetchall():
        emis4 = row[0]
        village = row[5]
        parish = row[4]
        subcounty = row[3]
        stype = row[2]

        c.execute("INSERT INTO facilities(school_name,Emis_no,school_type,village,parish,sub_county,category,ownership,library,science_lab,computer_lab,"
                  "kitchen,staff_room,administration_block,dining_hall,reliable_safe_water_supply,stores,workshop,playground,school_garden,"
                  "latrine,no_of_stances,handwashing_facility,p1_desk,p2_desk,p3_desk,p4_desk,p5_desk,p6_desk,"
                  "p7_desk,datestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school,emis4,stype,village,parish,subcounty,category,ownership,library,sciencelab,
                                                                                                              complab,kitchen,staffroom,adminblock,dininghall,watersupply,
                                                                                                              stores,workshop,playground,garden,latrine,stances,handwashing,
                                                                                                              p1desk,p2desk,p3desk,p4desk,p5desk,p6desk,p7desk,datestamp))
        

        conn.commit()

def sfacilities(school, category, ownership, library, sciencelab, complab, kitchen, staffroom,adminblock, dininghall,
                watersupply, stores, workshop, playground, garden, latrine, stances, handwashing, s1desk, s2desk, s3desk,
                s4desk,s5desk,s6desk):
    
    c.execute("SELECT * FROM school WHERE school_name = ?",(school,))
    datestamp = datetime.datetime.today().year
    for row in c.fetchall():
        emis4 = row[0]
        village = row[5]
        parish = row[4]
        subcounty = row[3]
        stype = row[2]

        c.execute("INSERT INTO secfacilities(school_name,Emis_no,school_type,village,parish,sub_county,category,ownership,library,science_lab,computer_lab,"
                  "kitchen,staff_room,administration_block,dining_hall,reliable_safe_water_supply,stores,workshop,playground,school_garden,"
                  "latrine,no_of_stances,handwashing_facility,s1_desk,s2_desk,s3_desk,s4_desk,s5_desk,s6_desk,"
                  "datestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school,emis4,stype,village,parish,subcounty,category,ownership,library,sciencelab,
                                                                                                    complab,kitchen,staffroom,adminblock,dininghall,watersupply,
                                                                                                    stores,workshop,playground,garden,latrine,stances,handwashing,
                                                                                                    s1desk,s2desk,s3desk,s4desk,s5desk,s6desk,datestamp))
        

        conn.commit() 

def classroom(school,category,ownership,p1_classroom,p2_classroom,p3_classroom,p4_classroom, p5_classroom, p6_classroom, p7_classroom,
              comppermanent,comptemporary,foundation,window,wallplate,withoutclass):

    c.execute("SELECT * FROM school WHERE school_name = ?",(school,))
    datestamp = datetime.datetime.today().year
    for row in c.fetchall():
        emis5 = row[0]
    
        village = row[5]
        parish = row[4]
        subcounty = row[3]
        stype = row[2]

        total = p1_classroom + p2_classroom + p3_classroom + p4_classroom + p5_classroom + p6_classroom + p7_classroom

        c.execute("INSERT INTO classroom(school_name,Emis_no,school_type,village,parish,sub_county,category,ownership,p1_classroom,"
                  "p2_classroom,p3_classroom, p4_classroom,p5_classroom,p6_classroom,p7_classroom,total_classrooms,"
                  "complete_permanent,complete_temporary,at_foundation,at_window,at_wallplate_and_above,"
                  "number_of_classes_without_structures,datestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school,emis5,stype,village,parish,subcounty,category,ownership,p1_classroom,p2_classroom,p3_classroom,
                                                                                                                           p4_classroom,p5_classroom,p6_classroom,p7_classroom,total,comppermanent,comptemporary,
                                                                                                                           foundation,window,wallplate,withoutclass,datestamp))

        conn.commit()

def sclassroom(school,category,ownership,s1_classroom,s2_classroom,s3_classroom,s4_classroom,s5_classroom,s6_classroom,
               comppermanent,comptemporary,foundation,window,wallplate, withoutclass):

    c.execute("SELECT * FROM school WHERE school_name = ?",(school,))
    datestamp = datetime.datetime.today().year
    for row in c.fetchall():
        emis5 = row[0]
        village = row[5]
        parish = row[4]
        subcounty = row[3]
        stype = row[2]

        total = s1_classroom + s2_classroom + s3_classroom + s4_classroom + s5_classroom + s6_classroom
        
        c.execute("INSERT INTO secclassroom(school_name,Emis_no,school_type,village,parish,sub_county,category,ownership,s1_classroom,"
                  "s2_classroom, s3_classroom, s4_classroom, s5_classroom, s6_classroom,total_classrooms,"
                  "complete_permanent, complete_temporary, at_foundation, at_window,at_wallplate_and_above,number_of_classes_without_structures,datestamp)"
                  " VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school,emis5,stype, village,parish,subcounty,category,ownership,s1_classroom,s2_classroom,s3_classroom,
                                                                          s4_classroom,s5_classroom, s6_classroom, total,comppermanent,comptemporary,
                                                                          foundation,window,wallplate, withoutclass,datestamp))
        conn.commit()


def housing(school,category,ownership,compermanent,comtemporary,foundation,window,wallplate):
    
    c.execute("SELECT * FROM school WHERE school_name = ?",(school,))
    datestamp = datetime.datetime.today().year
    for row in c.fetchall():
        emis5 = row[0]
        village = row[5]
        subcounty = row[3]
        parish = row[4]
        stype = row[2]
        
        c.execute("INSERT INTO teacher_housing(school_name,Emis_no,school_type,village,parish,sub_county,category,ownership, complete_permanent,"
                  "complete_temporary,permanent_at_foundation,permanent_at_window_level,"
                  "permanent_at_wallplate_and_above,datestamp) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school, emis5, stype, village, parish,subcounty, category, ownership, compermanent,
                                                                                                     comtemporary, foundation, window,wallplate,datestamp))
        conn.commit()

def users(fname,sname,uname,password):
    c.execute("INSERT INTO user(first_name,last_name,user_name,passward) VALUES(?,?,?,?)",(fname,sname,uname,password))
    conn.commit()

##################### Home page functions
    
def totalmaleprim():
    date = datetime.datetime.today()
    d = date.year
    m = c.execute("SELECT sum(maletotal) FROM enrollment WHERE datestamp = ?",(d,))
    x = m.fetchone()
    y = x[0]
    return y

def totalmalesec():
    date = datetime.datetime.today().year
    m = c.execute("SELECT sum(maletotal) FROM secenrollment WHERE datestamp = ?",(date,))
    x = m.fetchone()
    y = x[0]
    return y

def totalmalepupils():
    a = totalmaleprim()
    b = totalmalesec()
    try:
        c = a + b
        return c
    except Exception:
        return 0


def totalfemaleprime():
    date = datetime.datetime.today()
    d = date.year
    f = c.execute("SELECT sum(femaletotal) FROM enrollment WHERE datestamp = ?",(d,))
    x = f.fetchone()
    z = x[0]
    return z

def totalfemalesec():
    date = datetime.datetime.today()
    d = date.year
    f = c.execute("SELECT sum(femaletotal) FROM secenrollment WHERE datestamp = ?",(d,))
    x = f.fetchone()
    z = x[0]
    return z

def totalfemalepupils():
    a = totalfemaleprime()
    b = totalfemalesec()
    try:
        c = a + b
        return c
    except Exception:
        return 0

def totalpupils():
    m = totalmalepupils()
    f = totalfemalepupils()
    z = m+f
    return z

def totalclassroomprim():
    date = datetime.datetime.today()
    d = date.year
    g = c.execute("SELECT sum(total_classrooms) FROM classroom WHERE datestamp = ?",(d,))
    x = g.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def totalclassroomsec():
    date = datetime.datetime.today()
    d = date.year
    g = c.execute("SELECT sum(total_classrooms) FROM secclassroom WHERE datestamp = ?",(d,))
    x = g.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def totalclassroom():
    a = totalclassroomprim()
    b = totalclassroomsec()
    try:
        x = a + b
        return x
    except Exception:
        return 0

def district_pupilclassroomratio():
    a = totalclassroom()
    b = totalpupils()
    try:
        x = b/a
        return x
    except Exception:
        return 0

def districtlatrinestancesprime():
    date = datetime.datetime.today()
    d = date.year
    h = c.execute("SELECT sum(no_of_stances) FROM facilities WHERE datestamp = ?",(d,))
    x = h.fetchone()
    b = x[0]
    if b == None:
        return 0
    else:
        return b

def districtlatrinestancesec():
    date = datetime.datetime.today()
    d = date.year
    h = c.execute("SELECT sum(no_of_stances) FROM secfacilities WHERE datestamp = ?",(d,))
    x = h.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def districtlatrinestances():
    a = districtlatrinestancesprime()
    b = districtlatrinestancesec()
    try:
        x = a + b
        return x
    except Exception:
        return 0

def districtpupilstanceratio():
    a = totalpupils()
    b = districtlatrinestances()
    try:
        x = a/b
        return x
    except Exception:
        return 0

def maleteachers():
    h = c.execute("SELECT count(*) FROM teacher WHERE Gender = ?",("Male",))
    x = h.fetchone()
    try:
        e = x[0]
        return e
    except Exception:
        return 0

def femaleteachers():
    h = c.execute("SELECT count(*) FROM teacher WHERE Gender = ?",("Female",))
    x = h.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def totalteachers():
    x = maleteachers()
    y = femaleteachers()
    try:
        r = x + y
        return r
    except Exception:
        return 0

def certificatem():
    date = datetime.datetime.today()
    d = date.year
    t = c.execute("SELECT sum(certificate_m) FROM qualifications WHERE datestamp = ?",(d,))
    x = t.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def certificatef():
    date = datetime.datetime.today()
    d = date.year
    u = c.execute("SELECT sum(certificate_f) FROM qualifications WHERE datestamp = ?",(d,))
    v = u.fetchone()
    a = v[0]
    if a == None:
        return 0
    else:
        return a

def certificatems():
    date = datetime.datetime.today()
    d = date.year
    t = c.execute("SELECT sum(certificate_m) FROM secqualifications WHERE datestamp = ?",(d,))
    x = t.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def certificatefs():
    date = datetime.datetime.today()
    d = date.year
    u = c.execute("SELECT sum(certificate_f) FROM secqualifications WHERE datestamp = ?",(d,))
    v = u.fetchone()
    a = v[0]
    if a == None:
        return 0
    else:
        return a
    
def certificate():
    m = certificatem()
    f = certificatef()
    q = certificatems()
    w = certificatefs()
    try:
        x = m+f+q+w
        return x
    except Exception:
        return 0

def deplomam():
    date = datetime.datetime.today()
    d = date.year
    t = c.execute("SELECT sum(m_deploma) FROM qualifications WHERE datestamp = ?",(d,))
    x = t.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def deplomaf():
    date = datetime.datetime.today()
    d = date.year
    u = c.execute("SELECT sum(f_deploma) FROM qualifications WHERE datestamp = ?",(d,))
    y = u.fetchone()
    a = y[0]
    if a == None:
        return 0
    else:
        return a

def deplomamsec():
    date = datetime.datetime.today()
    d = date.year
    t = c.execute("SELECT sum(m_deploma) FROM secqualifications WHERE datestamp = ?",(d,))
    x = t.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def deplomafsec():
    date = datetime.datetime.today()
    d = date.year
    u = c.execute("SELECT sum(f_deploma) FROM secqualifications WHERE datestamp = ?",(d,))
    y = u.fetchone()
    a = y[0]
    if a == None:
        return 0
    else:
        return a

def deploma():
    x = deplomam()
    y = deplomaf()
    z = deplomamsec()
    q = deplomafsec()
    try:
        g = x+y+z+q
        return g
    except Exception:
        return 0

def bachelorsm():
    date = datetime.datetime.today()
    d = date.year
    t = c.execute("SELECT sum(m_bachelors) FROM qualifications WHERE datestamp = ?",(d,))
    x  = t.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def bachelorsf():
    date = datetime.datetime.today()
    d = date.year
    t = c.execute("SELECT sum(f_bachelors) FROM qualifications WHERE datestamp = ?",(d,))
    x  = t.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def bachelorsmsec():
    date = datetime.datetime.today()
    d = date.year
    t = c.execute("SELECT sum(m_bachelors) FROM secqualifications WHERE datestamp = ?",(d,))
    x  = t.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def bachelorsfsec():
    date = datetime.datetime.today()
    d = date.year
    t = c.execute("SELECT sum(f_bachelors) FROM secqualifications WHERE datestamp = ?",(d,))
    x  = t.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def bachelors():
    a = bachelorsm()
    b = bachelorsf()
    c = bachelorsmsec()
    d = bachelorsfsec()
    try:
        x = a + b + c +d
        return x
    except Exception:
        return 0

def mastersm():
    date = datetime.datetime.today()
    d = date.year
    t = c.execute("SELECT sum(m_masters) FROM qualifications WHERE datestamp = ?",(d,))
    x = t.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def mastersf():
    date = datetime.datetime.today()
    d = date.year
    t = c.execute("SELECT sum(f_master) FROM qualifications WHERE datestamp = ?",(d,))
    x = t.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def mastersmsec():
    date = datetime.datetime.today()
    d = date.year
    t = c.execute("SELECT sum(m_masters) FROM secqualifications WHERE datestamp = ?",(d,))
    x = t.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def mastersfsec():
    date = datetime.datetime.today()
    d = date.year
    t = c.execute("SELECT sum(f_master) FROM secqualifications WHERE datestamp = ?",(d,))
    x = t.fetchone()
    a = x[0]
    if a == None:
        return 0
    else:
        return a

def masters():
    a = mastersm()
    b = mastersf()
    c = mastersmsec()
    d = mastersfsec()
    try:
        x = a+b+c+d
        return x
    except Exception:
        return 0
############################################################# REPORT FUNCTIONS
    
def totaldeskpri():
    d = datetime.datetime.today().year
    try:
        h = c.execute("SELECT sum(p1_desk+p2_desk+p3_desk+p4_desk+p5_desk+p6_desk+p7_desk) FROM facilities WHERE datestamp =?)",(d,))
        x = h.fetchone()
        y = x[0]
        return y
    
    except Exception:
        return 0

def totaldesksec():
    d = datetime.datetime.today().year
    try:
        h = c.execute("SELECT sum(s1_desk+s2_desk+s3_desk+s4_desk+s5_desk+s6_desk) FROM secfacilities WHERE datestamp =?)",(d,))
        x = h.fetchone()
        y = x[0]
        return y
    except Exception:
        return 0
    
def totaldesk():
    a = totaldeskpri()
    b = totaldesksec()
    try:
        c = a+b
        return c
    except Exception:
        return 0

############################### SUB COUNTY AND PARISH FUNCTIONS

def totalmalep(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(maletotal) FROM enrollment WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    h = x[0]
    if h == None:
        return 0
    else:
        return h

def totalfemalep(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(femaletotal) FROM enrollment WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    h = x[0]
    if h == None:
        return 0
    else:
        return h

def totalmales(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(maletotal) FROM secenrollment WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def totalfemales(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(femaletotal) FROM secenrollment WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def classroompri(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(p1_classroom+p2_classroom+p3_classroom+p4_classroom+p5_classroom+p6_classroom+p7_classroom) FROM classroom WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def classroomsec(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(s1_classroom+s2_classroom+s3_classroom+s4_classroom+s5_classroom+s6_classroom) FROM secclassroom WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def stancepri(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(no_of_stances) FROM facilities WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def stancesec(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(no_of_stances) FROM secfacilities WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def deskpri(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(p1_desk+p2_desk+p3_desk+p4_desk+p5_desk+p6_desk+p7_desk) FROM facilities WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def desksec(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(s1_desk+s2_desk+s3_desk+s4_desk+s5_desk+s6_desk) FROM secfacilities WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def teachpri(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(total) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def teachsec(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(total) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def ftr(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT count(*) FROM teacher WHERE Gender = ? AND sub_county = ?",("Female",subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def mtr(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT count(*) FROM teacher WHERE Gender = ? AND sub_county = ?",("Male",subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def certm(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(certificate_m) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def certf(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(certificate_f) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def certms(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(certificate_m) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def certfs(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(certificate_f) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def licm(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(licensed_m) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def licf(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(licensed_f) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def licms(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(licensed_m) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def licfs(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(licensed_f) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def depm(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(m_deploma) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def depf(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(f_deploma) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def depms(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(m_deploma) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def depfs(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(f_deploma) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def bacm(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(m_bachelors) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def bacf(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(f_bachelors) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def bacms(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(m_bachelors) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def bacfs(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(f_bachelors) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def masm(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(m_masters) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def masf(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(f_master) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def masms(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(m_masters) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def masfs(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(f_master) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

####################################################################### Parish

def ptotalmalep(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(maletotal) FROM enrollment WHERE datestamp = ? AND parish = ?",(d,subcounty))
    x = m.fetchone()
    h = x[0]
    if h == None:
        return 0
    else:
        return h

def ptotalfemalep(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(femaletotal) FROM enrollment WHERE datestamp = ? AND parish = ?",(d,subcounty))
    x = m.fetchone()
    h = x[0]
    if h == None:
        return 0
    else:
        return h

def ptotalmales(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(maletotal) FROM secenrollment WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def ptotalfemales(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(femaletotal) FROM secenrollment WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pclassroompri(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(p1_classroom+p2_classroom+p3_classroom+p4_classroom+p5_classroom+p6_classroom+p7_classroom) FROM classroom WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pclassroomsec(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(s1_classroom+s2_classroom+s3_classroom+s4_classroom+s5_classroom+s6_classroom) FROM secclassroom WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pstancepri(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(no_of_stances) FROM facilities WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pstancesec(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(no_of_stances) FROM secfacilities WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pdeskpri(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(p1_desk+p2_desk+p3_desk+p4_desk+p5_desk+p6_desk+p7_desk) FROM facilities WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pdesksec(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(s1_desk+s2_desk+s3_desk+s4_desk+s5_desk+s6_desk) FROM secfacilities WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pteachpri(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(total) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pteachsec(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(total) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pftr(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT count(*) FROM teacher WHERE Gender = ? AND sub_county = ?",("Female",subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pmtr(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT count(*) FROM teacher WHERE Gender = ? AND sub_county = ?",("Male",subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pcertm(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(certificate_m) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pcertf(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(certificate_f) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pcertms(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(certificate_m) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pcertfs(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(certificate_f) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def plicm(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(licensed_m) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def plicf(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(licensed_f) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def plicms(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(licensed_m) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def plicfs(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(licensed_f) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pdepm(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(m_deploma) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pdepf(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(f_deploma) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pdepms(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(m_deploma) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pdepfs(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(f_deploma) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pbacm(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(m_bachelors) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pbacf(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(f_bachelors) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pbacms(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(m_bachelors) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pbacfs(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(f_bachelors) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pmasm(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(m_masters) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pmasf(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(f_master) FROM qualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pmasms(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(m_masters) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

def pmasfs(subcounty):
    d = datetime.datetime.today().year
    m = c.execute("SELECT sum(f_master) FROM secqualifications WHERE datestamp = ? AND sub_county = ?",(d,subcounty))
    x = m.fetchone()
    g = x[0]
    if g == None:
        return 0
    else:
        return g

##################################################################### Graph Function
def p1tm():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p1male) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    p1 = b[0]
    return p1

def p1tf():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p1female) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    p1 = b[0]
    return p1

def p2tm():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p2male) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    p1 = b[0]
    return p1

def p2tf():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p2female) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    p1 = b[0]
    return p1

def p3tm():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p3male) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    e = b[0]
    return e

def p3tf():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p3female) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    e = b[0]
    return e

def p4tm():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p4male) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    p1 = b[0]
    return p1

def p4tf():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p4female) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    p1 = b[0]
    return p1

def p5tm():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p5male) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    p1 = b[0]
    return p1

def p5tf():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p5female) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    p1 = b[0]
    return p1

def p6tm():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p6male) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    p1 = b[0]
    return p1

def p6tf():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p6female) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    p1 = b[0]
    return p1

def p7tm():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p7male) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    p1 = b[0]
    return p1

def p7tf():
    d = datetime.datetime.today().year
    a = c.execute("SELECT sum(p7female) FROM enrollment WHERE datestamp = ?",(d,))
    b = a.fetchone()
    p1 = b[0]
    return p1
####################################################################
def success():
    QMessageBox.warning(self,"Success","Record Saved")


#########################################################################################################

create_school_table()
create_user_table()
create_teacher_table()
create_enrollment_table()
create_senrollment_table()
create_teacher_qualifications_table()
create_steacher_qualifications_table()
create_school_facilities_table()
create_school_sfacilities_table()
create_classroom_table()
create_sclassroom_table()
create_teacher_housing_table()
create_leave_table()
create_retired_table()
create_deceased_table()
create_absconded_table()

############################## GUI class
class Login(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Login,self).__init__(parent)
        self.setWindowTitle("LogIn")
##        self.resize(100, 300)
        self.textName = QtWidgets.QLineEdit(self)
        self.textName.setPlaceholderText("Enter User Name")
        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setPlaceholderText("Enter Passward")
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buttonLogin = QtWidgets.QPushButton('Login',self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        x = "districtdb"
        y = "1234district5"
        a = self.textName.text()
        b = self.textPass.text()
        if self.textName.text() == x and self.textPass.text() == y:
            self.accept()

        else:
            c.execute("SELECT * FROM user WHERE user_name = ? AND passward = ?",(a,b))
            if len(c.fetchall()) > 0: 
                self.accept()
                
            else:
                QtWidgets.QMessageBox.warning(self,'Error','Incorrect Username or password')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1056, 735)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(9, 0, 1041, 701))
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.frame_3 = QtWidgets.QFrame(self.page)
        self.frame_3.setGeometry(QtCore.QRect(240, 15, 851, 831))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setGeometry(QtCore.QRect(10, 0, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setGeometry(QtCore.QRect(10, 29, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(10, 73, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(10, 110, 100, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 281, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        self.label_8.setGeometry(QtCore.QRect(10, 233, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(10, 272, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(456, 20, 201, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(456, 63, 61, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(456, 103, 70, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_3)
        self.label_13.setGeometry(QtCore.QRect(456, 179, 250, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(456, 223, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_3)
        self.label_15.setGeometry(QtCore.QRect(457, 263, 121, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(460, 344, 211, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        self.label_17.setGeometry(QtCore.QRect(10, 151, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setGeometry(QtCore.QRect(10, 316, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.frame_3)
        self.label_19.setGeometry(QtCore.QRect(454, 143, 61, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.frame_3)
        self.label_20.setGeometry(QtCore.QRect(460, 304, 91, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(90, 77, 351, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 118, 351, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 158, 351, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 188, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setFrame(False)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 233, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setFrame(False)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(290, 277, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(290, 318, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(536, 66, 261, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setFrame(False)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(536, 109, 261, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setFrame(False)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(536, 149, 261, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setFrame(False)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(569, 224, 231, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setFrame(False)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(570, 265, 231, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setFrame(False)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.lineEdit_13 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(570, 307, 231, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_13.setFont(font)
        self.lineEdit_13.setFrame(False)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_14 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_14.setGeometry(QtCore.QRect(642, 349, 161, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_14.setFont(font)
        self.lineEdit_14.setFrame(False)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.widget_3 = MplWidget(self.frame_3)
        self.widget_3.setGeometry(QtCore.QRect(0, 380, 801, 231))
        self.widget_3.setObjectName("widget_3")
        self.label_265 = QtWidgets.QLabel(self.frame_3)
        self.label_265.setGeometry(QtCore.QRect(10, 358, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_265.setFont(font)
        self.label_265.setObjectName("label_265")
        self.frame_2 = QtWidgets.QFrame(self.page)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 231, 721))
        self.frame_2.setMouseTracking(True)
        self.frame_2.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.Enterdata = QtWidgets.QPushButton(self.frame_2)
        self.Enterdata.setGeometry(QtCore.QRect(10, 10, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Enterdata.setFont(font)
        self.Enterdata.setMouseTracking(True)
        self.Enterdata.setTabletTracking(False)
        self.Enterdata.setAutoDefault(False)
        self.Enterdata.setDefault(False)
        self.Enterdata.setFlat(False)
        self.Enterdata.setObjectName("Enterdata")
        self.Reports = QtWidgets.QPushButton(self.frame_2)
        self.Reports.setGeometry(QtCore.QRect(10, 70, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Reports.setFont(font)
        self.Reports.setMouseTracking(True)
        self.Reports.setObjectName("Reports")
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setGeometry(QtCore.QRect(0, 580, 231, 101))
        self.textEdit.setObjectName("textEdit")
        self.Reports_2 = QtWidgets.QPushButton(self.frame_2)
        self.Reports_2.setGeometry(QtCore.QRect(10, 130, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Reports_2.setFont(font)
        self.Reports_2.setMouseTracking(True)
        self.Reports_2.setObjectName("Reports_2")
        self.Reports_3 = QtWidgets.QPushButton(self.frame_2)
        self.Reports_3.setGeometry(QtCore.QRect(10, 190, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Reports_3.setFont(font)
        self.Reports_3.setMouseTracking(True)
        self.Reports_3.setObjectName("Reports_3")
        self.Reports_4 = QtWidgets.QPushButton(self.frame_2)
        self.Reports_4.setGeometry(QtCore.QRect(10, 250, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Reports_4.setFont(font)
        self.Reports_4.setMouseTracking(True)
        self.Reports_4.setObjectName("Reports_4")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.teacherqualificationform = QtWidgets.QPushButton(self.page_2)
        self.teacherqualificationform.setGeometry(QtCore.QRect(500, 170, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.teacherqualificationform.setFont(font)
        self.teacherqualificationform.setMouseTracking(True)
        self.teacherqualificationform.setObjectName("teacherqualificationform")
        self.label_21 = QtWidgets.QLabel(self.page_2)
        self.label_21.setGeometry(QtCore.QRect(490, 0, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.schoolenrollmentform = QtWidgets.QPushButton(self.page_2)
        self.schoolenrollmentform.setGeometry(QtCore.QRect(500, 100, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.schoolenrollmentform.setFont(font)
        self.schoolenrollmentform.setMouseTracking(True)
        self.schoolenrollmentform.setObjectName("schoolenrollmentform")
        self.addnewteacher = QtWidgets.QPushButton(self.page_2)
        self.addnewteacher.setGeometry(QtCore.QRect(210, 170, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.addnewteacher.setFont(font)
        self.addnewteacher.setMouseTracking(True)
        self.addnewteacher.setObjectName("addnewteacher")
        self.schoolfacilitiesform = QtWidgets.QPushButton(self.page_2)
        self.schoolfacilitiesform.setGeometry(QtCore.QRect(500, 240, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.schoolfacilitiesform.setFont(font)
        self.schoolfacilitiesform.setMouseTracking(True)
        self.schoolfacilitiesform.setObjectName("schoolfacilitiesform")
        self.addnewschool = QtWidgets.QPushButton(self.page_2)
        self.addnewschool.setGeometry(QtCore.QRect(210, 100, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.addnewschool.setFont(font)
        self.addnewschool.setMouseTracking(True)
        self.addnewschool.setObjectName("addnewschool")
        self.teacherhousingform = QtWidgets.QPushButton(self.page_2)
        self.teacherhousingform.setGeometry(QtCore.QRect(210, 240, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.teacherhousingform.setFont(font)
        self.teacherhousingform.setMouseTracking(True)
        self.teacherhousingform.setObjectName("teacherhousingform")
        self.schoolclassroomform = QtWidgets.QPushButton(self.page_2)
        self.schoolclassroomform.setGeometry(QtCore.QRect(500, 310, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.schoolclassroomform.setFont(font)
        self.schoolclassroomform.setMouseTracking(True)
        self.schoolclassroomform.setObjectName("schoolclassroomform")
        self.frame = QtWidgets.QFrame(self.page_2)
        self.frame.setGeometry(QtCore.QRect(0, 10, 181, 701))
        self.frame.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_47 = QtWidgets.QLabel(self.page_2)
        self.label_47.setGeometry(QtCore.QRect(270, 60, 91, 31))
        self.label_47.setObjectName("label_47")
        self.label_48 = QtWidgets.QLabel(self.page_2)
        self.label_48.setGeometry(QtCore.QRect(550, 55, 141, 31))
        self.label_48.setObjectName("label_48")
        self.pushButton_15 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_15.setGeometry(QtCore.QRect(790, 100, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_15.setFont(font)
        self.pushButton_15.setObjectName("pushButton_15")
        self.label_49 = QtWidgets.QLabel(self.page_2)
        self.label_49.setGeometry(QtCore.QRect(830, 54, 141, 31))
        self.label_49.setObjectName("label_49")
        self.pushButton_30 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_30.setGeometry(QtCore.QRect(790, 170, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setObjectName("pushButton_30")
        self.pushButton_31 = QtWidgets.QPushButton(self.page_2)
        self.pushButton_31.setGeometry(QtCore.QRect(790, 240, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setObjectName("pushButton_31")
        self.schoolclassroomform_2 = QtWidgets.QPushButton(self.page_2)
        self.schoolclassroomform_2.setGeometry(QtCore.QRect(790, 310, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.schoolclassroomform_2.setFont(font)
        self.schoolclassroomform_2.setMouseTracking(True)
        self.schoolclassroomform_2.setObjectName("schoolclassroomform_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_22 = QtWidgets.QLabel(self.page_3)
        self.label_22.setGeometry(QtCore.QRect(500, 0, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.frame_5 = QtWidgets.QFrame(self.page_3)
        self.frame_5.setGeometry(QtCore.QRect(210, 620, 821, 71))
        self.frame_5.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.home = QtWidgets.QPushButton(self.page_3)
        self.home.setGeometry(QtCore.QRect(50, 60, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home.setFont(font)
        self.home.setMouseTracking(True)
        self.home.setObjectName("home")
        self.pushButton_4 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 160, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setMouseTracking(True)
        self.pushButton_4.setObjectName("pushButton_4")
        self.frame_6 = QtWidgets.QFrame(self.page_3)
        self.frame_6.setGeometry(QtCore.QRect(199, 59, 861, 551))
        self.frame_6.setStyleSheet("border-top-color: rgb(0, 0, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_25 = QtWidgets.QLabel(self.frame_6)
        self.label_25.setGeometry(QtCore.QRect(40, 30, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setMouseTracking(True)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.frame_6)
        self.label_26.setGeometry(QtCore.QRect(40, 100, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setMouseTracking(True)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.frame_6)
        self.label_27.setGeometry(QtCore.QRect(40, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setMouseTracking(True)
        self.label_27.setObjectName("label_27")
        self.label_28 = QtWidgets.QLabel(self.frame_6)
        self.label_28.setGeometry(QtCore.QRect(40, 270, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setMouseTracking(True)
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(self.frame_6)
        self.label_29.setGeometry(QtCore.QRect(40, 330, 131, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setMouseTracking(True)
        self.label_29.setObjectName("label_29")
        self.emis = QtWidgets.QLineEdit(self.frame_6)
        self.emis.setGeometry(QtCore.QRect(170, 30, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.emis.setFont(font)
        self.emis.setObjectName("emis")
        self.school = QtWidgets.QLineEdit(self.frame_6)
        self.school.setGeometry(QtCore.QRect(170, 90, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.school.setFont(font)
        self.school.setObjectName("school")
        self.subcounty = QtWidgets.QLineEdit(self.frame_6)
        self.subcounty.setGeometry(QtCore.QRect(170, 210, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.subcounty.setFont(font)
        self.subcounty.setObjectName("subcounty")
        self.parish = QtWidgets.QLineEdit(self.frame_6)
        self.parish.setGeometry(QtCore.QRect(170, 270, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.parish.setFont(font)
        self.parish.setObjectName("parish")
        self.village = QtWidgets.QLineEdit(self.frame_6)
        self.village.setGeometry(QtCore.QRect(170, 330, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.village.setFont(font)
        self.village.setObjectName("village")
        self.save = QtWidgets.QPushButton(self.frame_6)
        self.save.setGeometry(QtCore.QRect(230, 400, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save.setFont(font)
        self.save.setObjectName("save")
        self.label_50 = QtWidgets.QLabel(self.frame_6)
        self.label_50.setGeometry(QtCore.QRect(40, 160, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_50.setFont(font)
        self.label_50.setMouseTracking(True)
        self.label_50.setObjectName("label_50")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_6)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 160, 131, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.pushButton_34 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_34.setGeometry(QtCore.QRect(750, 30, 75, 41))
        self.pushButton_34.setObjectName("pushButton_34")
        self.save_2 = QtWidgets.QPushButton(self.frame_6)
        self.save_2.setGeometry(QtCore.QRect(560, 400, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_2.setFont(font)
        self.save_2.setObjectName("save_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 110, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setMouseTracking(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_30 = QtWidgets.QLabel(self.page_4)
        self.label_30.setGeometry(QtCore.QRect(180, -10, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.frame_7 = QtWidgets.QFrame(self.page_4)
        self.frame_7.setGeometry(QtCore.QRect(170, 30, 871, 671))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_85 = QtWidgets.QLabel(self.frame_7)
        self.label_85.setGeometry(QtCore.QRect(10, 20, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_85.setFont(font)
        self.label_85.setObjectName("label_85")
        self.label_86 = QtWidgets.QLabel(self.frame_7)
        self.label_86.setGeometry(QtCore.QRect(10, 60, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_86.setFont(font)
        self.label_86.setObjectName("label_86")
        self.label_87 = QtWidgets.QLabel(self.frame_7)
        self.label_87.setGeometry(QtCore.QRect(10, 100, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_87.setFont(font)
        self.label_87.setObjectName("label_87")
        self.label_88 = QtWidgets.QLabel(self.frame_7)
        self.label_88.setGeometry(QtCore.QRect(469, 91, 71, 29))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_88.setFont(font)
        self.label_88.setObjectName("label_88")
        self.label_89 = QtWidgets.QLabel(self.frame_7)
        self.label_89.setGeometry(QtCore.QRect(10, 140, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_89.setFont(font)
        self.label_89.setObjectName("label_89")
        self.label_91 = QtWidgets.QLabel(self.frame_7)
        self.label_91.setGeometry(QtCore.QRect(10, 180, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_91.setFont(font)
        self.label_91.setObjectName("label_91")
        self.label_92 = QtWidgets.QLabel(self.frame_7)
        self.label_92.setGeometry(QtCore.QRect(10, 260, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_92.setFont(font)
        self.label_92.setObjectName("label_92")
        self.label_93 = QtWidgets.QLabel(self.frame_7)
        self.label_93.setGeometry(QtCore.QRect(10, 300, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_93.setFont(font)
        self.label_93.setObjectName("label_93")
        self.label_94 = QtWidgets.QLabel(self.frame_7)
        self.label_94.setGeometry(QtCore.QRect(10, 340, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_94.setFont(font)
        self.label_94.setObjectName("label_94")
        self.label_95 = QtWidgets.QLabel(self.frame_7)
        self.label_95.setGeometry(QtCore.QRect(10, 380, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_95.setFont(font)
        self.label_95.setObjectName("label_95")
        self.label_96 = QtWidgets.QLabel(self.frame_7)
        self.label_96.setGeometry(QtCore.QRect(10, 420, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_96.setFont(font)
        self.label_96.setObjectName("label_96")
        self.label_97 = QtWidgets.QLabel(self.frame_7)
        self.label_97.setGeometry(QtCore.QRect(10, 460, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_97.setFont(font)
        self.label_97.setObjectName("label_97")
        self.label_98 = QtWidgets.QLabel(self.frame_7)
        self.label_98.setGeometry(QtCore.QRect(10, 500, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_98.setFont(font)
        self.label_98.setObjectName("label_98")
        self.label_99 = QtWidgets.QLabel(self.frame_7)
        self.label_99.setGeometry(QtCore.QRect(10, 540, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_99.setFont(font)
        self.label_99.setObjectName("label_99")
        self.label_100 = QtWidgets.QLabel(self.frame_7)
        self.label_100.setGeometry(QtCore.QRect(10, 580, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_100.setFont(font)
        self.label_100.setObjectName("label_100")
        self.label_101 = QtWidgets.QLabel(self.frame_7)
        self.label_101.setGeometry(QtCore.QRect(10, 611, 131, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_101.setFont(font)
        self.label_101.setObjectName("label_101")
        self.save_4 = QtWidgets.QPushButton(self.frame_7)
        self.save_4.setGeometry(QtCore.QRect(280, 610, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_4.setFont(font)
        self.save_4.setMouseTracking(True)
        self.save_4.setObjectName("save_4")
        self.school_4 = QtWidgets.QLineEdit(self.frame_7)
        self.school_4.setGeometry(QtCore.QRect(160, 10, 551, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.school_4.setFont(font)
        self.school_4.setObjectName("school_4")
        self.subcounty_4 = QtWidgets.QLineEdit(self.frame_7)
        self.subcounty_4.setGeometry(QtCore.QRect(160, 50, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.subcounty_4.setFont(font)
        self.subcounty_4.setObjectName("subcounty_4")
        self.name_3 = QtWidgets.QLineEdit(self.frame_7)
        self.name_3.setGeometry(QtCore.QRect(160, 90, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.name_3.setFont(font)
        self.name_3.setObjectName("name_3")
        self.gendercombo_3 = QtWidgets.QComboBox(self.frame_7)
        self.gendercombo_3.setGeometry(QtCore.QRect(540, 91, 61, 30))
        self.gendercombo_3.setObjectName("gendercombo_3")
        self.gendercombo_3.addItem("")
        self.gendercombo_3.addItem("")
        self.lineEdit_32 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_32.setGeometry(QtCore.QRect(160, 170, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_32.setFont(font)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_33.setGeometry(QtCore.QRect(160, 250, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_33.setFont(font)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.lineEdit_34 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_34.setGeometry(QtCore.QRect(160, 290, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_34.setFont(font)
        self.lineEdit_34.setObjectName("lineEdit_34")
        self.lineEdit_35 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_35.setGeometry(QtCore.QRect(160, 330, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_35.setFont(font)
        self.lineEdit_35.setObjectName("lineEdit_35")
        self.lineEdit_36 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_36.setGeometry(QtCore.QRect(160, 370, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_36.setFont(font)
        self.lineEdit_36.setObjectName("lineEdit_36")
        self.lineEdit_37 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_37.setGeometry(QtCore.QRect(170, 410, 701, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_37.setFont(font)
        self.lineEdit_37.setObjectName("lineEdit_37")
        self.lineEdit_38 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_38.setGeometry(QtCore.QRect(260, 450, 611, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_38.setFont(font)
        self.lineEdit_38.setObjectName("lineEdit_38")
        self.lineEdit_39 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_39.setGeometry(QtCore.QRect(160, 490, 641, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_39.setFont(font)
        self.lineEdit_39.setObjectName("lineEdit_39")
        self.lineEdit_40 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_40.setGeometry(QtCore.QRect(160, 530, 711, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_40.setFont(font)
        self.lineEdit_40.setObjectName("lineEdit_40")
        self.lineEdit_41 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_41.setGeometry(QtCore.QRect(220, 570, 651, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_41.setFont(font)
        self.lineEdit_41.setObjectName("lineEdit_41")
        self.comboBox_4 = QtWidgets.QComboBox(self.frame_7)
        self.comboBox_4.setGeometry(QtCore.QRect(160, 610, 69, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.lineEdit_42 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_42.setGeometry(QtCore.QRect(570, 170, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_42.setFont(font)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.label_102 = QtWidgets.QLabel(self.frame_7)
        self.label_102.setGeometry(QtCore.QRect(430, 180, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_102.setFont(font)
        self.label_102.setObjectName("label_102")
        self.lineEdit_43 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_43.setGeometry(QtCore.QRect(160, 210, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_43.setFont(font)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.label_103 = QtWidgets.QLabel(self.frame_7)
        self.label_103.setGeometry(QtCore.QRect(10, 220, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_103.setFont(font)
        self.label_103.setObjectName("label_103")
        self.lineEdit_44 = QtWidgets.QLineEdit(self.frame_7)
        self.lineEdit_44.setGeometry(QtCore.QRect(550, 210, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_44.setFont(font)
        self.lineEdit_44.setObjectName("lineEdit_44")
        self.label_104 = QtWidgets.QLabel(self.frame_7)
        self.label_104.setGeometry(QtCore.QRect(430, 220, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_104.setFont(font)
        self.label_104.setObjectName("label_104")
        self.label_105 = QtWidgets.QLabel(self.frame_7)
        self.label_105.setGeometry(QtCore.QRect(430, 135, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_105.setFont(font)
        self.label_105.setObjectName("label_105")
        self.dateEdit = QtWidgets.QDateEdit(self.frame_7)
        self.dateEdit.setGeometry(QtCore.QRect(160, 131, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.dateEdit.setFont(font)
        self.dateEdit.setMouseTracking(True)
        self.dateEdit.setTabletTracking(True)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(1990, 12, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_110 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_110.setGeometry(QtCore.QRect(810, 490, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_110.setFont(font)
        self.pushButton_110.setObjectName("pushButton_110")
        self.save_12 = QtWidgets.QPushButton(self.frame_7)
        self.save_12.setGeometry(QtCore.QRect(640, 610, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_12.setFont(font)
        self.save_12.setMouseTracking(True)
        self.save_12.setObjectName("save_12")
        self.frame_44 = QtWidgets.QFrame(self.frame_7)
        self.frame_44.setGeometry(QtCore.QRect(720, 0, 131, 141))
        self.frame_44.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_44.setObjectName("frame_44")
        self.pushButton_125 = QtWidgets.QPushButton(self.frame_7)
        self.pushButton_125.setGeometry(QtCore.QRect(759, 144, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_125.setFont(font)
        self.pushButton_125.setObjectName("pushButton_125")
        self.frame_8 = QtWidgets.QFrame(self.page_4)
        self.frame_8.setGeometry(QtCore.QRect(0, 30, 161, 191))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.home_4 = QtWidgets.QPushButton(self.frame_8)
        self.home_4.setGeometry(QtCore.QRect(10, -40, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_4.setFont(font)
        self.home_4.setMouseTracking(True)
        self.home_4.setObjectName("home_4")
        self.back_3 = QtWidgets.QPushButton(self.frame_8)
        self.back_3.setGeometry(QtCore.QRect(0, 20, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_3.setFont(font)
        self.back_3.setMouseTracking(True)
        self.back_3.setObjectName("back_3")
        self.viewteachertable_3 = QtWidgets.QPushButton(self.frame_8)
        self.viewteachertable_3.setGeometry(QtCore.QRect(0, 80, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.viewteachertable_3.setFont(font)
        self.viewteachertable_3.setMouseTracking(True)
        self.viewteachertable_3.setObjectName("viewteachertable_3")
        self.frame_9 = QtWidgets.QFrame(self.page_4)
        self.frame_9.setGeometry(QtCore.QRect(0, 170, 161, 501))
        self.frame_9.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.frame_10 = QtWidgets.QFrame(self.page_5)
        self.frame_10.setGeometry(QtCore.QRect(20, 0, 201, 151))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.home_5 = QtWidgets.QPushButton(self.frame_10)
        self.home_5.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_5.setFont(font)
        self.home_5.setObjectName("home_5")
        self.back_4 = QtWidgets.QPushButton(self.frame_10)
        self.back_4.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_4.setFont(font)
        self.back_4.setObjectName("back_4")
        self.pushButton_35 = QtWidgets.QPushButton(self.frame_10)
        self.pushButton_35.setGeometry(QtCore.QRect(10, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_35.setFont(font)
        self.pushButton_35.setObjectName("pushButton_35")
        self.frame_11 = QtWidgets.QFrame(self.page_5)
        self.frame_11.setGeometry(QtCore.QRect(230, 40, 841, 611))
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.label_112 = QtWidgets.QLabel(self.frame_11)
        self.label_112.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_112.setFont(font)
        self.label_112.setObjectName("label_112")
        self.label_115 = QtWidgets.QLabel(self.frame_11)
        self.label_115.setGeometry(QtCore.QRect(10, 40, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_115.setFont(font)
        self.label_115.setObjectName("label_115")
        self.label_116 = QtWidgets.QLabel(self.frame_11)
        self.label_116.setGeometry(QtCore.QRect(10, 70, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_116.setFont(font)
        self.label_116.setObjectName("label_116")
        self.label_117 = QtWidgets.QLabel(self.frame_11)
        self.label_117.setGeometry(QtCore.QRect(10, 100, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_117.setFont(font)
        self.label_117.setObjectName("label_117")
        self.label_118 = QtWidgets.QLabel(self.frame_11)
        self.label_118.setGeometry(QtCore.QRect(10, 130, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_118.setFont(font)
        self.label_118.setObjectName("label_118")
        self.label_119 = QtWidgets.QLabel(self.frame_11)
        self.label_119.setGeometry(QtCore.QRect(10, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_119.setFont(font)
        self.label_119.setObjectName("label_119")
        self.label_120 = QtWidgets.QLabel(self.frame_11)
        self.label_120.setGeometry(QtCore.QRect(10, 190, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_120.setFont(font)
        self.label_120.setObjectName("label_120")
        self.label_121 = QtWidgets.QLabel(self.frame_11)
        self.label_121.setGeometry(QtCore.QRect(10, 250, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_121.setFont(font)
        self.label_121.setObjectName("label_121")
        self.label_122 = QtWidgets.QLabel(self.frame_11)
        self.label_122.setGeometry(QtCore.QRect(10, 220, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_122.setFont(font)
        self.label_122.setObjectName("label_122")
        self.label_123 = QtWidgets.QLabel(self.frame_11)
        self.label_123.setGeometry(QtCore.QRect(10, 310, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_123.setFont(font)
        self.label_123.setObjectName("label_123")
        self.label_124 = QtWidgets.QLabel(self.frame_11)
        self.label_124.setGeometry(QtCore.QRect(10, 280, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_124.setFont(font)
        self.label_124.setObjectName("label_124")
        self.label_125 = QtWidgets.QLabel(self.frame_11)
        self.label_125.setGeometry(QtCore.QRect(10, 370, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_125.setFont(font)
        self.label_125.setObjectName("label_125")
        self.label_126 = QtWidgets.QLabel(self.frame_11)
        self.label_126.setGeometry(QtCore.QRect(10, 340, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_126.setFont(font)
        self.label_126.setObjectName("label_126")
        self.label_127 = QtWidgets.QLabel(self.frame_11)
        self.label_127.setGeometry(QtCore.QRect(10, 430, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_127.setFont(font)
        self.label_127.setObjectName("label_127")
        self.label_128 = QtWidgets.QLabel(self.frame_11)
        self.label_128.setGeometry(QtCore.QRect(10, 400, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_128.setFont(font)
        self.label_128.setObjectName("label_128")
        self.label_129 = QtWidgets.QLabel(self.frame_11)
        self.label_129.setGeometry(QtCore.QRect(10, 490, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_129.setFont(font)
        self.label_129.setObjectName("label_129")
        self.label_130 = QtWidgets.QLabel(self.frame_11)
        self.label_130.setGeometry(QtCore.QRect(10, 460, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_130.setFont(font)
        self.label_130.setObjectName("label_130")
        self.save_5 = QtWidgets.QPushButton(self.frame_11)
        self.save_5.setGeometry(QtCore.QRect(180, 520, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_5.setFont(font)
        self.save_5.setObjectName("save_5")
        self.category = QtWidgets.QLineEdit(self.frame_11)
        self.category.setGeometry(QtCore.QRect(150, 40, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.category.setFont(font)
        self.category.setObjectName("category")
        self.p1m = QtWidgets.QLineEdit(self.frame_11)
        self.p1m.setGeometry(QtCore.QRect(150, 100, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p1m.setFont(font)
        self.p1m.setObjectName("p1m")
        self.p1f = QtWidgets.QLineEdit(self.frame_11)
        self.p1f.setGeometry(QtCore.QRect(150, 130, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p1f.setFont(font)
        self.p1f.setObjectName("p1f")
        self.p2m = QtWidgets.QLineEdit(self.frame_11)
        self.p2m.setGeometry(QtCore.QRect(150, 160, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p2m.setFont(font)
        self.p2m.setObjectName("p2m")
        self.p2f = QtWidgets.QLineEdit(self.frame_11)
        self.p2f.setGeometry(QtCore.QRect(150, 190, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p2f.setFont(font)
        self.p2f.setObjectName("p2f")
        self.p3m = QtWidgets.QLineEdit(self.frame_11)
        self.p3m.setGeometry(QtCore.QRect(150, 220, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p3m.setFont(font)
        self.p3m.setObjectName("p3m")
        self.p3f = QtWidgets.QLineEdit(self.frame_11)
        self.p3f.setGeometry(QtCore.QRect(150, 250, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p3f.setFont(font)
        self.p3f.setObjectName("p3f")
        self.p4m = QtWidgets.QLineEdit(self.frame_11)
        self.p4m.setGeometry(QtCore.QRect(150, 280, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p4m.setFont(font)
        self.p4m.setObjectName("p4m")
        self.p4f = QtWidgets.QLineEdit(self.frame_11)
        self.p4f.setGeometry(QtCore.QRect(150, 310, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p4f.setFont(font)
        self.p4f.setObjectName("p4f")
        self.p5m = QtWidgets.QLineEdit(self.frame_11)
        self.p5m.setGeometry(QtCore.QRect(150, 340, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p5m.setFont(font)
        self.p5m.setObjectName("p5m")
        self.p5f = QtWidgets.QLineEdit(self.frame_11)
        self.p5f.setGeometry(QtCore.QRect(150, 370, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p5f.setFont(font)
        self.p5f.setObjectName("p5f")
        self.p6m = QtWidgets.QLineEdit(self.frame_11)
        self.p6m.setGeometry(QtCore.QRect(150, 400, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p6m.setFont(font)
        self.p6m.setObjectName("p6m")
        self.p6f = QtWidgets.QLineEdit(self.frame_11)
        self.p6f.setGeometry(QtCore.QRect(150, 430, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p6f.setFont(font)
        self.p6f.setObjectName("p6f")
        self.p7m = QtWidgets.QLineEdit(self.frame_11)
        self.p7m.setGeometry(QtCore.QRect(150, 460, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p7m.setFont(font)
        self.p7m.setObjectName("p7m")
        self.p7f = QtWidgets.QLineEdit(self.frame_11)
        self.p7f.setGeometry(QtCore.QRect(150, 490, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p7f.setFont(font)
        self.p7f.setObjectName("p7f")
        self.comboBox = QtWidgets.QComboBox(self.frame_11)
        self.comboBox.setGeometry(QtCore.QRect(150, 70, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.schooln = QtWidgets.QLineEdit(self.frame_11)
        self.schooln.setGeometry(QtCore.QRect(150, 10, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.schooln.setFont(font)
        self.schooln.setObjectName("schooln")
        self.save_15 = QtWidgets.QPushButton(self.frame_11)
        self.save_15.setGeometry(QtCore.QRect(660, 520, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_15.setFont(font)
        self.save_15.setObjectName("save_15")
        self.label_133 = QtWidgets.QLabel(self.page_5)
        self.label_133.setGeometry(QtCore.QRect(290, 0, 411, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_133.setFont(font)
        self.label_133.setObjectName("label_133")
        self.frame_12 = QtWidgets.QFrame(self.page_5)
        self.frame_12.setGeometry(QtCore.QRect(20, 160, 201, 491))
        self.frame_12.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.frame_13 = QtWidgets.QFrame(self.page_6)
        self.frame_13.setGeometry(QtCore.QRect(10, 140, 201, 531))
        self.frame_13.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.label_146 = QtWidgets.QLabel(self.page_6)
        self.label_146.setGeometry(QtCore.QRect(250, 0, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_146.setFont(font)
        self.label_146.setObjectName("label_146")
        self.frame_14 = QtWidgets.QFrame(self.page_6)
        self.frame_14.setGeometry(QtCore.QRect(10, 0, 201, 131))
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.home_6 = QtWidgets.QPushButton(self.frame_14)
        self.home_6.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_6.setFont(font)
        self.home_6.setObjectName("home_6")
        self.back_5 = QtWidgets.QPushButton(self.frame_14)
        self.back_5.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_5.setFont(font)
        self.back_5.setObjectName("back_5")
        self.pushButton_36 = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_36.setGeometry(QtCore.QRect(10, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_36.setFont(font)
        self.pushButton_36.setObjectName("pushButton_36")
        self.frame_15 = QtWidgets.QFrame(self.page_6)
        self.frame_15.setGeometry(QtCore.QRect(220, 40, 841, 801))
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.label_147 = QtWidgets.QLabel(self.frame_15)
        self.label_147.setGeometry(QtCore.QRect(10, 11, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_147.setFont(font)
        self.label_147.setObjectName("label_147")
        self.label_150 = QtWidgets.QLabel(self.frame_15)
        self.label_150.setGeometry(QtCore.QRect(10, 40, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_150.setFont(font)
        self.label_150.setObjectName("label_150")
        self.label_151 = QtWidgets.QLabel(self.frame_15)
        self.label_151.setGeometry(QtCore.QRect(10, 70, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_151.setFont(font)
        self.label_151.setObjectName("label_151")
        self.label_152 = QtWidgets.QLabel(self.frame_15)
        self.label_152.setGeometry(QtCore.QRect(10, 100, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_152.setFont(font)
        self.label_152.setObjectName("label_152")
        self.label_153 = QtWidgets.QLabel(self.frame_15)
        self.label_153.setGeometry(QtCore.QRect(10, 130, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_153.setFont(font)
        self.label_153.setObjectName("label_153")
        self.label_154 = QtWidgets.QLabel(self.frame_15)
        self.label_154.setGeometry(QtCore.QRect(10, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_154.setFont(font)
        self.label_154.setObjectName("label_154")
        self.label_155 = QtWidgets.QLabel(self.frame_15)
        self.label_155.setGeometry(QtCore.QRect(10, 190, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_155.setFont(font)
        self.label_155.setObjectName("label_155")
        self.label_156 = QtWidgets.QLabel(self.frame_15)
        self.label_156.setGeometry(QtCore.QRect(10, 220, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_156.setFont(font)
        self.label_156.setObjectName("label_156")
        self.label_157 = QtWidgets.QLabel(self.frame_15)
        self.label_157.setGeometry(QtCore.QRect(10, 250, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_157.setFont(font)
        self.label_157.setObjectName("label_157")
        self.label_158 = QtWidgets.QLabel(self.frame_15)
        self.label_158.setGeometry(QtCore.QRect(10, 280, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_158.setFont(font)
        self.label_158.setObjectName("label_158")
        self.save_6 = QtWidgets.QPushButton(self.frame_15)
        self.save_6.setGeometry(QtCore.QRect(200, 605, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_6.setFont(font)
        self.save_6.setObjectName("save_6")
        self.category_2 = QtWidgets.QLineEdit(self.frame_15)
        self.category_2.setGeometry(QtCore.QRect(150, 40, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.category_2.setFont(font)
        self.category_2.setObjectName("category_2")
        self.p1t = QtWidgets.QLineEdit(self.frame_15)
        self.p1t.setGeometry(QtCore.QRect(150, 100, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p1t.setFont(font)
        self.p1t.setObjectName("p1t")
        self.p2t = QtWidgets.QLineEdit(self.frame_15)
        self.p2t.setGeometry(QtCore.QRect(150, 130, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p2t.setFont(font)
        self.p2t.setObjectName("p2t")
        self.p3t = QtWidgets.QLineEdit(self.frame_15)
        self.p3t.setGeometry(QtCore.QRect(150, 160, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p3t.setFont(font)
        self.p3t.setObjectName("p3t")
        self.p4t = QtWidgets.QLineEdit(self.frame_15)
        self.p4t.setGeometry(QtCore.QRect(150, 190, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p4t.setFont(font)
        self.p4t.setObjectName("p4t")
        self.p5t = QtWidgets.QLineEdit(self.frame_15)
        self.p5t.setGeometry(QtCore.QRect(150, 220, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p5t.setFont(font)
        self.p5t.setObjectName("p5t")
        self.p6t = QtWidgets.QLineEdit(self.frame_15)
        self.p6t.setGeometry(QtCore.QRect(150, 250, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p6t.setFont(font)
        self.p6t.setObjectName("p6t")
        self.p7t = QtWidgets.QLineEdit(self.frame_15)
        self.p7t.setGeometry(QtCore.QRect(150, 280, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p7t.setFont(font)
        self.p7t.setObjectName("p7t")
        self.comboBox_5 = QtWidgets.QComboBox(self.frame_15)
        self.comboBox_5.setGeometry(QtCore.QRect(150, 70, 101, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_160 = QtWidgets.QLabel(self.frame_15)
        self.label_160.setGeometry(QtCore.QRect(10, 310, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_160.setFont(font)
        self.label_160.setObjectName("label_160")
        self.licencedm = QtWidgets.QLineEdit(self.frame_15)
        self.licencedm.setGeometry(QtCore.QRect(150, 310, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.licencedm.setFont(font)
        self.licencedm.setObjectName("licencedm")
        self.label_161 = QtWidgets.QLabel(self.frame_15)
        self.label_161.setGeometry(QtCore.QRect(10, 340, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_161.setFont(font)
        self.label_161.setObjectName("label_161")
        self.licencedf = QtWidgets.QLineEdit(self.frame_15)
        self.licencedf.setGeometry(QtCore.QRect(150, 340, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.licencedf.setFont(font)
        self.licencedf.setObjectName("licencedf")
        self.label_162 = QtWidgets.QLabel(self.frame_15)
        self.label_162.setGeometry(QtCore.QRect(10, 370, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_162.setFont(font)
        self.label_162.setObjectName("label_162")
        self.certificatem = QtWidgets.QLineEdit(self.frame_15)
        self.certificatem.setGeometry(QtCore.QRect(150, 370, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.certificatem.setFont(font)
        self.certificatem.setText("")
        self.certificatem.setObjectName("certificatem")
        self.label_163 = QtWidgets.QLabel(self.frame_15)
        self.label_163.setGeometry(QtCore.QRect(10, 400, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_163.setFont(font)
        self.label_163.setObjectName("label_163")
        self.certificatef = QtWidgets.QLineEdit(self.frame_15)
        self.certificatef.setGeometry(QtCore.QRect(150, 400, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.certificatef.setFont(font)
        self.certificatef.setObjectName("certificatef")
        self.label_164 = QtWidgets.QLabel(self.frame_15)
        self.label_164.setGeometry(QtCore.QRect(10, 430, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_164.setFont(font)
        self.label_164.setObjectName("label_164")
        self.deplomam = QtWidgets.QLineEdit(self.frame_15)
        self.deplomam.setGeometry(QtCore.QRect(150, 430, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.deplomam.setFont(font)
        self.deplomam.setObjectName("deplomam")
        self.label_165 = QtWidgets.QLabel(self.frame_15)
        self.label_165.setGeometry(QtCore.QRect(10, 460, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_165.setFont(font)
        self.label_165.setObjectName("label_165")
        self.deplomaf = QtWidgets.QLineEdit(self.frame_15)
        self.deplomaf.setGeometry(QtCore.QRect(150, 460, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.deplomaf.setFont(font)
        self.deplomaf.setObjectName("deplomaf")
        self.label_166 = QtWidgets.QLabel(self.frame_15)
        self.label_166.setGeometry(QtCore.QRect(10, 490, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_166.setFont(font)
        self.label_166.setObjectName("label_166")
        self.bachelorsm = QtWidgets.QLineEdit(self.frame_15)
        self.bachelorsm.setGeometry(QtCore.QRect(150, 490, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.bachelorsm.setFont(font)
        self.bachelorsm.setObjectName("bachelorsm")
        self.label_167 = QtWidgets.QLabel(self.frame_15)
        self.label_167.setGeometry(QtCore.QRect(10, 520, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_167.setFont(font)
        self.label_167.setObjectName("label_167")
        self.bachelorsf = QtWidgets.QLineEdit(self.frame_15)
        self.bachelorsf.setGeometry(QtCore.QRect(150, 520, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.bachelorsf.setFont(font)
        self.bachelorsf.setObjectName("bachelorsf")
        self.label_168 = QtWidgets.QLabel(self.frame_15)
        self.label_168.setGeometry(QtCore.QRect(10, 550, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_168.setFont(font)
        self.label_168.setObjectName("label_168")
        self.mastersm = QtWidgets.QLineEdit(self.frame_15)
        self.mastersm.setGeometry(QtCore.QRect(170, 550, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.mastersm.setFont(font)
        self.mastersm.setObjectName("mastersm")
        self.label_169 = QtWidgets.QLabel(self.frame_15)
        self.label_169.setGeometry(QtCore.QRect(10, 580, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_169.setFont(font)
        self.label_169.setObjectName("label_169")
        self.mastersf = QtWidgets.QLineEdit(self.frame_15)
        self.mastersf.setGeometry(QtCore.QRect(170, 580, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.mastersf.setFont(font)
        self.mastersf.setObjectName("mastersf")
        self.category_6 = QtWidgets.QLineEdit(self.frame_15)
        self.category_6.setGeometry(QtCore.QRect(150, 10, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.category_6.setFont(font)
        self.category_6.setObjectName("category_6")
        self.save_16 = QtWidgets.QPushButton(self.frame_15)
        self.save_16.setGeometry(QtCore.QRect(650, 605, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_16.setFont(font)
        self.save_16.setObjectName("save_16")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.frame_16 = QtWidgets.QFrame(self.page_7)
        self.frame_16.setGeometry(QtCore.QRect(0, 140, 201, 541))
        self.frame_16.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.label_176 = QtWidgets.QLabel(self.page_7)
        self.label_176.setGeometry(QtCore.QRect(212, -10, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_176.setFont(font)
        self.label_176.setObjectName("label_176")
        self.frame_17 = QtWidgets.QFrame(self.page_7)
        self.frame_17.setGeometry(QtCore.QRect(0, 0, 201, 131))
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.home_7 = QtWidgets.QPushButton(self.frame_17)
        self.home_7.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_7.setFont(font)
        self.home_7.setObjectName("home_7")
        self.back_6 = QtWidgets.QPushButton(self.frame_17)
        self.back_6.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_6.setFont(font)
        self.back_6.setObjectName("back_6")
        self.pushButton_37 = QtWidgets.QPushButton(self.frame_17)
        self.pushButton_37.setGeometry(QtCore.QRect(10, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_37.setFont(font)
        self.pushButton_37.setObjectName("pushButton_37")
        self.frame_18 = QtWidgets.QFrame(self.page_7)
        self.frame_18.setGeometry(QtCore.QRect(202, 30, 841, 801))
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.label_177 = QtWidgets.QLabel(self.frame_18)
        self.label_177.setGeometry(QtCore.QRect(10, 0, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_177.setFont(font)
        self.label_177.setObjectName("label_177")
        self.label_180 = QtWidgets.QLabel(self.frame_18)
        self.label_180.setGeometry(QtCore.QRect(10, 30, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_180.setFont(font)
        self.label_180.setObjectName("label_180")
        self.label_181 = QtWidgets.QLabel(self.frame_18)
        self.label_181.setGeometry(QtCore.QRect(10, 60, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_181.setFont(font)
        self.label_181.setObjectName("label_181")
        self.label_182 = QtWidgets.QLabel(self.frame_18)
        self.label_182.setGeometry(QtCore.QRect(10, 90, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_182.setFont(font)
        self.label_182.setObjectName("label_182")
        self.label_183 = QtWidgets.QLabel(self.frame_18)
        self.label_183.setGeometry(QtCore.QRect(10, 120, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_183.setFont(font)
        self.label_183.setObjectName("label_183")
        self.label_184 = QtWidgets.QLabel(self.frame_18)
        self.label_184.setGeometry(QtCore.QRect(10, 150, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_184.setFont(font)
        self.label_184.setObjectName("label_184")
        self.label_185 = QtWidgets.QLabel(self.frame_18)
        self.label_185.setGeometry(QtCore.QRect(10, 180, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_185.setFont(font)
        self.label_185.setObjectName("label_185")
        self.label_186 = QtWidgets.QLabel(self.frame_18)
        self.label_186.setGeometry(QtCore.QRect(10, 210, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_186.setFont(font)
        self.label_186.setObjectName("label_186")
        self.label_187 = QtWidgets.QLabel(self.frame_18)
        self.label_187.setGeometry(QtCore.QRect(10, 240, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_187.setFont(font)
        self.label_187.setObjectName("label_187")
        self.label_188 = QtWidgets.QLabel(self.frame_18)
        self.label_188.setGeometry(QtCore.QRect(10, 270, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_188.setFont(font)
        self.label_188.setObjectName("label_188")
        self.label_189 = QtWidgets.QLabel(self.frame_18)
        self.label_189.setGeometry(QtCore.QRect(10, 300, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_189.setFont(font)
        self.label_189.setObjectName("label_189")
        self.save_7 = QtWidgets.QPushButton(self.frame_18)
        self.save_7.setGeometry(QtCore.QRect(550, 600, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_7.setFont(font)
        self.save_7.setObjectName("save_7")
        self.library = QtWidgets.QLineEdit(self.frame_18)
        self.library.setGeometry(QtCore.QRect(150, 90, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.library.setFont(font)
        self.library.setObjectName("library")
        self.sciencelab = QtWidgets.QLineEdit(self.frame_18)
        self.sciencelab.setGeometry(QtCore.QRect(150, 120, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.sciencelab.setFont(font)
        self.sciencelab.setObjectName("sciencelab")
        self.complab = QtWidgets.QLineEdit(self.frame_18)
        self.complab.setGeometry(QtCore.QRect(170, 150, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.complab.setFont(font)
        self.complab.setObjectName("complab")
        self.kitchen = QtWidgets.QLineEdit(self.frame_18)
        self.kitchen.setGeometry(QtCore.QRect(150, 180, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.kitchen.setFont(font)
        self.kitchen.setObjectName("kitchen")
        self.staffroom = QtWidgets.QLineEdit(self.frame_18)
        self.staffroom.setGeometry(QtCore.QRect(150, 210, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.staffroom.setFont(font)
        self.staffroom.setObjectName("staffroom")
        self.adminblock = QtWidgets.QLineEdit(self.frame_18)
        self.adminblock.setGeometry(QtCore.QRect(170, 240, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.adminblock.setFont(font)
        self.adminblock.setObjectName("adminblock")
        self.dinninghall = QtWidgets.QLineEdit(self.frame_18)
        self.dinninghall.setGeometry(QtCore.QRect(150, 270, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.dinninghall.setFont(font)
        self.dinninghall.setObjectName("dinninghall")
        self.reliablesafewater = QtWidgets.QLineEdit(self.frame_18)
        self.reliablesafewater.setGeometry(QtCore.QRect(210, 300, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.reliablesafewater.setFont(font)
        self.reliablesafewater.setObjectName("reliablesafewater")
        self.comboBox_6 = QtWidgets.QComboBox(self.frame_18)
        self.comboBox_6.setGeometry(QtCore.QRect(150, 60, 101, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.label_190 = QtWidgets.QLabel(self.frame_18)
        self.label_190.setGeometry(QtCore.QRect(10, 330, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_190.setFont(font)
        self.label_190.setObjectName("label_190")
        self.stores = QtWidgets.QLineEdit(self.frame_18)
        self.stores.setGeometry(QtCore.QRect(150, 330, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.stores.setFont(font)
        self.stores.setObjectName("stores")
        self.label_191 = QtWidgets.QLabel(self.frame_18)
        self.label_191.setGeometry(QtCore.QRect(10, 360, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_191.setFont(font)
        self.label_191.setObjectName("label_191")
        self.workshop = QtWidgets.QLineEdit(self.frame_18)
        self.workshop.setGeometry(QtCore.QRect(150, 360, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.workshop.setFont(font)
        self.workshop.setObjectName("workshop")
        self.label_192 = QtWidgets.QLabel(self.frame_18)
        self.label_192.setGeometry(QtCore.QRect(10, 390, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_192.setFont(font)
        self.label_192.setObjectName("label_192")
        self.playground = QtWidgets.QLineEdit(self.frame_18)
        self.playground.setGeometry(QtCore.QRect(150, 390, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.playground.setFont(font)
        self.playground.setText("")
        self.playground.setObjectName("playground")
        self.label_193 = QtWidgets.QLabel(self.frame_18)
        self.label_193.setGeometry(QtCore.QRect(10, 420, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_193.setFont(font)
        self.label_193.setObjectName("label_193")
        self.garden = QtWidgets.QLineEdit(self.frame_18)
        self.garden.setGeometry(QtCore.QRect(150, 420, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.garden.setFont(font)
        self.garden.setObjectName("garden")
        self.label_194 = QtWidgets.QLabel(self.frame_18)
        self.label_194.setGeometry(QtCore.QRect(10, 450, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_194.setFont(font)
        self.label_194.setObjectName("label_194")
        self.latrine = QtWidgets.QLineEdit(self.frame_18)
        self.latrine.setGeometry(QtCore.QRect(150, 450, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.latrine.setFont(font)
        self.latrine.setObjectName("latrine")
        self.label_195 = QtWidgets.QLabel(self.frame_18)
        self.label_195.setGeometry(QtCore.QRect(10, 480, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_195.setFont(font)
        self.label_195.setObjectName("label_195")
        self.stances = QtWidgets.QLineEdit(self.frame_18)
        self.stances.setGeometry(QtCore.QRect(150, 480, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.stances.setFont(font)
        self.stances.setObjectName("stances")
        self.label_196 = QtWidgets.QLabel(self.frame_18)
        self.label_196.setGeometry(QtCore.QRect(10, 510, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_196.setFont(font)
        self.label_196.setObjectName("label_196")
        self.bachelorsm_2 = QtWidgets.QLineEdit(self.frame_18)
        self.bachelorsm_2.setGeometry(QtCore.QRect(180, 510, 651, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.bachelorsm_2.setFont(font)
        self.bachelorsm_2.setObjectName("bachelorsm_2")
        self.label_197 = QtWidgets.QLabel(self.frame_18)
        self.label_197.setGeometry(QtCore.QRect(10, 540, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_197.setFont(font)
        self.label_197.setObjectName("label_197")
        self.p1 = QtWidgets.QLineEdit(self.frame_18)
        self.p1.setGeometry(QtCore.QRect(80, 540, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p1.setFont(font)
        self.p1.setObjectName("p1")
        self.label_198 = QtWidgets.QLabel(self.frame_18)
        self.label_198.setGeometry(QtCore.QRect(220, 540, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_198.setFont(font)
        self.label_198.setObjectName("label_198")
        self.p2 = QtWidgets.QLineEdit(self.frame_18)
        self.p2.setGeometry(QtCore.QRect(290, 540, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p2.setFont(font)
        self.p2.setObjectName("p2")
        self.label_199 = QtWidgets.QLabel(self.frame_18)
        self.label_199.setGeometry(QtCore.QRect(440, 540, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_199.setFont(font)
        self.label_199.setObjectName("label_199")
        self.p3 = QtWidgets.QLineEdit(self.frame_18)
        self.p3.setGeometry(QtCore.QRect(510, 540, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p3.setFont(font)
        self.p3.setObjectName("p3")
        self.label_200 = QtWidgets.QLabel(self.frame_18)
        self.label_200.setGeometry(QtCore.QRect(660, 540, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_200.setFont(font)
        self.label_200.setObjectName("label_200")
        self.p4 = QtWidgets.QLineEdit(self.frame_18)
        self.p4.setGeometry(QtCore.QRect(730, 540, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p4.setFont(font)
        self.p4.setText("")
        self.p4.setObjectName("p4")
        self.label_201 = QtWidgets.QLabel(self.frame_18)
        self.label_201.setGeometry(QtCore.QRect(10, 570, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_201.setFont(font)
        self.label_201.setObjectName("label_201")
        self.p5 = QtWidgets.QLineEdit(self.frame_18)
        self.p5.setGeometry(QtCore.QRect(80, 570, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p5.setFont(font)
        self.p5.setObjectName("p5")
        self.p6 = QtWidgets.QLineEdit(self.frame_18)
        self.p6.setGeometry(QtCore.QRect(290, 570, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p6.setFont(font)
        self.p6.setObjectName("p6")
        self.label_202 = QtWidgets.QLabel(self.frame_18)
        self.label_202.setGeometry(QtCore.QRect(220, 570, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_202.setFont(font)
        self.label_202.setObjectName("label_202")
        self.p7 = QtWidgets.QLineEdit(self.frame_18)
        self.p7.setGeometry(QtCore.QRect(510, 570, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p7.setFont(font)
        self.p7.setObjectName("p7")
        self.label_203 = QtWidgets.QLabel(self.frame_18)
        self.label_203.setGeometry(QtCore.QRect(450, 570, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_203.setFont(font)
        self.label_203.setObjectName("label_203")
        self.category_7 = QtWidgets.QLineEdit(self.frame_18)
        self.category_7.setGeometry(QtCore.QRect(150, 0, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.category_7.setFont(font)
        self.category_7.setObjectName("category_7")
        self.sciencelab_2 = QtWidgets.QLineEdit(self.frame_18)
        self.sciencelab_2.setGeometry(QtCore.QRect(150, 30, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.sciencelab_2.setFont(font)
        self.sciencelab_2.setObjectName("sciencelab_2")
        self.save_17 = QtWidgets.QPushButton(self.frame_18)
        self.save_17.setGeometry(QtCore.QRect(710, 600, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_17.setFont(font)
        self.save_17.setObjectName("save_17")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.frame_19 = QtWidgets.QFrame(self.page_8)
        self.frame_19.setGeometry(QtCore.QRect(0, 130, 201, 581))
        self.frame_19.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.label_210 = QtWidgets.QLabel(self.page_8)
        self.label_210.setGeometry(QtCore.QRect(220, 0, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_210.setFont(font)
        self.label_210.setObjectName("label_210")
        self.frame_20 = QtWidgets.QFrame(self.page_8)
        self.frame_20.setGeometry(QtCore.QRect(210, 40, 841, 801))
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.label_211 = QtWidgets.QLabel(self.frame_20)
        self.label_211.setGeometry(QtCore.QRect(10, 20, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_211.setFont(font)
        self.label_211.setObjectName("label_211")
        self.label_214 = QtWidgets.QLabel(self.frame_20)
        self.label_214.setGeometry(QtCore.QRect(10, 50, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_214.setFont(font)
        self.label_214.setObjectName("label_214")
        self.label_215 = QtWidgets.QLabel(self.frame_20)
        self.label_215.setGeometry(QtCore.QRect(10, 80, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_215.setFont(font)
        self.label_215.setObjectName("label_215")
        self.label_216 = QtWidgets.QLabel(self.frame_20)
        self.label_216.setGeometry(QtCore.QRect(10, 110, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_216.setFont(font)
        self.label_216.setObjectName("label_216")
        self.label_217 = QtWidgets.QLabel(self.frame_20)
        self.label_217.setGeometry(QtCore.QRect(10, 140, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_217.setFont(font)
        self.label_217.setObjectName("label_217")
        self.label_218 = QtWidgets.QLabel(self.frame_20)
        self.label_218.setGeometry(QtCore.QRect(10, 170, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_218.setFont(font)
        self.label_218.setObjectName("label_218")
        self.label_219 = QtWidgets.QLabel(self.frame_20)
        self.label_219.setGeometry(QtCore.QRect(10, 200, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_219.setFont(font)
        self.label_219.setObjectName("label_219")
        self.label_220 = QtWidgets.QLabel(self.frame_20)
        self.label_220.setGeometry(QtCore.QRect(10, 230, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_220.setFont(font)
        self.label_220.setObjectName("label_220")
        self.label_221 = QtWidgets.QLabel(self.frame_20)
        self.label_221.setGeometry(QtCore.QRect(10, 260, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_221.setFont(font)
        self.label_221.setObjectName("label_221")
        self.label_222 = QtWidgets.QLabel(self.frame_20)
        self.label_222.setGeometry(QtCore.QRect(10, 290, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_222.setFont(font)
        self.label_222.setObjectName("label_222")
        self.save_8 = QtWidgets.QPushButton(self.frame_20)
        self.save_8.setGeometry(QtCore.QRect(280, 510, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_8.setFont(font)
        self.save_8.setObjectName("save_8")
        self.p1_2 = QtWidgets.QLineEdit(self.frame_20)
        self.p1_2.setGeometry(QtCore.QRect(150, 110, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p1_2.setFont(font)
        self.p1_2.setObjectName("p1_2")
        self.p2_2 = QtWidgets.QLineEdit(self.frame_20)
        self.p2_2.setGeometry(QtCore.QRect(150, 140, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p2_2.setFont(font)
        self.p2_2.setObjectName("p2_2")
        self.p3_2 = QtWidgets.QLineEdit(self.frame_20)
        self.p3_2.setGeometry(QtCore.QRect(170, 170, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p3_2.setFont(font)
        self.p3_2.setObjectName("p3_2")
        self.p4_2 = QtWidgets.QLineEdit(self.frame_20)
        self.p4_2.setGeometry(QtCore.QRect(170, 200, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p4_2.setFont(font)
        self.p4_2.setObjectName("p4_2")
        self.p5_2 = QtWidgets.QLineEdit(self.frame_20)
        self.p5_2.setGeometry(QtCore.QRect(170, 230, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p5_2.setFont(font)
        self.p5_2.setObjectName("p5_2")
        self.p6_2 = QtWidgets.QLineEdit(self.frame_20)
        self.p6_2.setGeometry(QtCore.QRect(170, 260, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p6_2.setFont(font)
        self.p6_2.setObjectName("p6_2")
        self.p7_2 = QtWidgets.QLineEdit(self.frame_20)
        self.p7_2.setGeometry(QtCore.QRect(170, 290, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p7_2.setFont(font)
        self.p7_2.setObjectName("p7_2")
        self.comboBox_7 = QtWidgets.QComboBox(self.frame_20)
        self.comboBox_7.setGeometry(QtCore.QRect(150, 80, 101, 22))
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.label_224 = QtWidgets.QLabel(self.frame_20)
        self.label_224.setGeometry(QtCore.QRect(10, 320, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_224.setFont(font)
        self.label_224.setObjectName("label_224")
        self.permanent = QtWidgets.QLineEdit(self.frame_20)
        self.permanent.setGeometry(QtCore.QRect(170, 320, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.permanent.setFont(font)
        self.permanent.setObjectName("permanent")
        self.label_225 = QtWidgets.QLabel(self.frame_20)
        self.label_225.setGeometry(QtCore.QRect(10, 350, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_225.setFont(font)
        self.label_225.setObjectName("label_225")
        self.temporary = QtWidgets.QLineEdit(self.frame_20)
        self.temporary.setGeometry(QtCore.QRect(170, 350, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.temporary.setFont(font)
        self.temporary.setObjectName("temporary")
        self.label_226 = QtWidgets.QLabel(self.frame_20)
        self.label_226.setGeometry(QtCore.QRect(10, 380, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_226.setFont(font)
        self.label_226.setObjectName("label_226")
        self.atfoundation = QtWidgets.QLineEdit(self.frame_20)
        self.atfoundation.setGeometry(QtCore.QRect(170, 380, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.atfoundation.setFont(font)
        self.atfoundation.setText("")
        self.atfoundation.setObjectName("atfoundation")
        self.label_227 = QtWidgets.QLabel(self.frame_20)
        self.label_227.setGeometry(QtCore.QRect(10, 410, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_227.setFont(font)
        self.label_227.setObjectName("label_227")
        self.atwindow = QtWidgets.QLineEdit(self.frame_20)
        self.atwindow.setGeometry(QtCore.QRect(170, 410, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.atwindow.setFont(font)
        self.atwindow.setObjectName("atwindow")
        self.label_228 = QtWidgets.QLabel(self.frame_20)
        self.label_228.setGeometry(QtCore.QRect(10, 440, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_228.setFont(font)
        self.label_228.setObjectName("label_228")
        self.wallpaltw = QtWidgets.QLineEdit(self.frame_20)
        self.wallpaltw.setGeometry(QtCore.QRect(200, 440, 631, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.wallpaltw.setFont(font)
        self.wallpaltw.setObjectName("wallpaltw")
        self.label_229 = QtWidgets.QLabel(self.frame_20)
        self.label_229.setGeometry(QtCore.QRect(10, 470, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_229.setFont(font)
        self.label_229.setObjectName("label_229")
        self.withoutstructures = QtWidgets.QLineEdit(self.frame_20)
        self.withoutstructures.setGeometry(QtCore.QRect(300, 470, 531, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.withoutstructures.setFont(font)
        self.withoutstructures.setObjectName("withoutstructures")
        self.category_8 = QtWidgets.QLineEdit(self.frame_20)
        self.category_8.setGeometry(QtCore.QRect(150, 20, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.category_8.setFont(font)
        self.category_8.setObjectName("category_8")
        self.p1_3 = QtWidgets.QLineEdit(self.frame_20)
        self.p1_3.setGeometry(QtCore.QRect(150, 50, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p1_3.setFont(font)
        self.p1_3.setObjectName("p1_3")
        self.save_18 = QtWidgets.QPushButton(self.frame_20)
        self.save_18.setGeometry(QtCore.QRect(590, 510, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_18.setFont(font)
        self.save_18.setObjectName("save_18")
        self.frame_21 = QtWidgets.QFrame(self.page_8)
        self.frame_21.setGeometry(QtCore.QRect(0, 0, 201, 131))
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.home_8 = QtWidgets.QPushButton(self.frame_21)
        self.home_8.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_8.setFont(font)
        self.home_8.setObjectName("home_8")
        self.back_7 = QtWidgets.QPushButton(self.frame_21)
        self.back_7.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_7.setFont(font)
        self.back_7.setObjectName("back_7")
        self.pushButton_38 = QtWidgets.QPushButton(self.frame_21)
        self.pushButton_38.setGeometry(QtCore.QRect(10, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_38.setFont(font)
        self.pushButton_38.setObjectName("pushButton_38")
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.frame_22 = QtWidgets.QFrame(self.page_9)
        self.frame_22.setGeometry(QtCore.QRect(0, 0, 201, 131))
        self.frame_22.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_22.setObjectName("frame_22")
        self.home_9 = QtWidgets.QPushButton(self.frame_22)
        self.home_9.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_9.setFont(font)
        self.home_9.setObjectName("home_9")
        self.back_8 = QtWidgets.QPushButton(self.frame_22)
        self.back_8.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_8.setFont(font)
        self.back_8.setObjectName("back_8")
        self.pushButton_50 = QtWidgets.QPushButton(self.frame_22)
        self.pushButton_50.setGeometry(QtCore.QRect(10, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_50.setFont(font)
        self.pushButton_50.setObjectName("pushButton_50")
        self.frame_23 = QtWidgets.QFrame(self.page_9)
        self.frame_23.setGeometry(QtCore.QRect(0, 140, 201, 551))
        self.frame_23.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.label_237 = QtWidgets.QLabel(self.page_9)
        self.label_237.setGeometry(QtCore.QRect(210, 0, 451, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_237.setFont(font)
        self.label_237.setObjectName("label_237")
        self.frame_24 = QtWidgets.QFrame(self.page_9)
        self.frame_24.setGeometry(QtCore.QRect(200, 40, 841, 651))
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.label_238 = QtWidgets.QLabel(self.frame_24)
        self.label_238.setGeometry(QtCore.QRect(10, 20, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_238.setFont(font)
        self.label_238.setObjectName("label_238")
        self.label_241 = QtWidgets.QLabel(self.frame_24)
        self.label_241.setGeometry(QtCore.QRect(10, 60, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_241.setFont(font)
        self.label_241.setObjectName("label_241")
        self.label_242 = QtWidgets.QLabel(self.frame_24)
        self.label_242.setGeometry(QtCore.QRect(10, 100, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_242.setFont(font)
        self.label_242.setObjectName("label_242")
        self.save_9 = QtWidgets.QPushButton(self.frame_24)
        self.save_9.setGeometry(QtCore.QRect(240, 360, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_9.setFont(font)
        self.save_9.setObjectName("save_9")
        self.category_5 = QtWidgets.QLineEdit(self.frame_24)
        self.category_5.setGeometry(QtCore.QRect(150, 60, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.category_5.setFont(font)
        self.category_5.setObjectName("category_5")
        self.comboBox_8 = QtWidgets.QComboBox(self.frame_24)
        self.comboBox_8.setGeometry(QtCore.QRect(150, 100, 101, 22))
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.label_243 = QtWidgets.QLabel(self.frame_24)
        self.label_243.setGeometry(QtCore.QRect(10, 140, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_243.setFont(font)
        self.label_243.setObjectName("label_243")
        self.permanent_2 = QtWidgets.QLineEdit(self.frame_24)
        self.permanent_2.setGeometry(QtCore.QRect(170, 140, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.permanent_2.setFont(font)
        self.permanent_2.setObjectName("permanent_2")
        self.label_244 = QtWidgets.QLabel(self.frame_24)
        self.label_244.setGeometry(QtCore.QRect(10, 180, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_244.setFont(font)
        self.label_244.setObjectName("label_244")
        self.temporary_2 = QtWidgets.QLineEdit(self.frame_24)
        self.temporary_2.setGeometry(QtCore.QRect(170, 180, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.temporary_2.setFont(font)
        self.temporary_2.setObjectName("temporary_2")
        self.label_245 = QtWidgets.QLabel(self.frame_24)
        self.label_245.setGeometry(QtCore.QRect(10, 220, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_245.setFont(font)
        self.label_245.setObjectName("label_245")
        self.atfoundation_2 = QtWidgets.QLineEdit(self.frame_24)
        self.atfoundation_2.setGeometry(QtCore.QRect(170, 220, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.atfoundation_2.setFont(font)
        self.atfoundation_2.setText("")
        self.atfoundation_2.setObjectName("atfoundation_2")
        self.label_246 = QtWidgets.QLabel(self.frame_24)
        self.label_246.setGeometry(QtCore.QRect(10, 260, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_246.setFont(font)
        self.label_246.setObjectName("label_246")
        self.atwindow_2 = QtWidgets.QLineEdit(self.frame_24)
        self.atwindow_2.setGeometry(QtCore.QRect(170, 260, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.atwindow_2.setFont(font)
        self.atwindow_2.setObjectName("atwindow_2")
        self.label_247 = QtWidgets.QLabel(self.frame_24)
        self.label_247.setGeometry(QtCore.QRect(10, 300, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_247.setFont(font)
        self.label_247.setObjectName("label_247")
        self.wallpaltw_2 = QtWidgets.QLineEdit(self.frame_24)
        self.wallpaltw_2.setGeometry(QtCore.QRect(200, 300, 631, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.wallpaltw_2.setFont(font)
        self.wallpaltw_2.setObjectName("wallpaltw_2")
        self.category_9 = QtWidgets.QLineEdit(self.frame_24)
        self.category_9.setGeometry(QtCore.QRect(150, 20, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.category_9.setFont(font)
        self.category_9.setObjectName("category_9")
        self.save_19 = QtWidgets.QPushButton(self.frame_24)
        self.save_19.setGeometry(QtCore.QRect(620, 360, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_19.setFont(font)
        self.save_19.setObjectName("save_19")
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.pushButton_7 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_7.setGeometry(QtCore.QRect(490, 200, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_9 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_9.setGeometry(QtCore.QRect(210, 200, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 150, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_6.setGeometry(QtCore.QRect(490, 150, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_10 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_10.setGeometry(QtCore.QRect(490, 250, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_11.setGeometry(QtCore.QRect(210, 350, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_3 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 100, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_13 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_13.setGeometry(QtCore.QRect(210, 400, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setObjectName("pushButton_13")
        self.frame_4 = QtWidgets.QFrame(self.page_10)
        self.frame_4.setGeometry(QtCore.QRect(0, 10, 181, 671))
        self.frame_4.setStyleSheet("\n"
"background-color: rgb(170, 170, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_23 = QtWidgets.QLabel(self.page_10)
        self.label_23.setGeometry(QtCore.QRect(530, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.pushButton_14 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_14.setGeometry(QtCore.QRect(490, 100, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_14.setFont(font)
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_16 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_16.setGeometry(QtCore.QRect(210, 300, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_17.setGeometry(QtCore.QRect(210, 250, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_17.setFont(font)
        self.pushButton_17.setObjectName("pushButton_17")
        self.label_33 = QtWidgets.QLabel(self.page_10)
        self.label_33.setGeometry(QtCore.QRect(290, 70, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.page_10)
        self.label_34.setGeometry(QtCore.QRect(570, 70, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.pushButton_12 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_12.setGeometry(QtCore.QRect(770, 250, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_20 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_20.setGeometry(QtCore.QRect(770, 150, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_20.setFont(font)
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_21.setGeometry(QtCore.QRect(770, 200, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_21.setFont(font)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_120 = QtWidgets.QPushButton(self.page_10)
        self.pushButton_120.setGeometry(QtCore.QRect(770, 100, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_120.setFont(font)
        self.pushButton_120.setObjectName("pushButton_120")
        self.label_35 = QtWidgets.QLabel(self.page_10)
        self.label_35.setGeometry(QtCore.QRect(850, 70, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.stackedWidget.addWidget(self.page_10)
        self.page_29 = QtWidgets.QWidget()
        self.page_29.setObjectName("page_29")
        self.tableWidget_8 = QtWidgets.QTableWidget(self.page_29)
        self.tableWidget_8.setGeometry(QtCore.QRect(150, 30, 891, 621))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_8.setFont(font)
        self.tableWidget_8.setMouseTracking(True)
        self.tableWidget_8.setRowCount(5)
        self.tableWidget_8.setColumnCount(6)
        self.tableWidget_8.setObjectName("tableWidget_8")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(5, item)
        self.label_66 = QtWidgets.QLabel(self.page_29)
        self.label_66.setGeometry(QtCore.QRect(550, 0, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_66.setFont(font)
        self.label_66.setObjectName("label_66")
        self.frame_56 = QtWidgets.QFrame(self.page_29)
        self.frame_56.setGeometry(QtCore.QRect(-20, 30, 161, 811))
        self.frame_56.setMouseTracking(True)
        self.frame_56.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_56.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_56.setObjectName("frame_56")
        self.pushButton_65 = QtWidgets.QPushButton(self.frame_56)
        self.pushButton_65.setGeometry(QtCore.QRect(30, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_65.setFont(font)
        self.pushButton_65.setMouseTracking(True)
        self.pushButton_65.setObjectName("pushButton_65")
        self.pushButton_66 = QtWidgets.QPushButton(self.frame_56)
        self.pushButton_66.setGeometry(QtCore.QRect(30, 50, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_66.setFont(font)
        self.pushButton_66.setMouseTracking(True)
        self.pushButton_66.setObjectName("pushButton_66")
        self.pushButton_68 = QtWidgets.QPushButton(self.frame_56)
        self.pushButton_68.setGeometry(QtCore.QRect(30, 120, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_68.setFont(font)
        self.pushButton_68.setMouseTracking(True)
        self.pushButton_68.setObjectName("pushButton_68")
        self.pushButton_69 = QtWidgets.QPushButton(self.frame_56)
        self.pushButton_69.setGeometry(QtCore.QRect(30, 160, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_69.setFont(font)
        self.pushButton_69.setMouseTracking(True)
        self.pushButton_69.setObjectName("pushButton_69")
        self.label_31 = QtWidgets.QLabel(self.frame_56)
        self.label_31.setGeometry(QtCore.QRect(30, 100, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.stackedWidget.addWidget(self.page_29)
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.label_24 = QtWidgets.QLabel(self.page_11)
        self.label_24.setGeometry(QtCore.QRect(500, 0, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.frame_25 = QtWidgets.QFrame(self.page_11)
        self.frame_25.setGeometry(QtCore.QRect(0, 30, 111, 651))
        self.frame_25.setMouseTracking(True)
        self.frame_25.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.pushButton_18 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_18.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setMouseTracking(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_19.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setMouseTracking(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_62 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_62.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_62.setFont(font)
        self.pushButton_62.setMouseTracking(True)
        self.pushButton_62.setObjectName("pushButton_62")
        self.pushButton_71 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_71.setGeometry(QtCore.QRect(10, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_71.setFont(font)
        self.pushButton_71.setMouseTracking(True)
        self.pushButton_71.setObjectName("pushButton_71")
        self.pushButton_73 = QtWidgets.QPushButton(self.frame_25)
        self.pushButton_73.setGeometry(QtCore.QRect(10, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_73.setFont(font)
        self.pushButton_73.setMouseTracking(True)
        self.pushButton_73.setObjectName("pushButton_73")
        self.label_32 = QtWidgets.QLabel(self.frame_25)
        self.label_32.setGeometry(QtCore.QRect(10, 140, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.tableWidget = QtWidgets.QTableWidget(self.page_11)
        self.tableWidget.setGeometry(QtCore.QRect(120, 30, 921, 621))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget.setFont(font)
        self.tableWidget.setMouseTracking(True)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(22)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        self.stackedWidget.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.page_12)
        self.tableWidget_3.setGeometry(QtCore.QRect(130, 30, 911, 611))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setMouseTracking(True)
        self.tableWidget_3.setRowCount(5)
        self.tableWidget_3.setColumnCount(26)
        self.tableWidget_3.setObjectName("tableWidget_3")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(25, item)
        self.frame_51 = QtWidgets.QFrame(self.page_12)
        self.frame_51.setGeometry(QtCore.QRect(0, 30, 121, 641))
        self.frame_51.setMouseTracking(True)
        self.frame_51.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_51.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_51.setObjectName("frame_51")
        self.pushButton_39 = QtWidgets.QPushButton(self.frame_51)
        self.pushButton_39.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_39.setFont(font)
        self.pushButton_39.setMouseTracking(True)
        self.pushButton_39.setObjectName("pushButton_39")
        self.pushButton_40 = QtWidgets.QPushButton(self.frame_51)
        self.pushButton_40.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_40.setFont(font)
        self.pushButton_40.setMouseTracking(True)
        self.pushButton_40.setObjectName("pushButton_40")
        self.pushButton_60 = QtWidgets.QPushButton(self.frame_51)
        self.pushButton_60.setGeometry(QtCore.QRect(10, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_60.setFont(font)
        self.pushButton_60.setMouseTracking(True)
        self.pushButton_60.setObjectName("pushButton_60")
        self.pushButton_61 = QtWidgets.QPushButton(self.frame_51)
        self.pushButton_61.setGeometry(QtCore.QRect(10, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_61.setFont(font)
        self.pushButton_61.setMouseTracking(True)
        self.pushButton_61.setObjectName("pushButton_61")
        self.label_61 = QtWidgets.QLabel(self.page_12)
        self.label_61.setGeometry(QtCore.QRect(500, 0, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_61.setFont(font)
        self.label_61.setObjectName("label_61")
        self.stackedWidget.addWidget(self.page_12)
        self.page_25 = QtWidgets.QWidget()
        self.page_25.setObjectName("page_25")
        self.tableWidget_4 = QtWidgets.QTableWidget(self.page_25)
        self.tableWidget_4.setGeometry(QtCore.QRect(120, 30, 911, 611))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_4.setFont(font)
        self.tableWidget_4.setMouseTracking(True)
        self.tableWidget_4.setRowCount(5)
        self.tableWidget_4.setColumnCount(25)
        self.tableWidget_4.setObjectName("tableWidget_4")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(24, item)
        self.frame_52 = QtWidgets.QFrame(self.page_25)
        self.frame_52.setGeometry(QtCore.QRect(0, 30, 111, 641))
        self.frame_52.setMouseTracking(True)
        self.frame_52.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_52.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_52.setObjectName("frame_52")
        self.pushButton_41 = QtWidgets.QPushButton(self.frame_52)
        self.pushButton_41.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_41.setFont(font)
        self.pushButton_41.setMouseTracking(True)
        self.pushButton_41.setObjectName("pushButton_41")
        self.pushButton_42 = QtWidgets.QPushButton(self.frame_52)
        self.pushButton_42.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_42.setFont(font)
        self.pushButton_42.setMouseTracking(True)
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_58 = QtWidgets.QPushButton(self.frame_52)
        self.pushButton_58.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_58.setFont(font)
        self.pushButton_58.setMouseTracking(True)
        self.pushButton_58.setObjectName("pushButton_58")
        self.pushButton_59 = QtWidgets.QPushButton(self.frame_52)
        self.pushButton_59.setGeometry(QtCore.QRect(10, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_59.setFont(font)
        self.pushButton_59.setMouseTracking(True)
        self.pushButton_59.setObjectName("pushButton_59")
        self.label_62 = QtWidgets.QLabel(self.page_25)
        self.label_62.setGeometry(QtCore.QRect(390, 0, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_62.setFont(font)
        self.label_62.setObjectName("label_62")
        self.stackedWidget.addWidget(self.page_25)
        self.page_26 = QtWidgets.QWidget()
        self.page_26.setObjectName("page_26")
        self.tableWidget_5 = QtWidgets.QTableWidget(self.page_26)
        self.tableWidget_5.setGeometry(QtCore.QRect(120, 30, 921, 621))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_5.setFont(font)
        self.tableWidget_5.setMouseTracking(True)
        self.tableWidget_5.setRowCount(5)
        self.tableWidget_5.setColumnCount(24)
        self.tableWidget_5.setObjectName("tableWidget_5")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(23, item)
        self.frame_53 = QtWidgets.QFrame(self.page_26)
        self.frame_53.setGeometry(QtCore.QRect(0, 30, 111, 641))
        self.frame_53.setMouseTracking(True)
        self.frame_53.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_53.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_53.setObjectName("frame_53")
        self.pushButton_43 = QtWidgets.QPushButton(self.frame_53)
        self.pushButton_43.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_43.setFont(font)
        self.pushButton_43.setMouseTracking(True)
        self.pushButton_43.setObjectName("pushButton_43")
        self.pushButton_44 = QtWidgets.QPushButton(self.frame_53)
        self.pushButton_44.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_44.setFont(font)
        self.pushButton_44.setMouseTracking(True)
        self.pushButton_44.setObjectName("pushButton_44")
        self.pushButton_56 = QtWidgets.QPushButton(self.frame_53)
        self.pushButton_56.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_56.setFont(font)
        self.pushButton_56.setMouseTracking(True)
        self.pushButton_56.setObjectName("pushButton_56")
        self.pushButton_57 = QtWidgets.QPushButton(self.frame_53)
        self.pushButton_57.setGeometry(QtCore.QRect(10, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_57.setFont(font)
        self.pushButton_57.setMouseTracking(True)
        self.pushButton_57.setObjectName("pushButton_57")
        self.label_63 = QtWidgets.QLabel(self.page_26)
        self.label_63.setGeometry(QtCore.QRect(450, 0, 371, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_63.setFont(font)
        self.label_63.setObjectName("label_63")
        self.stackedWidget.addWidget(self.page_26)
        self.page_27 = QtWidgets.QWidget()
        self.page_27.setObjectName("page_27")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.page_27)
        self.tableWidget_6.setGeometry(QtCore.QRect(120, 30, 911, 631))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_6.setFont(font)
        self.tableWidget_6.setMouseTracking(True)
        self.tableWidget_6.setRowCount(5)
        self.tableWidget_6.setColumnCount(22)
        self.tableWidget_6.setObjectName("tableWidget_6")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(21, item)
        self.frame_54 = QtWidgets.QFrame(self.page_27)
        self.frame_54.setGeometry(QtCore.QRect(0, 30, 111, 651))
        self.frame_54.setMouseTracking(True)
        self.frame_54.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_54.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_54.setObjectName("frame_54")
        self.pushButton_45 = QtWidgets.QPushButton(self.frame_54)
        self.pushButton_45.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_45.setFont(font)
        self.pushButton_45.setMouseTracking(True)
        self.pushButton_45.setObjectName("pushButton_45")
        self.pushButton_46 = QtWidgets.QPushButton(self.frame_54)
        self.pushButton_46.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_46.setFont(font)
        self.pushButton_46.setMouseTracking(True)
        self.pushButton_46.setObjectName("pushButton_46")
        self.pushButton_54 = QtWidgets.QPushButton(self.frame_54)
        self.pushButton_54.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_54.setFont(font)
        self.pushButton_54.setMouseTracking(True)
        self.pushButton_54.setObjectName("pushButton_54")
        self.pushButton_55 = QtWidgets.QPushButton(self.frame_54)
        self.pushButton_55.setGeometry(QtCore.QRect(10, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_55.setFont(font)
        self.pushButton_55.setMouseTracking(True)
        self.pushButton_55.setObjectName("pushButton_55")
        self.label_64 = QtWidgets.QLabel(self.page_27)
        self.label_64.setGeometry(QtCore.QRect(370, 0, 381, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.stackedWidget.addWidget(self.page_27)
        self.page_28 = QtWidgets.QWidget()
        self.page_28.setObjectName("page_28")
        self.tableWidget_7 = QtWidgets.QTableWidget(self.page_28)
        self.tableWidget_7.setGeometry(QtCore.QRect(120, 30, 921, 621))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_7.setFont(font)
        self.tableWidget_7.setMouseTracking(True)
        self.tableWidget_7.setRowCount(5)
        self.tableWidget_7.setColumnCount(13)
        self.tableWidget_7.setObjectName("tableWidget_7")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(12, item)
        self.frame_55 = QtWidgets.QFrame(self.page_28)
        self.frame_55.setGeometry(QtCore.QRect(0, 30, 111, 641))
        self.frame_55.setMouseTracking(True)
        self.frame_55.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_55.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_55.setObjectName("frame_55")
        self.pushButton_47 = QtWidgets.QPushButton(self.frame_55)
        self.pushButton_47.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_47.setFont(font)
        self.pushButton_47.setMouseTracking(True)
        self.pushButton_47.setObjectName("pushButton_47")
        self.pushButton_48 = QtWidgets.QPushButton(self.frame_55)
        self.pushButton_48.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_48.setFont(font)
        self.pushButton_48.setMouseTracking(True)
        self.pushButton_48.setObjectName("pushButton_48")
        self.pushButton_49 = QtWidgets.QPushButton(self.frame_55)
        self.pushButton_49.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_49.setFont(font)
        self.pushButton_49.setMouseTracking(True)
        self.pushButton_49.setObjectName("pushButton_49")
        self.pushButton_53 = QtWidgets.QPushButton(self.frame_55)
        self.pushButton_53.setGeometry(QtCore.QRect(10, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_53.setFont(font)
        self.pushButton_53.setMouseTracking(True)
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_86 = QtWidgets.QPushButton(self.frame_55)
        self.pushButton_86.setGeometry(QtCore.QRect(10, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_86.setFont(font)
        self.pushButton_86.setMouseTracking(True)
        self.pushButton_86.setObjectName("pushButton_86")
        self.pushButton_88 = QtWidgets.QPushButton(self.frame_55)
        self.pushButton_88.setGeometry(QtCore.QRect(10, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_88.setFont(font)
        self.pushButton_88.setMouseTracking(True)
        self.pushButton_88.setObjectName("pushButton_88")
        self.label_37 = QtWidgets.QLabel(self.frame_55)
        self.label_37.setGeometry(QtCore.QRect(10, 180, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_65 = QtWidgets.QLabel(self.page_28)
        self.label_65.setGeometry(QtCore.QRect(500, 0, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_65.setFont(font)
        self.label_65.setObjectName("label_65")
        self.stackedWidget.addWidget(self.page_28)
        self.page_22 = QtWidgets.QWidget()
        self.page_22.setObjectName("page_22")
        self.tableWidget_12 = QtWidgets.QTableWidget(self.page_22)
        self.tableWidget_12.setGeometry(QtCore.QRect(130, 30, 911, 641))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_12.setFont(font)
        self.tableWidget_12.setMouseTracking(True)
        self.tableWidget_12.setRowCount(5)
        self.tableWidget_12.setColumnCount(22)
        self.tableWidget_12.setObjectName("tableWidget_12")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(21, item)
        self.frame_57 = QtWidgets.QFrame(self.page_22)
        self.frame_57.setGeometry(QtCore.QRect(0, 30, 121, 661))
        self.frame_57.setMouseTracking(True)
        self.frame_57.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_57.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_57.setObjectName("frame_57")
        self.pushButton_67 = QtWidgets.QPushButton(self.frame_57)
        self.pushButton_67.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_67.setFont(font)
        self.pushButton_67.setMouseTracking(True)
        self.pushButton_67.setObjectName("pushButton_67")
        self.pushButton_74 = QtWidgets.QPushButton(self.frame_57)
        self.pushButton_74.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_74.setFont(font)
        self.pushButton_74.setMouseTracking(True)
        self.pushButton_74.setObjectName("pushButton_74")
        self.pushButton_75 = QtWidgets.QPushButton(self.frame_57)
        self.pushButton_75.setGeometry(QtCore.QRect(10, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_75.setFont(font)
        self.pushButton_75.setMouseTracking(True)
        self.pushButton_75.setObjectName("pushButton_75")
        self.pushButton_76 = QtWidgets.QPushButton(self.frame_57)
        self.pushButton_76.setGeometry(QtCore.QRect(10, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_76.setFont(font)
        self.pushButton_76.setMouseTracking(True)
        self.pushButton_76.setObjectName("pushButton_76")
        self.label_67 = QtWidgets.QLabel(self.page_22)
        self.label_67.setGeometry(QtCore.QRect(500, 0, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_67.setFont(font)
        self.label_67.setObjectName("label_67")
        self.stackedWidget.addWidget(self.page_22)
        self.page_23 = QtWidgets.QWidget()
        self.page_23.setObjectName("page_23")
        self.label_68 = QtWidgets.QLabel(self.page_23)
        self.label_68.setGeometry(QtCore.QRect(390, 0, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_68.setFont(font)
        self.label_68.setObjectName("label_68")
        self.frame_58 = QtWidgets.QFrame(self.page_23)
        self.frame_58.setGeometry(QtCore.QRect(0, 30, 111, 651))
        self.frame_58.setMouseTracking(True)
        self.frame_58.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_58.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_58.setObjectName("frame_58")
        self.pushButton_77 = QtWidgets.QPushButton(self.frame_58)
        self.pushButton_77.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_77.setFont(font)
        self.pushButton_77.setMouseTracking(True)
        self.pushButton_77.setObjectName("pushButton_77")
        self.pushButton_78 = QtWidgets.QPushButton(self.frame_58)
        self.pushButton_78.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_78.setFont(font)
        self.pushButton_78.setMouseTracking(True)
        self.pushButton_78.setObjectName("pushButton_78")
        self.pushButton_79 = QtWidgets.QPushButton(self.frame_58)
        self.pushButton_79.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_79.setFont(font)
        self.pushButton_79.setMouseTracking(True)
        self.pushButton_79.setObjectName("pushButton_79")
        self.pushButton_80 = QtWidgets.QPushButton(self.frame_58)
        self.pushButton_80.setGeometry(QtCore.QRect(10, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_80.setFont(font)
        self.pushButton_80.setMouseTracking(True)
        self.pushButton_80.setObjectName("pushButton_80")
        self.tableWidget_13 = QtWidgets.QTableWidget(self.page_23)
        self.tableWidget_13.setGeometry(QtCore.QRect(120, 30, 921, 631))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_13.setFont(font)
        self.tableWidget_13.setMouseTracking(True)
        self.tableWidget_13.setRowCount(5)
        self.tableWidget_13.setColumnCount(23)
        self.tableWidget_13.setObjectName("tableWidget_13")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_13.setHorizontalHeaderItem(22, item)
        self.stackedWidget.addWidget(self.page_23)
        self.page_24 = QtWidgets.QWidget()
        self.page_24.setObjectName("page_24")
        self.label_69 = QtWidgets.QLabel(self.page_24)
        self.label_69.setGeometry(QtCore.QRect(440, 0, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_69.setFont(font)
        self.label_69.setObjectName("label_69")
        self.frame_59 = QtWidgets.QFrame(self.page_24)
        self.frame_59.setGeometry(QtCore.QRect(0, 30, 111, 641))
        self.frame_59.setMouseTracking(True)
        self.frame_59.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_59.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_59.setObjectName("frame_59")
        self.pushButton_81 = QtWidgets.QPushButton(self.frame_59)
        self.pushButton_81.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_81.setFont(font)
        self.pushButton_81.setMouseTracking(True)
        self.pushButton_81.setObjectName("pushButton_81")
        self.pushButton_82 = QtWidgets.QPushButton(self.frame_59)
        self.pushButton_82.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_82.setFont(font)
        self.pushButton_82.setMouseTracking(True)
        self.pushButton_82.setObjectName("pushButton_82")
        self.pushButton_83 = QtWidgets.QPushButton(self.frame_59)
        self.pushButton_83.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_83.setFont(font)
        self.pushButton_83.setMouseTracking(True)
        self.pushButton_83.setObjectName("pushButton_83")
        self.pushButton_84 = QtWidgets.QPushButton(self.frame_59)
        self.pushButton_84.setGeometry(QtCore.QRect(10, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_84.setFont(font)
        self.pushButton_84.setMouseTracking(True)
        self.pushButton_84.setObjectName("pushButton_84")
        self.tableWidget_14 = QtWidgets.QTableWidget(self.page_24)
        self.tableWidget_14.setGeometry(QtCore.QRect(120, 30, 921, 621))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_14.setFont(font)
        self.tableWidget_14.setMouseTracking(True)
        self.tableWidget_14.setRowCount(5)
        self.tableWidget_14.setColumnCount(28)
        self.tableWidget_14.setObjectName("tableWidget_14")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(25, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(26, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_14.setHorizontalHeaderItem(27, item)
        self.stackedWidget.addWidget(self.page_24)
        self.page_30 = QtWidgets.QWidget()
        self.page_30.setObjectName("page_30")
        self.tableWidget_15 = QtWidgets.QTableWidget(self.page_30)
        self.tableWidget_15.setGeometry(QtCore.QRect(120, 30, 921, 631))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_15.setFont(font)
        self.tableWidget_15.setMouseTracking(True)
        self.tableWidget_15.setRowCount(5)
        self.tableWidget_15.setColumnCount(22)
        self.tableWidget_15.setObjectName("tableWidget_15")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_15.setHorizontalHeaderItem(21, item)
        self.label_70 = QtWidgets.QLabel(self.page_30)
        self.label_70.setGeometry(QtCore.QRect(390, 0, 471, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_70.setFont(font)
        self.label_70.setObjectName("label_70")
        self.frame_60 = QtWidgets.QFrame(self.page_30)
        self.frame_60.setGeometry(QtCore.QRect(0, 30, 111, 651))
        self.frame_60.setMouseTracking(True)
        self.frame_60.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_60.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_60.setObjectName("frame_60")
        self.pushButton_85 = QtWidgets.QPushButton(self.frame_60)
        self.pushButton_85.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_85.setFont(font)
        self.pushButton_85.setMouseTracking(True)
        self.pushButton_85.setObjectName("pushButton_85")
        self.pushButton_117 = QtWidgets.QPushButton(self.frame_60)
        self.pushButton_117.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_117.setFont(font)
        self.pushButton_117.setMouseTracking(True)
        self.pushButton_117.setObjectName("pushButton_117")
        self.pushButton_118 = QtWidgets.QPushButton(self.frame_60)
        self.pushButton_118.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_118.setFont(font)
        self.pushButton_118.setMouseTracking(True)
        self.pushButton_118.setObjectName("pushButton_118")
        self.pushButton_119 = QtWidgets.QPushButton(self.frame_60)
        self.pushButton_119.setGeometry(QtCore.QRect(10, 130, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_119.setFont(font)
        self.pushButton_119.setMouseTracking(True)
        self.pushButton_119.setObjectName("pushButton_119")
        self.stackedWidget.addWidget(self.page_30)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.label_38 = QtWidgets.QLabel(self.page_13)
        self.label_38.setGeometry(QtCore.QRect(500, 0, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.frame_26 = QtWidgets.QFrame(self.page_13)
        self.frame_26.setGeometry(QtCore.QRect(0, 30, 111, 641))
        self.frame_26.setMouseTracking(True)
        self.frame_26.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.pushButton_22 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_22.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_22.setFont(font)
        self.pushButton_22.setMouseTracking(True)
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_23.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_23.setFont(font)
        self.pushButton_23.setMouseTracking(True)
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_64 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_64.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_64.setFont(font)
        self.pushButton_64.setMouseTracking(True)
        self.pushButton_64.setObjectName("pushButton_64")
        self.pushButton_92 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_92.setGeometry(QtCore.QRect(10, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_92.setFont(font)
        self.pushButton_92.setMouseTracking(True)
        self.pushButton_92.setObjectName("pushButton_92")
        self.pushButton_94 = QtWidgets.QPushButton(self.frame_26)
        self.pushButton_94.setGeometry(QtCore.QRect(10, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_94.setFont(font)
        self.pushButton_94.setMouseTracking(True)
        self.pushButton_94.setObjectName("pushButton_94")
        self.label_40 = QtWidgets.QLabel(self.frame_26)
        self.label_40.setGeometry(QtCore.QRect(10, 140, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setObjectName("label_40")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.page_13)
        self.tableWidget_2.setGeometry(QtCore.QRect(120, 30, 921, 621))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_2.setFont(font)
        self.tableWidget_2.setMouseTracking(True)
        self.tableWidget_2.setRowCount(5)
        self.tableWidget_2.setColumnCount(8)
        self.tableWidget_2.setObjectName("tableWidget_2")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, item)
        self.stackedWidget.addWidget(self.page_13)
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.label_41 = QtWidgets.QLabel(self.page_14)
        self.label_41.setGeometry(QtCore.QRect(500, 0, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setObjectName("label_41")
        self.frame_27 = QtWidgets.QFrame(self.page_14)
        self.frame_27.setGeometry(QtCore.QRect(0, 30, 111, 811))
        self.frame_27.setMouseTracking(True)
        self.frame_27.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.pushButton_24 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_24.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_24.setFont(font)
        self.pushButton_24.setMouseTracking(True)
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_25.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_25.setFont(font)
        self.pushButton_25.setMouseTracking(True)
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_95 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_95.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_95.setFont(font)
        self.pushButton_95.setMouseTracking(True)
        self.pushButton_95.setObjectName("pushButton_95")
        self.pushButton_96 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_96.setGeometry(QtCore.QRect(10, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_96.setFont(font)
        self.pushButton_96.setMouseTracking(True)
        self.pushButton_96.setObjectName("pushButton_96")
        self.pushButton_98 = QtWidgets.QPushButton(self.frame_27)
        self.pushButton_98.setGeometry(QtCore.QRect(10, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_98.setFont(font)
        self.pushButton_98.setMouseTracking(True)
        self.pushButton_98.setObjectName("pushButton_98")
        self.label_42 = QtWidgets.QLabel(self.frame_27)
        self.label_42.setGeometry(QtCore.QRect(10, 140, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.tableWidget_9 = QtWidgets.QTableWidget(self.page_14)
        self.tableWidget_9.setGeometry(QtCore.QRect(120, 30, 921, 641))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_9.setFont(font)
        self.tableWidget_9.setMouseTracking(True)
        self.tableWidget_9.setRowCount(5)
        self.tableWidget_9.setColumnCount(20)
        self.tableWidget_9.setObjectName("tableWidget_9")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_9.setHorizontalHeaderItem(19, item)
        self.stackedWidget.addWidget(self.page_14)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.label_43 = QtWidgets.QLabel(self.page_15)
        self.label_43.setGeometry(QtCore.QRect(500, 0, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.frame_28 = QtWidgets.QFrame(self.page_15)
        self.frame_28.setGeometry(QtCore.QRect(0, 30, 111, 641))
        self.frame_28.setMouseTracking(True)
        self.frame_28.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.pushButton_26 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_26.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_26.setFont(font)
        self.pushButton_26.setMouseTracking(True)
        self.pushButton_26.setObjectName("pushButton_26")
        self.pushButton_27 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_27.setGeometry(QtCore.QRect(10, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setMouseTracking(True)
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_99 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_99.setGeometry(QtCore.QRect(10, 90, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_99.setFont(font)
        self.pushButton_99.setMouseTracking(True)
        self.pushButton_99.setObjectName("pushButton_99")
        self.pushButton_100 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_100.setGeometry(QtCore.QRect(10, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_100.setFont(font)
        self.pushButton_100.setMouseTracking(True)
        self.pushButton_100.setObjectName("pushButton_100")
        self.pushButton_102 = QtWidgets.QPushButton(self.frame_28)
        self.pushButton_102.setGeometry(QtCore.QRect(10, 160, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_102.setFont(font)
        self.pushButton_102.setMouseTracking(True)
        self.pushButton_102.setObjectName("pushButton_102")
        self.label_44 = QtWidgets.QLabel(self.frame_28)
        self.label_44.setGeometry(QtCore.QRect(10, 140, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setObjectName("label_44")
        self.tableWidget_10 = QtWidgets.QTableWidget(self.page_15)
        self.tableWidget_10.setGeometry(QtCore.QRect(120, 30, 921, 621))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_10.setFont(font)
        self.tableWidget_10.setMouseTracking(True)
        self.tableWidget_10.setRowCount(5)
        self.tableWidget_10.setColumnCount(21)
        self.tableWidget_10.setObjectName("tableWidget_10")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_10.setHorizontalHeaderItem(20, item)
        self.stackedWidget.addWidget(self.page_15)
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setObjectName("page_17")
        self.frame_30 = QtWidgets.QFrame(self.page_17)
        self.frame_30.setGeometry(QtCore.QRect(200, 40, 841, 801))
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.label_113 = QtWidgets.QLabel(self.frame_30)
        self.label_113.setGeometry(QtCore.QRect(10, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_113.setFont(font)
        self.label_113.setObjectName("label_113")
        self.label_131 = QtWidgets.QLabel(self.frame_30)
        self.label_131.setGeometry(QtCore.QRect(10, 50, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_131.setFont(font)
        self.label_131.setObjectName("label_131")
        self.label_132 = QtWidgets.QLabel(self.frame_30)
        self.label_132.setGeometry(QtCore.QRect(10, 90, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_132.setFont(font)
        self.label_132.setObjectName("label_132")
        self.label_134 = QtWidgets.QLabel(self.frame_30)
        self.label_134.setGeometry(QtCore.QRect(10, 130, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_134.setFont(font)
        self.label_134.setObjectName("label_134")
        self.label_135 = QtWidgets.QLabel(self.frame_30)
        self.label_135.setGeometry(QtCore.QRect(10, 170, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_135.setFont(font)
        self.label_135.setObjectName("label_135")
        self.label_136 = QtWidgets.QLabel(self.frame_30)
        self.label_136.setGeometry(QtCore.QRect(10, 210, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_136.setFont(font)
        self.label_136.setObjectName("label_136")
        self.label_137 = QtWidgets.QLabel(self.frame_30)
        self.label_137.setGeometry(QtCore.QRect(10, 250, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_137.setFont(font)
        self.label_137.setObjectName("label_137")
        self.label_138 = QtWidgets.QLabel(self.frame_30)
        self.label_138.setGeometry(QtCore.QRect(10, 330, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_138.setFont(font)
        self.label_138.setObjectName("label_138")
        self.label_139 = QtWidgets.QLabel(self.frame_30)
        self.label_139.setGeometry(QtCore.QRect(10, 290, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_139.setFont(font)
        self.label_139.setObjectName("label_139")
        self.label_140 = QtWidgets.QLabel(self.frame_30)
        self.label_140.setGeometry(QtCore.QRect(10, 410, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_140.setFont(font)
        self.label_140.setObjectName("label_140")
        self.label_141 = QtWidgets.QLabel(self.frame_30)
        self.label_141.setGeometry(QtCore.QRect(10, 370, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_141.setFont(font)
        self.label_141.setObjectName("label_141")
        self.label_142 = QtWidgets.QLabel(self.frame_30)
        self.label_142.setGeometry(QtCore.QRect(10, 490, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_142.setFont(font)
        self.label_142.setObjectName("label_142")
        self.label_143 = QtWidgets.QLabel(self.frame_30)
        self.label_143.setGeometry(QtCore.QRect(10, 450, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_143.setFont(font)
        self.label_143.setObjectName("label_143")
        self.label_144 = QtWidgets.QLabel(self.frame_30)
        self.label_144.setGeometry(QtCore.QRect(10, 570, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_144.setFont(font)
        self.label_144.setObjectName("label_144")
        self.label_145 = QtWidgets.QLabel(self.frame_30)
        self.label_145.setGeometry(QtCore.QRect(10, 530, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_145.setFont(font)
        self.label_145.setObjectName("label_145")
        self.save_10 = QtWidgets.QPushButton(self.frame_30)
        self.save_10.setGeometry(QtCore.QRect(190, 600, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_10.setFont(font)
        self.save_10.setObjectName("save_10")
        self.category_3 = QtWidgets.QLineEdit(self.frame_30)
        self.category_3.setGeometry(QtCore.QRect(150, 50, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.category_3.setFont(font)
        self.category_3.setObjectName("category_3")
        self.s1m = QtWidgets.QLineEdit(self.frame_30)
        self.s1m.setGeometry(QtCore.QRect(150, 130, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s1m.setFont(font)
        self.s1m.setObjectName("s1m")
        self.s1f = QtWidgets.QLineEdit(self.frame_30)
        self.s1f.setGeometry(QtCore.QRect(150, 170, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s1f.setFont(font)
        self.s1f.setObjectName("s1f")
        self.s2m = QtWidgets.QLineEdit(self.frame_30)
        self.s2m.setGeometry(QtCore.QRect(150, 210, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s2m.setFont(font)
        self.s2m.setObjectName("s2m")
        self.s2f = QtWidgets.QLineEdit(self.frame_30)
        self.s2f.setGeometry(QtCore.QRect(150, 250, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s2f.setFont(font)
        self.s2f.setObjectName("s2f")
        self.s3m = QtWidgets.QLineEdit(self.frame_30)
        self.s3m.setGeometry(QtCore.QRect(150, 290, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s3m.setFont(font)
        self.s3m.setObjectName("s3m")
        self.s3f = QtWidgets.QLineEdit(self.frame_30)
        self.s3f.setGeometry(QtCore.QRect(150, 330, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s3f.setFont(font)
        self.s3f.setObjectName("s3f")
        self.s4m = QtWidgets.QLineEdit(self.frame_30)
        self.s4m.setGeometry(QtCore.QRect(150, 370, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s4m.setFont(font)
        self.s4m.setObjectName("s4m")
        self.s4f = QtWidgets.QLineEdit(self.frame_30)
        self.s4f.setGeometry(QtCore.QRect(150, 410, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s4f.setFont(font)
        self.s4f.setObjectName("s4f")
        self.s5m = QtWidgets.QLineEdit(self.frame_30)
        self.s5m.setGeometry(QtCore.QRect(150, 450, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s5m.setFont(font)
        self.s5m.setObjectName("s5m")
        self.s5f = QtWidgets.QLineEdit(self.frame_30)
        self.s5f.setGeometry(QtCore.QRect(150, 490, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s5f.setFont(font)
        self.s5f.setObjectName("s5f")
        self.s6m = QtWidgets.QLineEdit(self.frame_30)
        self.s6m.setGeometry(QtCore.QRect(150, 530, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s6m.setFont(font)
        self.s6m.setObjectName("s6m")
        self.p6f_2 = QtWidgets.QLineEdit(self.frame_30)
        self.p6f_2.setGeometry(QtCore.QRect(150, 570, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p6f_2.setFont(font)
        self.p6f_2.setObjectName("p6f_2")
        self.comboBox_15 = QtWidgets.QComboBox(self.frame_30)
        self.comboBox_15.setGeometry(QtCore.QRect(150, 90, 101, 22))
        self.comboBox_15.setObjectName("comboBox_15")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.comboBox_15.addItem("")
        self.schooln_2 = QtWidgets.QLineEdit(self.frame_30)
        self.schooln_2.setGeometry(QtCore.QRect(150, 10, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.schooln_2.setFont(font)
        self.schooln_2.setObjectName("schooln_2")
        self.save_23 = QtWidgets.QPushButton(self.frame_30)
        self.save_23.setGeometry(QtCore.QRect(670, 600, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_23.setFont(font)
        self.save_23.setObjectName("save_23")
        self.frame_31 = QtWidgets.QFrame(self.page_17)
        self.frame_31.setGeometry(QtCore.QRect(0, 10, 201, 131))
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.home_10 = QtWidgets.QPushButton(self.frame_31)
        self.home_10.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_10.setFont(font)
        self.home_10.setObjectName("home_10")
        self.back_9 = QtWidgets.QPushButton(self.frame_31)
        self.back_9.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_9.setFont(font)
        self.back_9.setObjectName("back_9")
        self.pushButton_112 = QtWidgets.QPushButton(self.frame_31)
        self.pushButton_112.setGeometry(QtCore.QRect(10, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_112.setFont(font)
        self.pushButton_112.setObjectName("pushButton_112")
        self.label_159 = QtWidgets.QLabel(self.page_17)
        self.label_159.setGeometry(QtCore.QRect(260, 0, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_159.setFont(font)
        self.label_159.setObjectName("label_159")
        self.frame_32 = QtWidgets.QFrame(self.page_17)
        self.frame_32.setGeometry(QtCore.QRect(0, 150, 201, 551))
        self.frame_32.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_32.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_32.setObjectName("frame_32")
        self.stackedWidget.addWidget(self.page_17)
        self.page_18 = QtWidgets.QWidget()
        self.page_18.setObjectName("page_18")
        self.label_148 = QtWidgets.QLabel(self.page_18)
        self.label_148.setGeometry(QtCore.QRect(240, -10, 591, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_148.setFont(font)
        self.label_148.setObjectName("label_148")
        self.frame_33 = QtWidgets.QFrame(self.page_18)
        self.frame_33.setGeometry(QtCore.QRect(0, 0, 201, 131))
        self.frame_33.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_33.setObjectName("frame_33")
        self.home_11 = QtWidgets.QPushButton(self.frame_33)
        self.home_11.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_11.setFont(font)
        self.home_11.setObjectName("home_11")
        self.back_10 = QtWidgets.QPushButton(self.frame_33)
        self.back_10.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_10.setFont(font)
        self.back_10.setObjectName("back_10")
        self.pushButton_113 = QtWidgets.QPushButton(self.frame_33)
        self.pushButton_113.setGeometry(QtCore.QRect(10, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_113.setFont(font)
        self.pushButton_113.setObjectName("pushButton_113")
        self.frame_34 = QtWidgets.QFrame(self.page_18)
        self.frame_34.setGeometry(QtCore.QRect(0, 140, 201, 551))
        self.frame_34.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_34.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_34.setObjectName("frame_34")
        self.frame_35 = QtWidgets.QFrame(self.page_18)
        self.frame_35.setGeometry(QtCore.QRect(210, 30, 841, 801))
        self.frame_35.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_35.setObjectName("frame_35")
        self.label_149 = QtWidgets.QLabel(self.frame_35)
        self.label_149.setGeometry(QtCore.QRect(10, 11, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_149.setFont(font)
        self.label_149.setObjectName("label_149")
        self.label_170 = QtWidgets.QLabel(self.frame_35)
        self.label_170.setGeometry(QtCore.QRect(10, 40, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_170.setFont(font)
        self.label_170.setObjectName("label_170")
        self.label_171 = QtWidgets.QLabel(self.frame_35)
        self.label_171.setGeometry(QtCore.QRect(10, 70, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_171.setFont(font)
        self.label_171.setObjectName("label_171")
        self.label_172 = QtWidgets.QLabel(self.frame_35)
        self.label_172.setGeometry(QtCore.QRect(10, 100, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_172.setFont(font)
        self.label_172.setObjectName("label_172")
        self.label_173 = QtWidgets.QLabel(self.frame_35)
        self.label_173.setGeometry(QtCore.QRect(10, 130, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_173.setFont(font)
        self.label_173.setObjectName("label_173")
        self.label_174 = QtWidgets.QLabel(self.frame_35)
        self.label_174.setGeometry(QtCore.QRect(10, 160, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_174.setFont(font)
        self.label_174.setObjectName("label_174")
        self.label_175 = QtWidgets.QLabel(self.frame_35)
        self.label_175.setGeometry(QtCore.QRect(10, 190, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_175.setFont(font)
        self.label_175.setObjectName("label_175")
        self.label_178 = QtWidgets.QLabel(self.frame_35)
        self.label_178.setGeometry(QtCore.QRect(10, 220, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_178.setFont(font)
        self.label_178.setObjectName("label_178")
        self.label_179 = QtWidgets.QLabel(self.frame_35)
        self.label_179.setGeometry(QtCore.QRect(10, 250, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_179.setFont(font)
        self.label_179.setObjectName("label_179")
        self.save_11 = QtWidgets.QPushButton(self.frame_35)
        self.save_11.setGeometry(QtCore.QRect(210, 580, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_11.setFont(font)
        self.save_11.setObjectName("save_11")
        self.category_4 = QtWidgets.QLineEdit(self.frame_35)
        self.category_4.setGeometry(QtCore.QRect(130, 40, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.category_4.setFont(font)
        self.category_4.setObjectName("category_4")
        self.S1t = QtWidgets.QLineEdit(self.frame_35)
        self.S1t.setGeometry(QtCore.QRect(130, 100, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.S1t.setFont(font)
        self.S1t.setObjectName("S1t")
        self.s2t = QtWidgets.QLineEdit(self.frame_35)
        self.s2t.setGeometry(QtCore.QRect(130, 130, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s2t.setFont(font)
        self.s2t.setObjectName("s2t")
        self.s3t = QtWidgets.QLineEdit(self.frame_35)
        self.s3t.setGeometry(QtCore.QRect(130, 160, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s3t.setFont(font)
        self.s3t.setObjectName("s3t")
        self.s4t = QtWidgets.QLineEdit(self.frame_35)
        self.s4t.setGeometry(QtCore.QRect(130, 190, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s4t.setFont(font)
        self.s4t.setObjectName("s4t")
        self.s5t = QtWidgets.QLineEdit(self.frame_35)
        self.s5t.setGeometry(QtCore.QRect(130, 220, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.s5t.setFont(font)
        self.s5t.setObjectName("s5t")
        self.p6t_2 = QtWidgets.QLineEdit(self.frame_35)
        self.p6t_2.setGeometry(QtCore.QRect(130, 250, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p6t_2.setFont(font)
        self.p6t_2.setObjectName("p6t_2")
        self.comboBox_9 = QtWidgets.QComboBox(self.frame_35)
        self.comboBox_9.setGeometry(QtCore.QRect(130, 70, 101, 22))
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.label_205 = QtWidgets.QLabel(self.frame_35)
        self.label_205.setGeometry(QtCore.QRect(10, 280, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_205.setFont(font)
        self.label_205.setObjectName("label_205")
        self.licencedm_2 = QtWidgets.QLineEdit(self.frame_35)
        self.licencedm_2.setGeometry(QtCore.QRect(130, 280, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.licencedm_2.setFont(font)
        self.licencedm_2.setObjectName("licencedm_2")
        self.label_206 = QtWidgets.QLabel(self.frame_35)
        self.label_206.setGeometry(QtCore.QRect(10, 310, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_206.setFont(font)
        self.label_206.setObjectName("label_206")
        self.licencedf_2 = QtWidgets.QLineEdit(self.frame_35)
        self.licencedf_2.setGeometry(QtCore.QRect(130, 310, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.licencedf_2.setFont(font)
        self.licencedf_2.setObjectName("licencedf_2")
        self.label_207 = QtWidgets.QLabel(self.frame_35)
        self.label_207.setGeometry(QtCore.QRect(10, 340, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_207.setFont(font)
        self.label_207.setObjectName("label_207")
        self.certificatem_2 = QtWidgets.QLineEdit(self.frame_35)
        self.certificatem_2.setGeometry(QtCore.QRect(130, 340, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.certificatem_2.setFont(font)
        self.certificatem_2.setText("")
        self.certificatem_2.setObjectName("certificatem_2")
        self.label_208 = QtWidgets.QLabel(self.frame_35)
        self.label_208.setGeometry(QtCore.QRect(10, 370, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_208.setFont(font)
        self.label_208.setObjectName("label_208")
        self.certificatef_2 = QtWidgets.QLineEdit(self.frame_35)
        self.certificatef_2.setGeometry(QtCore.QRect(130, 370, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.certificatef_2.setFont(font)
        self.certificatef_2.setObjectName("certificatef_2")
        self.label_209 = QtWidgets.QLabel(self.frame_35)
        self.label_209.setGeometry(QtCore.QRect(10, 400, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_209.setFont(font)
        self.label_209.setObjectName("label_209")
        self.deplomam_2 = QtWidgets.QLineEdit(self.frame_35)
        self.deplomam_2.setGeometry(QtCore.QRect(130, 400, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.deplomam_2.setFont(font)
        self.deplomam_2.setObjectName("deplomam_2")
        self.label_212 = QtWidgets.QLabel(self.frame_35)
        self.label_212.setGeometry(QtCore.QRect(10, 430, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_212.setFont(font)
        self.label_212.setObjectName("label_212")
        self.deplomaf_2 = QtWidgets.QLineEdit(self.frame_35)
        self.deplomaf_2.setGeometry(QtCore.QRect(130, 430, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.deplomaf_2.setFont(font)
        self.deplomaf_2.setObjectName("deplomaf_2")
        self.label_213 = QtWidgets.QLabel(self.frame_35)
        self.label_213.setGeometry(QtCore.QRect(10, 460, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_213.setFont(font)
        self.label_213.setObjectName("label_213")
        self.bachelorsm_3 = QtWidgets.QLineEdit(self.frame_35)
        self.bachelorsm_3.setGeometry(QtCore.QRect(130, 460, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.bachelorsm_3.setFont(font)
        self.bachelorsm_3.setObjectName("bachelorsm_3")
        self.label_223 = QtWidgets.QLabel(self.frame_35)
        self.label_223.setGeometry(QtCore.QRect(10, 490, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_223.setFont(font)
        self.label_223.setObjectName("label_223")
        self.bachelorsf_2 = QtWidgets.QLineEdit(self.frame_35)
        self.bachelorsf_2.setGeometry(QtCore.QRect(130, 490, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.bachelorsf_2.setFont(font)
        self.bachelorsf_2.setObjectName("bachelorsf_2")
        self.label_230 = QtWidgets.QLabel(self.frame_35)
        self.label_230.setGeometry(QtCore.QRect(10, 520, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_230.setFont(font)
        self.label_230.setObjectName("label_230")
        self.mastersm_2 = QtWidgets.QLineEdit(self.frame_35)
        self.mastersm_2.setGeometry(QtCore.QRect(170, 520, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.mastersm_2.setFont(font)
        self.mastersm_2.setObjectName("mastersm_2")
        self.label_231 = QtWidgets.QLabel(self.frame_35)
        self.label_231.setGeometry(QtCore.QRect(10, 550, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_231.setFont(font)
        self.label_231.setObjectName("label_231")
        self.mastersf_2 = QtWidgets.QLineEdit(self.frame_35)
        self.mastersf_2.setGeometry(QtCore.QRect(170, 550, 641, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.mastersf_2.setFont(font)
        self.mastersf_2.setObjectName("mastersf_2")
        self.category_10 = QtWidgets.QLineEdit(self.frame_35)
        self.category_10.setGeometry(QtCore.QRect(130, 10, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.category_10.setFont(font)
        self.category_10.setObjectName("category_10")
        self.save_22 = QtWidgets.QPushButton(self.frame_35)
        self.save_22.setGeometry(QtCore.QRect(650, 580, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_22.setFont(font)
        self.save_22.setObjectName("save_22")
        self.stackedWidget.addWidget(self.page_18)
        self.page_19 = QtWidgets.QWidget()
        self.page_19.setObjectName("page_19")
        self.frame_36 = QtWidgets.QFrame(self.page_19)
        self.frame_36.setGeometry(QtCore.QRect(0, 130, 201, 561))
        self.frame_36.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_36.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_36.setObjectName("frame_36")
        self.frame_37 = QtWidgets.QFrame(self.page_19)
        self.frame_37.setGeometry(QtCore.QRect(0, 0, 201, 131))
        self.frame_37.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_37.setObjectName("frame_37")
        self.home_13 = QtWidgets.QPushButton(self.frame_37)
        self.home_13.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_13.setFont(font)
        self.home_13.setObjectName("home_13")
        self.back_12 = QtWidgets.QPushButton(self.frame_37)
        self.back_12.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_12.setFont(font)
        self.back_12.setObjectName("back_12")
        self.pushButton_89 = QtWidgets.QPushButton(self.frame_37)
        self.pushButton_89.setGeometry(QtCore.QRect(10, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_89.setFont(font)
        self.pushButton_89.setObjectName("pushButton_89")
        self.label_204 = QtWidgets.QLabel(self.page_19)
        self.label_204.setGeometry(QtCore.QRect(210, -6, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_204.setFont(font)
        self.label_204.setObjectName("label_204")
        self.frame_38 = QtWidgets.QFrame(self.page_19)
        self.frame_38.setGeometry(QtCore.QRect(200, 20, 841, 821))
        self.frame_38.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_38.setObjectName("frame_38")
        self.label_267 = QtWidgets.QLabel(self.frame_38)
        self.label_267.setGeometry(QtCore.QRect(10, 0, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_267.setFont(font)
        self.label_267.setObjectName("label_267")
        self.label_268 = QtWidgets.QLabel(self.frame_38)
        self.label_268.setGeometry(QtCore.QRect(10, 30, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_268.setFont(font)
        self.label_268.setObjectName("label_268")
        self.label_269 = QtWidgets.QLabel(self.frame_38)
        self.label_269.setGeometry(QtCore.QRect(10, 60, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_269.setFont(font)
        self.label_269.setObjectName("label_269")
        self.label_270 = QtWidgets.QLabel(self.frame_38)
        self.label_270.setGeometry(QtCore.QRect(10, 90, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_270.setFont(font)
        self.label_270.setObjectName("label_270")
        self.label_271 = QtWidgets.QLabel(self.frame_38)
        self.label_271.setGeometry(QtCore.QRect(10, 120, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_271.setFont(font)
        self.label_271.setObjectName("label_271")
        self.label_272 = QtWidgets.QLabel(self.frame_38)
        self.label_272.setGeometry(QtCore.QRect(10, 150, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_272.setFont(font)
        self.label_272.setObjectName("label_272")
        self.label_273 = QtWidgets.QLabel(self.frame_38)
        self.label_273.setGeometry(QtCore.QRect(10, 180, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_273.setFont(font)
        self.label_273.setObjectName("label_273")
        self.label_274 = QtWidgets.QLabel(self.frame_38)
        self.label_274.setGeometry(QtCore.QRect(10, 210, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_274.setFont(font)
        self.label_274.setObjectName("label_274")
        self.label_275 = QtWidgets.QLabel(self.frame_38)
        self.label_275.setGeometry(QtCore.QRect(10, 240, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_275.setFont(font)
        self.label_275.setObjectName("label_275")
        self.label_276 = QtWidgets.QLabel(self.frame_38)
        self.label_276.setGeometry(QtCore.QRect(10, 270, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_276.setFont(font)
        self.label_276.setObjectName("label_276")
        self.label_277 = QtWidgets.QLabel(self.frame_38)
        self.label_277.setGeometry(QtCore.QRect(10, 300, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_277.setFont(font)
        self.label_277.setObjectName("label_277")
        self.save_13 = QtWidgets.QPushButton(self.frame_38)
        self.save_13.setGeometry(QtCore.QRect(150, 600, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_13.setFont(font)
        self.save_13.setObjectName("save_13")
        self.library_3 = QtWidgets.QLineEdit(self.frame_38)
        self.library_3.setGeometry(QtCore.QRect(150, 90, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.library_3.setFont(font)
        self.library_3.setObjectName("library_3")
        self.sciencelab_5 = QtWidgets.QLineEdit(self.frame_38)
        self.sciencelab_5.setGeometry(QtCore.QRect(150, 120, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.sciencelab_5.setFont(font)
        self.sciencelab_5.setObjectName("sciencelab_5")
        self.complab_3 = QtWidgets.QLineEdit(self.frame_38)
        self.complab_3.setGeometry(QtCore.QRect(170, 150, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.complab_3.setFont(font)
        self.complab_3.setObjectName("complab_3")
        self.kitchen_3 = QtWidgets.QLineEdit(self.frame_38)
        self.kitchen_3.setGeometry(QtCore.QRect(150, 180, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.kitchen_3.setFont(font)
        self.kitchen_3.setObjectName("kitchen_3")
        self.staffroom_3 = QtWidgets.QLineEdit(self.frame_38)
        self.staffroom_3.setGeometry(QtCore.QRect(150, 210, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.staffroom_3.setFont(font)
        self.staffroom_3.setObjectName("staffroom_3")
        self.adminblock_3 = QtWidgets.QLineEdit(self.frame_38)
        self.adminblock_3.setGeometry(QtCore.QRect(170, 240, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.adminblock_3.setFont(font)
        self.adminblock_3.setObjectName("adminblock_3")
        self.dinninghall_3 = QtWidgets.QLineEdit(self.frame_38)
        self.dinninghall_3.setGeometry(QtCore.QRect(150, 270, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.dinninghall_3.setFont(font)
        self.dinninghall_3.setObjectName("dinninghall_3")
        self.reliablesafewater_3 = QtWidgets.QLineEdit(self.frame_38)
        self.reliablesafewater_3.setGeometry(QtCore.QRect(210, 300, 621, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.reliablesafewater_3.setFont(font)
        self.reliablesafewater_3.setObjectName("reliablesafewater_3")
        self.comboBox_11 = QtWidgets.QComboBox(self.frame_38)
        self.comboBox_11.setGeometry(QtCore.QRect(150, 60, 101, 22))
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.label_278 = QtWidgets.QLabel(self.frame_38)
        self.label_278.setGeometry(QtCore.QRect(10, 330, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_278.setFont(font)
        self.label_278.setObjectName("label_278")
        self.stores_3 = QtWidgets.QLineEdit(self.frame_38)
        self.stores_3.setGeometry(QtCore.QRect(150, 330, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.stores_3.setFont(font)
        self.stores_3.setObjectName("stores_3")
        self.label_279 = QtWidgets.QLabel(self.frame_38)
        self.label_279.setGeometry(QtCore.QRect(10, 360, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_279.setFont(font)
        self.label_279.setObjectName("label_279")
        self.workshop_3 = QtWidgets.QLineEdit(self.frame_38)
        self.workshop_3.setGeometry(QtCore.QRect(150, 360, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.workshop_3.setFont(font)
        self.workshop_3.setObjectName("workshop_3")
        self.label_280 = QtWidgets.QLabel(self.frame_38)
        self.label_280.setGeometry(QtCore.QRect(10, 390, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_280.setFont(font)
        self.label_280.setObjectName("label_280")
        self.playground_3 = QtWidgets.QLineEdit(self.frame_38)
        self.playground_3.setGeometry(QtCore.QRect(150, 390, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.playground_3.setFont(font)
        self.playground_3.setText("")
        self.playground_3.setObjectName("playground_3")
        self.label_281 = QtWidgets.QLabel(self.frame_38)
        self.label_281.setGeometry(QtCore.QRect(10, 420, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_281.setFont(font)
        self.label_281.setObjectName("label_281")
        self.garden_3 = QtWidgets.QLineEdit(self.frame_38)
        self.garden_3.setGeometry(QtCore.QRect(150, 420, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.garden_3.setFont(font)
        self.garden_3.setObjectName("garden_3")
        self.label_282 = QtWidgets.QLabel(self.frame_38)
        self.label_282.setGeometry(QtCore.QRect(10, 450, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_282.setFont(font)
        self.label_282.setObjectName("label_282")
        self.latrine_3 = QtWidgets.QLineEdit(self.frame_38)
        self.latrine_3.setGeometry(QtCore.QRect(150, 450, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.latrine_3.setFont(font)
        self.latrine_3.setObjectName("latrine_3")
        self.label_283 = QtWidgets.QLabel(self.frame_38)
        self.label_283.setGeometry(QtCore.QRect(10, 480, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_283.setFont(font)
        self.label_283.setObjectName("label_283")
        self.stances_3 = QtWidgets.QLineEdit(self.frame_38)
        self.stances_3.setGeometry(QtCore.QRect(150, 480, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.stances_3.setFont(font)
        self.stances_3.setObjectName("stances_3")
        self.label_284 = QtWidgets.QLabel(self.frame_38)
        self.label_284.setGeometry(QtCore.QRect(10, 510, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_284.setFont(font)
        self.label_284.setObjectName("label_284")
        self.bachelorsm_5 = QtWidgets.QLineEdit(self.frame_38)
        self.bachelorsm_5.setGeometry(QtCore.QRect(180, 510, 651, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.bachelorsm_5.setFont(font)
        self.bachelorsm_5.setObjectName("bachelorsm_5")
        self.label_285 = QtWidgets.QLabel(self.frame_38)
        self.label_285.setGeometry(QtCore.QRect(10, 540, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_285.setFont(font)
        self.label_285.setObjectName("label_285")
        self.p1_5 = QtWidgets.QLineEdit(self.frame_38)
        self.p1_5.setGeometry(QtCore.QRect(90, 540, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p1_5.setFont(font)
        self.p1_5.setObjectName("p1_5")
        self.label_286 = QtWidgets.QLabel(self.frame_38)
        self.label_286.setGeometry(QtCore.QRect(290, 540, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_286.setFont(font)
        self.label_286.setObjectName("label_286")
        self.p2_4 = QtWidgets.QLineEdit(self.frame_38)
        self.p2_4.setGeometry(QtCore.QRect(370, 540, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p2_4.setFont(font)
        self.p2_4.setObjectName("p2_4")
        self.label_287 = QtWidgets.QLabel(self.frame_38)
        self.label_287.setGeometry(QtCore.QRect(590, 540, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_287.setFont(font)
        self.label_287.setObjectName("label_287")
        self.p3_4 = QtWidgets.QLineEdit(self.frame_38)
        self.p3_4.setGeometry(QtCore.QRect(660, 540, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p3_4.setFont(font)
        self.p3_4.setObjectName("p3_4")
        self.label_288 = QtWidgets.QLabel(self.frame_38)
        self.label_288.setGeometry(QtCore.QRect(10, 570, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_288.setFont(font)
        self.label_288.setObjectName("label_288")
        self.p4_4 = QtWidgets.QLineEdit(self.frame_38)
        self.p4_4.setGeometry(QtCore.QRect(90, 570, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p4_4.setFont(font)
        self.p4_4.setText("")
        self.p4_4.setObjectName("p4_4")
        self.label_289 = QtWidgets.QLabel(self.frame_38)
        self.label_289.setGeometry(QtCore.QRect(290, 570, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_289.setFont(font)
        self.label_289.setObjectName("label_289")
        self.p5_4 = QtWidgets.QLineEdit(self.frame_38)
        self.p5_4.setGeometry(QtCore.QRect(370, 570, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p5_4.setFont(font)
        self.p5_4.setObjectName("p5_4")
        self.p6_4 = QtWidgets.QLineEdit(self.frame_38)
        self.p6_4.setGeometry(QtCore.QRect(660, 570, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p6_4.setFont(font)
        self.p6_4.setObjectName("p6_4")
        self.label_290 = QtWidgets.QLabel(self.frame_38)
        self.label_290.setGeometry(QtCore.QRect(590, 570, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_290.setFont(font)
        self.label_290.setObjectName("label_290")
        self.category_12 = QtWidgets.QLineEdit(self.frame_38)
        self.category_12.setGeometry(QtCore.QRect(150, 0, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.category_12.setFont(font)
        self.category_12.setObjectName("category_12")
        self.sciencelab_6 = QtWidgets.QLineEdit(self.frame_38)
        self.sciencelab_6.setGeometry(QtCore.QRect(150, 30, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.sciencelab_6.setFont(font)
        self.sciencelab_6.setObjectName("sciencelab_6")
        self.save_21 = QtWidgets.QPushButton(self.frame_38)
        self.save_21.setGeometry(QtCore.QRect(640, 600, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_21.setFont(font)
        self.save_21.setObjectName("save_21")
        self.stackedWidget.addWidget(self.page_19)
        self.page_20 = QtWidgets.QWidget()
        self.page_20.setObjectName("page_20")
        self.frame_39 = QtWidgets.QFrame(self.page_20)
        self.frame_39.setGeometry(QtCore.QRect(0, 0, 201, 131))
        self.frame_39.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_39.setObjectName("frame_39")
        self.home_14 = QtWidgets.QPushButton(self.frame_39)
        self.home_14.setGeometry(QtCore.QRect(10, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.home_14.setFont(font)
        self.home_14.setObjectName("home_14")
        self.back_13 = QtWidgets.QPushButton(self.frame_39)
        self.back_13.setGeometry(QtCore.QRect(10, 50, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.back_13.setFont(font)
        self.back_13.setObjectName("back_13")
        self.pushButton_90 = QtWidgets.QPushButton(self.frame_39)
        self.pushButton_90.setGeometry(QtCore.QRect(10, 90, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_90.setFont(font)
        self.pushButton_90.setObjectName("pushButton_90")
        self.frame_40 = QtWidgets.QFrame(self.page_20)
        self.frame_40.setGeometry(QtCore.QRect(200, 40, 841, 571))
        self.frame_40.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_40.setObjectName("frame_40")
        self.label_292 = QtWidgets.QLabel(self.frame_40)
        self.label_292.setGeometry(QtCore.QRect(10, 20, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_292.setFont(font)
        self.label_292.setObjectName("label_292")
        self.label_293 = QtWidgets.QLabel(self.frame_40)
        self.label_293.setGeometry(QtCore.QRect(10, 50, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_293.setFont(font)
        self.label_293.setObjectName("label_293")
        self.label_294 = QtWidgets.QLabel(self.frame_40)
        self.label_294.setGeometry(QtCore.QRect(10, 80, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_294.setFont(font)
        self.label_294.setObjectName("label_294")
        self.label_295 = QtWidgets.QLabel(self.frame_40)
        self.label_295.setGeometry(QtCore.QRect(10, 110, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_295.setFont(font)
        self.label_295.setObjectName("label_295")
        self.label_296 = QtWidgets.QLabel(self.frame_40)
        self.label_296.setGeometry(QtCore.QRect(10, 140, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_296.setFont(font)
        self.label_296.setObjectName("label_296")
        self.label_297 = QtWidgets.QLabel(self.frame_40)
        self.label_297.setGeometry(QtCore.QRect(10, 170, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_297.setFont(font)
        self.label_297.setObjectName("label_297")
        self.label_298 = QtWidgets.QLabel(self.frame_40)
        self.label_298.setGeometry(QtCore.QRect(10, 200, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_298.setFont(font)
        self.label_298.setObjectName("label_298")
        self.label_299 = QtWidgets.QLabel(self.frame_40)
        self.label_299.setGeometry(QtCore.QRect(10, 230, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_299.setFont(font)
        self.label_299.setObjectName("label_299")
        self.label_300 = QtWidgets.QLabel(self.frame_40)
        self.label_300.setGeometry(QtCore.QRect(10, 260, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_300.setFont(font)
        self.label_300.setObjectName("label_300")
        self.save_14 = QtWidgets.QPushButton(self.frame_40)
        self.save_14.setGeometry(QtCore.QRect(260, 470, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_14.setFont(font)
        self.save_14.setObjectName("save_14")
        self.p1_6 = QtWidgets.QLineEdit(self.frame_40)
        self.p1_6.setGeometry(QtCore.QRect(150, 110, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p1_6.setFont(font)
        self.p1_6.setObjectName("p1_6")
        self.p2_5 = QtWidgets.QLineEdit(self.frame_40)
        self.p2_5.setGeometry(QtCore.QRect(150, 140, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p2_5.setFont(font)
        self.p2_5.setObjectName("p2_5")
        self.p3_5 = QtWidgets.QLineEdit(self.frame_40)
        self.p3_5.setGeometry(QtCore.QRect(170, 170, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p3_5.setFont(font)
        self.p3_5.setObjectName("p3_5")
        self.p4_5 = QtWidgets.QLineEdit(self.frame_40)
        self.p4_5.setGeometry(QtCore.QRect(170, 200, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p4_5.setFont(font)
        self.p4_5.setObjectName("p4_5")
        self.p5_5 = QtWidgets.QLineEdit(self.frame_40)
        self.p5_5.setGeometry(QtCore.QRect(170, 230, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p5_5.setFont(font)
        self.p5_5.setObjectName("p5_5")
        self.p6_5 = QtWidgets.QLineEdit(self.frame_40)
        self.p6_5.setGeometry(QtCore.QRect(170, 260, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p6_5.setFont(font)
        self.p6_5.setObjectName("p6_5")
        self.comboBox_12 = QtWidgets.QComboBox(self.frame_40)
        self.comboBox_12.setGeometry(QtCore.QRect(150, 80, 101, 22))
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.label_302 = QtWidgets.QLabel(self.frame_40)
        self.label_302.setGeometry(QtCore.QRect(10, 290, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_302.setFont(font)
        self.label_302.setObjectName("label_302")
        self.permanent_3 = QtWidgets.QLineEdit(self.frame_40)
        self.permanent_3.setGeometry(QtCore.QRect(170, 290, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.permanent_3.setFont(font)
        self.permanent_3.setObjectName("permanent_3")
        self.label_303 = QtWidgets.QLabel(self.frame_40)
        self.label_303.setGeometry(QtCore.QRect(10, 320, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_303.setFont(font)
        self.label_303.setObjectName("label_303")
        self.temporary_3 = QtWidgets.QLineEdit(self.frame_40)
        self.temporary_3.setGeometry(QtCore.QRect(170, 320, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.temporary_3.setFont(font)
        self.temporary_3.setObjectName("temporary_3")
        self.label_304 = QtWidgets.QLabel(self.frame_40)
        self.label_304.setGeometry(QtCore.QRect(10, 350, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_304.setFont(font)
        self.label_304.setObjectName("label_304")
        self.atfoundation_3 = QtWidgets.QLineEdit(self.frame_40)
        self.atfoundation_3.setGeometry(QtCore.QRect(170, 350, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.atfoundation_3.setFont(font)
        self.atfoundation_3.setText("")
        self.atfoundation_3.setObjectName("atfoundation_3")
        self.label_305 = QtWidgets.QLabel(self.frame_40)
        self.label_305.setGeometry(QtCore.QRect(10, 380, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_305.setFont(font)
        self.label_305.setObjectName("label_305")
        self.atwindow_3 = QtWidgets.QLineEdit(self.frame_40)
        self.atwindow_3.setGeometry(QtCore.QRect(170, 380, 661, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.atwindow_3.setFont(font)
        self.atwindow_3.setObjectName("atwindow_3")
        self.label_306 = QtWidgets.QLabel(self.frame_40)
        self.label_306.setGeometry(QtCore.QRect(10, 410, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_306.setFont(font)
        self.label_306.setObjectName("label_306")
        self.wallpaltw_3 = QtWidgets.QLineEdit(self.frame_40)
        self.wallpaltw_3.setGeometry(QtCore.QRect(200, 410, 631, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.wallpaltw_3.setFont(font)
        self.wallpaltw_3.setObjectName("wallpaltw_3")
        self.label_307 = QtWidgets.QLabel(self.frame_40)
        self.label_307.setGeometry(QtCore.QRect(10, 440, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_307.setFont(font)
        self.label_307.setObjectName("label_307")
        self.withoutstructures_2 = QtWidgets.QLineEdit(self.frame_40)
        self.withoutstructures_2.setGeometry(QtCore.QRect(300, 440, 531, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.withoutstructures_2.setFont(font)
        self.withoutstructures_2.setObjectName("withoutstructures_2")
        self.category_13 = QtWidgets.QLineEdit(self.frame_40)
        self.category_13.setGeometry(QtCore.QRect(150, 20, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.category_13.setFont(font)
        self.category_13.setObjectName("category_13")
        self.p1_7 = QtWidgets.QLineEdit(self.frame_40)
        self.p1_7.setGeometry(QtCore.QRect(150, 50, 681, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.p1_7.setFont(font)
        self.p1_7.setObjectName("p1_7")
        self.save_20 = QtWidgets.QPushButton(self.frame_40)
        self.save_20.setGeometry(QtCore.QRect(660, 470, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.save_20.setFont(font)
        self.save_20.setObjectName("save_20")
        self.label_308 = QtWidgets.QLabel(self.page_20)
        self.label_308.setGeometry(QtCore.QRect(210, 0, 541, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_308.setFont(font)
        self.label_308.setObjectName("label_308")
        self.frame_41 = QtWidgets.QFrame(self.page_20)
        self.frame_41.setGeometry(QtCore.QRect(0, 130, 201, 551))
        self.frame_41.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_41.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_41.setObjectName("frame_41")
        self.stackedWidget.addWidget(self.page_20)
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setObjectName("page_16")
        self.tableWidget_11 = QtWidgets.QTableWidget(self.page_16)
        self.tableWidget_11.setGeometry(QtCore.QRect(130, 30, 911, 611))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.tableWidget_11.setFont(font)
        self.tableWidget_11.setMouseTracking(True)
        self.tableWidget_11.setRowCount(5)
        self.tableWidget_11.setColumnCount(23)
        self.tableWidget_11.setObjectName("tableWidget_11")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_11.setHorizontalHeaderItem(22, item)
        self.label_71 = QtWidgets.QLabel(self.page_16)
        self.label_71.setGeometry(QtCore.QRect(500, 0, 291, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_71.setFont(font)
        self.label_71.setObjectName("label_71")
        self.frame_61 = QtWidgets.QFrame(self.page_16)
        self.frame_61.setGeometry(QtCore.QRect(0, 30, 121, 641))
        self.frame_61.setMouseTracking(True)
        self.frame_61.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_61.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_61.setObjectName("frame_61")
        self.pushButton_63 = QtWidgets.QPushButton(self.frame_61)
        self.pushButton_63.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_63.setFont(font)
        self.pushButton_63.setMouseTracking(True)
        self.pushButton_63.setObjectName("pushButton_63")
        self.pushButton_103 = QtWidgets.QPushButton(self.frame_61)
        self.pushButton_103.setGeometry(QtCore.QRect(10, 50, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_103.setFont(font)
        self.pushButton_103.setMouseTracking(True)
        self.pushButton_103.setObjectName("pushButton_103")
        self.pushButton_104 = QtWidgets.QPushButton(self.frame_61)
        self.pushButton_104.setGeometry(QtCore.QRect(10, 90, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_104.setFont(font)
        self.pushButton_104.setMouseTracking(True)
        self.pushButton_104.setObjectName("pushButton_104")
        self.stackedWidget.addWidget(self.page_16)
        self.page_21 = QtWidgets.QWidget()
        self.page_21.setObjectName("page_21")
        self.pushButton_28 = QtWidgets.QPushButton(self.page_21)
        self.pushButton_28.setGeometry(QtCore.QRect(570, 70, 75, 31))
        self.pushButton_28.setMouseTracking(True)
        self.pushButton_28.setObjectName("pushButton_28")
        self.label_36 = QtWidgets.QLabel(self.page_21)
        self.label_36.setGeometry(QtCore.QRect(270, 60, 241, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.frame_29 = QtWidgets.QFrame(self.page_21)
        self.frame_29.setGeometry(QtCore.QRect(0, 50, 151, 591))
        self.frame_29.setMouseTracking(True)
        self.frame_29.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.pushButton_29 = QtWidgets.QPushButton(self.frame_29)
        self.pushButton_29.setGeometry(QtCore.QRect(10, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_32 = QtWidgets.QPushButton(self.frame_29)
        self.pushButton_32.setGeometry(QtCore.QRect(10, 50, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setObjectName("pushButton_32")
        self.pushButton_121 = QtWidgets.QPushButton(self.frame_29)
        self.pushButton_121.setGeometry(QtCore.QRect(10, 120, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_121.setFont(font)
        self.pushButton_121.setObjectName("pushButton_121")
        self.pushButton_122 = QtWidgets.QPushButton(self.frame_29)
        self.pushButton_122.setGeometry(QtCore.QRect(10, 160, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_122.setFont(font)
        self.pushButton_122.setObjectName("pushButton_122")
        self.label_39 = QtWidgets.QLabel(self.frame_29)
        self.label_39.setGeometry(QtCore.QRect(50, 100, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.pushButton_33 = QtWidgets.QPushButton(self.page_21)
        self.pushButton_33.setGeometry(QtCore.QRect(290, 600, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_33.setFont(font)
        self.pushButton_33.setObjectName("pushButton_33")
        self.pushButton_106 = QtWidgets.QPushButton(self.page_21)
        self.pushButton_106.setGeometry(QtCore.QRect(450, 600, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_106.setFont(font)
        self.pushButton_106.setObjectName("pushButton_106")
        self.label_45 = QtWidgets.QLabel(self.page_21)
        self.label_45.setGeometry(QtCore.QRect(470, 0, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setObjectName("label_45")
        self.textEdit_2 = QtWidgets.QTextEdit(self.page_21)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 110, 881, 481))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setMouseTracking(True)
        self.textEdit_2.setTabletTracking(True)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton_115 = QtWidgets.QPushButton(self.page_21)
        self.pushButton_115.setGeometry(QtCore.QRect(610, 600, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_115.setFont(font)
        self.pushButton_115.setObjectName("pushButton_115")
        self.lineEdit_15 = QtWidgets.QLineEdit(self.page_21)
        self.lineEdit_15.setGeometry(QtCore.QRect(270, 30, 671, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_15.setFont(font)
        self.lineEdit_15.setInputMask("")
        self.lineEdit_15.setText("")
        self.lineEdit_15.setDragEnabled(True)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.pushButton_116 = QtWidgets.QPushButton(self.page_21)
        self.pushButton_116.setGeometry(QtCore.QRect(770, 600, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_116.setFont(font)
        self.pushButton_116.setObjectName("pushButton_116")
        self.stackedWidget.addWidget(self.page_21)
        self.page_32 = QtWidgets.QWidget()
        self.page_32.setObjectName("page_32")
        self.frame_107 = QtWidgets.QFrame(self.page_32)
        self.frame_107.setGeometry(QtCore.QRect(0, 40, 111, 801))
        self.frame_107.setMouseTracking(True)
        self.frame_107.setStyleSheet("background-color: rgb(170, 170, 255);")
        self.frame_107.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_107.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_107.setObjectName("frame_107")
        self.pushButton_249 = QtWidgets.QPushButton(self.frame_107)
        self.pushButton_249.setGeometry(QtCore.QRect(10, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_249.setFont(font)
        self.pushButton_249.setObjectName("pushButton_249")
        self.label_507 = QtWidgets.QLabel(self.page_32)
        self.label_507.setGeometry(QtCore.QRect(0, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_507.setFont(font)
        self.label_507.setObjectName("label_507")
        self.tabWidget = QtWidgets.QTabWidget(self.page_32)
        self.tabWidget.setGeometry(QtCore.QRect(120, 10, 1041, 831))
        self.tabWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label_51 = QtWidgets.QLabel(self.tab_3)
        self.label_51.setGeometry(QtCore.QRect(20, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_51.setFont(font)
        self.label_51.setObjectName("label_51")
        self.textEdit_3 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_3.setGeometry(QtCore.QRect(20, 20, 391, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_3.setFont(font)
        self.textEdit_3.setObjectName("textEdit_3")
        self.widget = MplWidget(self.tab_3)
        self.widget.setGeometry(QtCore.QRect(420, 30, 251, 281))
        self.widget.setObjectName("widget")
        self.label_52 = QtWidgets.QLabel(self.tab_3)
        self.label_52.setGeometry(QtCore.QRect(20, 220, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.textEdit_4 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_4.setGeometry(QtCore.QRect(20, 240, 391, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_4.setFont(font)
        self.textEdit_4.setObjectName("textEdit_4")
        self.label_54 = QtWidgets.QLabel(self.tab_3)
        self.label_54.setGeometry(QtCore.QRect(420, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_54.setFont(font)
        self.label_54.setObjectName("label_54")
        self.widget_2 = MplWidget(self.tab_3)
        self.widget_2.setGeometry(QtCore.QRect(420, 360, 251, 281))
        self.widget_2.setObjectName("widget_2")
        self.label_56 = QtWidgets.QLabel(self.tab_3)
        self.label_56.setGeometry(QtCore.QRect(20, 390, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_56.setFont(font)
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(self.tab_3)
        self.label_57.setGeometry(QtCore.QRect(420, 330, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_57.setFont(font)
        self.label_57.setObjectName("label_57")
        self.textEdit_5 = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit_5.setGeometry(QtCore.QRect(20, 410, 391, 241))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setObjectName("textEdit_5")
        self.widget_48 = MplWidget(self.tab_3)
        self.widget_48.setGeometry(QtCore.QRect(680, 30, 231, 281))
        self.widget_48.setObjectName("widget_48")
        self.widget_49 = MplWidget(self.tab_3)
        self.widget_49.setGeometry(QtCore.QRect(680, 360, 231, 281))
        self.widget_49.setObjectName("widget_49")
        self.label_55 = QtWidgets.QLabel(self.tab_3)
        self.label_55.setGeometry(QtCore.QRect(420, 20, 47, 13))
        self.label_55.setObjectName("label_55")
        self.label_311 = QtWidgets.QLabel(self.tab_3)
        self.label_311.setGeometry(QtCore.QRect(680, 20, 71, 16))
        self.label_311.setObjectName("label_311")
        self.label_312 = QtWidgets.QLabel(self.tab_3)
        self.label_312.setGeometry(QtCore.QRect(420, 350, 47, 13))
        self.label_312.setObjectName("label_312")
        self.label_313 = QtWidgets.QLabel(self.tab_3)
        self.label_313.setGeometry(QtCore.QRect(680, 350, 71, 16))
        self.label_313.setObjectName("label_313")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.tab_4)
        self.tabWidget_2.setGeometry(QtCore.QRect(-10, 0, 1041, 811))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget_2.setFont(font)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget_4 = MplWidget(self.tab_2)
        self.widget_4.setGeometry(QtCore.QRect(420, 30, 241, 261))
        self.widget_4.setObjectName("widget_4")
        self.textEdit_6 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_6.setGeometry(QtCore.QRect(20, 250, 391, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_6.setFont(font)
        self.textEdit_6.setObjectName("textEdit_6")
        self.widget_5 = MplWidget(self.tab_2)
        self.widget_5.setGeometry(QtCore.QRect(420, 380, 241, 261))
        self.widget_5.setObjectName("widget_5")
        self.label_58 = QtWidgets.QLabel(self.tab_2)
        self.label_58.setGeometry(QtCore.QRect(20, 410, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_58.setFont(font)
        self.label_58.setObjectName("label_58")
        self.label_59 = QtWidgets.QLabel(self.tab_2)
        self.label_59.setGeometry(QtCore.QRect(30, 230, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_59.setFont(font)
        self.label_59.setObjectName("label_59")
        self.textEdit_8 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_8.setGeometry(QtCore.QRect(20, 430, 391, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_8.setFont(font)
        self.textEdit_8.setObjectName("textEdit_8")
        self.label_60 = QtWidgets.QLabel(self.tab_2)
        self.label_60.setGeometry(QtCore.QRect(20, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_60.setFont(font)
        self.label_60.setObjectName("label_60")
        self.label_72 = QtWidgets.QLabel(self.tab_2)
        self.label_72.setGeometry(QtCore.QRect(420, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.label_73 = QtWidgets.QLabel(self.tab_2)
        self.label_73.setGeometry(QtCore.QRect(420, 310, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.textEdit_9 = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_9.setGeometry(QtCore.QRect(20, 30, 391, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_9.setFont(font)
        self.textEdit_9.setObjectName("textEdit_9")
        self.widget_26 = MplWidget(self.tab_2)
        self.widget_26.setGeometry(QtCore.QRect(670, 30, 251, 261))
        self.widget_26.setObjectName("widget_26")
        self.widget_27 = MplWidget(self.tab_2)
        self.widget_27.setGeometry(QtCore.QRect(670, 380, 251, 261))
        self.widget_27.setObjectName("widget_27")
        self.label_314 = QtWidgets.QLabel(self.tab_2)
        self.label_314.setGeometry(QtCore.QRect(420, 20, 47, 13))
        self.label_314.setObjectName("label_314")
        self.label_315 = QtWidgets.QLabel(self.tab_2)
        self.label_315.setGeometry(QtCore.QRect(670, 20, 71, 16))
        self.label_315.setObjectName("label_315")
        self.label_316 = QtWidgets.QLabel(self.tab_2)
        self.label_316.setGeometry(QtCore.QRect(420, 360, 47, 13))
        self.label_316.setObjectName("label_316")
        self.label_317 = QtWidgets.QLabel(self.tab_2)
        self.label_317.setGeometry(QtCore.QRect(670, 360, 71, 16))
        self.label_317.setObjectName("label_317")
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_75 = QtWidgets.QWidget()
        self.tab_75.setObjectName("tab_75")
        self.label_613 = QtWidgets.QLabel(self.tab_75)
        self.label_613.setGeometry(QtCore.QRect(30, 230, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_613.setFont(font)
        self.label_613.setObjectName("label_613")
        self.label_614 = QtWidgets.QLabel(self.tab_75)
        self.label_614.setGeometry(QtCore.QRect(420, 10, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_614.setFont(font)
        self.label_614.setObjectName("label_614")
        self.textEdit_217 = QtWidgets.QTextEdit(self.tab_75)
        self.textEdit_217.setGeometry(QtCore.QRect(20, 250, 391, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_217.setFont(font)
        self.textEdit_217.setObjectName("textEdit_217")
        self.widget_144 = MplWidget(self.tab_75)
        self.widget_144.setGeometry(QtCore.QRect(420, 40, 251, 231))
        self.widget_144.setObjectName("widget_144")
        self.widget_145 = MplWidget(self.tab_75)
        self.widget_145.setGeometry(QtCore.QRect(420, 380, 251, 271))
        self.widget_145.setObjectName("widget_145")
        self.textEdit_218 = QtWidgets.QTextEdit(self.tab_75)
        self.textEdit_218.setGeometry(QtCore.QRect(20, 430, 391, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_218.setFont(font)
        self.textEdit_218.setObjectName("textEdit_218")
        self.label_615 = QtWidgets.QLabel(self.tab_75)
        self.label_615.setGeometry(QtCore.QRect(20, 10, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_615.setFont(font)
        self.label_615.setObjectName("label_615")
        self.textEdit_219 = QtWidgets.QTextEdit(self.tab_75)
        self.textEdit_219.setGeometry(QtCore.QRect(20, 40, 391, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_219.setFont(font)
        self.textEdit_219.setObjectName("textEdit_219")
        self.label_616 = QtWidgets.QLabel(self.tab_75)
        self.label_616.setGeometry(QtCore.QRect(420, 350, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_616.setFont(font)
        self.label_616.setObjectName("label_616")
        self.label_617 = QtWidgets.QLabel(self.tab_75)
        self.label_617.setGeometry(QtCore.QRect(20, 410, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_617.setFont(font)
        self.label_617.setObjectName("label_617")
        self.widget_150 = MplWidget(self.tab_75)
        self.widget_150.setGeometry(QtCore.QRect(680, 40, 241, 231))
        self.widget_150.setObjectName("widget_150")
        self.widget_151 = MplWidget(self.tab_75)
        self.widget_151.setGeometry(QtCore.QRect(680, 380, 241, 271))
        self.widget_151.setObjectName("widget_151")
        self.label_318 = QtWidgets.QLabel(self.tab_75)
        self.label_318.setGeometry(QtCore.QRect(420, 30, 47, 13))
        self.label_318.setObjectName("label_318")
        self.label_319 = QtWidgets.QLabel(self.tab_75)
        self.label_319.setGeometry(QtCore.QRect(680, 30, 71, 16))
        self.label_319.setObjectName("label_319")
        self.label_320 = QtWidgets.QLabel(self.tab_75)
        self.label_320.setGeometry(QtCore.QRect(420, 370, 47, 13))
        self.label_320.setObjectName("label_320")
        self.label_321 = QtWidgets.QLabel(self.tab_75)
        self.label_321.setGeometry(QtCore.QRect(680, 370, 71, 16))
        self.label_321.setObjectName("label_321")
        self.tabWidget_2.addTab(self.tab_75, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.textEdit_10 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_10.setGeometry(QtCore.QRect(20, 450, 391, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_10.setFont(font)
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_11.setGeometry(QtCore.QRect(20, 234, 391, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_11.setFont(font)
        self.textEdit_11.setObjectName("textEdit_11")
        self.widget_6 = MplWidget(self.tab_6)
        self.widget_6.setGeometry(QtCore.QRect(420, 400, 241, 231))
        self.widget_6.setObjectName("widget_6")
        self.label_74 = QtWidgets.QLabel(self.tab_6)
        self.label_74.setGeometry(QtCore.QRect(30, 214, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_74.setFont(font)
        self.label_74.setObjectName("label_74")
        self.label_75 = QtWidgets.QLabel(self.tab_6)
        self.label_75.setGeometry(QtCore.QRect(420, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_75.setFont(font)
        self.label_75.setObjectName("label_75")
        self.label_76 = QtWidgets.QLabel(self.tab_6)
        self.label_76.setGeometry(QtCore.QRect(20, 430, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_76.setFont(font)
        self.label_76.setObjectName("label_76")
        self.label_77 = QtWidgets.QLabel(self.tab_6)
        self.label_77.setGeometry(QtCore.QRect(20, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_77.setFont(font)
        self.label_77.setObjectName("label_77")
        self.widget_7 = MplWidget(self.tab_6)
        self.widget_7.setGeometry(QtCore.QRect(420, 30, 241, 241))
        self.widget_7.setObjectName("widget_7")
        self.label_78 = QtWidgets.QLabel(self.tab_6)
        self.label_78.setGeometry(QtCore.QRect(420, 350, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_78.setFont(font)
        self.label_78.setObjectName("label_78")
        self.textEdit_12 = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_12.setGeometry(QtCore.QRect(20, 30, 391, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_12.setFont(font)
        self.textEdit_12.setObjectName("textEdit_12")
        self.widget_28 = MplWidget(self.tab_6)
        self.widget_28.setGeometry(QtCore.QRect(670, 30, 251, 241))
        self.widget_28.setObjectName("widget_28")
        self.widget_29 = MplWidget(self.tab_6)
        self.widget_29.setGeometry(QtCore.QRect(670, 400, 251, 231))
        self.widget_29.setObjectName("widget_29")
        self.label_322 = QtWidgets.QLabel(self.tab_6)
        self.label_322.setGeometry(QtCore.QRect(420, 20, 47, 13))
        self.label_322.setObjectName("label_322")
        self.label_323 = QtWidgets.QLabel(self.tab_6)
        self.label_323.setGeometry(QtCore.QRect(670, 19, 71, 16))
        self.label_323.setObjectName("label_323")
        self.label_324 = QtWidgets.QLabel(self.tab_6)
        self.label_324.setGeometry(QtCore.QRect(420, 380, 47, 13))
        self.label_324.setObjectName("label_324")
        self.label_325 = QtWidgets.QLabel(self.tab_6)
        self.label_325.setGeometry(QtCore.QRect(670, 380, 71, 16))
        self.label_325.setObjectName("label_325")
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setObjectName("tab_7")
        self.textEdit_13 = QtWidgets.QTextEdit(self.tab_7)
        self.textEdit_13.setGeometry(QtCore.QRect(20, 420, 391, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_13.setFont(font)
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(self.tab_7)
        self.textEdit_14.setGeometry(QtCore.QRect(20, 230, 391, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_14.setFont(font)
        self.textEdit_14.setObjectName("textEdit_14")
        self.widget_8 = MplWidget(self.tab_7)
        self.widget_8.setGeometry(QtCore.QRect(420, 370, 241, 251))
        self.widget_8.setObjectName("widget_8")
        self.label_79 = QtWidgets.QLabel(self.tab_7)
        self.label_79.setGeometry(QtCore.QRect(30, 210, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_79.setFont(font)
        self.label_79.setObjectName("label_79")
        self.label_80 = QtWidgets.QLabel(self.tab_7)
        self.label_80.setGeometry(QtCore.QRect(420, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_80.setFont(font)
        self.label_80.setObjectName("label_80")
        self.label_83 = QtWidgets.QLabel(self.tab_7)
        self.label_83.setGeometry(QtCore.QRect(20, 400, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_83.setFont(font)
        self.label_83.setObjectName("label_83")
        self.label_84 = QtWidgets.QLabel(self.tab_7)
        self.label_84.setGeometry(QtCore.QRect(20, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_84.setFont(font)
        self.label_84.setObjectName("label_84")
        self.widget_9 = MplWidget(self.tab_7)
        self.widget_9.setGeometry(QtCore.QRect(420, 30, 241, 231))
        self.widget_9.setObjectName("widget_9")
        self.label_90 = QtWidgets.QLabel(self.tab_7)
        self.label_90.setGeometry(QtCore.QRect(420, 310, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_90.setFont(font)
        self.label_90.setObjectName("label_90")
        self.textEdit_15 = QtWidgets.QTextEdit(self.tab_7)
        self.textEdit_15.setGeometry(QtCore.QRect(20, 30, 391, 171))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_15.setFont(font)
        self.textEdit_15.setObjectName("textEdit_15")
        self.widget_30 = MplWidget(self.tab_7)
        self.widget_30.setGeometry(QtCore.QRect(670, 30, 251, 231))
        self.widget_30.setObjectName("widget_30")
        self.widget_31 = MplWidget(self.tab_7)
        self.widget_31.setGeometry(QtCore.QRect(670, 370, 251, 251))
        self.widget_31.setObjectName("widget_31")
        self.label_326 = QtWidgets.QLabel(self.tab_7)
        self.label_326.setGeometry(QtCore.QRect(420, 20, 47, 13))
        self.label_326.setObjectName("label_326")
        self.label_327 = QtWidgets.QLabel(self.tab_7)
        self.label_327.setGeometry(QtCore.QRect(670, 20, 71, 16))
        self.label_327.setObjectName("label_327")
        self.label_328 = QtWidgets.QLabel(self.tab_7)
        self.label_328.setGeometry(QtCore.QRect(420, 340, 47, 13))
        self.label_328.setObjectName("label_328")
        self.label_329 = QtWidgets.QLabel(self.tab_7)
        self.label_329.setGeometry(QtCore.QRect(730, 340, 71, 16))
        self.label_329.setObjectName("label_329")
        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.textEdit_16 = QtWidgets.QTextEdit(self.tab_8)
        self.textEdit_16.setGeometry(QtCore.QRect(10, 420, 391, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_16.setFont(font)
        self.textEdit_16.setObjectName("textEdit_16")
        self.textEdit_17 = QtWidgets.QTextEdit(self.tab_8)
        self.textEdit_17.setGeometry(QtCore.QRect(10, 210, 391, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_17.setFont(font)
        self.textEdit_17.setObjectName("textEdit_17")
        self.widget_10 = MplWidget(self.tab_8)
        self.widget_10.setGeometry(QtCore.QRect(410, 370, 251, 261))
        self.widget_10.setObjectName("widget_10")
        self.label_106 = QtWidgets.QLabel(self.tab_8)
        self.label_106.setGeometry(QtCore.QRect(20, 190, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_106.setFont(font)
        self.label_106.setObjectName("label_106")
        self.label_107 = QtWidgets.QLabel(self.tab_8)
        self.label_107.setGeometry(QtCore.QRect(410, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_107.setFont(font)
        self.label_107.setObjectName("label_107")
        self.label_108 = QtWidgets.QLabel(self.tab_8)
        self.label_108.setGeometry(QtCore.QRect(10, 400, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_108.setFont(font)
        self.label_108.setObjectName("label_108")
        self.label_109 = QtWidgets.QLabel(self.tab_8)
        self.label_109.setGeometry(QtCore.QRect(10, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_109.setFont(font)
        self.label_109.setObjectName("label_109")
        self.widget_11 = MplWidget(self.tab_8)
        self.widget_11.setGeometry(QtCore.QRect(410, 30, 251, 281))
        self.widget_11.setObjectName("widget_11")
        self.label_110 = QtWidgets.QLabel(self.tab_8)
        self.label_110.setGeometry(QtCore.QRect(410, 330, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_110.setFont(font)
        self.label_110.setObjectName("label_110")
        self.textEdit_18 = QtWidgets.QTextEdit(self.tab_8)
        self.textEdit_18.setGeometry(QtCore.QRect(10, 30, 391, 151))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_18.setFont(font)
        self.textEdit_18.setObjectName("textEdit_18")
        self.widget_32 = MplWidget(self.tab_8)
        self.widget_32.setGeometry(QtCore.QRect(670, 30, 251, 281))
        self.widget_32.setObjectName("widget_32")
        self.widget_33 = MplWidget(self.tab_8)
        self.widget_33.setGeometry(QtCore.QRect(670, 360, 251, 271))
        self.widget_33.setObjectName("widget_33")
        self.label_330 = QtWidgets.QLabel(self.tab_8)
        self.label_330.setGeometry(QtCore.QRect(410, 20, 47, 13))
        self.label_330.setObjectName("label_330")
        self.label_331 = QtWidgets.QLabel(self.tab_8)
        self.label_331.setGeometry(QtCore.QRect(670, 20, 71, 16))
        self.label_331.setObjectName("label_331")
        self.label_332 = QtWidgets.QLabel(self.tab_8)
        self.label_332.setGeometry(QtCore.QRect(410, 350, 47, 13))
        self.label_332.setObjectName("label_332")
        self.label_333 = QtWidgets.QLabel(self.tab_8)
        self.label_333.setGeometry(QtCore.QRect(670, 350, 71, 16))
        self.label_333.setObjectName("label_333")
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_9 = QtWidgets.QWidget()
        self.tab_9.setObjectName("tab_9")
        self.textEdit_19 = QtWidgets.QTextEdit(self.tab_9)
        self.textEdit_19.setGeometry(QtCore.QRect(10, 420, 391, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_19.setFont(font)
        self.textEdit_19.setObjectName("textEdit_19")
        self.textEdit_20 = QtWidgets.QTextEdit(self.tab_9)
        self.textEdit_20.setGeometry(QtCore.QRect(10, 230, 391, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_20.setFont(font)
        self.textEdit_20.setObjectName("textEdit_20")
        self.widget_12 = MplWidget(self.tab_9)
        self.widget_12.setGeometry(QtCore.QRect(410, 360, 241, 271))
        self.widget_12.setObjectName("widget_12")
        self.label_111 = QtWidgets.QLabel(self.tab_9)
        self.label_111.setGeometry(QtCore.QRect(20, 210, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_111.setFont(font)
        self.label_111.setObjectName("label_111")
        self.label_114 = QtWidgets.QLabel(self.tab_9)
        self.label_114.setGeometry(QtCore.QRect(410, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_114.setFont(font)
        self.label_114.setObjectName("label_114")
        self.label_232 = QtWidgets.QLabel(self.tab_9)
        self.label_232.setGeometry(QtCore.QRect(10, 400, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_232.setFont(font)
        self.label_232.setObjectName("label_232")
        self.label_233 = QtWidgets.QLabel(self.tab_9)
        self.label_233.setGeometry(QtCore.QRect(10, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_233.setFont(font)
        self.label_233.setObjectName("label_233")
        self.widget_13 = MplWidget(self.tab_9)
        self.widget_13.setGeometry(QtCore.QRect(410, 30, 241, 281))
        self.widget_13.setObjectName("widget_13")
        self.label_234 = QtWidgets.QLabel(self.tab_9)
        self.label_234.setGeometry(QtCore.QRect(410, 330, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_234.setFont(font)
        self.label_234.setObjectName("label_234")
        self.textEdit_21 = QtWidgets.QTextEdit(self.tab_9)
        self.textEdit_21.setGeometry(QtCore.QRect(10, 30, 391, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_21.setFont(font)
        self.textEdit_21.setObjectName("textEdit_21")
        self.widget_34 = MplWidget(self.tab_9)
        self.widget_34.setGeometry(QtCore.QRect(660, 30, 261, 281))
        self.widget_34.setObjectName("widget_34")
        self.widget_35 = MplWidget(self.tab_9)
        self.widget_35.setGeometry(QtCore.QRect(660, 360, 261, 271))
        self.widget_35.setObjectName("widget_35")
        self.label_334 = QtWidgets.QLabel(self.tab_9)
        self.label_334.setGeometry(QtCore.QRect(410, 17, 47, 13))
        self.label_334.setObjectName("label_334")
        self.label_335 = QtWidgets.QLabel(self.tab_9)
        self.label_335.setGeometry(QtCore.QRect(660, 17, 71, 16))
        self.label_335.setObjectName("label_335")
        self.label_336 = QtWidgets.QLabel(self.tab_9)
        self.label_336.setGeometry(QtCore.QRect(408, 340, 47, 13))
        self.label_336.setObjectName("label_336")
        self.label_337 = QtWidgets.QLabel(self.tab_9)
        self.label_337.setGeometry(QtCore.QRect(718, 340, 71, 16))
        self.label_337.setObjectName("label_337")
        self.tabWidget_2.addTab(self.tab_9, "")
        self.tab_11 = QtWidgets.QWidget()
        self.tab_11.setObjectName("tab_11")
        self.textEdit_22 = QtWidgets.QTextEdit(self.tab_11)
        self.textEdit_22.setGeometry(QtCore.QRect(10, 430, 391, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_22.setFont(font)
        self.textEdit_22.setObjectName("textEdit_22")
        self.textEdit_23 = QtWidgets.QTextEdit(self.tab_11)
        self.textEdit_23.setGeometry(QtCore.QRect(10, 240, 391, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_23.setFont(font)
        self.textEdit_23.setObjectName("textEdit_23")
        self.widget_14 = MplWidget(self.tab_11)
        self.widget_14.setGeometry(QtCore.QRect(410, 360, 251, 261))
        self.widget_14.setObjectName("widget_14")
        self.label_235 = QtWidgets.QLabel(self.tab_11)
        self.label_235.setGeometry(QtCore.QRect(20, 220, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_235.setFont(font)
        self.label_235.setObjectName("label_235")
        self.label_236 = QtWidgets.QLabel(self.tab_11)
        self.label_236.setGeometry(QtCore.QRect(410, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_236.setFont(font)
        self.label_236.setObjectName("label_236")
        self.label_239 = QtWidgets.QLabel(self.tab_11)
        self.label_239.setGeometry(QtCore.QRect(10, 410, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_239.setFont(font)
        self.label_239.setObjectName("label_239")
        self.label_240 = QtWidgets.QLabel(self.tab_11)
        self.label_240.setGeometry(QtCore.QRect(10, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_240.setFont(font)
        self.label_240.setObjectName("label_240")
        self.widget_15 = MplWidget(self.tab_11)
        self.widget_15.setGeometry(QtCore.QRect(410, 30, 251, 281))
        self.widget_15.setObjectName("widget_15")
        self.label_248 = QtWidgets.QLabel(self.tab_11)
        self.label_248.setGeometry(QtCore.QRect(410, 320, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_248.setFont(font)
        self.label_248.setObjectName("label_248")
        self.textEdit_24 = QtWidgets.QTextEdit(self.tab_11)
        self.textEdit_24.setGeometry(QtCore.QRect(10, 30, 391, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_24.setFont(font)
        self.textEdit_24.setObjectName("textEdit_24")
        self.widget_36 = MplWidget(self.tab_11)
        self.widget_36.setGeometry(QtCore.QRect(670, 30, 251, 281))
        self.widget_36.setObjectName("widget_36")
        self.widget_37 = MplWidget(self.tab_11)
        self.widget_37.setGeometry(QtCore.QRect(670, 360, 251, 261))
        self.widget_37.setObjectName("widget_37")
        self.label_338 = QtWidgets.QLabel(self.tab_11)
        self.label_338.setGeometry(QtCore.QRect(410, 18, 47, 13))
        self.label_338.setObjectName("label_338")
        self.label_339 = QtWidgets.QLabel(self.tab_11)
        self.label_339.setGeometry(QtCore.QRect(670, 18, 71, 16))
        self.label_339.setObjectName("label_339")
        self.label_340 = QtWidgets.QLabel(self.tab_11)
        self.label_340.setGeometry(QtCore.QRect(410, 340, 47, 13))
        self.label_340.setObjectName("label_340")
        self.label_341 = QtWidgets.QLabel(self.tab_11)
        self.label_341.setGeometry(QtCore.QRect(680, 340, 71, 16))
        self.label_341.setObjectName("label_341")
        self.tabWidget_2.addTab(self.tab_11, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.textEdit_25 = QtWidgets.QTextEdit(self.tab_12)
        self.textEdit_25.setGeometry(QtCore.QRect(10, 420, 391, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_25.setFont(font)
        self.textEdit_25.setObjectName("textEdit_25")
        self.textEdit_26 = QtWidgets.QTextEdit(self.tab_12)
        self.textEdit_26.setGeometry(QtCore.QRect(10, 250, 391, 141))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_26.setFont(font)
        self.textEdit_26.setObjectName("textEdit_26")
        self.widget_16 = MplWidget(self.tab_12)
        self.widget_16.setGeometry(QtCore.QRect(410, 370, 251, 251))
        self.widget_16.setObjectName("widget_16")
        self.label_249 = QtWidgets.QLabel(self.tab_12)
        self.label_249.setGeometry(QtCore.QRect(20, 230, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_249.setFont(font)
        self.label_249.setObjectName("label_249")
        self.label_250 = QtWidgets.QLabel(self.tab_12)
        self.label_250.setGeometry(QtCore.QRect(410, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_250.setFont(font)
        self.label_250.setObjectName("label_250")
        self.label_251 = QtWidgets.QLabel(self.tab_12)
        self.label_251.setGeometry(QtCore.QRect(10, 400, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_251.setFont(font)
        self.label_251.setObjectName("label_251")
        self.label_252 = QtWidgets.QLabel(self.tab_12)
        self.label_252.setGeometry(QtCore.QRect(10, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_252.setFont(font)
        self.label_252.setObjectName("label_252")
        self.widget_17 = MplWidget(self.tab_12)
        self.widget_17.setGeometry(QtCore.QRect(410, 30, 251, 281))
        self.widget_17.setObjectName("widget_17")
        self.label_253 = QtWidgets.QLabel(self.tab_12)
        self.label_253.setGeometry(QtCore.QRect(410, 330, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_253.setFont(font)
        self.label_253.setObjectName("label_253")
        self.textEdit_27 = QtWidgets.QTextEdit(self.tab_12)
        self.textEdit_27.setGeometry(QtCore.QRect(10, 30, 391, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_27.setFont(font)
        self.textEdit_27.setObjectName("textEdit_27")
        self.widget_38 = MplWidget(self.tab_12)
        self.widget_38.setGeometry(QtCore.QRect(670, 30, 251, 281))
        self.widget_38.setObjectName("widget_38")
        self.widget_39 = MplWidget(self.tab_12)
        self.widget_39.setGeometry(QtCore.QRect(670, 370, 251, 251))
        self.widget_39.setObjectName("widget_39")
        self.label_342 = QtWidgets.QLabel(self.tab_12)
        self.label_342.setGeometry(QtCore.QRect(410, 20, 47, 13))
        self.label_342.setObjectName("label_342")
        self.label_343 = QtWidgets.QLabel(self.tab_12)
        self.label_343.setGeometry(QtCore.QRect(670, 20, 71, 16))
        self.label_343.setObjectName("label_343")
        self.label_344 = QtWidgets.QLabel(self.tab_12)
        self.label_344.setGeometry(QtCore.QRect(410, 350, 47, 13))
        self.label_344.setObjectName("label_344")
        self.label_345 = QtWidgets.QLabel(self.tab_12)
        self.label_345.setGeometry(QtCore.QRect(710, 340, 71, 16))
        self.label_345.setObjectName("label_345")
        self.tabWidget_2.addTab(self.tab_12, "")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.textEdit_28 = QtWidgets.QTextEdit(self.tab_10)
        self.textEdit_28.setGeometry(QtCore.QRect(10, 430, 391, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_28.setFont(font)
        self.textEdit_28.setObjectName("textEdit_28")
        self.textEdit_29 = QtWidgets.QTextEdit(self.tab_10)
        self.textEdit_29.setGeometry(QtCore.QRect(10, 230, 391, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_29.setFont(font)
        self.textEdit_29.setObjectName("textEdit_29")
        self.widget_18 = MplWidget(self.tab_10)
        self.widget_18.setGeometry(QtCore.QRect(410, 350, 241, 271))
        self.widget_18.setObjectName("widget_18")
        self.label_254 = QtWidgets.QLabel(self.tab_10)
        self.label_254.setGeometry(QtCore.QRect(20, 210, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_254.setFont(font)
        self.label_254.setObjectName("label_254")
        self.label_255 = QtWidgets.QLabel(self.tab_10)
        self.label_255.setGeometry(QtCore.QRect(410, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_255.setFont(font)
        self.label_255.setObjectName("label_255")
        self.label_256 = QtWidgets.QLabel(self.tab_10)
        self.label_256.setGeometry(QtCore.QRect(10, 412, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_256.setFont(font)
        self.label_256.setObjectName("label_256")
        self.label_257 = QtWidgets.QLabel(self.tab_10)
        self.label_257.setGeometry(QtCore.QRect(10, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_257.setFont(font)
        self.label_257.setObjectName("label_257")
        self.widget_19 = MplWidget(self.tab_10)
        self.widget_19.setGeometry(QtCore.QRect(410, 30, 241, 281))
        self.widget_19.setObjectName("widget_19")
        self.label_258 = QtWidgets.QLabel(self.tab_10)
        self.label_258.setGeometry(QtCore.QRect(410, 320, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_258.setFont(font)
        self.label_258.setObjectName("label_258")
        self.textEdit_30 = QtWidgets.QTextEdit(self.tab_10)
        self.textEdit_30.setGeometry(QtCore.QRect(10, 30, 391, 171))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_30.setFont(font)
        self.textEdit_30.setObjectName("textEdit_30")
        self.widget_40 = MplWidget(self.tab_10)
        self.widget_40.setGeometry(QtCore.QRect(660, 30, 261, 281))
        self.widget_40.setObjectName("widget_40")
        self.widget_41 = MplWidget(self.tab_10)
        self.widget_41.setGeometry(QtCore.QRect(660, 350, 261, 271))
        self.widget_41.setObjectName("widget_41")
        self.label_346 = QtWidgets.QLabel(self.tab_10)
        self.label_346.setGeometry(QtCore.QRect(410, 20, 47, 13))
        self.label_346.setObjectName("label_346")
        self.label_347 = QtWidgets.QLabel(self.tab_10)
        self.label_347.setGeometry(QtCore.QRect(660, 20, 71, 16))
        self.label_347.setObjectName("label_347")
        self.label_348 = QtWidgets.QLabel(self.tab_10)
        self.label_348.setGeometry(QtCore.QRect(410, 340, 47, 13))
        self.label_348.setObjectName("label_348")
        self.label_349 = QtWidgets.QLabel(self.tab_10)
        self.label_349.setGeometry(QtCore.QRect(660, 340, 71, 16))
        self.label_349.setObjectName("label_349")
        self.tabWidget_2.addTab(self.tab_10, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.textEdit_31 = QtWidgets.QTextEdit(self.tab_13)
        self.textEdit_31.setGeometry(QtCore.QRect(10, 420, 391, 211))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_31.setFont(font)
        self.textEdit_31.setObjectName("textEdit_31")
        self.textEdit_32 = QtWidgets.QTextEdit(self.tab_13)
        self.textEdit_32.setGeometry(QtCore.QRect(10, 230, 391, 161))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_32.setFont(font)
        self.textEdit_32.setObjectName("textEdit_32")
        self.widget_20 = MplWidget(self.tab_13)
        self.widget_20.setGeometry(QtCore.QRect(410, 360, 241, 271))
        self.widget_20.setObjectName("widget_20")
        self.label_259 = QtWidgets.QLabel(self.tab_13)
        self.label_259.setGeometry(QtCore.QRect(20, 210, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_259.setFont(font)
        self.label_259.setObjectName("label_259")
        self.label_260 = QtWidgets.QLabel(self.tab_13)
        self.label_260.setGeometry(QtCore.QRect(410, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_260.setFont(font)
        self.label_260.setObjectName("label_260")
        self.label_261 = QtWidgets.QLabel(self.tab_13)
        self.label_261.setGeometry(QtCore.QRect(10, 400, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_261.setFont(font)
        self.label_261.setObjectName("label_261")
        self.label_262 = QtWidgets.QLabel(self.tab_13)
        self.label_262.setGeometry(QtCore.QRect(10, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_262.setFont(font)
        self.label_262.setObjectName("label_262")
        self.widget_21 = MplWidget(self.tab_13)
        self.widget_21.setGeometry(QtCore.QRect(410, 30, 241, 281))
        self.widget_21.setObjectName("widget_21")
        self.label_263 = QtWidgets.QLabel(self.tab_13)
        self.label_263.setGeometry(QtCore.QRect(410, 320, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_263.setFont(font)
        self.label_263.setObjectName("label_263")
        self.textEdit_33 = QtWidgets.QTextEdit(self.tab_13)
        self.textEdit_33.setGeometry(QtCore.QRect(10, 30, 391, 171))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_33.setFont(font)
        self.textEdit_33.setObjectName("textEdit_33")
        self.widget_42 = MplWidget(self.tab_13)
        self.widget_42.setGeometry(QtCore.QRect(660, 30, 261, 281))
        self.widget_42.setObjectName("widget_42")
        self.widget_43 = MplWidget(self.tab_13)
        self.widget_43.setGeometry(QtCore.QRect(660, 360, 261, 271))
        self.widget_43.setObjectName("widget_43")
        self.label_350 = QtWidgets.QLabel(self.tab_13)
        self.label_350.setGeometry(QtCore.QRect(410, 20, 47, 13))
        self.label_350.setObjectName("label_350")
        self.label_351 = QtWidgets.QLabel(self.tab_13)
        self.label_351.setGeometry(QtCore.QRect(660, 20, 71, 16))
        self.label_351.setObjectName("label_351")
        self.label_352 = QtWidgets.QLabel(self.tab_13)
        self.label_352.setGeometry(QtCore.QRect(410, 340, 47, 13))
        self.label_352.setObjectName("label_352")
        self.label_353 = QtWidgets.QLabel(self.tab_13)
        self.label_353.setGeometry(QtCore.QRect(660, 340, 71, 16))
        self.label_353.setObjectName("label_353")
        self.tabWidget_2.addTab(self.tab_13, "")
        self.tab_76 = QtWidgets.QWidget()
        self.tab_76.setObjectName("tab_76")
        self.label_618 = QtWidgets.QLabel(self.tab_76)
        self.label_618.setGeometry(QtCore.QRect(30, 210, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_618.setFont(font)
        self.label_618.setObjectName("label_618")
        self.label_619 = QtWidgets.QLabel(self.tab_76)
        self.label_619.setGeometry(QtCore.QRect(420, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_619.setFont(font)
        self.label_619.setObjectName("label_619")
        self.textEdit_220 = QtWidgets.QTextEdit(self.tab_76)
        self.textEdit_220.setGeometry(QtCore.QRect(20, 230, 391, 171))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_220.setFont(font)
        self.textEdit_220.setObjectName("textEdit_220")
        self.widget_146 = MplWidget(self.tab_76)
        self.widget_146.setGeometry(QtCore.QRect(420, 30, 251, 281))
        self.widget_146.setObjectName("widget_146")
        self.widget_147 = MplWidget(self.tab_76)
        self.widget_147.setGeometry(QtCore.QRect(420, 370, 251, 261))
        self.widget_147.setObjectName("widget_147")
        self.textEdit_221 = QtWidgets.QTextEdit(self.tab_76)
        self.textEdit_221.setGeometry(QtCore.QRect(20, 430, 391, 201))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_221.setFont(font)
        self.textEdit_221.setObjectName("textEdit_221")
        self.label_620 = QtWidgets.QLabel(self.tab_76)
        self.label_620.setGeometry(QtCore.QRect(20, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_620.setFont(font)
        self.label_620.setObjectName("label_620")
        self.textEdit_222 = QtWidgets.QTextEdit(self.tab_76)
        self.textEdit_222.setGeometry(QtCore.QRect(20, 30, 391, 171))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_222.setFont(font)
        self.textEdit_222.setObjectName("textEdit_222")
        self.label_621 = QtWidgets.QLabel(self.tab_76)
        self.label_621.setGeometry(QtCore.QRect(420, 330, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_621.setFont(font)
        self.label_621.setObjectName("label_621")
        self.label_622 = QtWidgets.QLabel(self.tab_76)
        self.label_622.setGeometry(QtCore.QRect(20, 410, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_622.setFont(font)
        self.label_622.setObjectName("label_622")
        self.widget_44 = MplWidget(self.tab_76)
        self.widget_44.setGeometry(QtCore.QRect(680, 30, 241, 281))
        self.widget_44.setObjectName("widget_44")
        self.widget_45 = MplWidget(self.tab_76)
        self.widget_45.setGeometry(QtCore.QRect(680, 370, 241, 261))
        self.widget_45.setObjectName("widget_45")
        self.label_354 = QtWidgets.QLabel(self.tab_76)
        self.label_354.setGeometry(QtCore.QRect(420, 20, 47, 13))
        self.label_354.setObjectName("label_354")
        self.label_355 = QtWidgets.QLabel(self.tab_76)
        self.label_355.setGeometry(QtCore.QRect(680, 20, 71, 16))
        self.label_355.setObjectName("label_355")
        self.label_356 = QtWidgets.QLabel(self.tab_76)
        self.label_356.setGeometry(QtCore.QRect(420, 360, 47, 13))
        self.label_356.setObjectName("label_356")
        self.label_357 = QtWidgets.QLabel(self.tab_76)
        self.label_357.setGeometry(QtCore.QRect(680, 360, 71, 16))
        self.label_357.setObjectName("label_357")
        self.tabWidget_2.addTab(self.tab_76, "")
        self.tab_77 = QtWidgets.QWidget()
        self.tab_77.setObjectName("tab_77")
        self.label_623 = QtWidgets.QLabel(self.tab_77)
        self.label_623.setGeometry(QtCore.QRect(30, 213, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_623.setFont(font)
        self.label_623.setObjectName("label_623")
        self.label_624 = QtWidgets.QLabel(self.tab_77)
        self.label_624.setGeometry(QtCore.QRect(420, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_624.setFont(font)
        self.label_624.setObjectName("label_624")
        self.textEdit_223 = QtWidgets.QTextEdit(self.tab_77)
        self.textEdit_223.setGeometry(QtCore.QRect(20, 233, 391, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_223.setFont(font)
        self.textEdit_223.setObjectName("textEdit_223")
        self.widget_148 = MplWidget(self.tab_77)
        self.widget_148.setGeometry(QtCore.QRect(420, 30, 241, 281))
        self.widget_148.setObjectName("widget_148")
        self.widget_149 = MplWidget(self.tab_77)
        self.widget_149.setGeometry(QtCore.QRect(420, 350, 241, 281))
        self.widget_149.setObjectName("widget_149")
        self.textEdit_224 = QtWidgets.QTextEdit(self.tab_77)
        self.textEdit_224.setGeometry(QtCore.QRect(20, 440, 391, 191))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_224.setFont(font)
        self.textEdit_224.setObjectName("textEdit_224")
        self.label_625 = QtWidgets.QLabel(self.tab_77)
        self.label_625.setGeometry(QtCore.QRect(20, 0, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_625.setFont(font)
        self.label_625.setObjectName("label_625")
        self.textEdit_225 = QtWidgets.QTextEdit(self.tab_77)
        self.textEdit_225.setGeometry(QtCore.QRect(20, 30, 391, 181))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textEdit_225.setFont(font)
        self.textEdit_225.setObjectName("textEdit_225")
        self.label_626 = QtWidgets.QLabel(self.tab_77)
        self.label_626.setGeometry(QtCore.QRect(420, 320, 251, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_626.setFont(font)
        self.label_626.setObjectName("label_626")
        self.label_627 = QtWidgets.QLabel(self.tab_77)
        self.label_627.setGeometry(QtCore.QRect(20, 420, 171, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_627.setFont(font)
        self.label_627.setObjectName("label_627")
        self.widget_46 = MplWidget(self.tab_77)
        self.widget_46.setGeometry(QtCore.QRect(670, 30, 251, 281))
        self.widget_46.setObjectName("widget_46")
        self.widget_47 = MplWidget(self.tab_77)
        self.widget_47.setGeometry(QtCore.QRect(670, 350, 251, 281))
        self.widget_47.setObjectName("widget_47")
        self.label_358 = QtWidgets.QLabel(self.tab_77)
        self.label_358.setGeometry(QtCore.QRect(420, 15, 47, 13))
        self.label_358.setObjectName("label_358")
        self.label_359 = QtWidgets.QLabel(self.tab_77)
        self.label_359.setGeometry(QtCore.QRect(670, 15, 71, 16))
        self.label_359.setObjectName("label_359")
        self.label_360 = QtWidgets.QLabel(self.tab_77)
        self.label_360.setGeometry(QtCore.QRect(420, 340, 47, 13))
        self.label_360.setObjectName("label_360")
        self.label_361 = QtWidgets.QLabel(self.tab_77)
        self.label_361.setGeometry(QtCore.QRect(670, 340, 71, 16))
        self.label_361.setObjectName("label_361")
        self.tabWidget_2.addTab(self.tab_77, "")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.label_264 = QtWidgets.QLabel(self.tab_5)
        self.label_264.setGeometry(QtCore.QRect(440, 10, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_264.setFont(font)
        self.label_264.setObjectName("label_264")
        self.lineEdit_17 = QtWidgets.QLineEdit(self.tab_5)
        self.lineEdit_17.setGeometry(QtCore.QRect(200, 40, 621, 31))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.pushButton_124 = QtWidgets.QPushButton(self.tab_5)
        self.pushButton_124.setGeometry(QtCore.QRect(480, 80, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_124.setFont(font)
        self.pushButton_124.setObjectName("pushButton_124")
        self.textEdit_35 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_35.setGeometry(QtCore.QRect(10, 150, 441, 151))
        self.textEdit_35.setObjectName("textEdit_35")
        self.textEdit_36 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_36.setGeometry(QtCore.QRect(10, 323, 441, 151))
        self.textEdit_36.setObjectName("textEdit_36")
        self.textEdit_37 = QtWidgets.QTextEdit(self.tab_5)
        self.textEdit_37.setGeometry(QtCore.QRect(10, 500, 441, 151))
        self.textEdit_37.setObjectName("textEdit_37")
        self.widget_22 = MplWidget(self.tab_5)
        self.widget_22.setGeometry(QtCore.QRect(460, 150, 231, 241))
        self.widget_22.setObjectName("widget_22")
        self.widget_23 = MplWidget(self.tab_5)
        self.widget_23.setGeometry(QtCore.QRect(700, 150, 211, 241))
        self.widget_23.setObjectName("widget_23")
        self.widget_24 = MplWidget(self.tab_5)
        self.widget_24.setGeometry(QtCore.QRect(460, 428, 231, 221))
        self.widget_24.setObjectName("widget_24")
        self.widget_25 = MplWidget(self.tab_5)
        self.widget_25.setGeometry(QtCore.QRect(700, 428, 211, 221))
        self.widget_25.setObjectName("widget_25")
        self.label_266 = QtWidgets.QLabel(self.tab_5)
        self.label_266.setGeometry(QtCore.QRect(10, 130, 71, 16))
        self.label_266.setObjectName("label_266")
        self.label_291 = QtWidgets.QLabel(self.tab_5)
        self.label_291.setGeometry(QtCore.QRect(10, 303, 71, 16))
        self.label_291.setObjectName("label_291")
        self.label_301 = QtWidgets.QLabel(self.tab_5)
        self.label_301.setGeometry(QtCore.QRect(10, 480, 151, 16))
        self.label_301.setObjectName("label_301")
        self.label_309 = QtWidgets.QLabel(self.tab_5)
        self.label_309.setGeometry(QtCore.QRect(460, 130, 121, 16))
        self.label_309.setObjectName("label_309")
        self.label_310 = QtWidgets.QLabel(self.tab_5)
        self.label_310.setGeometry(QtCore.QRect(470, 398, 191, 30))
        self.label_310.setObjectName("label_310")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_81 = QtWidgets.QLabel(self.tab)
        self.label_81.setGeometry(QtCore.QRect(410, 3, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_81.setFont(font)
        self.label_81.setObjectName("label_81")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_19.setGeometry(QtCore.QRect(220, 40, 511, 31))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_82 = QtWidgets.QLabel(self.tab)
        self.label_82.setGeometry(QtCore.QRect(220, 20, 131, 16))
        self.label_82.setObjectName("label_82")
        self.pushButton_51 = QtWidgets.QPushButton(self.tab)
        self.pushButton_51.setGeometry(QtCore.QRect(220, 80, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_51.setFont(font)
        self.pushButton_51.setMouseTracking(True)
        self.pushButton_51.setTabletTracking(True)
        self.pushButton_51.setObjectName("pushButton_51")
        self.pushButton_91 = QtWidgets.QPushButton(self.tab)
        self.pushButton_91.setGeometry(QtCore.QRect(220, 110, 101, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_91.setFont(font)
        self.pushButton_91.setMouseTracking(True)
        self.pushButton_91.setTabletTracking(True)
        self.pushButton_91.setObjectName("pushButton_91")
        self.pushButton_107 = QtWidgets.QPushButton(self.tab)
        self.pushButton_107.setGeometry(QtCore.QRect(350, 80, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_107.setFont(font)
        self.pushButton_107.setMouseTracking(True)
        self.pushButton_107.setTabletTracking(True)
        self.pushButton_107.setObjectName("pushButton_107")
        self.pushButton_109 = QtWidgets.QPushButton(self.tab)
        self.pushButton_109.setGeometry(QtCore.QRect(350, 110, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_109.setFont(font)
        self.pushButton_109.setMouseTracking(True)
        self.pushButton_109.setTabletTracking(True)
        self.pushButton_109.setObjectName("pushButton_109")
        self.pushButton_111 = QtWidgets.QPushButton(self.tab)
        self.pushButton_111.setGeometry(QtCore.QRect(490, 80, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_111.setFont(font)
        self.pushButton_111.setMouseTracking(True)
        self.pushButton_111.setTabletTracking(True)
        self.pushButton_111.setObjectName("pushButton_111")
        self.pushButton_114 = QtWidgets.QPushButton(self.tab)
        self.pushButton_114.setGeometry(QtCore.QRect(490, 110, 111, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_114.setFont(font)
        self.pushButton_114.setMouseTracking(True)
        self.pushButton_114.setTabletTracking(True)
        self.pushButton_114.setObjectName("pushButton_114")
        self.pushButton_123 = QtWidgets.QPushButton(self.tab)
        self.pushButton_123.setGeometry(QtCore.QRect(630, 80, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_123.setFont(font)
        self.pushButton_123.setMouseTracking(True)
        self.pushButton_123.setTabletTracking(True)
        self.pushButton_123.setObjectName("pushButton_123")
        self.textEdit_34 = QtWidgets.QTextEdit(self.tab)
        self.textEdit_34.setGeometry(QtCore.QRect(20, 140, 871, 521))
        self.textEdit_34.setObjectName("textEdit_34")
        self.tabWidget.addTab(self.tab, "")
        self.stackedWidget.addWidget(self.page_32)
        self.page_65 = QtWidgets.QWidget()
        self.page_65.setObjectName("page_65")
        self.label_46 = QtWidgets.QLabel(self.page_65)
        self.label_46.setGeometry(QtCore.QRect(490, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setObjectName("label_46")
        self.lineEdit_59 = QtWidgets.QLineEdit(self.page_65)
        self.lineEdit_59.setGeometry(QtCore.QRect(510, 60, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_59.setFont(font)
        self.lineEdit_59.setReadOnly(False)
        self.lineEdit_59.setObjectName("lineEdit_59")
        self.label_53 = QtWidgets.QLabel(self.page_65)
        self.label_53.setGeometry(QtCore.QRect(330, 60, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_53.setFont(font)
        self.label_53.setObjectName("label_53")
        self.label_508 = QtWidgets.QLabel(self.page_65)
        self.label_508.setGeometry(QtCore.QRect(330, 110, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_508.setFont(font)
        self.label_508.setObjectName("label_508")
        self.label_509 = QtWidgets.QLabel(self.page_65)
        self.label_509.setGeometry(QtCore.QRect(330, 260, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_509.setFont(font)
        self.label_509.setObjectName("label_509")
        self.label_510 = QtWidgets.QLabel(self.page_65)
        self.label_510.setGeometry(QtCore.QRect(330, 310, 161, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_510.setFont(font)
        self.label_510.setObjectName("label_510")
        self.dateEdit_3 = QtWidgets.QDateEdit(self.page_65)
        self.dateEdit_3.setGeometry(QtCore.QRect(510, 260, 211, 22))
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.dateEdit_4 = QtWidgets.QDateEdit(self.page_65)
        self.dateEdit_4.setGeometry(QtCore.QRect(510, 310, 211, 22))
        self.dateEdit_4.setObjectName("dateEdit_4")
        self.textEdit_7 = QtWidgets.QTextEdit(self.page_65)
        self.textEdit_7.setGeometry(QtCore.QRect(510, 110, 211, 131))
        self.textEdit_7.setObjectName("textEdit_7")
        self.pushButton_52 = QtWidgets.QPushButton(self.page_65)
        self.pushButton_52.setGeometry(QtCore.QRect(330, 400, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_52.setFont(font)
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_108 = QtWidgets.QPushButton(self.page_65)
        self.pushButton_108.setGeometry(QtCore.QRect(600, 400, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_108.setFont(font)
        self.pushButton_108.setObjectName("pushButton_108")
        self.frame_108 = QtWidgets.QFrame(self.page_65)
        self.frame_108.setGeometry(QtCore.QRect(290, 10, 501, 501))
        self.frame_108.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_108.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_108.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_108.setObjectName("frame_108")
        self.frame_108.raise_()
        self.label_46.raise_()
        self.lineEdit_59.raise_()
        self.label_53.raise_()
        self.label_508.raise_()
        self.label_509.raise_()
        self.label_510.raise_()
        self.dateEdit_3.raise_()
        self.dateEdit_4.raise_()
        self.textEdit_7.raise_()
        self.pushButton_52.raise_()
        self.pushButton_108.raise_()
        self.stackedWidget.addWidget(self.page_65)
        self.page_31 = QtWidgets.QWidget()
        self.page_31.setObjectName("page_31")
        self.frame_42 = QtWidgets.QFrame(self.page_31)
        self.frame_42.setGeometry(QtCore.QRect(280, 50, 431, 241))
        self.frame_42.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_42.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_42.setObjectName("frame_42")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.frame_42)
        self.lineEdit_16.setGeometry(QtCore.QRect(180, 30, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_16.setFont(font)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.frame_42)
        self.lineEdit_18.setGeometry(QtCore.QRect(180, 70, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_18.setFont(font)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_20 = QtWidgets.QLineEdit(self.frame_42)
        self.lineEdit_20.setGeometry(QtCore.QRect(180, 110, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_20.setFont(font)
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame_42)
        self.lineEdit_21.setGeometry(QtCore.QRect(180, 150, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_21.setFont(font)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_364 = QtWidgets.QLabel(self.frame_42)
        self.label_364.setGeometry(QtCore.QRect(70, 30, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_364.setFont(font)
        self.label_364.setObjectName("label_364")
        self.label_365 = QtWidgets.QLabel(self.frame_42)
        self.label_365.setGeometry(QtCore.QRect(70, 70, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_365.setFont(font)
        self.label_365.setObjectName("label_365")
        self.label_366 = QtWidgets.QLabel(self.frame_42)
        self.label_366.setGeometry(QtCore.QRect(70, 110, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_366.setFont(font)
        self.label_366.setObjectName("label_366")
        self.label_367 = QtWidgets.QLabel(self.frame_42)
        self.label_367.setGeometry(QtCore.QRect(70, 150, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_367.setFont(font)
        self.label_367.setObjectName("label_367")
        self.frame_43 = QtWidgets.QFrame(self.page_31)
        self.frame_43.setGeometry(QtCore.QRect(280, 320, 431, 121))
        self.frame_43.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_43.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_43.setObjectName("frame_43")
        self.label_368 = QtWidgets.QLabel(self.frame_43)
        self.label_368.setGeometry(QtCore.QRect(70, 70, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_368.setFont(font)
        self.label_368.setObjectName("label_368")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame_43)
        self.lineEdit_22.setGeometry(QtCore.QRect(180, 70, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_22.setFont(font)
        self.lineEdit_22.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.frame_43)
        self.lineEdit_23.setGeometry(QtCore.QRect(180, 30, 201, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_23.setFont(font)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_369 = QtWidgets.QLabel(self.frame_43)
        self.label_369.setGeometry(QtCore.QRect(70, 30, 101, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_369.setFont(font)
        self.label_369.setObjectName("label_369")
        self.label_362 = QtWidgets.QLabel(self.page_31)
        self.label_362.setGeometry(QtCore.QRect(440, 10, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_362.setFont(font)
        self.label_362.setObjectName("label_362")
        self.label_363 = QtWidgets.QLabel(self.page_31)
        self.label_363.setGeometry(QtCore.QRect(280, 300, 151, 16))
        self.label_363.setObjectName("label_363")
        self.pushButton_70 = QtWidgets.QPushButton(self.page_31)
        self.pushButton_70.setGeometry(QtCore.QRect(320, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_70.setFont(font)
        self.pushButton_70.setObjectName("pushButton_70")
        self.pushButton_72 = QtWidgets.QPushButton(self.page_31)
        self.pushButton_72.setGeometry(QtCore.QRect(560, 460, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_72.setFont(font)
        self.pushButton_72.setObjectName("pushButton_72")
        self.stackedWidget.addWidget(self.page_31)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1056, 21))
        self.menubar.setObjectName("menubar")
        self.menuImport_Data = QtWidgets.QMenu(self.menubar)
        self.menuImport_Data.setObjectName("menuImport_Data")
        self.menuExport_data = QtWidgets.QMenu(self.menubar)
        self.menuExport_data.setObjectName("menuExport_data")
        self.menuUpdate = QtWidgets.QMenu(self.menubar)
        self.menuUpdate.setObjectName("menuUpdate")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport_Data = QtWidgets.QAction(MainWindow)
        self.actionImport_Data.setObjectName("actionImport_Data")
        self.actionExport_Data = QtWidgets.QAction(MainWindow)
        self.actionExport_Data.setObjectName("actionExport_Data")
        self.actionPrint = QtWidgets.QAction(MainWindow)
        self.actionPrint.setObjectName("actionPrint")
        self.actionTutorial = QtWidgets.QAction(MainWindow)
        self.actionTutorial.setObjectName("actionTutorial")
        self.actionImport_School = QtWidgets.QAction(MainWindow)
        self.actionImport_School.setObjectName("actionImport_School")
        self.actionImport_Teacher = QtWidgets.QAction(MainWindow)
        self.actionImport_Teacher.setObjectName("actionImport_Teacher")
        self.actionImport_School_Enrollment = QtWidgets.QAction(MainWindow)
        self.actionImport_School_Enrollment.setObjectName("actionImport_School_Enrollment")
        self.actionImport_school_Facilities = QtWidgets.QAction(MainWindow)
        self.actionImport_school_Facilities.setObjectName("actionImport_school_Facilities")
        self.actionImport_school_Classroom = QtWidgets.QAction(MainWindow)
        self.actionImport_school_Classroom.setObjectName("actionImport_school_Classroom")
        self.actionImport_All = QtWidgets.QAction(MainWindow)
        self.actionImport_All.setObjectName("actionImport_All")
        self.actionImport_Secondary_School_Enrollment = QtWidgets.QAction(MainWindow)
        self.actionImport_Secondary_School_Enrollment.setObjectName("actionImport_Secondary_School_Enrollment")
        self.actionImport_Secondary_School_Facilities = QtWidgets.QAction(MainWindow)
        self.actionImport_Secondary_School_Facilities.setObjectName("actionImport_Secondary_School_Facilities")
        self.actionImport_Secondary_School_Classrooms = QtWidgets.QAction(MainWindow)
        self.actionImport_Secondary_School_Classrooms.setObjectName("actionImport_Secondary_School_Classrooms")
        self.actionImport_Teacher_Housing = QtWidgets.QAction(MainWindow)
        self.actionImport_Teacher_Housing.setObjectName("actionImport_Teacher_Housing")
        self.actionGet_Update = QtWidgets.QAction(MainWindow)
        self.actionGet_Update.setObjectName("actionGet_Update")
        self.actionExport_All_Date = QtWidgets.QAction(MainWindow)
        self.actionExport_All_Date.setObjectName("actionExport_All_Date")
        self.actionCheck_for_Updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName("actionCheck_for_Updates")
        self.menuImport_Data.addAction(self.actionImport_School)
        self.menuImport_Data.addAction(self.actionImport_Teacher)
        self.menuImport_Data.addAction(self.actionImport_School_Enrollment)
        self.menuImport_Data.addAction(self.actionImport_school_Facilities)
        self.menuImport_Data.addAction(self.actionImport_school_Classroom)
        self.menuImport_Data.addSeparator()
        self.menuImport_Data.addAction(self.actionImport_Secondary_School_Enrollment)
        self.menuImport_Data.addAction(self.actionImport_Secondary_School_Facilities)
        self.menuImport_Data.addAction(self.actionImport_Secondary_School_Classrooms)
        self.menuImport_Data.addSeparator()
        self.menuImport_Data.addAction(self.actionImport_Teacher_Housing)
        self.menuUpdate.addAction(self.actionCheck_for_Updates)
        self.menubar.addAction(self.menuImport_Data.menuAction())
        self.menubar.addAction(self.menuExport_data.menuAction())
        self.menubar.addAction(self.menuUpdate.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

############################################################### Navigation Buttons
        
        self.Enterdata.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.pushButton_8.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.addnewschool.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(2))
        self.home.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_2.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.addnewteacher.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(3))
        self.home_4.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.back_3.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.schoolenrollmentform.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(4))
        self.home_5.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.back_4.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.teacherqualificationform.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(5))
        self.home_6.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.back_5.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.schoolfacilitiesform.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(6))
        self.home_7.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.back_6.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.schoolclassroomform.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(7))
        self.home_8.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.back_7.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.teacherhousingform.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(8))
        self.home_9.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.back_8.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        
        self.pushButton_15.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(24))
        self.home_10.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.back_9.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))

        self.pushButton_30.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(25))
        self.home_11.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.back_10.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))

        self.pushButton_31.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(26))
        self.home_13.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.back_12.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))

        self.pushButton_32.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(27))
        self.home_14.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.back_13.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))

        self.Reports_3.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(29))
        self.pushButton_29.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_32.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.pushButton_121.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(3))
        self.pushButton_122.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(11))
        
### TABLE NAVIGATION ## HOME AND BACK
        self.Reports_2.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        self.pushButton.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_65.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_66.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        self.pushButton_18.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_19.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        self.pushButton_39.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_40.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        self.pushButton_41.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_42.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        self.pushButton_43.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_44.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        self.pushButton_45.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_46.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        self.pushButton_47.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_48.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        self.pushButton_249.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
### OTHER NAVIGATIONS IN TABLE
        self.pushButton_3.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(10))
        self.pushButton_14.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(13))
        self.pushButton_6.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(12))
        self.pushButton_7.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(14))
        self.pushButton_10.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(15))
        self.pushButton_9.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(16))
        self.pushButton_5.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(11))

        self.pushButton_4.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(10))
        self.viewteachertable_3.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(11))
        self.pushButton_35.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(12))
        self.pushButton_36.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(13))
        self.pushButton_37.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(14))
        self.pushButton_38.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(15))
        self.pushButton_50.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(11))

        self.pushButton_17.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(21))
        self.pushButton_16.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(22))
        self.pushButton_11.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(23))
        self.pushButton_120.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(13))
        self.pushButton_20.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(17))
        self.pushButton_21.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(19))
        self.pushButton_12.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(20))
        self.pushButton_23.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        self.pushButton_25.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        self.pushButton_27.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        self.pushButton_74.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        
        self.pushButton_81.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_82.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))
        
        self.pushButton_13.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(28))
        
        self.pushButton_63.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_103.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))

        self.pushButton_85.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.pushButton_117.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(9))

        self.schoolclassroomform_2.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(27))
        self.home_14.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.back_13.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(1))
        self.pushButton_90.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(20))
        
############################################################# REPORT NAV
        self.pushButton_249.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        self.Reports.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(30))

############################################################# ADMIN NAVIGATION BUTTONS
        self.pushButton_115.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(31))
        self.pushButton_108.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(29))
        self.Reports_4.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(32))
        self.pushButton_72.clicked.connect(lambda:self.stackedWidget.setCurrentIndex(0))
        
############################################################## table sqlite button connections
        self.pushButton_3.clicked.connect(self.schooltable)
        self.pushButton_4.clicked.connect(self.schooltable)
        self.pushButton_5.clicked.connect(self.teachertable)
        self.viewteachertable_3.clicked.connect(self.teachertable)
        self.pushButton_6.clicked.connect(self.enrollmenttable1)
        self.pushButton_35.clicked.connect(self.enrollmenttable1)
        self.pushButton_61.clicked.connect(self.enrollmenttable1all)
        self.pushButton_14.clicked.connect(self.qualificationtable)
        self.pushButton_36.clicked.connect(self.qualificationtable)
        self.pushButton_59.clicked.connect(self.qualificationtableall)
        self.pushButton_7.clicked.connect(self.facilitiestable)
        self.pushButton_37.clicked.connect(self.facilitiestable)
        self.pushButton_57.clicked.connect(self.facilitiestableall)
        self.pushButton_10.clicked.connect(self.classroomtable)
        self.pushButton_38.clicked.connect(self.classroomtable)
        self.pushButton_55.clicked.connect(self.classroomtableall)
        self.pushButton_9.clicked.connect(self.housingtable)
        self.pushButton_50.clicked.connect(self.housingtable)
        self.pushButton_53.clicked.connect(self.housingtableall)

        self.pushButton_20.clicked.connect(self.secenrollmenttable)
        self.pushButton_76.clicked.connect(self.secenrollmenttableall)
        self.pushButton_120.clicked.connect(self.secqualificationtable)
        self.pushButton_80.clicked.connect(self.secqualificationtableall)
        self.pushButton_21.clicked.connect(self.secfacilitiestable)
        self.pushButton_84.clicked.connect(self.secfacilitiestableall)
        self.pushButton_12.clicked.connect(self.secclassroomtable)
        self.pushButton_118.clicked.connect(self.secclassroomtable)
        self.pushButton_119.clicked.connect(self.secclassroomtableall)
        self.pushButton_17.clicked.connect(self.leavetable)
        self.pushButton_64.clicked.connect(self.leavetable)
        self.pushButton_16.clicked.connect(self.retiredtable)
        self.pushButton_95.clicked.connect(self.retiredtable)
        self.pushButton_11.clicked.connect(self.deceasedtable)
        self.pushButton_99.clicked.connect(self.deceasedtable)
        self.pushButton_13.clicked.connect(self.abscondedtable)
        self.pushButton_104.clicked.connect(self.abscondedtable)

############################################################## Home page functions
        
        self.lineEdit.insert(str(totalmalepupils()))
        self.lineEdit_2.insert(str(totalfemalepupils()))
        self.lineEdit_3.insert(str(totalpupils()))
        self.lineEdit_4.insert(str(totalclassroom()))
        self.lineEdit_5.insert(str(district_pupilclassroomratio()))
        self.lineEdit_6.insert(str(districtlatrinestances()))
        self.lineEdit_7.insert(str(districtpupilstanceratio()))
        self.lineEdit_8.insert(str(maleteachers()))
        self.lineEdit_9.insert(str(femaleteachers()))
        self.lineEdit_10.insert(str(totalteachers()))
        self.lineEdit_11.insert(str(certificate()))
        self.lineEdit_12.insert(str(deploma()))
        self.lineEdit_13.insert(str(bachelors()))
        self.lineEdit_14.insert(str(masters()))

###########################################################  Entry connections
        self.save.clicked.connect(self.addschool)
        self.save_2.clicked.connect(self.addschool)
        self.save_2.clicked.connect(self.reset)

        self.save_4.clicked.connect(self.addteacher)
        self.save_12.clicked.connect(self.addteacher)
        self.save_12.clicked.connect(self.resetteacher)

        self.save_5.clicked.connect(self.enrollment)
        self.save_15.clicked.connect(self.enrollment)
        self.save_15.clicked.connect(self.resetenrollment)

        self.save_6.clicked.connect(self.qualification)
        self.save_16.clicked.connect(self.qualification)
        self.save_16.clicked.connect(self.resetqualification)

        self.save_7.clicked.connect(self.facilitiesform)
        self.save_17.clicked.connect(self.facilitiesform)
        self.save_17.clicked.connect(self.resetfacilities)

        self.save_8.clicked.connect(self.classroomform)
        self.save_18.clicked.connect(self.classroomform)
        self.save_18.clicked.connect(self.resetclassroom)

        self.save_9.clicked.connect(self.teacherhousing)
        self.save_19.clicked.connect(self.teacherhousing)
        self.save_19.clicked.connect(self.resetteacherhousing)

        self.save_10.clicked.connect(self.secenrollment)
        self.save_23.clicked.connect(self.secenrollment)
        self.save_23.clicked.connect(self.resetensec)

        self.save_11.clicked.connect(self.secqualification)
        self.save_22.clicked.connect(self.secqualification)
        self.save_22.clicked.connect(self.resetsecqualification)

        self.save_13.clicked.connect(self.secfacilities)
        self.save_21.clicked.connect(self.secfacilities)
        self.save_21.clicked.connect(self.resetsecfacilities)

        self.save_14.clicked.connect(self.secclassroom)
        self.save_20.clicked.connect(self.secclassroom)
        self.save_20.clicked.connect(self.resetsecclassroom)

########################################################### OTHER TABLE FUNCTIONS
        self.pushButton_68.clicked.connect(self.schooltable2)
        self.pushButton_69.clicked.connect(self.schooltable3)
        self.pushButton_73.clicked.connect(self.teachertable2)
        self.pushButton_71.clicked.connect(self.teachertable3)
        self.pushButton_88.clicked.connect(self.housingtable2)
        self.pushButton_86.clicked.connect(self.housingtable3)
        self.pushButton_96.clicked.connect(self.leavetable2)
        self.pushButton_92.clicked.connect(self.leavetable3)
        self.pushButton_98.clicked.connect(self.retiredtable2)
        self.pushButton_96.clicked.connect(self.retiredtable3)
        self.pushButton_102.clicked.connect(self.deceasedtable2)
        self.pushButton_100.clicked.connect(self.deceasedtable3)
        self.pushButton_12.clicked.connect(self.secclassroomtable)
        self.pushButton_119.clicked.connect(self.secclassroomtableall)
        
        
        
########################################################### SEARCH BUTTONS

        self.pushButton_34.clicked.connect(self.searchschool)
        self.pushButton_110.clicked.connect(self.searchteacherprofile)

########################################################### ADMIN BUTTONS
        self.pushButton_28.clicked.connect(self.searchteacher)
        self.pushButton_33.clicked.connect(self.absconded)
        self.pushButton_116.clicked.connect(self.deletet)
        self.pushButton_52.clicked.connect(self.leavesave)
        self.pushButton_106.clicked.connect(self.deceased)
        
############################################################ MAIN MANU CONNECTIONS

        self.actionImport_School.setShortcut("ctrl+s")
        self.actionImport_School.setStatusTip("Import Schools")
        self.actionImport_School.triggered.connect(self.file_school)

        self.actionImport_Teacher.setShortcut("ctrl+t")
        self.actionImport_Teacher.setStatusTip("Import Teachers")
        self.actionImport_Teacher.triggered.connect(self.file_teacher)

        self.actionImport_School_Enrollment.setShortcut("ctrl+e")
        self.actionImport_School_Enrollment.setStatusTip("Import Primary Schools Enrollment")
        self.actionImport_School_Enrollment.triggered.connect(self.file_priennrollment)

        self.actionImport_Secondary_School_Enrollment.setShortcut("ctrl+a")
        self.actionImport_Secondary_School_Enrollment.setStatusTip("Import Secondary Schools Enrollment")
        self.actionImport_Secondary_School_Enrollment.triggered.connect(self.file_secenrollment)

        self.actionImport_school_Facilities.setShortcut("ctrl+f")
        self.actionImport_school_Facilities.setStatusTip("Import Primary Schools Facilities")
        self.actionImport_school_Facilities.triggered.connect(self.file_prifaciities)

        self.actionImport_Secondary_School_Facilities.setShortcut("ctrl+g")
        self.actionImport_Secondary_School_Facilities.setStatusTip("Import Secondary Schools Facilities")
        self.actionImport_Secondary_School_Facilities.triggered.connect(self.file_secfaciities)

        self.actionImport_school_Classroom.setShortcut("ctrl+c")
        self.actionImport_school_Classroom.setStatusTip("Import Primary School classrooms")
        self.actionImport_school_Classroom.triggered.connect(self.file_priclassroom)

        self.actionImport_Secondary_School_Classrooms.setShortcut("ctrl+w")
        self.actionImport_Secondary_School_Classrooms.setStatusTip("Import secondary School classrooms")
        self.actionImport_Secondary_School_Classrooms.triggered.connect(self.file_secclassroom)

        self.actionImport_Teacher_Housing.setShortcut("ctrl+h")
        self.actionImport_Teacher_Housing.setStatusTip("Import Teacher Housing")
        self.actionImport_Teacher_Housing.triggered.connect(self.file_secclassroom)

############################################################ REPORT CONNECTIONS

        self.Reports.clicked.connect(self.district)
        self.Reports.clicked.connect(self.adekokwok)
        self.Reports.clicked.connect(self.agali)
        self.Reports.clicked.connect(self.adyel)
        self.Reports.clicked.connect(self.agweng)
        self.Reports.clicked.connect(self.amach)
        self.Reports.clicked.connect(self.aromo)
        self.Reports.clicked.connect(self.barr)
        self.Reports.clicked.connect(self.lira)
        self.Reports.clicked.connect(self.ngetta)
        self.Reports.clicked.connect(self.ogur)
        self.Reports.clicked.connect(self.ojwina)
        self.Reports.clicked.connect(self.railways)

############################################################ SEARCH AND PARISHES SCHOOL REPORT
        self.pushButton_51.clicked.connect(self.searchenr)
        self.pushButton_91.clicked.connect(self.searchsecenr)
        self.pushButton_107.clicked.connect(self.searchfacil)
        self.pushButton_109.clicked.connect(self.searchsecfacil)
        self.pushButton_111.clicked.connect(self.searchqual)
        self.pushButton_114.clicked.connect(self.searchsecqual)
        self.pushButton_123.clicked.connect(self.searchhousing)

        self.pushButton_124.clicked.connect(self.pari)
        self.pushButton_124.clicked.connect(self.prigraph)

############################################################ USERS
        self.pushButton_70.clicked.connect(self.adduser)
########################################################### Graph refresh
        self.pushButton.clicked.connect(self.graph1)
        self.Reports.clicked.connect(self.graph2)
        self.Reports.clicked.connect(self.graph3)
        self.Reports.clicked.connect(self.graph4)
        self.Reports.clicked.connect(self.graph5)
        self.Reports.clicked.connect(self.graph6)
        self.Reports.clicked.connect(self.graph7)
        self.Reports.clicked.connect(self.graph8)
        self.Reports.clicked.connect(self.graph9)

############################################################ GRAPH 2


        self.graph1()
        self.graph2()
        self.graph3()
        self.graph4()
        self.graph5()
        self.graph6()
        self.graph7()
        self.graph8()
        self.graph9()
        self.graph10()
        self.graph11()
        self.graph12()
        self.graph13()
        self.graph14()
        self.graph15()
        self.graph16()
        self.graph17()
        self.graph18()
        self.graph19()
        self.graph20()
        self.graph21()
        self.graph22()
        self.graph23()
        self.graph24()
        self.graph25()
        self.graph26()
        self.graph27()
        self.graph28()
        self.graph29()
        self.graph30()
        self.graph31()
        self.graph32()
        self.graph33()
        self.graph34()
        self.graph35()
        self.graph36()
        self.graph37()
        self.graph38()
        self.graph39()
        self.graph40()
        self.graph41()
        self.graph42()
        self.graph43()
        self.graph44()
        self.graph45()
        self.graph46()
        self.graph47()
        self.graph48()
        self.graph49()
        self.graph50()
        self.graph51()
        self.graph52()
        self.graph53()

########################################################### PHOTOS

    def photo(self):
        photofile,_ = QFileDialog.getOpenFileName(None,"Open Image File","","JPG (*.jpg *.png)")
        filename = photofile.rpartition("/")[2]        

########################################################### USERS
    def EnUsers(self):
        
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('Success')
        mb.setText("User Successfully Added")
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_()

    def EnFailed(self):
        
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('Error')
        mb.setText("User Not Added")
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_()

    def adduser(self):
        try:
            x = "districtdb"
            y = "1234district5"
            self.name = self.lineEdit_23.text()
            self.passd = self.lineEdit_22.text()
            
            fn = self.lineEdit_16.text()
            sn = self.lineEdit_18.text()
            un = self.lineEdit_20.text()
            ps = self.lineEdit_21.text()
            
            if self.name == x and self.passd == y:
                users(fn,sn,un,ps)
                self.EnUsers()

            c.execute("SELECT * FROM user WHERE user_name = ? AND passward = ?",(self.name,self.passd))
            if len(c.fetchall()) > 0:
                users(fn,sn,un,ps)
                self.EnUsers()
        except Exception:
                self.EnFailed()
            
############################################################ GRAPH FUNCTIONS

    def prigraph(self):
        self.emp = self.lineEdit_17.text()

        mpri = ptotalmalep(self.emp)
        fpri = ptotalfemalep(self.emp)

        msec = ptotalmales(self.emp)
        fsec = ptotalfemales(self.emp)
        
        lst = [mpri,fpri]
        labels = [r'Male',r'Female']
        try:
            self.widget_22.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_22.canvas.draw()
        except Exception:
            x = [1]
            self.widget_22.canvas.ax.pie(x)
            self.widget_22.canvas.draw()

        lst2 = [msec,fsec]
        try:
            self.widget_23.canvas.ax.pie(lst2,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_23.canvas.draw()
        except Exception:
            x = [1]
            self.widget_23.canvas.ax.pie(x)
            self.widget_23.canvas.draw()

        crmp = pcertm(self.emp)
        crfp = pcertf(self.emp)
        licem = plicm(self.emp)
        licef = plicf(self.emp)
        deplm = pdepm(self.emp)
        deplf = pdepf(self.emp)
        bcm = pbacm(self.emp)
        bcf = pbacf(self.emp)
        mam = pmasm(self.emp)
        maf = pmasf(self.emp)

        a = crmp+crfp
        b = licem+licef
        c = deplm+deplf
        d = bcm+bcf
        e = mam+maf
        lst3 = [a,b,c,d,e]
        labels2 = [r'Certifcate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_24.canvas.ax.pie(lst3,labels=labels2,autopct='%1.1f%%',shadow=False)
            self.widget_24.canvas.draw()
        except Exception:
            x = [1]
            self.widget_24.canvas.ax.pie(x)
            self.widget_24.canvas.draw()

        crmps = pcertms(self.emp)
        crfps = pcertfs(self.emp)
        licems = plicms(self.emp)
        licefs = plicfs(self.emp)
        deplms = pdepms(self.emp)
        deplfs = pdepfs(self.emp)
        bcms = pbacms(self.emp)
        bcfs = pbacfs(self.emp)
        mams = pmasms(self.emp)
        mafs = pmasfs(self.emp)

        an = crmps+crfps
        bn = licems+licefs
        cn = deplms+deplfs
        dn = bcms+bcfs
        en = mams+mafs

        lst4 = [an,bn,cn,dn,en]
        try:
            self.widget_25.canvas.ax.pie(lst4,labels=labels2,autopct='%1.1f%%',shadow=False)
            self.widget_25.canvas.draw()
        except Exception:
            x = [1]
            self.widget_25.canvas.ax.pie(x)
            self.widget_25.canvas.draw()

        

############################################################################

    def graph53(self):
        x = "Railways"
        crmp = certms(x)
        crfp = certfs(x)
        licem = licms(x)
        licef = licfs(x)
        deplm = depms(x)
        deplf = depfs(x)
        bcm = bacms(x)
        bcf = bacfs(x)
        mam = masms(x)
        maf = masfs(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_47.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_47.canvas.draw()
        except Exception:
            x = [1]
            self.widget_47.canvas.ax.pie(x)
            self.widget_47.canvas.draw()

    def graph52(self):
        x = "Railways"
        crmp = certm(x)
        crfp = certf(x)
        licem = licm(x)
        licef = licf(x)
        deplm = depm(x)
        deplf = depf(x)
        bcm = bacm(x)
        bcf = bacf(x)
        mam = masm(x)
        maf = masf(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_149.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_149.canvas.draw()
        except Exception:
            x = [1]
            self.widget_149.canvas.ax.pie(x)
            self.widget_149.canvas.draw()
        
    def graph51(self):
        x = "Railways"
        mp = totalmales(x)
        fp = totalfemales(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_46.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_46.canvas.draw()
        except Exception:
            x = [1]
            self.widget_46.canvas.ax.pie(x)
            self.widget_46.canvas.draw()
            
    def graph50(self):
        x = "Railways"
        mp = totalmalep(x)
        fp = totalfemalep(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_148.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_148.canvas.draw()
        except Exception:
            x = [1]
            self.widget_148.canvas.ax.pie(x)
            self.widget_148.canvas.draw()

######################################################################################################################

    def graph49(self):
        x = "Ojwina"
        crmp = certms(x)
        crfp = certfs(x)
        licem = licms(x)
        licef = licfs(x)
        deplm = depms(x)
        deplf = depfs(x)
        bcm = bacms(x)
        bcf = bacfs(x)
        mam = masms(x)
        maf = masfs(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_45.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_45.canvas.draw()
        except Exception:
            x = [1]
            self.widget_45.canvas.ax.pie(x)
            self.widget_45.canvas.draw()

    def graph48(self):
        x = "Ojwina"
        crmp = certm(x)
        crfp = certf(x)
        licem = licm(x)
        licef = licf(x)
        deplm = depm(x)
        deplf = depf(x)
        bcm = bacm(x)
        bcf = bacf(x)
        mam = masm(x)
        maf = masf(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_147.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_147.canvas.draw()
        except Exception:
            x = [1]
            self.widget_147.canvas.ax.pie(x)
            self.widget_147.canvas.draw()
        
    def graph47(self):
        x = "Ojwina"
        mp = totalmales(x)
        fp = totalfemales(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_44.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_44.canvas.draw()
        except Exception:
            x = [1]
            self.widget_44.canvas.ax.pie(x)
            self.widget_44.canvas.draw()
            
    def graph46(self):
        x = "Ojwina"
        mp = totalmalep(x)
        fp = totalfemalep(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_146.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_146.canvas.draw()
        except Exception:
            x = [1]
            self.widget_146.canvas.ax.pie(x)
            self.widget_146.canvas.draw()

######################################################################################################################
    
    def graph45(self):
        x = "Ogur"
        crmp = certms(x)
        crfp = certfs(x)
        licem = licms(x)
        licef = licfs(x)
        deplm = depms(x)
        deplf = depfs(x)
        bcm = bacms(x)
        bcf = bacfs(x)
        mam = masms(x)
        maf = masfs(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_43.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_43.canvas.draw()
        except Exception:
            x = [1]
            self.widget_43.canvas.ax.pie(x)
            self.widget_43.canvas.draw()

    def graph44(self):
        x = "Ogur"
        crmp = certm(x)
        crfp = certf(x)
        licem = licm(x)
        licef = licf(x)
        deplm = depm(x)
        deplf = depf(x)
        bcm = bacm(x)
        bcf = bacf(x)
        mam = masm(x)
        maf = masf(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_20.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_20.canvas.draw()
        except Exception:
            x = [1]
            self.widget_20.canvas.ax.pie(x)
            self.widget_20.canvas.draw()
        
    def graph43(self):
        x = "Ogur"
        mp = totalmales(x)
        fp = totalfemales(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_42.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_42.canvas.draw()
        except Exception:
            x = [1]
            self.widget_42.canvas.ax.pie(x)
            self.widget_42.canvas.draw()
            
    def graph42(self):
        x = "Ogur"
        mp = totalmalep(x)
        fp = totalfemalep(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_21.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_21.canvas.draw()
        except Exception:
            x = [1]
            self.widget_21.canvas.ax.pie(x)
            self.widget_21.canvas.draw()

######################################################################################################################

    def graph41(self):
        x = "Ngetta"
        crmp = certms(x)
        crfp = certfs(x)
        licem = licms(x)
        licef = licfs(x)
        deplm = depms(x)
        deplf = depfs(x)
        bcm = bacms(x)
        bcf = bacfs(x)
        mam = masms(x)
        maf = masfs(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_41.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_41.canvas.draw()
        except Exception:
            x = [1]
            self.widget_41.canvas.ax.pie(x)
            self.widget_41.canvas.draw()

    def graph40(self):
        x = "Ngetta"
        crmp = certm(x)
        crfp = certf(x)
        licem = licm(x)
        licef = licf(x)
        deplm = depm(x)
        deplf = depf(x)
        bcm = bacm(x)
        bcf = bacf(x)
        mam = masm(x)
        maf = masf(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_18.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_18.canvas.draw()
        except Exception:
            x = [1]
            self.widget_18.canvas.ax.pie(x)
            self.widget_18.canvas.draw()
        
    def graph39(self):
        x = "Ngetta"
        mp = totalmales(x)
        fp = totalfemales(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_40.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_40.canvas.draw()
        except Exception:
            x = [1]
            self.widget_40.canvas.ax.pie(x)
            self.widget_40.canvas.draw()
            
    def graph38(self):
        x = "Ngetta"
        mp = totalmalep(x)
        fp = totalfemalep(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_19.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_19.canvas.draw()
        except Exception:
            x = [1]
            self.widget_19.canvas.ax.pie(x)
            self.widget_19.canvas.draw()

######################################################################################################################

    def graph37(self):
        x = "Lira"
        crmp = certms(x)
        crfp = certfs(x)
        licem = licms(x)
        licef = licfs(x)
        deplm = depms(x)
        deplf = depfs(x)
        bcm = bacms(x)
        bcf = bacfs(x)
        mam = masms(x)
        maf = masfs(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_39.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_39.canvas.draw()
        except Exception:
            x = [1]
            self.widget_39.canvas.ax.pie(x)
            self.widget_39.canvas.draw()

    def graph36(self):
        x = "Lira"
        crmp = certm(x)
        crfp = certf(x)
        licem = licm(x)
        licef = licf(x)
        deplm = depm(x)
        deplf = depf(x)
        bcm = bacm(x)
        bcf = bacf(x)
        mam = masm(x)
        maf = masf(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_16.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_16.canvas.draw()
        except Exception:
            x = [1]
            self.widget_16.canvas.ax.pie(x)
            self.widget_16.canvas.draw()
        
    def graph35(self):
        x = "Lira"
        mp = totalmales(x)
        fp = totalfemales(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_38.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_38.canvas.draw()
        except Exception:
            x = [1]
            self.widget_38.canvas.ax.pie(x)
            self.widget_38.canvas.draw()
            
    def graph34(self):
        x = "Lira"
        mp = totalmalep(x)
        fp = totalfemalep(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_17.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=False)
            self.widget_17.canvas.draw()
        except Exception:
            x = [1]
            self.widget_17.canvas.ax.pie(x)
            self.widget_17.canvas.draw()

######################################################################################################################

    def graph33(self):
        x = "Barr"
        crmp = certms(x)
        crfp = certfs(x)
        licem = licms(x)
        licef = licfs(x)
        deplm = depms(x)
        deplf = depfs(x)
        bcm = bacms(x)
        bcf = bacfs(x)
        mam = masms(x)
        maf = masfs(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_37.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_37.canvas.draw()
        except Exception:
            x = [1]
            self.widget_37.canvas.ax.pie(x)
            self.widget_37.canvas.draw()

    def graph32(self):
        x = "Barr"
        crmp = certm(x)
        crfp = certf(x)
        licem = licm(x)
        licef = licf(x)
        deplm = depm(x)
        deplf = depf(x)
        bcm = bacm(x)
        bcf = bacf(x)
        mam = masm(x)
        maf = masf(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_14.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_14.canvas.draw()
        except Exception:
            x = [1]
            self.widget_14.canvas.ax.pie(x)
            self.widget_14.canvas.draw()
        
    def graph31(self):
        x = "Barr"
        mp = totalmales(x)
        fp = totalfemales(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_36.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_36.canvas.draw()
        except Exception:
            x = [1]
            self.widget_36.canvas.ax.pie(x)
            self.widget_36.canvas.draw()
            
    def graph30(self):
        x = "Barr"
        mp = totalmalep(x)
        fp = totalfemalep(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_15.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_15.canvas.draw()
        except Exception:
            x = [1]
            self.widget_15.canvas.ax.pie(x)
            self.widget_15.canvas.draw()

######################################################################################################################

    def graph29(self):
        x = "Aromo"
        crmp = certms(x)
        crfp = certfs(x)
        licem = licms(x)
        licef = licfs(x)
        deplm = depms(x)
        deplf = depfs(x)
        bcm = bacms(x)
        bcf = bacfs(x)
        mam = masms(x)
        maf = masfs(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_35.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_35.canvas.draw()
        except Exception:
            x = [1]
            self.widget_35.canvas.ax.pie(x)
            self.widget_35.canvas.draw()

    def graph28(self):
        x = "Aromo"
        crmp = certm(x)
        crfp = certf(x)
        licem = licm(x)
        licef = licf(x)
        deplm = depm(x)
        deplf = depf(x)
        bcm = bacm(x)
        bcf = bacf(x)
        mam = masm(x)
        maf = masf(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_12.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_12.canvas.draw()
        except Exception:
            x = [1]
            self.widget_12.canvas.ax.pie(x)
            self.widget_12.canvas.draw()
        
    def graph27(self):
        x = "Aromo"
        mp = totalmales(x)
        fp = totalfemales(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_34.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_34.canvas.draw()
        except Exception:
            x = [1]
            self.widget_34.canvas.ax.pie(x)
            self.widget_34.canvas.draw()
            
    def graph26(self):
        x = "Aromo"
        mp = totalmalep(x)
        fp = totalfemalep(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_13.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_13.canvas.draw()
        except Exception:
            x = [1]
            self.widget_13.canvas.ax.pie(x)
            self.widget_13.canvas.draw()

######################################################################################################################

    def graph25(self):
        x = "Amach"
        crmp = certms(x)
        crfp = certfs(x)
        licem = licms(x)
        licef = licfs(x)
        deplm = depms(x)
        deplf = depfs(x)
        bcm = bacms(x)
        bcf = bacfs(x)
        mam = masms(x)
        maf = masfs(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_33.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_33.canvas.draw()
        except Exception:
            x = [1]
            self.widget_33.canvas.ax.pie(x)
            self.widget_33.canvas.draw()

    def graph24(self):
        x = "Amach"
        crmp = certm(x)
        crfp = certf(x)
        licem = licm(x)
        licef = licf(x)
        deplm = depm(x)
        deplf = depf(x)
        bcm = bacm(x)
        bcf = bacf(x)
        mam = masm(x)
        maf = masf(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_10.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_10.canvas.draw()
        except Exception:
            x = [1]
            self.widget_10.canvas.ax.pie(x)
            self.widget_10.canvas.draw()
        
    def graph23(self):
        x = "Amach"
        mp = totalmales(x)
        fp = totalfemales(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_32.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_32.canvas.draw()
        except Exception:
            x = [1]
            self.widget_32.canvas.ax.pie(x)
            self.widget_32.canvas.draw()
            
    def graph22(self):
        x = "Amach"
        mp = totalmalep(x)
        fp = totalfemalep(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_11.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_11.canvas.draw()
        except Exception:
            x = [1]
            self.widget_11.canvas.ax.pie(x)
            self.widget_11.canvas.draw()

######################################################################################################################

    def graph21(self):
        x = "Agweng"
        crmp = certms(x)
        crfp = certfs(x)
        licem = licms(x)
        licef = licfs(x)
        deplm = depms(x)
        deplf = depfs(x)
        bcm = bacms(x)
        bcf = bacfs(x)
        mam = masms(x)
        maf = masfs(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_31.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_31.canvas.draw()
        except Exception:
            x = [1]
            self.widget_31.canvas.ax.pie(x)
            self.widget_31.canvas.draw()

    def graph20(self):
        x = "Agweng"
        crmp = certm(x)
        crfp = certf(x)
        licem = licm(x)
        licef = licf(x)
        deplm = depm(x)
        deplf = depf(x)
        bcm = bacm(x)
        bcf = bacf(x)
        mam = masm(x)
        maf = masf(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_8.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_8.canvas.draw()
        except Exception:
            x = [1]
            self.widget_8.canvas.ax.pie(x)
            self.widget_8.canvas.draw()
        
    def graph19(self):
        x = "Agweng"
        mp = totalmales(x)
        fp = totalfemales(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_30.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_30.canvas.draw()
        except Exception:
            x = [1]
            self.widget_30.canvas.ax.pie(x)
            self.widget_30.canvas.draw()
            
    def graph18(self):
        x = "Agweng"
        mp = totalmalep(x)
        fp = totalfemalep(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_9.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_9.canvas.draw()
        except Exception:
            x = [1]
            self.widget_9.canvas.ax.pie(x)
            self.widget_9.canvas.draw()

######################################################################################################################

    def graph17(self):
        x = "Agali"
        crmp = certms(x)
        crfp = certfs(x)
        licem = licms(x)
        licef = licfs(x)
        deplm = depms(x)
        deplf = depfs(x)
        bcm = bacms(x)
        bcf = bacfs(x)
        mam = masms(x)
        maf = masfs(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_29.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_29.canvas.draw()
        except Exception:
            x = [1]
            self.widget_29.canvas.ax.pie(x)
            self.widget_29.canvas.draw()

    def graph16(self):
        x = "Agali"
        crmp = certm(x)
        crfp = certf(x)
        licem = licm(x)
        licef = licf(x)
        deplm = depm(x)
        deplf = depf(x)
        bcm = bacm(x)
        bcf = bacf(x)
        mam = masm(x)
        maf = masf(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_6.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_6.canvas.draw()
        except Exception:
            x = [1]
            self.widget_6.canvas.ax.pie(x)
            self.widget_6.canvas.draw()
        
    def graph15(self):
        x = "Agali"
        mp = totalmales(x)
        fp = totalfemales(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_28.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_28.canvas.draw()
        except Exception:
            x = [1]
            self.widget_28.canvas.ax.pie(x)
            self.widget_28.canvas.draw()
            
    def graph14(self):
        x = "Agali"
        mp = totalmalep(x)
        fp = totalfemalep(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_7.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_7.canvas.draw()
        except Exception:
            x = [1]
            self.widget_7.canvas.ax.pie(x)
            self.widget_7.canvas.draw()

######################################################################################################################
        
    def graph13(self):
        x = "Adyel"
        crmp = certms(x)
        crfp = certfs(x)
        licem = licms(x)
        licef = licfs(x)
        deplm = depms(x)
        deplf = depfs(x)
        bcm = bacms(x)
        bcf = bacfs(x)
        mam = masms(x)
        maf = masfs(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_151.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_151.canvas.draw()
        except Exception:
            x = [1]
            self.widget_151.canvas.ax.pie(x)
            self.widget_151.canvas.draw()

    def graph12(self):
        x = "Adyel"
        crmp = certm(x)
        crfp = certf(x)
        licem = licm(x)
        licef = licf(x)
        deplm = depm(x)
        deplf = depf(x)
        bcm = bacm(x)
        bcf = bacf(x)
        mam = masm(x)
        maf = masf(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_145.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_145.canvas.draw()
        except Exception:
            x = [1]
            self.widget_145.canvas.ax.pie(x)
            self.widget_145.canvas.draw()
        
    def graph11(self):
        x = "Adyel"
        mp = totalmales(x)
        fp = totalfemales(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_150.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_150.canvas.draw()
        except Exception:
            x = [1]
            self.widget_150.canvas.ax.pie(x)
            self.widget_150.canvas.draw()
            
    def graph10(self):
        x = "Adyel"
        mp = totalmalep(x)
        fp = totalfemalep(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_144.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_144.canvas.draw()
        except Exception:
            x = [1]
            self.widget_144.canvas.ax.pie(x)
            self.widget_144.canvas.draw()

######################################################################################################################

    def graph9(self):
        x = "Adekokwok"
        crmp = certms(x)
        crfp = certfs(x)
        licem = licms(x)
        licef = licfs(x)
        deplm = depms(x)
        deplf = depfs(x)
        bcm = bacms(x)
        bcf = bacfs(x)
        mam = masms(x)
        maf = masfs(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_27.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_27.canvas.draw()
        except Exception:
            x = [1]
            self.widget_27.canvas.ax.pie(x)
            self.widget_27.canvas.draw()

    def graph8(self):
        x = "Adekokwok"
        crmp = certm(x)
        crfp = certf(x)
        licem = licm(x)
        licef = licf(x)
        deplm = depm(x)
        deplf = depf(x)
        bcm = bacm(x)
        bcf = bacf(x)
        mam = masm(x)
        maf = masf(x)
        
        tc = crmp+crfp
        lc = licem+licef
        dp = deplm+deplf
        bc = bcm+bcf
        mm = mam+maf
        lst = [tc,lc,dp,bc,mm]
        labels = [r'Certificate',r'Licensed',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_5.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_5.canvas.draw()
        except Exception:
            x = [1]
            self.widget_5.canvas.ax.pie(x)
            self.widget_5.canvas.draw()
        
    def graph7(self):
        x = "Adekokwok"
        mp = totalmales(x)
        fp = totalfemales(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_26.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_26.canvas.draw()
        except Exception:
            x = [1]
            self.widget_26.canvas.ax.pie(x)
            self.widget_26.canvas.draw()
            
    def graph6(self):
        x = "Adekokwok"
        mp = totalmalep(x)
        fp = totalfemalep(x)
        lst = [mp,fp]
        labels = [r'Male',r'Female']
        try:
            self.widget_4.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_4.canvas.draw()
        except Exception:
            x = [1]
            self.widget_4.canvas.ax.pie(x)
            self.widget_4.canvas.draw()

######################################################################################################################
        
    def graph5(self):
        
        crmp = certificatems()
        crfp = certificatefs()
        dmp = deplomamsec()
        dfp = deplomafsec()
        bam = bachelorsmsec()
        baf = bachelorsfsec()
        mam = mastersmsec()
        maf = mastersfsec()
        
        tc = crmp+crfp
        td = dmp+dfp
        tb = bam+baf
        mm = mam+maf

        lst = [tc,td,tb,mm]
        labels = [r'Certificate',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_49.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_49.canvas.draw()
        except Exception:
            x = [1]
            self.widget_49.canvas.ax.pie(x)
            self.widget_49.canvas.draw()
            
    def graph4(self):
        
        crmp = certificatem()
        crfp = certificatef()
        dmp = deplomam()
        dfp = deplomaf()
        bam = bachelorsm()
        baf = bachelorsf()
        mam = mastersm()
        maf = mastersf()
        
        tc = crmp+crfp
        td = dmp+dfp
        tb = bam+baf
        mm = mam+maf

        lst = [tc,td,tb,mm]
        labels = [r'Certificate',r'Deploma',r'Bachelors',r'Masters']
        try:
            self.widget_2.canvas.ax.pie(lst,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_2.canvas.draw()
        except Exception:
            x = [1]
            self.widget_2.canvas.ax.pie(x)
            self.widget_2.canvas.draw()
        
    def graph3(self):
        em = totalmalesec()
        ef = totalfemalesec()
        lst = [em,ef]
        labels = [r'Male',r'Female']
        colors = ['blue','red']
        try:
            self.widget_48.canvas.ax.pie(lst,colors=colors,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget_48.canvas.draw()
        except Exception:
            x = [1]
            self.widget_48.canvas.ax.pie(x)
            self.widget_48.canvas.draw()

    def graph2(self):
        em = totalmaleprim()
        ef = totalfemaleprime()
        lst = [em,ef]
        labels = [r'Male',r'Female']
        colors = ['blue','red']
        try:
            self.widget.canvas.ax.pie(lst,colors=colors,labels=labels,autopct='%1.1f%%',shadow=True)
            self.widget.canvas.draw()
        except Exception:
            x = [1]
            self.widget.canvas.ax.pie(x)
            self.widget.canvas.draw()
    
    def graph1(self):

        m1 = p1tm()
        f1 = p1tf()
        m2 = p2tm()
        f2 = p2tf()
        m3 = p3tm()
        f3 = p3tf()
        m4 = p4tm()
        f4 = p4tf()
        m5 = p5tm()
        f5 = p5tf()
        m6 = p6tm()
        f6 = p6tf()
        m7 = p7tm()
        f7 = p7tf()

        lst = [m1,f1,m2,f2,m3,f3,m4,f4,m5,f5,m6,f6,m7,f7]
    
        name = ["P1 M","P1 F","P2 M","P2 F","P3 M","P3 F","P4 M","P4 F","P5 M","P5 F","P6 M","P6 F","P7 M","P7 F"]
        try:
            self.widget_3.canvas.ax.bar(name,lst)
            self.widget_3.canvas.draw()
        except Exception:
            x = [1]
            self.widget.canvas.ax.pie(x)
            self.widget.canvas.draw()
        

############################################################ REPORT FUNCTIONS

    def pari(self):
        self.emp = self.lineEdit_17.text()
        
        mpri = ptotalmalep(self.emp)
        fpri = ptotalfemalep(str(self.emp))
        msec = ptotalmales(str(self.emp))
        fsec = ptotalfemales(str(self.emp))

        totalp = int(mpri)+int(fpri)
        totals = int(msec)+int(fsec)

        mprin = "Total Male Pupils = "+ str(mpri)
        fprin = "Total Female Pupils = "+ str(fpri)
        totalpn = "Total Number of Pupils = "+ str(totalp)
        msecn = "Total Male Students = "+ str(msec)
        fsecn = "Total Female Students = "+ str(fsec)
        totalsn = "Total Number of Students Pupils = "+ str(totals)

        self.textEdit_35.append(str(mprin))
        self.textEdit_35.append("")
        self.textEdit_35.append(str(fprin))
        self.textEdit_35.append("")
        self.textEdit_35.append(str(totalpn))
        self.textEdit_35.append("")
        self.textEdit_35.append(str(msecn))
        self.textEdit_35.append("")
        self.textEdit_35.append(str(fsecn))
        self.textEdit_35.append("")
        self.textEdit_35.append(str(totalsn))
        self.textEdit_35.append("")

        cl = pclassroompri(self.emp)
        cls = pclassroomsec(self.emp)
        stpr = pstancepri(self.emp)
        stprs = pstancesec(self.emp)
        dr = pdeskpri(self.emp)
        drp = pdesksec(self.emp)
        tr =  pteachpri(self.emp)
        trs = pteachsec(self.emp)

        priclass = totalp/(cl+0.00000001)
        secclass = totals/(cls+0.00000001)
        pristance = totalp/(stpr+0.00000001)
        secstance = totals/(stprs+0.00000001)
        pridesk = totalp/(dr+0.0000001)
        secdesk = totals/(drp+0.0000001)
        priteachers = totalp/(tr+0.0000001)
        secteachers = totals/(trs+0.0000001)

        priclassn = "Primary School Pupil Classroom Ratio = "+str(priclass)
        secclassn = "Primary School Student Classroom Ratio = "+str(secclass)
        pristancen = "Primary School Pupil Latrine Stance Ratio = "+str(pristance)
        secstancen = "Primary School Student Classroom Ratio = "+str(secstance)
        prideskn = "Primary School Pupil Desk Ratio = "+str(pridesk)
        secdeskn = "Primary School Student Desk Ratio = "+str(secdesk)
        priteachersn = "Primary School Pupil Teacher Ratio = "+str(priteachers)
        secteachersn = "Primary School Student Teacher Ratio = "+str(secteachers)

        self.textEdit_36.append(str(priclassn))
        self.textEdit_36.append("")
        self.textEdit_36.append(str(secclassn))
        self.textEdit_36.append("")
        self.textEdit_36.append(str(pristancen))
        self.textEdit_36.append("")
        self.textEdit_36.append(str(secstancen))
        self.textEdit_36.append("")
        self.textEdit_36.append(str(prideskn))
        self.textEdit_36.append("")
        self.textEdit_36.append(str(secdeskn))
        self.textEdit_36.append("")
        self.textEdit_36.append(str(priteachersn))
        self.textEdit_36.append("")
        self.textEdit_36.append(str(secteachersn))
        self.textEdit_36.append("")

        crmp = pcertm(self.emp)
        crfp = pcertf(self.emp)
        cerms = pcertms(self.emp)
        cerfs = pcertfs(self.emp)

        licem = plicm(self.emp)
        licef = plicf(self.emp)
        licems = plicms(self.emp)
        licefs = plicfs(self.emp)

        deplm = pdepm(self.emp)
        deplf = pdepf(self.emp)
        deplms = pdepms(self.emp)
        deplmfs = pdepfs(self.emp)

        bcm = pbacm(self.emp)
        bcf = pbacf(self.emp)
        bcms = pbacms(self.emp)
        bcfs = pbacfs(self.emp)

        mam = pmasm(self.emp)
        maf = pmasf(self.emp)
        mams = pmasms(self.emp)
        mafs = pmasfs(self.emp)

        crmpn = "Certificate Holders Primary Male = "+ str(crmp)
        crfn = "Certificate Holders Primary Female = "+ str(crfp)
        cermsn = "Certificate Holders Secondary Male = "+ str(cerms)
        cerfsn = "Certificate Holders Secondary Female = "+ str(cerfs)
        licemn = "Licence Holders Primary Male = "+ str(licem)
        licefn = "Licence Holders Primary Female = "+ str(licef)
        licemsn = "Licence Holders Secondary Male = "+ str(licems)
        licefsn = "Licence Holders Secondary Female = "+ str(licefs)
        deplmn = "Deploma Holders Primary Male = "+ str(deplm)
        deplfn = "Deploma Holders Primary Female = "+ str(deplf)
        deplmsn = "Deploma Holders Secondary Male = "+ str(deplms)
        deplfsn = "Deploma Holders Secondary Female = "+ str(deplmfs)
        bcmn = "Bachelors Holders Primary Male = "+ str(bcm)
        bcfn = "Bachelors Holders Primary Female = "+ str(bcf)
        bcmsn = "Bachelors Holders Secondary Male = "+ str(bcms)
        bcfsn = "Deploma Holders Secondary Female = "+ str(bcfs)
        mamn = "Masters and Above Primary Male = "+ str(mam)
        mafn = "Masters and Above Primary Female = "+ str(maf)
        mamsn = "Masters and Above Secondary Male = "+ str(mams)
        mafsn = "Masters and Above Secondary Female = "+ str(mafs)

        self.textEdit_37.append(str(crmpn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(crfn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(cermsn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(cerfsn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(licemn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(licefn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(licemsn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(licefsn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(deplmn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(deplfn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(deplmsn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(bcmn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(bcfn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(bcmsn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(bcfsn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(mamn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(mafn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(mamsn))
        self.textEdit_37.append("")
        self.textEdit_37.append(str(mafsn))
        self.textEdit_37.append("")
        

    def district(self):
        
        em = totalmalepupils()
        emn = 'Total Male Students = '+str(em)
        ef = totalfemalepupils()
        efn = 'Total Female Students = '+str(ef)
        t = totalpupils()
        tn = 'Total Students = '+str(t)

        self.textEdit_3.append(str(emn))
        self.textEdit_3.append("")
        self.textEdit_3.append(str(efn))
        self.textEdit_3.append("")
        self.textEdit_3.append(str(tn))
        self.textEdit_3.append("")

        r1 = district_pupilclassroomratio()
        r1n = 'District Pupil Classroom ratio Ratio = '+ str(r1)
        r2 = districtpupilstanceratio()
        r2n = 'District Latrine Stance Ratio = '+str(r2)
        u = totaldesk()
        x = 1
        h = u+1
        c = t/h
        cn = 'District Student Desk ratio = ' + str(c)
        q = totalteachers()
        l = q+1
        w = t/l
        wn = 'District Student Teacher Ratio = ' + str(w)

        self.textEdit_4.append(str(r1n))
        self.textEdit_4.append("")
        self.textEdit_4.append(str(r2n))
        self.textEdit_4.append("")
        self.textEdit_4.append(str(cn))
        self.textEdit_4.append("")
        self.textEdit_4.append(str(wn))
        self.textEdit_4.append("")

        f = femaleteachers()
        fn = 'Total Female Teachers = ' + str(f)
        m = maleteachers()
        mn = 'Total Male Teachers = ' + str(m)
        z = totalteachers()
        zn = 'Total Number of Teachers = '+ str(z)
        cr = certificate()
        crn = 'Certificate Holders = '+ str(cr)
        dp = deploma()
        dpn = 'Deploma Holders = '+ str(dp)
        bac = bachelors()
        bacn = 'Bachelors Holders = ' + str(bac)
        ma = masters()
        man = "Masters and Above = '" + str(ma)

        self.textEdit_5.append(str(fn))
        self.textEdit_5.append("")
        self.textEdit_5.append(str(mn))
        self.textEdit_5.append("")
        self.textEdit_5.append(str(zn))
        self.textEdit_5.append("")
        self.textEdit_5.append(str(crn))
        self.textEdit_5.append("")
        self.textEdit_5.append(str(dpn))
        self.textEdit_5.append("")
        self.textEdit_5.append(str(bacn))
        self.textEdit_5.append("")
        self.textEdit_5.append(str(man))
        self.textEdit_5.append("")
        

    def adekokwok(self):
        x = "Adekokwok"
###################################### STUDENTS    
        a = totalmalep(x)
        m = totalmales(x)
        
        try:
            t = a + m
            an = 'Total Male Students = ' + str(t)
            self.textEdit_9.append(str(an))
            self.textEdit_9.append("")
            
        except Exception:
            an = 'Total Male Students = ' + str(0)
            self.textEdit_9.append(str(an))
            self.textEdit_9.append("")
            
        
        b = totalfemalep(x)
        o = totalfemales(x)
        
        try:
            q = b+o
            bn = 'Total Female Students = '+ str(q)
            self.textEdit_9.append(str(bn))
            self.textEdit_9.append("")
            
        except Exception:
            bn = 'Total Female Students = '+ str(0)
            self.textEdit_9.append(str(bn))
            self.textEdit_9.append("")
            
        try:
            c = t+q
            cn = 'Total Number of Students = '+ str(o)
            self.textEdit_9.append(str(cn))
            self.textEdit_9.append("")

        except Exception:
            cn = 'Total Number of Students = '+ str(0)
            self.textEdit_9.append(str(cn))
            self.textEdit_9.append("")
            
####################################### Ratios

        cl =classroompri(x)
        cls = classroomsec(x)

        try:
            clsf = cl+cls
            pls = b+o
            clr = pls/clsf
            clrn = "Student Classroom Ratio = "+str(clrn)
            self.textEdit_6.append(str(clrn))
            self.textEdit_6.append("")
            
        except Exception:
            clrn = "Student Classroom Ratio = "+str(0)
            self.textEdit_6.append(str(clrn))
            self.textEdit_6.append("")

        stpr = stancepri(x)
        stprs = stancesec(x)

        try:
            stu = b+o
            sn = stpr+stprs
            stanceratio = stu/sn
            stanceration = "Student Latrine Stance Ratio = "+str(stanceratio)
            self.textEdit_6.append(str(stanceration))
            self.textEdit_6.append("")

        except Exception:
            stanceration = "Student Latrine Stance Ratio = "+str(0)
            self.textEdit_6.append(stanceration)
            self.textEdit_6.append("")

        dr = deskpri(x)
        drp = desksec(x)

        try:
            stud = b+o
            dsk = dr+drp
            studdsk = stud/dsk
            studdskn = "Student Desk Ratio = "+ str(studdsk)
            self.textEdit_6.append(str(studdskn))
            self.textEdit_6.append("")

        except Exception:
            studdskn = "Student Desk Ratio = "+ str(0)
            self.textEdit_6.append(str(studdskn))
            self.textEdit_6.append("")

        tr =  teachpri(x)
        trs = teachsec(x)

        try:
            trn = tr + trs
            studn = b+o
            ratiot = studn/trn
            rationtr = "Student Teacher Ratio = "+ ratiot
            self.textEdit_6.append(str(rationtr))
            self.textEdit_6.append("")
            
        except Exception:
            rationtr = "Student Teacher Ratio = "+ str(0)
            self.textEdit_6.append(str(rationtr))
            self.textEdit_6.append("")

################################# TEACHERS

        crmp = certm(x)
        crfp = certf(x)
        cerms = certms(x)
        cerfs = certfs(x)

        try:
            cert = crmp+crfp+cerms+cerfs
            rationtr = "Certicate Holders = "+ str(cert)
            self.textEdit_8.append(str(rationtr))
            self.textEdit_8.append("")

        except Exception:
            rationtr = "Certificate Holder = "+ str(0)
            self.textEdit_8.append(str(rationtr))
            self.textEdit_8.append("")

        licem = licm(x)
        licef = licf(x)
        licems = licms(x)
        licefs = licfs(x)
        try:
            lice = licem+licef+licems+licefs
            licen = "Licenced Teachers" + str(lice)
            self.textEdit_8.append(str(licen))
            self.textEdit_8.append("")

        except Exception:
            licen = "Licenced Teachers" + str(0)
            self.textEdit_8.append(str(licen))
            self.textEdit_8.append("")
        
        deplm = depm(x)
        deplf = depf(x)
        deplms = depms(x)
        deplmf = depfs(x)

        try:
            dl = deplm+deplf+deplms+deplmf
            dln = "Deploma Holders =" + str(dl)
            self.textEdit_8.append(str(dln))
            self.textEdit_8.append("")

        except Exception:
            dln = "Deploma Holders = " + str(0)
            self.textEdit_8.append(str(dln))
            self.textEdit_8.append("")

        bcm = bacm(x)
        bcf = bacf(x)
        bcms = bacms(x)
        bcfs = bacfs(x)

        try:
            bc = bcm+bcf+bcms+bcfs
            bcn = "Bachelors Holders = " + str(bcn)
            self.textEdit_8.append(str(bcn))
            self.textEdit_8.append("")

        except Exception:
            bcn = "Bachelors Holders = " + str(0)
            self.textEdit_8.append(str(bcn))
            self.textEdit_8.append("")

        mam = masm(x)
        maf = masf(x)
        mams = masms(x)
        mafs = masfs(x)

        try:
            mas = mam+maf+mams+mafs
            masn = "Masters and Above = " + str(mas)
            self.textEdit_8.append(str(masn))
            self.textEdit_8.append("")

        except Exception:
            masn = "Masters and Above = " + str(0)
            self.textEdit_8.append(str(masn))
            self.textEdit_8.append("")

    def agali(self):
        x = "Agali"
    
        a = totalmalep(x)
        m = totalmales(x)
        
        try:
            t = a + m
            an = 'Total Male Students = ' + str(t)
            self.textEdit_12.append(str(an))
            self.textEdit_12.append("")
            
        except Exception:
            an = 'Total Male Students = ' + str(0)
            self.textEdit_12.append(str(an))
            self.textEdit_12.append("")
            
        
        b = totalfemalep(x)
        o = totalfemales(x)
        
        try:
            q = b+o
            bn = 'Total Female Students = '+ str(q)
            self.textEdit_12.append(str(bn))
            self.textEdit_12.append("")
            
        except Exception:
            bn = 'Total Female Students = '+ str(0)
            self.textEdit_12.append(str(bn))
            self.textEdit_12.append("")
            
        try:
            c = t+q
            cn = 'Total Number of Students = '+ str(o)
            self.textEdit_12.append(str(cn))
            self.textEdit_12.append("")

        except Exception:
            cn = 'Total Number of Students = '+ str(0)
            self.textEdit_12.append(str(cn))
            self.textEdit_12.append("")
            
####################################### Ratios

        cl =classroompri(x)
        cls = classroomsec(x)

        try:
            clsf = cl+cls
            pls = b+o
            clr = pls/clsf
            clrn = "Student Classroom Ratio = "+str(clrn)
            self.textEdit_11.append(str(clrn))
            self.textEdit_11.append("")
            
        except Exception:
            clrn = "Student Classroom Ratio = "+str(0)
            self.textEdit_11.append(str(clrn))
            self.textEdit_11.append("")

        stpr = stancepri(x)
        stprs = stancesec(x)

        try:
            stu = b+o
            sn = stpr+stprs
            stanceratio = stu/sn
            stanceration = "Student Latrine Stance Ratio = "+str(stanceratio)
            self.textEdit_11.append(str(stanceration))
            self.textEdit_11.append("")

        except Exception:
            stanceration = "Student Latrine Stance Ratio = "+str(0)
            self.textEdit_11.append(stanceration)
            self.textEdit_11.append("")

        dr = deskpri(x)
        drp = desksec(x)

        try:
            stud = b+o
            dsk = dr+drp
            studdsk = stud/dsk
            studdskn = "Student Desk Ratio = "+ str(studdsk)
            self.textEdit_11.append(str(studdskn))
            self.textEdit_11.append("")

        except Exception:
            studdskn = "Student Desk Ratio = "+ str(0)
            self.textEdit_11.append(str(studdskn))
            self.textEdit_11.append("")

        tr =  teachpri(x)
        trs = teachsec(x)

        try:
            trn = tr + trs
            studn = b+o
            ratiot = studn/trn
            rationtr = "Student Teacher Ratio = "+ ratiot
            self.textEdit_11.append(str(rationtr))
            self.textEdit_11.append("")
            
        except Exception:
            rationtr = "Student Teacher Ratio = "+ str(0)
            self.textEdit_11.append(str(rationtr))
            self.textEdit_11.append("")

################################# TEACHERS

        crmp = certm(x)
        crfp = certf(x)
        cerms = certms(x)
        cerfs = certfs(x)

        try:
            cert = crmp+crfp+cerms+cerfs
            rationtr = "Certicate Holders = "+ str(cert)
            self.textEdit_10.append(str(rationtr))
            self.textEdit_10.append("")

        except Exception:
            rationtr = "Certificate Holder = "+ str(0)
            self.textEdit_10.append(str(rationtr))
            self.textEdit_10.append("")

        licem = licm(x)
        licef = licf(x)
        licems = licms(x)
        licefs = licfs(x)
        try:
            lice = licem+licef+licems+licefs
            licen = "Licenced Teachers" + str(lice)
            self.textEdit_10.append(str(licen))
            self.textEdit_10.append("")

        except Exception:
            licen = "Licenced Teachers" + str(0)
            self.textEdit_10.append(str(licen))
            self.textEdit_10.append("")
        
        deplm = depm(x)
        deplf = depf(x)
        deplms = depms(x)
        deplmf = depfs(x)

        try:
            dl = deplm+deplf+deplms+deplmf
            dln = "Deploma Holders =" + str(dl)
            self.textEdit_10.append(str(dln))
            self.textEdit_10.append("")

        except Exception:
            dln = "Deploma Holders = " + str(0)
            self.textEdit_10.append(str(dln))
            self.textEdit_10.append("")

        bcm = bacm(x)
        bcf = bacf(x)
        bcms = bacms(x)
        bcfs = bacfs(x)

        try:
            bc = bcm+bcf+bcms+bcfs
            bcn = "Bachelors Holders = " + str(bcn)
            self.textEdit_10.append(str(bcn))
            self.textEdit_10.append("")

        except Exception:
            bcn = "Bachelors Holders = " + str(0)
            self.textEdit_10.append(str(bcn))
            self.textEdit_10.append("")

        mam = masm(x)
        maf = masf(x)
        mams = masms(x)
        mafs = masfs(x)

        try:
            mas = mam+maf+mams+mafs
            masn = "Masters and Above = " + str(mas)
            self.textEdit_10.append(str(masn))
            self.textEdit_10.append("")

        except Exception:
            masn = "Masters and Above = " + str(0)
            self.textEdit_10.append(str(masn))
            self.textEdit_10.append("")

    def adyel(self):
        x = "Adyel"
    
        a = totalmalep(x)
        m = totalmales(x)
        
        try:
            t = a + m
            an = 'Total Male Students = ' + str(t)
            self.textEdit_219.append(str(an))
            self.textEdit_219.append("")
            
        except Exception:
            an = 'Total Male Students = ' + str(0)
            self.textEdit_219.append(str(an))
            self.textEdit_219.append("")
            
        
        b = totalfemalep(x)
        o = totalfemales(x)
        
        try:
            q = b+o
            bn = 'Total Female Students = '+ str(q)
            self.textEdit_219.append(str(bn))
            self.textEdit_219.append("")
            
        except Exception:
            bn = 'Total Female Students = '+ str(0)
            self.textEdit_219.append(str(bn))
            self.textEdit_219.append("")
            
        try:
            c = t+q
            cn = 'Total Number of Students = '+ str(o)
            self.textEdit_219.append(str(cn))
            self.textEdit_219.append("")

        except Exception:
            cn = 'Total Number of Students = '+ str(0)
            self.textEdit_219.append(str(cn))
            self.textEdit_219.append("")
            
####################################### Ratios

        cl =classroompri(x)
        cls = classroomsec(x)

        try:
            clsf = cl+cls
            pls = b+o
            clr = pls/clsf
            clrn = "Student Classroom Ratio = "+str(clrn)
            self.textEdit_217.append(str(clrn))
            self.textEdit_217.append("")
            
        except Exception:
            clrn = "Student Classroom Ratio = "+str(0)
            self.textEdit_217.append(str(clrn))
            self.textEdit_217.append("")

        stpr = stancepri(x)
        stprs = stancesec(x)

        try:
            stu = b+o
            sn = stpr+stprs
            stanceratio = stu/sn
            stanceration = "Student Latrine Stance Ratio = "+str(stanceratio)
            self.textEdit_217.append(str(stanceration))
            self.textEdit_217.append("")

        except Exception:
            stanceration = "Student Latrine Stance Ratio = "+str(0)
            self.textEdit_217.append(stanceration)
            self.textEdit_217.append("")

        dr = deskpri(x)
        drp = desksec(x)

        try:
            stud = b+o
            dsk = dr+drp
            studdsk = stud/dsk
            studdskn = "Student Desk Ratio = "+ str(studdsk)
            self.textEdit_217.append(str(studdskn))
            self.textEdit_217.append("")

        except Exception:
            studdskn = "Student Desk Ratio = "+ str(0)
            self.textEdit_217.append(str(studdskn))
            self.textEdit_217.append("")

        tr =  teachpri(x)
        trs = teachsec(x)

        try:
            trn = tr + trs
            studn = b+o
            ratiot = studn/trn
            rationtr = "Student Teacher Ratio = "+ ratiot
            self.textEdit_217.append(str(rationtr))
            self.textEdit_217.append("")
            
        except Exception:
            rationtr = "Student Teacher Ratio = "+ str(0)
            self.textEdit_217.append(str(rationtr))
            self.textEdit_217.append("")

################################# TEACHERS

        crmp = certm(x)
        crfp = certf(x)
        cerms = certms(x)
        cerfs = certfs(x)

        try:
            cert = crmp+crfp+cerms+cerfs
            rationtr = "Certicate Holders = "+ str(cert)
            self.textEdit_218.append(str(rationtr))
            self.textEdit_218.append("")

        except Exception:
            rationtr = "Certificate Holder = "+ str(0)
            self.textEdit_218.append(str(rationtr))
            self.textEdit_218.append("")

        licem = licm(x)
        licef = licf(x)
        licems = licms(x)
        licefs = licfs(x)
        try:
            lice = licem+licef+licems+licefs
            licen = "Licenced Teachers" + str(lice)
            self.textEdit_218.append(str(licen))
            self.textEdit_218.append("")

        except Exception:
            licen = "Licenced Teachers" + str(0)
            self.textEdit_218.append(str(licen))
            self.textEdit_218.append("")
        
        deplm = depm(x)
        deplf = depf(x)
        deplms = depms(x)
        deplmf = depfs(x)

        try:
            dl = deplm+deplf+deplms+deplmf
            dln = "Deploma Holders =" + str(dl)
            self.textEdit_218.append(str(dln))
            self.textEdit_218.append("")

        except Exception:
            dln = "Deploma Holders = " + str(0)
            self.textEdit_218.append(str(dln))
            self.textEdit_218.append("")

        bcm = bacm(x)
        bcf = bacf(x)
        bcms = bacms(x)
        bcfs = bacfs(x)

        try:
            bc = bcm+bcf+bcms+bcfs
            bcn = "Bachelors Holders = " + str(bcn)
            self.textEdit_218.append(str(bcn))
            self.textEdit_218.append("")

        except Exception:
            bcn = "Bachelors Holders = " + str(0)
            self.textEdit_218.append(str(bcn))
            self.textEdit_218.append("")

        mam = masm(x)
        maf = masf(x)
        mams = masms(x)
        mafs = masfs(x)

        try:
            mas = mam+maf+mams+mafs
            masn = "Masters and Above = " + str(mas)
            self.textEdit_15.append(str(masn))
            self.textEdit_15.append("")

        except Exception:
            masn = "Masters and Above = " + str(0)
            self.textEdit_15.append(str(masn))
            self.textEdit_15.append("")

    def agweng(self):
        x = "Agweng"
    
        a = totalmalep(x)
        m = totalmales(x)
        
        try:
            t = a + m
            an = 'Total Male Students = ' + str(t)
            self.textEdit_15.append(str(an))
            self.textEdit_15.append("")
            
        except Exception:
            an = 'Total Male Students = ' + str(0)
            self.textEdit_15.append(str(an))
            self.textEdit_15.append("")
            
        
        b = totalfemalep(x)
        o = totalfemales(x)
        
        try:
            q = b+o
            bn = 'Total Female Students = '+ str(q)
            self.textEdit_15.append(str(bn))
            self.textEdit_15.append("")
            
        except Exception:
            bn = 'Total Female Students = '+ str(0)
            self.textEdit_15.append(str(bn))
            self.textEdit_15.append("")
            
        try:
            c = t+q
            cn = 'Total Number of Students = '+ str(o)
            self.textEdit_15.append(str(cn))
            self.textEdit_15.append("")

        except Exception:
            cn = 'Total Number of Students = '+ str(0)
            self.textEdit_15.append(str(cn))
            self.textEdit_15.append("")
            
####################################### Ratios

        cl =classroompri(x)
        cls = classroomsec(x)

        try:
            clsf = cl+cls
            pls = b+o
            clr = pls/clsf
            clrn = "Student Classroom Ratio = "+str(clrn)
            self.textEdit_14.append(str(clrn))
            self.textEdit_14.append("")
            
        except Exception:
            clrn = "Student Classroom Ratio = "+str(0)
            self.textEdit_14.append(str(clrn))
            self.textEdit_14.append("")

        stpr = stancepri(x)
        stprs = stancesec(x)

        try:
            stu = b+o
            sn = stpr+stprs
            stanceratio = stu/sn
            stanceration = "Student Latrine Stance Ratio = "+str(stanceratio)
            self.textEdit_14.append(str(stanceration))
            self.textEdit_14.append("")

        except Exception:
            stanceration = "Student Latrine Stance Ratio = "+str(0)
            self.textEdit_14.append(stanceration)
            self.textEdit_14.append("")

        dr = deskpri(x)
        drp = desksec(x)

        try:
            stud = b+o
            dsk = dr+drp
            studdsk = stud/dsk
            studdskn = "Student Desk Ratio = "+ str(studdsk)
            self.textEdit_14.append(str(studdskn))
            self.textEdit_14.append("")

        except Exception:
            studdskn = "Student Desk Ratio = "+ str(0)
            self.textEdit_14.append(str(studdskn))
            self.textEdit_14.append("")

        tr =  teachpri(x)
        trs = teachsec(x)

        try:
            trn = tr + trs
            studn = b+o
            ratiot = studn/trn
            rationtr = "Student Teacher Ratio = "+ ratiot
            self.textEdit_14.append(str(rationtr))
            self.textEdit_14.append("")
            
        except Exception:
            rationtr = "Student Teacher Ratio = "+ str(0)
            self.textEdit_14.append(str(rationtr))
            self.textEdit_14.append("")

################################# TEACHERS

        crmp = certm(x)
        crfp = certf(x)
        cerms = certms(x)
        cerfs = certfs(x)

        try:
            cert = crmp+crfp+cerms+cerfs
            rationtr = "Certicate Holders = "+ str(cert)
            self.textEdit_13.append(str(rationtr))
            self.textEdit_13.append("")

        except Exception:
            rationtr = "Certificate Holder = "+ str(0)
            self.textEdit_13.append(str(rationtr))
            self.textEdit_13.append("")

        licem = licm(x)
        licef = licf(x)
        licems = licms(x)
        licefs = licfs(x)
        try:
            lice = licem+licef+licems+licefs
            licen = "Licenced Teachers" + str(lice)
            self.textEdit_13.append(str(licen))
            self.textEdit_13.append("")

        except Exception:
            licen = "Licenced Teachers" + str(0)
            self.textEdit_13.append(str(licen))
            self.textEdit_13.append("")
        
        deplm = depm(x)
        deplf = depf(x)
        deplms = depms(x)
        deplmf = depfs(x)

        try:
            dl = deplm+deplf+deplms+deplmf
            dln = "Deploma Holders =" + str(dl)
            self.textEdit_13.append(str(dln))
            self.textEdit_13.append("")

        except Exception:
            dln = "Deploma Holders = " + str(0)
            self.textEdit_13.append(str(dln))
            self.textEdit_13.append("")

        bcm = bacm(x)
        bcf = bacf(x)
        bcms = bacms(x)
        bcfs = bacfs(x)

        try:
            bc = bcm+bcf+bcms+bcfs
            bcn = "Bachelors Holders = " + str(bcn)
            self.textEdit_13.append(str(bcn))
            self.textEdit_13.append("")

        except Exception:
            bcn = "Bachelors Holders = " + str(0)
            self.textEdit_13.append(str(bcn))
            self.textEdit_13.append("")

        mam = masm(x)
        maf = masf(x)
        mams = masms(x)
        mafs = masfs(x)

        try:
            mas = mam+maf+mams+mafs
            masn = "Masters and Above = " + str(mas)
            self.textEdit_13.append(str(masn))
            self.textEdit_13.append("")

        except Exception:
            masn = "Masters and Above = " + str(0)
            self.textEdit_13.append(str(masn))
            self.textEdit_13.append("")

##################################################            

    def amach(self):
        x = "Amach"
    
        a = totalmalep(x)
        m = totalmales(x)
        
        try:
            t = a + m
            an = 'Total Male Students = ' + str(t)
            self.textEdit_18.append(str(an))
            self.textEdit_18.append("")
            
        except Exception:
            an = 'Total Male Students = ' + str(0)
            self.textEdit_18.append(str(an))
            self.textEdit_18.append("")
            
        
        b = totalfemalep(x)
        o = totalfemales(x)
        
        try:
            q = b+o
            bn = 'Total Female Students = '+ str(q)
            self.textEdit_18.append(str(bn))
            self.textEdit_18.append("")
            
        except Exception:
            bn = 'Total Female Students = '+ str(0)
            self.textEdit_18.append(str(bn))
            self.textEdit_18.append("")
            
        try:
            c = t+q
            cn = 'Total Number of Students = '+ str(o)
            self.textEdit_18.append(str(cn))
            self.textEdit_18.append("")

        except Exception:
            cn = 'Total Number of Students = '+ str(0)
            self.textEdit_18.append(str(cn))
            self.textEdit_18.append("")
            
####################################### Ratios

        cl =classroompri(x)
        cls = classroomsec(x)

        try:
            clsf = cl+cls
            pls = b+o
            clr = pls/clsf
            clrn = "Student Classroom Ratio = "+str(clrn)
            self.textEdit_17.append(str(clrn))
            self.textEdit_17.append("")
            
        except Exception:
            clrn = "Student Classroom Ratio = "+str(0)
            self.textEdit_17.append(str(clrn))
            self.textEdit_17.append("")

        stpr = stancepri(x)
        stprs = stancesec(x)

        try:
            stu = b+o
            sn = stpr+stprs
            stanceratio = stu/sn
            stanceration = "Student Latrine Stance Ratio = "+str(stanceratio)
            self.textEdit_17.append(str(stanceration))
            self.textEdit_17.append("")

        except Exception:
            stanceration = "Student Latrine Stance Ratio = "+str(0)
            self.textEdit_17.append(stanceration)
            self.textEdit_17.append("")

        dr = deskpri(x)
        drp = desksec(x)

        try:
            stud = b+o
            dsk = dr+drp
            studdsk = stud/dsk
            studdskn = "Student Desk Ratio = "+ str(studdsk)
            self.textEdit_17.append(str(studdskn))
            self.textEdit_17.append("")

        except Exception:
            studdskn = "Student Desk Ratio = "+ str(0)
            self.textEdit_17.append(str(studdskn))
            self.textEdit_17.append("")

        tr =  teachpri(x)
        trs = teachsec(x)

        try:
            trn = tr + trs
            studn = b+o
            ratiot = studn/trn
            rationtr = "Student Teacher Ratio = "+ ratiot
            self.textEdit_17.append(str(rationtr))
            self.textEdit_17.append("")
            
        except Exception:
            rationtr = "Student Teacher Ratio = "+ str(0)
            self.textEdit_17.append(str(rationtr))
            self.textEdit_17.append("")

################################# TEACHERS

        crmp = certm(x)
        crfp = certf(x)
        cerms = certms(x)
        cerfs = certfs(x)

        try:
            cert = crmp+crfp+cerms+cerfs
            rationtr = "Certicate Holders = "+ str(cert)
            self.textEdit_16.append(str(rationtr))
            self.textEdit_16.append("")

        except Exception:
            rationtr = "Certificate Holder = "+ str(0)
            self.textEdit_16.append(str(rationtr))
            self.textEdit_16.append("")

        licem = licm(x)
        licef = licf(x)
        licems = licms(x)
        licefs = licfs(x)
        try:
            lice = licem+licef+licems+licefs
            licen = "Licenced Teachers" + str(lice)
            self.textEdit_16.append(str(licen))
            self.textEdit_16.append("")

        except Exception:
            licen = "Licenced Teachers" + str(0)
            self.textEdit_16.append(str(licen))
            self.textEdit_16.append("")
        
        deplm = depm(x)
        deplf = depf(x)
        deplms = depms(x)
        deplmf = depfs(x)

        try:
            dl = deplm+deplf+deplms+deplmf
            dln = "Deploma Holders =" + str(dl)
            self.textEdit_16.append(str(dln))
            self.textEdit_16.append("")

        except Exception:
            dln = "Deploma Holders = " + str(0)
            self.textEdit_16.append(str(dln))
            self.textEdit_16.append("")

        bcm = bacm(x)
        bcf = bacf(x)
        bcms = bacms(x)
        bcfs = bacfs(x)

        try:
            bc = bcm+bcf+bcms+bcfs
            bcn = "Bachelors Holders = " + str(bcn)
            self.textEdit_16.append(str(bcn))
            self.textEdit_16.append("")

        except Exception:
            bcn = "Bachelors Holders = " + str(0)
            self.textEdit_16.append(str(bcn))
            self.textEdit_16.append("")

        mam = masm(x)
        maf = masf(x)
        mams = masms(x)
        mafs = masfs(x)

        try:
            mas = mam+maf+mams+mafs
            masn = "Masters and Above = " + str(mas)
            self.textEdit_16.append(str(masn))
            self.textEdit_16.append("")

        except Exception:
            masn = "Masters and Above = " + str(0)
            self.textEdit_16.append(str(masn))
            self.textEdit_16.append("")

##################################################            

    def aromo(self):
        x = "Aromo"
    
        a = totalmalep(x)
        m = totalmales(x)
        
        try:
            t = a + m
            an = 'Total Male Students = ' + str(t)
            self.textEdit_21.append(str(an))
            self.textEdit_21.append("")
            
        except Exception:
            an = 'Total Male Students = ' + str(0)
            self.textEdit_21.append(str(an))
            self.textEdit_21.append("")
            
        
        b = totalfemalep(x)
        o = totalfemales(x)
        
        try:
            q = b+o
            bn = 'Total Female Students = '+ str(q)
            self.textEdit_21.append(str(bn))
            self.textEdit_21.append("")
            
        except Exception:
            bn = 'Total Female Students = '+ str(0)
            self.textEdit_21.append(str(bn))
            self.textEdit_21.append("")
            
        try:
            c = t+q
            cn = 'Total Number of Students = '+ str(o)
            self.textEdit_21.append(str(cn))
            self.textEdit_21.append("")

        except Exception:
            cn = 'Total Number of Students = '+ str(0)
            self.textEdit_21.append(str(cn))
            self.textEdit_21.append("")
            
####################################### Ratios

        cl =classroompri(x)
        cls = classroomsec(x)

        try:
            clsf = cl+cls
            pls = b+o
            clr = pls/clsf
            clrn = "Student Classroom Ratio = "+str(clrn)
            self.textEdit_20.append(str(clrn))
            self.textEdit_20.append("")
            
        except Exception:
            clrn = "Student Classroom Ratio = "+str(0)
            self.textEdit_20.append(str(clrn))
            self.textEdit_20.append("")

        stpr = stancepri(x)
        stprs = stancesec(x)

        try:
            stu = b+o
            sn = stpr+stprs
            stanceratio = stu/sn
            stanceration = "Student Latrine Stance Ratio = "+str(stanceratio)
            self.textEdit_20.append(str(stanceration))
            self.textEdit_20.append("")

        except Exception:
            stanceration = "Student Latrine Stance Ratio = "+str(0)
            self.textEdit_20.append(stanceration)
            self.textEdit_20.append("")

        dr = deskpri(x)
        drp = desksec(x)

        try:
            stud = b+o
            dsk = dr+drp
            studdsk = stud/dsk
            studdskn = "Student Desk Ratio = "+ str(studdsk)
            self.textEdit_20.append(str(studdskn))
            self.textEdit_20.append("")

        except Exception:
            studdskn = "Student Desk Ratio = "+ str(0)
            self.textEdit_20.append(str(studdskn))
            self.textEdit_20.append("")

        tr =  teachpri(x)
        trs = teachsec(x)

        try:
            trn = tr + trs
            studn = b+o
            ratiot = studn/trn
            rationtr = "Student Teacher Ratio = "+ ratiot
            self.textEdit_20.append(str(rationtr))
            self.textEdit_20.append("")
            
        except Exception:
            rationtr = "Student Teacher Ratio = "+ str(0)
            self.textEdit_20.append(str(rationtr))
            self.textEdit_20.append("")

################################# TEACHERS

        crmp = certm(x)
        crfp = certf(x)
        cerms = certms(x)
        cerfs = certfs(x)

        try:
            cert = crmp+crfp+cerms+cerfs
            rationtr = "Certicate Holders = "+ str(cert)
            self.textEdit_19.append(str(rationtr))
            self.textEdit_19.append("")

        except Exception:
            rationtr = "Certificate Holder = "+ str(0)
            self.textEdit_19.append(str(rationtr))
            self.textEdit_19.append("")

        licem = licm(x)
        licef = licf(x)
        licems = licms(x)
        licefs = licfs(x)
        try:
            lice = licem+licef+licems+licefs
            licen = "Licenced Teachers" + str(lice)
            self.textEdit_19.append(str(licen))
            self.textEdit_19.append("")

        except Exception:
            licen = "Licenced Teachers" + str(0)
            self.textEdit_19.append(str(licen))
            self.textEdit_19.append("")
        
        deplm = depm(x)
        deplf = depf(x)
        deplms = depms(x)
        deplmf = depfs(x)

        try:
            dl = deplm+deplf+deplms+deplmf
            dln = "Deploma Holders =" + str(dl)
            self.textEdit_19.append(str(dln))
            self.textEdit_19.append("")

        except Exception:
            dln = "Deploma Holders = " + str(0)
            self.textEdit_19.append(str(dln))
            self.textEdit_19.append("")

        bcm = bacm(x)
        bcf = bacf(x)
        bcms = bacms(x)
        bcfs = bacfs(x)

        try:
            bc = bcm+bcf+bcms+bcfs
            bcn = "Bachelors Holders = " + str(bcn)
            self.textEdit_19.append(str(bcn))
            self.textEdit_19.append("")

        except Exception:
            bcn = "Bachelors Holders = " + str(0)
            self.textEdit_19.append(str(bcn))
            self.textEdit_19.append("")

        mam = masm(x)
        maf = masf(x)
        mams = masms(x)
        mafs = masfs(x)

        try:
            mas = mam+maf+mams+mafs
            masn = "Masters and Above = " + str(mas)
            self.textEdit_19.append(str(masn))
            self.textEdit_19.append("")

        except Exception:
            masn = "Masters and Above = " + str(0)
            self.textEdit_19.append(str(masn))
            self.textEdit_19.append("")

##################################################            

    def barr(self):
        x = "Barr"
    
        a = totalmalep(x)
        m = totalmales(x)
        
        try:
            t = a + m
            an = 'Total Male Students = ' + str(t)
            self.textEdit_24.append(str(an))
            self.textEdit_24.append("")
            
        except Exception:
            an = 'Total Male Students = ' + str(0)
            self.textEdit_24.append(str(an))
            self.textEdit_24.append("")
            
        
        b = totalfemalep(x)
        o = totalfemales(x)
        
        try:
            q = b+o
            bn = 'Total Female Students = '+ str(q)
            self.textEdit_24.append(str(bn))
            self.textEdit_24.append("")
            
        except Exception:
            bn = 'Total Female Students = '+ str(0)
            self.textEdit_24.append(str(bn))
            self.textEdit_24.append("")
            
        try:
            c = t+q
            cn = 'Total Number of Students = '+ str(o)
            self.textEdit_24.append(str(cn))
            self.textEdit_24.append("")

        except Exception:
            cn = 'Total Number of Students = '+ str(0)
            self.textEdit_24.append(str(cn))
            self.textEdit_24.append("")
            
####################################### Ratios

        cl =classroompri(x)
        cls = classroomsec(x)

        try:
            clsf = cl+cls
            pls = b+o
            clr = pls/clsf
            clrn = "Student Classroom Ratio = "+str(clrn)
            self.textEdit_23.append(str(clrn))
            self.textEdit_23.append("")
            
        except Exception:
            clrn = "Student Classroom Ratio = "+str(0)
            self.textEdit_23.append(str(clrn))
            self.textEdit_23.append("")

        stpr = stancepri(x)
        stprs = stancesec(x)

        try:
            stu = b+o
            sn = stpr+stprs
            stanceratio = stu/sn
            stanceration = "Student Latrine Stance Ratio = "+str(stanceratio)
            self.textEdit_23.append(str(stanceration))
            self.textEdit_23.append("")

        except Exception:
            stanceration = "Student Latrine Stance Ratio = "+str(0)
            self.textEdit_23.append(stanceration)
            self.textEdit_23.append("")

        dr = deskpri(x)
        drp = desksec(x)

        try:
            stud = b+o
            dsk = dr+drp
            studdsk = stud/dsk
            studdskn = "Student Desk Ratio = "+ str(studdsk)
            self.textEdit_23.append(str(studdskn))
            self.textEdit_23.append("")

        except Exception:
            studdskn = "Student Desk Ratio = "+ str(0)
            self.textEdit_23.append(str(studdskn))
            self.textEdit_23.append("")

        tr =  teachpri(x)
        trs = teachsec(x)

        try:
            trn = tr + trs
            studn = b+o
            ratiot = studn/trn
            rationtr = "Student Teacher Ratio = "+ ratiot
            self.textEdit_23.append(str(rationtr))
            self.textEdit_23.append("")
            
        except Exception:
            rationtr = "Student Teacher Ratio = "+ str(0)
            self.textEdit_23.append(str(rationtr))
            self.textEdit_23.append("")

################################# TEACHERS

        crmp = certm(x)
        crfp = certf(x)
        cerms = certms(x)
        cerfs = certfs(x)

        try:
            cert = crmp+crfp+cerms+cerfs
            rationtr = "Certicate Holders = "+ str(cert)
            self.textEdit_22.append(str(rationtr))
            self.textEdit_22.append("")

        except Exception:
            rationtr = "Certificate Holder = "+ str(0)
            self.textEdit_22.append(str(rationtr))
            self.textEdit_22.append("")

        licem = licm(x)
        licef = licf(x)
        licems = licms(x)
        licefs = licfs(x)
        try:
            lice = licem+licef+licems+licefs
            licen = "Licenced Teachers" + str(lice)
            self.textEdit_22.append(str(licen))
            self.textEdit_22.append("")

        except Exception:
            licen = "Licenced Teachers" + str(0)
            self.textEdit_22.append(str(licen))
            self.textEdit_22.append("")
        
        deplm = depm(x)
        deplf = depf(x)
        deplms = depms(x)
        deplmf = depfs(x)

        try:
            dl = deplm+deplf+deplms+deplmf
            dln = "Deploma Holders =" + str(dl)
            self.textEdit_22.append(str(dln))
            self.textEdit_22.append("")

        except Exception:
            dln = "Deploma Holders = " + str(0)
            self.textEdit_22.append(str(dln))
            self.textEdit_22.append("")

        bcm = bacm(x)
        bcf = bacf(x)
        bcms = bacms(x)
        bcfs = bacfs(x)

        try:
            bc = bcm+bcf+bcms+bcfs
            bcn = "Bachelors Holders = " + str(bcn)
            self.textEdit_22.append(str(bcn))
            self.textEdit_22.append("")

        except Exception:
            bcn = "Bachelors Holders = " + str(0)
            self.textEdit_22.append(str(bcn))
            self.textEdit_22.append("")

        mam = masm(x)
        maf = masf(x)
        mams = masms(x)
        mafs = masfs(x)

        try:
            mas = mam+maf+mams+mafs
            masn = "Masters and Above = " + str(mas)
            self.textEdit_22.append(str(masn))
            self.textEdit_22.append("")

        except Exception:
            masn = "Masters and Above = " + str(0)
            self.textEdit_22.append(str(masn))
            self.textEdit_22.append("")

##################################################            

    def lira(self):
        x = "Lira"
    
        a = totalmalep(x)
        m = totalmales(x)
        
        try:
            t = a + m
            an = 'Total Male Students = ' + str(t)
            self.textEdit_27.append(str(an))
            self.textEdit_27.append("")
            
        except Exception:
            an = 'Total Male Students = ' + str(0)
            self.textEdit_27.append(str(an))
            self.textEdit_27.append("")
            
        
        b = totalfemalep(x)
        o = totalfemales(x)
        
        try:
            q = b+o
            bn = 'Total Female Students = '+ str(q)
            self.textEdit_27.append(str(bn))
            self.textEdit_27.append("")
            
        except Exception:
            bn = 'Total Female Students = '+ str(0)
            self.textEdit_27.append(str(bn))
            self.textEdit_27.append("")
            
        try:
            c = t+q
            cn = 'Total Number of Students = '+ str(o)
            self.textEdit_27.append(str(cn))
            self.textEdit_27.append("")

        except Exception:
            cn = 'Total Number of Students = '+ str(0)
            self.textEdit_27.append(str(cn))
            self.textEdit_27.append("")
            
####################################### Ratios

        cl =classroompri(x)
        cls = classroomsec(x)

        try:
            clsf = cl+cls
            pls = b+o
            clr = pls/clsf
            clrn = "Student Classroom Ratio = "+str(clrn)
            self.textEdit_26.append(str(clrn))
            self.textEdit_26.append("")
            
        except Exception:
            clrn = "Student Classroom Ratio = "+str(0)
            self.textEdit_26.append(str(clrn))
            self.textEdit_26.append("")

        stpr = stancepri(x)
        stprs = stancesec(x)

        try:
            stu = b+o
            sn = stpr+stprs
            stanceratio = stu/sn
            stanceration = "Student Latrine Stance Ratio = "+str(stanceratio)
            self.textEdit_26.append(str(stanceration))
            self.textEdit_26.append("")

        except Exception:
            stanceration = "Student Latrine Stance Ratio = "+str(0)
            self.textEdit_26.append(stanceration)
            self.textEdit_26.append("")

        dr = deskpri(x)
        drp = desksec(x)

        try:
            stud = b+o
            dsk = dr+drp
            studdsk = stud/dsk
            studdskn = "Student Desk Ratio = "+ str(studdsk)
            self.textEdit_26.append(str(studdskn))
            self.textEdit_26.append("")

        except Exception:
            studdskn = "Student Desk Ratio = "+ str(0)
            self.textEdit_26.append(str(studdskn))
            self.textEdit_26.append("")

        tr =  teachpri(x)
        trs = teachsec(x)

        try:
            trn = tr + trs
            studn = b+o
            ratiot = studn/trn
            rationtr = "Student Teacher Ratio = "+ ratiot
            self.textEdit_26.append(str(rationtr))
            self.textEdit_26.append("")
            
        except Exception:
            rationtr = "Student Teacher Ratio = "+ str(0)
            self.textEdit_26.append(str(rationtr))
            self.textEdit_26.append("")

################################# TEACHERS

        crmp = certm(x)
        crfp = certf(x)
        cerms = certms(x)
        cerfs = certfs(x)

        try:
            cert = crmp+crfp+cerms+cerfs
            rationtr = "Certicate Holders = "+ str(cert)
            self.textEdit_25.append(str(rationtr))
            self.textEdit_25.append("")

        except Exception:
            rationtr = "Certificate Holder = "+ str(0)
            self.textEdit_25.append(str(rationtr))
            self.textEdit_25.append("")

        licem = licm(x)
        licef = licf(x)
        licems = licms(x)
        licefs = licfs(x)
        try:
            lice = licem+licef+licems+licefs
            licen = "Licenced Teachers" + str(lice)
            self.textEdit_25.append(str(licen))
            self.textEdit_25.append("")

        except Exception:
            licen = "Licenced Teachers" + str(0)
            self.textEdit_25.append(str(licen))
            self.textEdit_25.append("")
        
        deplm = depm(x)
        deplf = depf(x)
        deplms = depms(x)
        deplmf = depfs(x)

        try:
            dl = deplm+deplf+deplms+deplmf
            dln = "Deploma Holders =" + str(dl)
            self.textEdit_25.append(str(dln))
            self.textEdit_25.append("")

        except Exception:
            dln = "Deploma Holders = " + str(0)
            self.textEdit_25.append(str(dln))
            self.textEdit_25.append("")

        bcm = bacm(x)
        bcf = bacf(x)
        bcms = bacms(x)
        bcfs = bacfs(x)

        try:
            bc = bcm+bcf+bcms+bcfs
            bcn = "Bachelors Holders = " + str(bcn)
            self.textEdit_25.append(str(bcn))
            self.textEdit_25.append("")

        except Exception:
            bcn = "Bachelors Holders = " + str(0)
            self.textEdit_25.append(str(bcn))
            self.textEdit_25.append("")

        mam = masm(x)
        maf = masf(x)
        mams = masms(x)
        mafs = masfs(x)

        try:
            mas = mam+maf+mams+mafs
            masn = "Masters and Above = " + str(mas)
            self.textEdit_25.append(str(masn))
            self.textEdit_25.append("")

        except Exception:
            masn = "Masters and Above = " + str(0)
            self.textEdit_25.append(str(masn))
            self.textEdit_25.append("")
        
############################################################

    def ngetta(self):
        x = "Ngetta"
    
        a = totalmalep(x)
        m = totalmales(x)
        
        try:
            t = a + m
            an = 'Total Male Students = ' + str(t)
            self.textEdit_30.append(str(an))
            self.textEdit_30.append("")
            
        except Exception:
            an = 'Total Male Students = ' + str(0)
            self.textEdit_30.append(str(an))
            self.textEdit_30.append("")
            
        
        b = totalfemalep(x)
        o = totalfemales(x)
        
        try:
            q = b+o
            bn = 'Total Female Students = '+ str(q)
            self.textEdit_30.append(str(bn))
            self.textEdit_30.append("")
            
        except Exception:
            bn = 'Total Female Students = '+ str(0)
            self.textEdit_30.append(str(bn))
            self.textEdit_30.append("")
            
        try:
            c = t+q
            cn = 'Total Number of Students = '+ str(o)
            self.textEdit_30.append(str(cn))
            self.textEdit_30.append("")

        except Exception:
            cn = 'Total Number of Students = '+ str(0)
            self.textEdit_30.append(str(cn))
            self.textEdit_30.append("")
            
####################################### Ratios

        cl =classroompri(x)
        cls = classroomsec(x)

        try:
            clsf = cl+cls
            pls = b+o
            clr = pls/clsf
            clrn = "Student Classroom Ratio = "+str(clrn)
            self.textEdit_29.append(str(clrn))
            self.textEdit_29.append("")
            
        except Exception:
            clrn = "Student Classroom Ratio = "+str(0)
            self.textEdit_29.append(str(clrn))
            self.textEdit_29.append("")

        stpr = stancepri(x)
        stprs = stancesec(x)

        try:
            stu = b+o
            sn = stpr+stprs
            stanceratio = stu/sn
            stanceration = "Student Latrine Stance Ratio = "+str(stanceratio)
            self.textEdit_29.append(str(stanceration))
            self.textEdit_29.append("")

        except Exception:
            stanceration = "Student Latrine Stance Ratio = "+str(0)
            self.textEdit_29.append(stanceration)
            self.textEdit_29.append("")

        dr = deskpri(x)
        drp = desksec(x)

        try:
            stud = b+o
            dsk = dr+drp
            studdsk = stud/dsk
            studdskn = "Student Desk Ratio = "+ str(studdsk)
            self.textEdit_29.append(str(studdskn))
            self.textEdit_29.append("")

        except Exception:
            studdskn = "Student Desk Ratio = "+ str(0)
            self.textEdit_29.append(str(studdskn))
            self.textEdit_29.append("")

        tr =  teachpri(x)
        trs = teachsec(x)

        try:
            trn = tr + trs
            studn = b+o
            ratiot = studn/trn
            rationtr = "Student Teacher Ratio = "+ ratiot
            self.textEdit_29.append(str(rationtr))
            self.textEdit_29.append("")
            
        except Exception:
            rationtr = "Student Teacher Ratio = "+ str(0)
            self.textEdit_29.append(str(rationtr))
            self.textEdit_29.append("")

################################# TEACHERS

        crmp = certm(x)
        crfp = certf(x)
        cerms = certms(x)
        cerfs = certfs(x)

        try:
            cert = crmp+crfp+cerms+cerfs
            rationtr = "Certicate Holders = "+ str(cert)
            self.textEdit_28.append(str(rationtr))
            self.textEdit_28.append("")

        except Exception:
            rationtr = "Certificate Holder = "+ str(0)
            self.textEdit_28.append(str(rationtr))
            self.textEdit_28.append("")

        licem = licm(x)
        licef = licf(x)
        licems = licms(x)
        licefs = licfs(x)
        try:
            lice = licem+licef+licems+licefs
            licen = "Licenced Teachers" + str(lice)
            self.textEdit_28.append(str(licen))
            self.textEdit_28.append("")

        except Exception:
            licen = "Licenced Teachers" + str(0)
            self.textEdit_28.append(str(licen))
            self.textEdit_28.append("")
        
        deplm = depm(x)
        deplf = depf(x)
        deplms = depms(x)
        deplmf = depfs(x)

        try:
            dl = deplm+deplf+deplms+deplmf
            dln = "Deploma Holders =" + str(dl)
            self.textEdit_28.append(str(dln))
            self.textEdit_28.append("")

        except Exception:
            dln = "Deploma Holders = " + str(0)
            self.textEdit_28.append(str(dln))
            self.textEdit_28.append("")

        bcm = bacm(x)
        bcf = bacf(x)
        bcms = bacms(x)
        bcfs = bacfs(x)

        try:
            bc = bcm+bcf+bcms+bcfs
            bcn = "Bachelors Holders = " + str(bcn)
            self.textEdit_28.append(str(bcn))
            self.textEdit_28.append("")

        except Exception:
            bcn = "Bachelors Holders = " + str(0)
            self.textEdit_28.append(str(bcn))
            self.textEdit_28.append("")

        mam = masm(x)
        maf = masf(x)
        mams = masms(x)
        mafs = masfs(x)

        try:
            mas = mam+maf+mams+mafs
            masn = "Masters and Above = " + str(mas)
            self.textEdit_28.append(str(masn))
            self.textEdit_28.append("")

        except Exception:
            masn = "Masters and Above = " + str(0)
            self.textEdit_28.append(str(masn))
            self.textEdit_28.append("")

############################################################

    def ogur(self):
        x = "Ogur"
    
        a = totalmalep(x)
        m = totalmales(x)
        
        try:
            t = a + m
            an = 'Total Male Students = ' + str(t)
            self.textEdit_33.append(str(an))
            self.textEdit_33.append("")
            
        except Exception:
            an = 'Total Male Students = ' + str(0)
            self.textEdit_33.append(str(an))
            self.textEdit_33.append("")
            
        
        b = totalfemalep(x)
        o = totalfemales(x)
        
        try:
            q = b+o
            bn = 'Total Female Students = '+ str(q)
            self.textEdit_33.append(str(bn))
            self.textEdit_33.append("")
            
        except Exception:
            bn = 'Total Female Students = '+ str(0)
            self.textEdit_33.append(str(bn))
            self.textEdit_33.append("")
            
        try:
            c = t+q
            cn = 'Total Number of Students = '+ str(o)
            self.textEdit_33.append(str(cn))
            self.textEdit_33.append("")

        except Exception:
            cn = 'Total Number of Students = '+ str(0)
            self.textEdit_33.append(str(cn))
            self.textEdit_33.append("")
            
####################################### Ratios

        cl =classroompri(x)
        cls = classroomsec(x)

        try:
            clsf = cl+cls
            pls = b+o
            clr = pls/clsf
            clrn = "Student Classroom Ratio = "+str(clrn)
            self.textEdit_32.append(str(clrn))
            self.textEdit_32.append("")
            
        except Exception:
            clrn = "Student Classroom Ratio = "+str(0)
            self.textEdit_32.append(str(clrn))
            self.textEdit_32.append("")

        stpr = stancepri(x)
        stprs = stancesec(x)

        try:
            stu = b+o
            sn = stpr+stprs
            stanceratio = stu/sn
            stanceration = "Student Latrine Stance Ratio = "+str(stanceratio)
            self.textEdit_32.append(str(stanceration))
            self.textEdit_32.append("")

        except Exception:
            stanceration = "Student Latrine Stance Ratio = "+str(0)
            self.textEdit_32.append(stanceration)
            self.textEdit_32.append("")

        dr = deskpri(x)
        drp = desksec(x)

        try:
            stud = b+o
            dsk = dr+drp
            studdsk = stud/dsk
            studdskn = "Student Desk Ratio = "+ str(studdsk)
            self.textEdit_32.append(str(studdskn))
            self.textEdit_32.append("")

        except Exception:
            studdskn = "Student Desk Ratio = "+ str(0)
            self.textEdit_32.append(str(studdskn))
            self.textEdit_32.append("")

        tr =  teachpri(x)
        trs = teachsec(x)

        try:
            trn = tr + trs
            studn = b+o
            ratiot = studn/trn
            rationtr = "Student Teacher Ratio = "+ ratiot
            self.textEdit_32.append(str(rationtr))
            self.textEdit_32.append("")
            
        except Exception:
            rationtr = "Student Teacher Ratio = "+ str(0)
            self.textEdit_32.append(str(rationtr))
            self.textEdit_32.append("")

################################# TEACHERS

        crmp = certm(x)
        crfp = certf(x)
        cerms = certms(x)
        cerfs = certfs(x)

        try:
            cert = crmp+crfp+cerms+cerfs
            rationtr = "Certicate Holders = "+ str(cert)
            self.textEdit_31.append(str(rationtr))
            self.textEdit_31.append("")

        except Exception:
            rationtr = "Certificate Holder = "+ str(0)
            self.textEdit_31.append(str(rationtr))
            self.textEdit_31.append("")

        licem = licm(x)
        licef = licf(x)
        licems = licms(x)
        licefs = licfs(x)
        try:
            lice = licem+licef+licems+licefs
            licen = "Licenced Teachers" + str(lice)
            self.textEdit_31.append(str(licen))
            self.textEdit_31.append("")

        except Exception:
            licen = "Licenced Teachers" + str(0)
            self.textEdit_31.append(str(licen))
            self.textEdit_31.append("")
        
        deplm = depm(x)
        deplf = depf(x)
        deplms = depms(x)
        deplmf = depfs(x)

        try:
            dl = deplm+deplf+deplms+deplmf
            dln = "Deploma Holders =" + str(dl)
            self.textEdit_31.append(str(dln))
            self.textEdit_31.append("")

        except Exception:
            dln = "Deploma Holders = " + str(0)
            self.textEdit_31.append(str(dln))
            self.textEdit_31.append("")

        bcm = bacm(x)
        bcf = bacf(x)
        bcms = bacms(x)
        bcfs = bacfs(x)

        try:
            bc = bcm+bcf+bcms+bcfs
            bcn = "Bachelors Holders = " + str(bcn)
            self.textEdit_31.append(str(bcn))
            self.textEdit_31.append("")

        except Exception:
            bcn = "Bachelors Holders = " + str(0)
            self.textEdit_31.append(str(bcn))
            self.textEdit_31.append("")

        mam = masm(x)
        maf = masf(x)
        mams = masms(x)
        mafs = masfs(x)

        try:
            mas = mam+maf+mams+mafs
            masn = "Masters and Above = " + str(mas)
            self.textEdit_31.append(str(masn))
            self.textEdit_31.append("")

        except Exception:
            masn = "Masters and Above = " + str(0)
            self.textEdit_31.append(str(masn))
            self.textEdit_31.append("")

############################################################

    def ojwina(self):
        x = "Ojwina"
    
        a = totalmalep(x)
        m = totalmales(x)
        
        try:
            t = a + m
            an = 'Total Male Students = ' + str(t)
            self.textEdit_222.append(str(an))
            self.textEdit_222.append("")
            
        except Exception:
            an = 'Total Male Students = ' + str(0)
            self.textEdit_222.append(str(an))
            self.textEdit_222.append("")
            
        
        b = totalfemalep(x)
        o = totalfemales(x)
        
        try:
            q = b+o
            bn = 'Total Female Students = '+ str(q)
            self.textEdit_222.append(str(bn))
            self.textEdit_222.append("")
            
        except Exception:
            bn = 'Total Female Students = '+ str(0)
            self.textEdit_222.append(str(bn))
            self.textEdit_222.append("")
            
        try:
            c = t+q
            cn = 'Total Number of Students = '+ str(o)
            self.textEdit_222.append(str(cn))
            self.textEdit_222.append("")

        except Exception:
            cn = 'Total Number of Students = '+ str(0)
            self.textEdit_222.append(str(cn))
            self.textEdit_222.append("")
            
####################################### Ratios

        cl =classroompri(x)
        cls = classroomsec(x)

        try:
            clsf = cl+cls
            pls = b+o
            clr = pls/clsf
            clrn = "Student Classroom Ratio = "+str(clrn)
            self.textEdit_220.append(str(clrn))
            self.textEdit_220.append("")
            
        except Exception:
            clrn = "Student Classroom Ratio = "+str(0)
            self.textEdit_220.append(str(clrn))
            self.textEdit_220.append("")

        stpr = stancepri(x)
        stprs = stancesec(x)

        try:
            stu = b+o
            sn = stpr+stprs
            stanceratio = stu/sn
            stanceration = "Student Latrine Stance Ratio = "+str(stanceratio)
            self.textEdit_220.append(str(stanceration))
            self.textEdit_220.append("")

        except Exception:
            stanceration = "Student Latrine Stance Ratio = "+str(0)
            self.textEdit_220.append(stanceration)
            self.textEdit_220.append("")

        dr = deskpri(x)
        drp = desksec(x)

        try:
            stud = b+o
            dsk = dr+drp
            studdsk = stud/dsk
            studdskn = "Student Desk Ratio = "+ str(studdsk)
            self.textEdit_220.append(str(studdskn))
            self.textEdit_220.append("")

        except Exception:
            studdskn = "Student Desk Ratio = "+ str(0)
            self.textEdit_220.append(str(studdskn))
            self.textEdit_220.append("")

        tr =  teachpri(x)
        trs = teachsec(x)

        try:
            trn = tr + trs
            studn = b+o
            ratiot = studn/trn
            rationtr = "Student Teacher Ratio = "+ ratiot
            self.textEdit_220.append(str(rationtr))
            self.textEdit_220.append("")
            
        except Exception:
            rationtr = "Student Teacher Ratio = "+ str(0)
            self.textEdit_220.append(str(rationtr))
            self.textEdit_220.append("")

################################# TEACHERS

        crmp = certm(x)
        crfp = certf(x)
        cerms = certms(x)
        cerfs = certfs(x)

        try:
            cert = crmp+crfp+cerms+cerfs
            rationtr = "Certicate Holders = "+ str(cert)
            self.textEdit_221.append(str(rationtr))
            self.textEdit_221.append("")

        except Exception:
            rationtr = "Certificate Holder = "+ str(0)
            self.textEdit_221.append(str(rationtr))
            self.textEdit_221.append("")

        licem = licm(x)
        licef = licf(x)
        licems = licms(x)
        licefs = licfs(x)
        try:
            lice = licem+licef+licems+licefs
            licen = "Licenced Teachers" + str(lice)
            self.textEdit_221.append(str(licen))
            self.textEdit_221.append("")

        except Exception:
            licen = "Licenced Teachers" + str(0)
            self.textEdit_221.append(str(licen))
            self.textEdit_221.append("")
        
        deplm = depm(x)
        deplf = depf(x)
        deplms = depms(x)
        deplmf = depfs(x)

        try:
            dl = deplm+deplf+deplms+deplmf
            dln = "Deploma Holders =" + str(dl)
            self.textEdit_221.append(str(dln))
            self.textEdit_221.append("")

        except Exception:
            dln = "Deploma Holders = " + str(0)
            self.textEdit_221.append(str(dln))
            self.textEdit_221.append("")

        bcm = bacm(x)
        bcf = bacf(x)
        bcms = bacms(x)
        bcfs = bacfs(x)

        try:
            bc = bcm+bcf+bcms+bcfs
            bcn = "Bachelors Holders = " + str(bcn)
            self.textEdit_221.append(str(bcn))
            self.textEdit_221.append("")

        except Exception:
            bcn = "Bachelors Holders = " + str(0)
            self.textEdit_221.append(str(bcn))
            self.textEdit_221.append("")

        mam = masm(x)
        maf = masf(x)
        mams = masms(x)
        mafs = masfs(x)

        try:
            mas = mam+maf+mams+mafs
            masn = "Masters and Above = " + str(mas)
            self.textEdit_221.append(str(masn))
            self.textEdit_221.append("")

        except Exception:
            masn = "Masters and Above = " + str(0)
            self.textEdit_221.append(str(masn))
            self.textEdit_221.append("")

############################################################

    def railways(self):
        x = "Railways"
    
        a = totalmalep(x)
        m = totalmales(x)
        
        try:
            t = a + m
            an = 'Total Male Students = ' + str(t)
            self.textEdit_225.append(str(an))
            self.textEdit_225.append("")
            
        except Exception:
            an = 'Total Male Students = ' + str(0)
            self.textEdit_225.append(str(an))
            self.textEdit_225.append("")
            
        
        b = totalfemalep(x)
        o = totalfemales(x)
        
        try:
            q = b+o
            bn = 'Total Female Students = '+ str(q)
            self.textEdit_225.append(str(bn))
            self.textEdit_225.append("")
            
        except Exception:
            bn = 'Total Female Students = '+ str(0)
            self.textEdit_225.append(str(bn))
            self.textEdit_225.append("")
            
        try:
            c = t+q
            cn = 'Total Number of Students = '+ str(o)
            self.textEdit_225.append(str(cn))
            self.textEdit_225.append("")

        except Exception:
            cn = 'Total Number of Students = '+ str(0)
            self.textEdit_225.append(str(cn))
            self.textEdit_225.append("")
            
####################################### Ratios

        cl =classroompri(x)
        cls = classroomsec(x)

        try:
            clsf = cl+cls
            pls = b+o
            clr = pls/clsf
            clrn = "Student Classroom Ratio = "+str(clrn)
            self.textEdit_223.append(str(clrn))
            self.textEdit_223.append("")
            
        except Exception:
            clrn = "Student Classroom Ratio = "+str(0)
            self.textEdit_223.append(str(clrn))
            self.textEdit_223.append("")

        stpr = stancepri(x)
        stprs = stancesec(x)

        try:
            stu = b+o
            sn = stpr+stprs
            stanceratio = stu/sn
            stanceration = "Student Latrine Stance Ratio = "+str(stanceratio)
            self.textEdit_223.append(str(stanceration))
            self.textEdit_223.append("")

        except Exception:
            stanceration = "Student Latrine Stance Ratio = "+str(0)
            self.textEdit_223.append(stanceration)
            self.textEdit_223.append("")

        dr = deskpri(x)
        drp = desksec(x)

        try:
            stud = b+o
            dsk = dr+drp
            studdsk = stud/dsk
            studdskn = "Student Desk Ratio = "+ str(studdsk)
            self.textEdit_223.append(str(studdskn))
            self.textEdit_223.append("")

        except Exception:
            studdskn = "Student Desk Ratio = "+ str(0)
            self.textEdit_223.append(str(studdskn))
            self.textEdit_223.append("")

        tr =  teachpri(x)
        trs = teachsec(x)

        try:
            trn = tr + trs
            studn = b+o
            ratiot = studn/trn
            rationtr = "Student Teacher Ratio = "+ ratiot
            self.textEdit_223.append(str(rationtr))
            self.textEdit_223.append("")
            
        except Exception:
            rationtr = "Student Teacher Ratio = "+ str(0)
            self.textEdit_223.append(str(rationtr))
            self.textEdit_223.append("")

################################# TEACHERS

        crmp = certm(x)
        crfp = certf(x)
        cerms = certms(x)
        cerfs = certfs(x)

        try:
            cert = crmp+crfp+cerms+cerfs
            rationtr = "Certicate Holders = "+ str(cert)
            self.textEdit_224.append(str(rationtr))
            self.textEdit_224.append("")

        except Exception:
            rationtr = "Certificate Holder = "+ str(0)
            self.textEdit_224.append(str(rationtr))
            self.textEdit_224.append("")

        licem = licm(x)
        licef = licf(x)
        licems = licms(x)
        licefs = licfs(x)
        try:
            lice = licem+licef+licems+licefs
            licen = "Licenced Teachers" + str(lice)
            self.textEdit_224.append(str(licen))
            self.textEdit_224.append("")

        except Exception:
            licen = "Licenced Teachers" + str(0)
            self.textEdit_224.append(str(licen))
            self.textEdit_224.append("")
        
        deplm = depm(x)
        deplf = depf(x)
        deplms = depms(x)
        deplmf = depfs(x)

        try:
            dl = deplm+deplf+deplms+deplmf
            dln = "Deploma Holders =" + str(dl)
            self.textEdit_224.append(str(dln))
            self.textEdit_224.append("")

        except Exception:
            dln = "Deploma Holders = " + str(0)
            self.textEdit_224.append(str(dln))
            self.textEdit_224.append("")

        bcm = bacm(x)
        bcf = bacf(x)
        bcms = bacms(x)
        bcfs = bacfs(x)

        try:
            bc = bcm+bcf+bcms+bcfs
            bcn = "Bachelors Holders = " + str(bcn)
            self.textEdit_224.append(str(bcn))
            self.textEdit_224.append("")

        except Exception:
            bcn = "Bachelors Holders = " + str(0)
            self.textEdit_224.append(str(bcn))
            self.textEdit_224.append("")

        mam = masm(x)
        maf = masf(x)
        mams = masms(x)
        mafs = masfs(x)

        try:
            mas = mam+maf+mams+mafs
            masn = "Masters and Above = " + str(mas)
            self.textEdit_224.append(str(masn))
            self.textEdit_224.append("")

        except Exception:
            masn = "Masters and Above = " + str(0)
            self.textEdit_224.append(str(masn))
            self.textEdit_224.append("")

############################################################ SCHOOL SEARCH REPORT
    def searchhousing(self):
    
        d = datetime.datetime.today().year
        emis = self.lineEdit_19.text()
        c.execute("SELECT * FROM teacher_housing WHERE Emis_no = ? AND datestamp = ?",(emis,d))
        for row in c.fetchall():

            subcounty = row[6]
            parish = row[5]
            village = row[4]
            p1t = row[9]
            p2t = row[10]
            p3t = row[11]
            p4t = row[12]
            p5t = row[13]

            subcountyn = "Sub County      "+ subcounty
            parishn = "Parish             "+ parish
            villagen = "Village           "+ village
            libn = "Complete Permanent               "+ str(p1t)
            slabn = "Complete Temporary             "+ str(p2t)
            clabn = "Permanent at foundation               "+ str(p3t)
            kitn = "Permanent at window level             "+ str(p4t)
            staffn = "Permanent at wallplate level and above               "+ str(p5t)
        
            self.textEdit_34.append(str(subcountyn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(parishn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(villagen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(libn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(slabn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(clabn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(kitn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(staffn))
            self.textEdit_34.append("")

    def searchsecqual(self):
    
        d = datetime.datetime.today().year
        emis = self.lineEdit_19.text()
        c.execute("SELECT * FROM secqualifications WHERE Emis_no = ? AND datestamp = ?",(emis,d))
        for row in c.fetchall():

            subcounty = row[6]
            parish = row[5]
            village = row[4]
            p1t = row[9]
            p2t = row[10]
            p3t = row[11]
            p4t = row[12]
            p5t = row[13]
            p6t = row[14]
            total = row[15]
            lm = row[16]
            lf = row[17]
            cm = row[18]
            cf = row[19]
            dm = row[20]
            df = row[21]
            bm = row[22]
            bf = row[23]
            mm = row[24]
            mf = row[25]


            subcountyn = "Sub County      "+ subcounty
            parishn = "Parish             "+ parish
            villagen = "Village           "+ village
            libn = "S1 Teachers               "+ str(p1t)
            slabn = "S2 Teachers             "+ str(p2t)
            clabn = "S3 Teachers               "+ str(p3t)
            kitn = "S4 Teachers             "+ str(p4t)
            staffn = "S5 Teachers               "+ str(p5t)
            adminn = "S6 Teachers             "+ str(p6t)
            watern = "Total Number of Teachers             "+ str(total)
            storen = "Licenced Male Teachers               "+ str(lm)
            workn = "Licenced female Teachers             "+ str(lf)
            playn = "Certificate Male               "+ str(cm)
            gardenn = "Certificate female             "+ str(cf)
            latn = "Deploma Male   "+ str(dm)
            stann = "Deploma Female   "+ str(df)
            handn = "Bachelores Male             "+ str(bm)
            p1n = "Bachelors Female   "+ str(bf)
            p2n = "Masters and Above Male   "+ str(mm)
            p3n = "Master and Above Female   "+ str(mf)
        
            self.textEdit_34.append(str(subcountyn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(parishn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(villagen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(libn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(slabn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(clabn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(kitn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(staffn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(adminn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(watern))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(storen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(workn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(playn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(gardenn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(latn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(stann))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(handn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p1n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p2n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p3n))

    def searchqual(self):
    
        d = datetime.datetime.today().year
        emis = self.lineEdit_19.text()
        c.execute("SELECT * FROM qualifications WHERE Emis_no = ? AND datestamp = ?",(emis,d))
        for row in c.fetchall():

            subcounty = row[6]
            parish = row[5]
            village = row[4]
            p1t = row[9]
            p2t = row[10]
            p3t = row[11]
            p4t = row[12]
            p5t = row[13]
            p6t = row[14]
            p7t = row[15]
            total = row[16]
            lm = row[17]
            lf = row[18]
            cm = row[19]
            cf = row[20]
            dm = row[21]
            df = row[22]
            bm = row[23]
            bf = row[24]
            mm = row[25]
            mf = row[26]


            subcountyn = "Sub County      "+ subcounty
            parishn = "Parish             "+ parish
            villagen = "Village           "+ village
            libn = "P1 Teachers               "+ str(p1t)
            slabn = "P2 Teachers             "+ str(p2t)
            clabn = "P3 Teachers               "+ str(p3t)
            kitn = "P4 Teachers             "+ str(p4t)
            staffn = "P5 Teachers               "+ str(p5t)
            adminn = "P6 Teachers             "+ str(p6t)
            dinn = "P7 Teachers               "+ str(p7t)
            watern = "Total Number of Teachers             "+ str(total)
            storen = "Licenced Male Teachers               "+ str(lm)
            workn = "Licenced female Teachers             "+ str(lf)
            playn = "Certificate Male               "+ str(cm)
            gardenn = "Certificate female             "+ str(cf)
            latn = "Deploma Male   "+ str(dm)
            stann = "Deploma Female   "+ str(df)
            handn = "Bachelores Male             "+ str(bm)
            p1n = "Bachelors Female   "+ str(bf)
            p2n = "Masters and Above Male   "+ str(mm)
            p3n = "Master and Above Female   "+ str(mf)
        
            self.textEdit_34.append(str(subcountyn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(parishn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(villagen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(libn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(slabn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(clabn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(kitn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(staffn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(adminn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(dinn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(watern))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(storen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(workn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(playn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(gardenn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(latn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(stann))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(handn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p1n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p2n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p3n))

    def searchsecfacil(self):
    
        d = datetime.datetime.today().year
        emis = self.lineEdit_19.text()
        c.execute("SELECT * FROM facilities WHERE Emis_no = ? AND datestamp = ?",(emis,d))
        for row in c.fetchall():

            subcounty = row[6]
            parish = row[5]
            village = row[4]
            lib = row[9]
            slab = row[10]
            clab = row[11]
            kit = row[12]
            staff = row[13]
            admin = row[14]
            din = row[15]
            water = row[16]
            store = row[17]
            work = row[18]
            play = row[19]
            garden = row[20]
            lat = row[21]
            stan = row[22]
            hand = row[23]
            p1 = row[24]
            p2 = row[25]
            p3 = row[26]
            p4 = row[27]
            p5 = row[28]
            p6 = row[29]

            subcountyn = "Sub County      "+ subcounty
            parishn = "Parish             "+ parish
            villagen = "Village           "+ village
            libn = "Library               "+ str(lib)
            slabn = "Science Laboratory             "+ str(slab)
            clabn = "Computer Laboratory               "+ str(clab)
            kitn = "Kitchen             "+ str(kit)
            staffn = "Staff Room               "+ str(staff)
            adminn = "Administration Block             "+ str(admin)
            dinn = "Dining Hall               "+ str(din)
            watern = "Safe Water Supply             "+ str(water)
            storen = "Stores               "+ str(store)
            workn = "Workshop             "+ str(work)
            playn = "Play Ground               "+ str(play)
            gardenn = "School Garden             "+ str(garden)
            latn = "Latrine   "+ str(lat)
            stann = "Number of Latrine Stances   "+ str(stan)
            handn = "Hand Washing Facilities             "+ str(hand)
            p1n = "S1 Desk   "+ str(p1)
            p2n = "S2 Desk   "+ str(p2)
            p3n = "S3 Desk   "+ str(p3)
            p4n = "S4 Desk   "+ str(p4)
            p5n = "S5 Desk   "+ str(p5)
            p6n = "S6 Desk   "+ str(p6)
        
            self.textEdit_34.append(str(subcountyn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(parishn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(villagen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(libn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(slabn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(clabn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(kitn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(staffn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(adminn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(dinn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(watern))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(storen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(workn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(playn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(gardenn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(latn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(stann))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(handn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p1n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p2n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p3n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p4n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p5n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p6n))
            self.textEdit_34.append("")

    def searchfacil(self):
    
        d = datetime.datetime.today().year
        emis = self.lineEdit_19.text()
        c.execute("SELECT * FROM facilities WHERE Emis_no = ? AND datestamp = ?",(emis,d))
        for row in c.fetchall():

            subcounty = row[6]
            parish = row[5]
            village = row[4]
            lib = row[9]
            slab = row[10]
            clab = row[11]
            kit = row[12]
            staff = row[13]
            admin = row[14]
            din = row[15]
            water = row[16]
            store = row[17]
            work = row[18]
            play = row[19]
            garden = row[20]
            lat = row[21]
            stan = row[22]
            hand = row[23]
            p1 = row[24]
            p2 = row[25]
            p3 = row[26]
            p4 = row[27]
            p5 = row[28]
            p6 = row[29]
            p7 = row[22]

            subcountyn = "Sub County      "+ subcounty
            parishn = "Parish             "+ parish
            villagen = "Village           "+ village
            libn = "Library               "+ str(lib)
            slabn = "Science Laboratory             "+ str(slab)
            clabn = "Computer Laboratory               "+ str(clab)
            kitn = "Kitchen             "+ str(kit)
            staffn = "Staff Room               "+ str(staff)
            adminn = "Administration Block             "+ str(admin)
            dinn = "Dining Hall               "+ str(din)
            watern = "Safe Water Supply             "+ str(water)
            storen = "Stores               "+ str(store)
            workn = "Workshop             "+ str(work)
            playn = "Play Ground               "+ str(play)
            gardenn = "School Garden             "+ str(garden)
            latn = "Latrine   "+ str(lat)
            stann = "Number of Latrine Stances   "+ str(stan)
            handn = "Hand Washing Facilities             "+ str(hand)
            p1n = "P1 Desk   "+ str(p1)
            p2n = "P2 Desk   "+ str(p2)
            p3n = "P3 Desk   "+ str(p3)
            p4n = "P4 Desk   "+ str(p4)
            p5n = "P5 Desk   "+ str(p5)
            p6n = "P6 Desk   "+ str(p6)
            p7n = "P7 Desk   "+ str(p7)
        
            self.textEdit_34.append(str(subcountyn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(parishn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(villagen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(libn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(slabn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(clabn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(kitn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(staffn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(adminn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(dinn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(watern))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(storen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(workn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(playn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(gardenn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(latn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(stann))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(handn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p1n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p2n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p3n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p4n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p5n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p6n))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p7n))
            self.textEdit_34.append("")
            
    def searchsecenr(self):
        d = datetime.datetime.today().year
        emis = self.lineEdit_19.text()
        c.execute("SELECT * FROM secenrollment WHERE Emis_no = ? AND datestamp = ?",(emis,d))
        for row in c.fetchall():

            subcounty = row[6]
            parish = row[5]
            village = row[4]
            p1male = row[9]
            p1female = row[10]
            p2male = row[11]
            p2female = row[12]
            p3male = row[13]
            p3female = row[14]
            p4male = row[15]
            p4female = row[16]
            p5male = row[17]
            p5female = row[18]
            p6male = row[19]
            p6female = row[20]
            tmale = row[21]
            tfemale = row[22]

            subcountyn = "Sub County      "+ subcounty
            parishn = "Parish             "+ parish
            villagen = "Village           "+ village
            p1mn = "S1 Male               "+ str(p1male)
            p1fn = "S1 Female             "+ str(p1female)
            p2mn = "S2 Male               "+ str(p2male)
            p2fn = "S2 Female             "+ str(p2female)
            p3mn = "S3 Male               "+ str(p3male)
            p3fn = "S3 Female             "+ str(p3female)
            p4mn = "S4 Male               "+ str(p4male)
            p4fn = "S4 Female             "+ str(p4female)
            p5mn = "S5 Male               "+ str(p5male)
            p5fn = "S5 Female             "+ str(p5female)
            p6mn = "S6 Male               "+ str(p6male)
            p6fn = "S6 Female             "+ str(p6female)
            tmalen = "Total Male Students   "+ str(tmale)
            tfemalen = "Total Female Students   "+ str(tfemale)

            self.textEdit_34.append(str(subcountyn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(parishn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(villagen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p1mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p1fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p2mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p2fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p3mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p3fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p4mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p4fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p5mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p5fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p6mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p6fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(tmalen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(tfemalen))
            self.textEdit_34.append("")
    
    def searchenr(self):
        d = datetime.datetime.today().year
        emis = self.lineEdit_19.text()
        c.execute("SELECT * FROM enrollment WHERE Emis_no = ? AND datestamp = ?",(emis,d))
        for row in c.fetchall():

            subcounty = row[6]
            parish = row[5]
            village = row[4]
            p1male = row[9]
            p1female = row[10]
            p2male = row[11]
            p2female = row[12]
            p3male = row[13]
            p3female = row[14]
            p4male = row[15]
            p4female = row[16]
            p5male = row[17]
            p5female = row[18]
            p6male = row[19]
            p6female = row[20]
            p7male = row[21]
            p7female = row[22]
            tmale = row[23]
            tfemale = row[24]

            subcountyn = "Sub County      "+ subcounty
            parishn = "Parish             "+ parish
            villagen = "Village           "+ village
            p1mn = "P1 Male               "+ str(p1male)
            p1fn = "P1 Female             "+ str(p1female)
            p2mn = "P2 Male               "+ str(p2male)
            p2fn = "P2 Female             "+ str(p2female)
            p3mn = "P3 Male               "+ str(p3male)
            p3fn = "P3 Female             "+ str(p3female)
            p4mn = "P4 Male               "+ str(p4male)
            p4fn = "P4 Female             "+ str(p4female)
            p5mn = "P5 Male               "+ str(p5male)
            p5fn = "P5 Female             "+ str(p5female)
            p6mn = "P6 Male               "+ str(p6male)
            p6fn = "P6 Female             "+ str(p6female)
            p7mn = "P7 Male               "+ str(p7male)
            p7fn = "P7 Female             "+ str(p7female)
            tmalen = "Total Male Pupils   "+ str(tmale)
            tfemalen = "Total Female Pupils   "+ str(tfemale)

            self.textEdit_34.append(str(subcountyn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(parishn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(villagen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p1mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p1fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p2mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p2fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p3mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p3fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p4mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p4fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p5mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p5fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p6mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p6fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p7mn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(p7fn))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(tmalen))
            self.textEdit_34.append("")
            self.textEdit_34.append(str(tfemalen))
            self.textEdit_34.append("")


############################################################ FILE PICKER AND IMPORT FUNCTIONS AND MAIN MENU FUNCTIONS
        
    def file_school(self):
        csvfile, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV (*.csv *.tsv *.txt)")
        filename = csvfile.rpartition("/")[2].replace(".csv", "")
        w = filename+".csv"
        
        with open(str(w),'r') as f:
            
            dr = csv.DictReader(f,delimiter=',')
            for i in dr:
                emis = i.get('Emis_no')
                school = i.get('school_name')
                types = i.get('school_type')
                subcounty = i.get('sub_county')
                parish = i.get('parish')
                village = i.get('village')
                try:
                    c.execute("INSERT INTO school VALUES(?,?,?,?,?,?)",(emis,school,types,subcounty,parish,village))
                    conn.commit()
                except Exception:
                    self.failed()
                    break

####        c.executemany("INSERT INTO school VALUES(?,?,?,?,?,?);",to_db)
####        print(4)
####        conn.commit()
####        print(5)        

    def file_teacher(self):

        csvfile, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV (*.csv *.tsv *.txt)")
        filename = csvfile.rpartition("/")[2].replace(".csv", "")
        w = filename+".csv"

        with open(str(w),'r') as f:
            
            dr = csv.DictReader(f,delimiter=',')
            for i in dr:
                emp = i.get('EmployeeNo')
                school = i.get('school_name')
                emis = i.get('Emis_no')
                types = i.get('school_type')
                subcounty = i.get('sub_county')
                qualification = i.get('Qualification')
                eod = i.get('Expected_Date_of_retirement')
                name = i.get('name')
                Gender = i.get('Gender')
                dob = i.get('Date_of_Birth')
                marital = i.get('Marital_status')
                hd = i.get('home_district')
                hs = i.get('home_subcounty')
                hp = i.get('home_parish')
                hv = i.get('home_village')
                nok = i.get('Next_of_kin')
                title = i.get('Title')
                conf = i.get('confirmation_status')
                nin = i.get('nin')
                sup = i.get('supplier_no')
                tin = i.get('tin')
                reg = i.get('reg_no')
                datestamp = datetime.datetime.today().year
                try:
                    c.execute("INSERT INTO teacher VALUES(?,?,?,?,?,?,?,?,?,,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(emp,school,emis,types,subcounty,qualification,eod,name,Gender,
                                                                                                            dob,marital,hd,hs,hp,hv,nok,title,conf,nin,sup,tin,reg,datestamp))
                    conn.commit()
                except Exception:
                    self.failed()
                    break

    def file_priennrollment(self):

        csvfile, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV (*.csv *.tsv *.txt)")
        filename = csvfile.rpartition("/")[2].replace(".csv", "")
        w = filename+".csv"

        with open(str(w),'r') as f:
            
            dr = csv.DictReader(f,delimiter=',')
            for i in dr:
                school = i.get('school_name')
                emis = i.get('Emis_no')
                types = i.get('school_type')
                village = i.get('village')
                parish = i.get('parish')
                subcounty = i.get('sub_county')
                category = i.get('category')
                owner = i.get('ownership')
                p1m = int(i.get('p1male'))
                p1f = int(i.get('p1female'))
                p2m = int(i.get('p2male'))
                p2f = int(i.get('p2female'))
                p3m = int(i.get('p3male'))
                p3f = int(i.get('p3female'))
                p4m = int(i.get('p4male'))
                p4f = int(i.get('p4female'))
                p5m = int(i.get('p5male'))
                p5f = int(i.get('p5female'))
                p6m = int(i.get('p6male'))
                p6f = int(i.get('p6female'))
                p7m = int(i.get('p7male'))
                p7f = int(i.get('p7female'))
                mtotal = int(i.get("maletotal"))
                ftotal = int(i.get("femaletotal"))
                d = datetime.datetime.today().year
                try:
                
                    c.execute("INSERT INTO enrollment VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school,emis,types,village,parish,subcounty,category,owner,p1m,p1f,p2m,p2f,
                                                                                                                  p3m,p3f,p4m,p4f,p5m,p5f,p6m,p6f,p7m,p7f,mtotal,ftotal,d))
                    conn.commit()
                except Exception:
                    self.failed()
                    break
        
    def file_secenrollment(self):

        csvfile, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV (*.csv *.tsv *.txt)")
        filename = csvfile.rpartition("/")[2].replace(".csv", "")
        print(filename)
        w = filename+".csv"

        with open(str(w),'r') as f:
            
            dr = csv.DictReader(f,delimiter=',')
            for i in dr:
                school = i.get('school_name')
                emis = i.get('Emis_no')
                types = i.get('school_type')
                village = i.get('village')
                parish = i.get('parish')
                subcounty = i.get('sub_county')
                category = i.get('category')
                owner = i.get('ownership')
                s1m = int(i.get('s1male'))
                s1f = int(i.get('s1female'))
                s2m = int(i.get('s2male'))
                s2f = int(i.get('s2female'))
                s3m = int(i.get('s3male'))
                s3f = int(i.get('s3female'))
                s4m = int(i.get('s4male'))
                s4f = int(i.get('s4female'))
                s5m = int(i.get('s5male'))
                s5f = int(i.get('s5female'))
                s6m = int(i.get('s6male'))
                s6f = int(i.get('s6female'))
                mtotal = int(i.get("maletotal"))
                ftotal = int(i.get("femaletotal"))
                d = datetime.datetime.today().year
                try:
                    c.execute("INSERT INTO secenrollment VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school,emis,types,village,parish,subcounty,category,owner,s1m,s1f,s2m,s2f,
                                                                                                                 s3m,s3f,s4m,s4f,s5m,s5f,s6m,s6f,mtotal,ftotal,d))
                    conn.commit()
                except Exception:
                    self.failed()
                    break

    def file_prifaciities(self):

        csvfile, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV (*.csv *.tsv *.txt)")
        filename = csvfile.rpartition("/")[2].replace(".csv", "")
        print(filename)
        w = filename+".csv"

        with open(str(w),'r') as f:
            
            dr = csv.DictReader(f,delimiter=',')
            for i in dr:
                school = i.get('school_name')
                emis = i.get('Emis_no')
                types = i.get('school_type')
                village = i.get('village')
                parish = i.get('parish')
                subcounty = i.get('sub_county')
                category = i.get('category')
                owner = i.get('ownership')
                lib = i.get('library')
                slab = i.get('science_lab')
                clab = i.get('computer_lab')
                kit = i.get('kitchen')
                staff = i.get('staff_room')
                admin = i.get('administration_block')
                din = i.get('dinning_hall')
                water = i.get('reliable_safe_water_supply')
                stores = i.get('stores')
                workshop = i.get('workshop')
                playground = i.get('playground')
                garden = i.get('playground')
                latrine = i.get('latrine')
                stances = int(i.get('no_of_stances'))
                p1d = int(i.get('p1_desk'))
                p2d = int(i.get('p2_desk'))
                p3d = int(i.get('P3_desk'))
                p4d = int(i.get('p4_desk'))
                p5d = int(i.get('p5_desk'))
                p6d = int(i.get('p6_desk'))
                p7d = int(i.get('p7_desk'))
                d = datetime.datetime.today().year

                try:
                    c.execute("INSERT INTO faciities VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school,emis,types,village,parish,subcounty,category,owner,lib,
                                                                                                                           slab,clab,kit,staff,admin,din,water,stores,workshop,
                                                                                                                           playground,garden,latrine,stances,p1d,p2d,p3d,p4d,
                                                                                                                           p5d,p6d,p7d,d))
                    
                    conn.commit()
                except Exception:
                    self.failed()
                    break

    def file_secfaciities(self):

        csvfile, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV (*.csv *.tsv *.txt)")
        filename = csvfile.rpartition("/")[2].replace(".csv", "")
        w = filename+".csv"

        with open(str(w),'r') as f:
            
            dr = csv.DictReader(f,delimiter=',')
            for i in dr:
                school = i.get('school_name')
                emis = i.get('Emis_no')
                types = i.get('school_type')
                village = i.get('village')
                parish = i.get('parish')
                subcounty = i.get('sub_county')
                category = i.get('category')
                owner = i.get('ownership')
                lib = i.get('library')
                slab = i.get('science_lab')
                clab = i.get('computer_lab')
                kit = i.get('kitchen')
                staff = i.get('staff_room')
                admin = i.get('administration_block')
                din = i.get('dinning_hall')
                water = i.get('reliable_safe_water_supply')
                stores = i.get('stores')
                workshop = i.get('workshop')
                playground = i.get('playground')
                garden = i.get('playground')
                latrine = i.get('latrine')
                stances = int(i.get('no_of_stances'))
                s1d = int(i.get('s1_desk'))
                s2d = int(i.get('s2_desk'))
                s3d = int(i.get('s3_desk'))
                s4d = int(i.get('s4_desk'))
                s5d = int(i.get('s5_desk'))
                s6d = int(i.get('s6_desk'))
                d = datetime.datetime.today().year

                try:
                    c.execute("INSERT INTO secfaciities VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school,emis,types,village,parish,subcounty,category,owner,lib,
                                                                                                                            slab,clab,kit,staff,admin,din,water,stores,workshop,
                                                                                                                            playground,garden,latrine,stances,s1d,s2d,s3d,s4d,
                                                                                                                            s5d,s6d,d))
                    conn.commit()
                except Exception:
                    self.failed()
                    break

    def file_priclassroom(self):

        csvfile, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV (*.csv *.tsv *.txt)")
        filename = csvfile.rpartition("/")[2].replace(".csv", "")
        w = filename+".csv"

        with open(str(w),'r') as f:
            
            dr = csv.DictReader(f,delimiter=',')
            for i in dr:
                school = i.get('school_name')
                emis = i.get('Emis_no')
                types = i.get('school_type')
                village = i.get('village')
                parish = i.get('parish')
                subcounty = i.get('sub_county')
                category = i.get('category')
                owner = i.get('ownership')
                p1d = int(i.get('p1_classroom'))
                p2d = int(i.get('p2_classroom'))
                p3d = int(i.get('P3_classroom'))
                p4d = int(i.get('p4_classroom'))
                p5d = int(i.get('p5_classroom'))
                p6d = int(i.get('p6_classroom'))
                p7d = int(i.get('p7_classroom'))
                total = int(i.get('total_classrooms'))
                cp = int(i.get('complete_permanent'))
                ct = int(i.get('complete_temporary'))
                af = int(i.get('at_foundation'))
                aw = int(i.get('at_window'))
                wp = int(i.get('at_wallplate_and_above'))
                nc = int(i.get('number_of_classroom_without_structures'))
                
                d = datetime.datetime.today().year
                try:
                    c.execute("INSERT INTO classroom VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school,emis,types,village,parish,subcounty,category,owner,p1d,p2d,p3d,p4d,p5d,
                                                                                                         p6d,p7d,total,cp,ct,af,aw,wp,nc))
                    conn.commit()
                except Exception:
                    self.failed()
                    break

    def file_secclassroom(self):

        csvfile, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV (*.csv *.tsv *.txt)")
        filename = csvfile.rpartition("/")[2].replace(".csv", "")
        w = filename+".csv"

        with open(str(w),'r') as f:
            
            dr = csv.DictReader(f,delimiter=',')
            for i in dr:
                school = i.get('school_name')
                emis = i.get('Emis_no')
                types = i.get('school_type')
                village = i.get('village')
                parish = i.get('parish')
                subcounty = i.get('sub_county')
                category = i.get('category')
                owner = i.get('ownership')
                p1d = int(i.get('s1_classroom'))
                p2d = int(i.get('s2_classroom'))
                p3d = int(i.get('s3_classroom'))
                p4d = int(i.get('s4_classroom'))
                p5d = int(i.get('s5_classroom'))
                p6d = int(i.get('s6_classroom'))
                total = int(i.get('total_classrooms'))
                cp = int(i.get('complete_permanent'))
                ct = int(i.get('complete_temporary'))
                af = int(i.get('at_foundation'))
                aw = int(i.get('at_window'))
                wp = int(i.get('at_wallplate_and_above'))
                nc = int(i.get('number_of_classroom_without_structures'))
                
                d = datetime.datetime.today().year
                try:
                    c.execute("INSERT INTO secclassroom VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school,emis,types,village,parish,subcounty,category,owner,p1d,p2d,p3d,p4d,p5d,
                                                                                                          p6d,total,cp,ct,af,aw,wp,nc))
                    conn.commit()
                except Exception:
                    self.failed()
                    break

    def file_housing(self):

        csvfile, _ = QFileDialog.getOpenFileName(None, "Open CSV File", "", "CSV (*.csv *.tsv *.txt)")
        filename = csvfile.rpartition("/")[2].replace(".csv", "")
        w = filename+".csv"

        with open(str(w),'r') as f:
            
            dr = csv.DictReader(f,delimiter=',')
            for i in dr:
                school = i.get('school_name')
                emis = i.get('Emis_no')
                types = i.get('school_type')
                village = i.get('village')
                parish = i.get('parish')
                subcounty = i.get('sub_county')
                category = i.get('category')
                owner = i.get('ownership')
                cp = int(i.get('complete_permanent'))
                ct = int(i.get('complete_temporary'))
                af = int(i.get('at_foundation'))
                aw = int(i.get('at_window'))
                wp = int(i.get('at_wallplate_and_above'))
                nc = int(i.get('number_of_classroom_without_structures'))
                
                d = datetime.datetime.today().year
                try:
                    c.execute("INSERT INTO teacher_housing VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(school,emis,types,village,parish,subcounty,category,
                                                                                                 owner,cp,ct,af,aw,wp,nc))
                    conn.commit()
                except Exception:
                    self.failed()
                    break

##ADMIN FUNCTIONS
    def deletet(self):
        try:
            empn = self.lineEdit_15.text()
            connection = sqlite3.connect('Education.db')
            cur = connection.cursor()
            connection.commit()
            cur.execute("DELETE FROM teacher WHERE EmployeeNo = ?",(empn,))
            connection.commit()
            self.success1()

        except Exception:
            self.failed1()

    def leavesave(self):
        try:
            empn = self.lineEdit_59.text()
            connection = sqlite3.connect('Education.db')
            cur = connection.cursor()
            connection.commit()
            cur.execute("SELECT * FROM teacher WHERE EmployeeNo = ?",(empn,))
            for row in cur.fetchall():
                
                self.empno = row[0]
                self.name = row[7]
                self.school = row[1]
                self.typen = row[3]
                self.detail = self.textEdit_7.toPlainText()
                self.start1 = self.dateEdit_3.date()
                self.end1 = self.dateEdit_4.date()
                x = str(self.start1.year())
                y = str(self.start1.month())
                z = str(self.start1.day())
                self.start = str(y+"/"+z+"/"+x)
                a = str(self.end1.year())
                b = str(self.end1.month())
                c = str(self.end1.day())
                self.end = str(b+"/"+c+"/"+c)

                cur.execute("INSERT INTO leave(empno,name,school,schoo_type,details_of_leave,startdate,enddate) VALUES(?,?,?,?,?,?,?)",(self.empno,self.name,self.school,self.typen,self.detail,self.start,self.end))
                connection.commit()
                self.success1()

        except Exception:
            self.failed1()
        
    def deceased(self):
        
        empn = self.lineEdit_15.text()
        date = datetime.datetime.today()
        try:
            c.execute("SELECT * FROM teacher WHERE EmployeeNo = ?",(empn,))
        
            for row in c.fetchall():
                empno = row[0]
                school = row[1]
                emis = row[2]
                stype = row[3]
                scounty = row[4]
                qualification = row[5]
                eod = row[6]
                name = row[7]
                gender = row[8]
                dob = row[9]
                mstatus = row[10]
                hdistrict = row[11]
                hsubcounty = row[12]
                hparish = row[13]
                hvillage = row[14]
                nok = row[15]
                title = row[16]
                conf = row[17]
                nin = row[18]
                sup = row[19]
                tin = row[20]
                reg = row[21]

                c.execute("INSERT INTO deceased(EmployeeNo,school,Emis_No,school_type, sub_county, Qualification, expected_Date_of_retirement,"
                          "name, Gender, Date_of_Birth, Marital_status, home_district, home_subcounty, home_parish, home_village,"
                          "Next_of_kin, Title, confirmation_status, nin,"
                          "supplier_no, tin,reg_no,date_of_death) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (empno, school, emis,stype,scounty,qualification,eod,name,gender,
                                                                                                                  dob,mstatus,hdistrict,hsubcounty,hparish,hvillage,nok,title,
                                                                                                                  conf,nin,sup,tin,reg,date))
                conn.commit()

            c.execute("DELETE FROM teacher WHERE EmployeeNo = ?",(empn,))
            conn.commit()
            conn.close()
            self.success1()

        except Exception:
            self.failed1()
            
    def absconded(self):
        empn = self.lineEdit_15.text()
        date = datetime.datetime.today()
        try:
            c.execute("SELECT * FROM teacher WHERE EmployeeNo = ?",(empn,))
            for row in c.fetchall():
                empno = row[0]
                school = row[1]
                emis = row[2]
                stype = row[3]
                scounty = row[4]
                qualification = row[5]
                eod = row[6]
                name = row[7]
                gender = row[8]
                dob = row[9]
                mstatus = row[10]
                hdistrict = row[11]
                hsubcounty = row[12]
                hparish = row[13]
                hvillage = row[14]
                nok = row[15]
                title = row[16]
                conf = row[17]
                nin = row[18]
                sup = row[19]
                tin = row[20]
                reg = row[21]

                c.execute("INSERT INTO absconded(EmployeeNo,school,Emis_No,school_type, sub_county, Qualification, expected_Date_of_retirement,"
                          "name, Gender, Date_of_Birth, Marital_status, home_district, home_subcounty, home_parish, home_village,"
                          "Next_of_kin, Title, confirmation_status, nin,"
                          "supplier_no, tin,reg_no,date) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (empno, school, emis,stype,scounty,qualification,eod,name,gender,
                                                                                                                  dob,mstatus,hdistrict,hsubcounty,hparish,hvillage,nok,title,
                                                                                                                  conf,nin,sup,tin,reg,date))
                conn.commit()
            
            c.execute("DELETE FROM teacher WHERE EmployeeNo = ?",(empn,))
            conn.commit()
            self.success1()
        except Exception:
            self.failed1()
            
    def success1(self):
        
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('SUCCESS')
        mb.setText("ACTION SUCCESSFUL")
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_()

    def failed1(self):
        
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('FAILED')
        mb.setText("ACTION NOT COMPLETED")
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_()
        
    def searchteacher(self):
        self.searcht = self.lineEdit_15.text()
        self.textEdit_2.clear()
        c.execute("SELECT * FROM teacher WHERE EmployeeNo = ?",(self.searcht,))

        for row in c.fetchall():
            school = row[1]
            schooln = "School Name:      " + school
            subcounty = row[4]
            subcountyn = "Sub County:    " + subcounty
            name = row[7]
            namen = "Teacher's Name:     " + name
            gender = row[8]
            gendern = "Gender:           " + gender
            dob = row[9]
            dobn = "Date of Birth:       " + dob
            marital = row[10]
            maritaln = "Marital Status:  " + marital
            eod = row[6]
            eodn = "Expected Date of Retirement:    " + eod
            hdist = row[11]
            hdistn = "Home District:     " + hdist
            hsub = row[12]
            hsubn = "Home Subcounty:     " + hsub
            hpar = row[13]
            hparn = "Home Parish:        " + hpar
            hvil = row[14]
            hviln = "Home Village:       " + hvil
            nok = row[15]
            nokn = "Next of Kin:         " + nok
            qlif = row[5]
            qlifn = "Qualification:      " + qlif
            reg = row[21]
            regn = "Registration Number: " + reg
            title = row[16]
            titlen = "Title:             " + title
            confm = row[17]
            confmn = "Confirmation Status" + confm
            nin = row[18]
            ninn = "National Identification Number(NIN):  " + nin
            sup = row[19]
            supn = "Supplier Number:     " + sup
            tin = row[20]
            tinn = "Tax Identification Number:     " + tin
            
            self.textEdit_2.append(str(schooln))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(subcountyn))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(namen))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(gendern))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(dobn))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(eodn))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(hdistn))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(hsubn))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(hparn))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(hviln))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(nokn))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(qlifn))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(regn))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(titlen))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(confmn))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(ninn))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(supn))
            self.textEdit_2.append("")
            self.textEdit_2.append(str(tinn))
            
############################################################ SEARCH FUNCTIONS

    def searchteacherprofile(self):
        self.empno = self.lineEdit_39.text()
        c.execute("SELECT * FROM teacher WHERE EmployeeNo = ?",(self.empno,))
        for row in c.fetchall():
            school = row[1]
            subcounty = row[4]
            qlif = row[5]
            name = row[7]
            gender = row[8]
            dob = row[9]
            marital = row[10]
            hdist = row[11]
            hsub = row[12]
            hpar = row[13]
            hvil = row[14]
            nok = row[15]
            title = row[16]
            confm = row[17]
            nin = row[18]
            sup = row[19]
            tin = row[20]
            reg = row[21]

            self.school_4.insert(str(school))
            self.subcounty_4.insert(str(subcounty))
            self.name_3.insert(str(name))
            self.lineEdit_32.insert(str(hdist))
            self.lineEdit_42.insert(str(hsub))
            self.lineEdit_43.insert(str(hpar))
            self.lineEdit_44.insert(str(hvil))
            self.lineEdit_33.insert(str(nok))
            self.lineEdit_34.insert(str(qlif))
            self.lineEdit_35.insert(str(reg))
            self.lineEdit_36.insert(str(qlif))
            self.lineEdit_37.insert(str(confm))
            self.lineEdit_38.insert(str(nin))
            self.lineEdit_40.insert(str(sup))
            self.lineEdit_41.insert(str(qlif))

    def searchschool(self):
        self.emis = self.emis.text()
        c.execute("SELECT * FROM school WHERE Emis_no = ?",(self.emis,))
        for row in c.fetchall():
            school = row[1]
            stype = row[2]
            subcounty = row[3]
            parish = row[4]
            village = row[5]
            self.school.insert(str(school))
            self.subcounty.insert(str(subcounty))
            self.parish.insert(str(parish))
            self.village.insert(str(village))

############################################################ sec classroom form

    def secclassroom(self):
        
        try:
            self.schooln = self.category_13.text()
            self.cate = self.p1_7.text()
            self.owner = self.comboBox_12.currentText()
            self.s1classes = int(self.p1_6.text())
            self.s2classes = int(self.p2_5.text())
            self.s3classes = int(self.p3_5.text())
            self.s4classes = int(self.p4_5.text())
            self.s5classes = int(self.p5_5.text())
            self.s6classes = int(self.p6_5.text())
            self.cpm = int(self.permanent_3.text())
            self.ctm = int(self.temporary_3.text())
            self.atf = int(self.atfoundation_3.text())
            self.atwin = int(self.atwindow_3.text())
            self.atwall = int(self.wallpaltw_3.text())
            self.ws = int(self.withoutstructures_2.text())
        except Exception:
            self.EnInteger()

        try:
            
            sclassroom(self.schooln,self.cate,self.owner,self.s1classes,self.s2classes,self.s3classes,self.s4classes,self.s5classes,self.s6classes,self.cpm,
                       self.ctm,self.atf,self.atwin,self.atwall,self.ws)
            self.saved()

        except Exception:
            self.failed()

    def resetsecclassroom(self):
        self.category_13.setText("")
        self.p1_7.setText("")
        self.p1_6.setText("")
        self.p2_5.setText("")
        self.p3_5.setText("")
        self.p4_5.setText("")
        self.p5_5.setText("")
        self.p6_5.setText("")
        self.permanent_3.setText("")
        self.temporary_3.setText("")
        self.atfoundation_3.setText("")
        self.atwindow_3.setText("")
        self.wallpaltw.setText("")
        self.withoutstructures_2.setText("")
        
############################################################ sec facilities form        

    def secfacilities(self):
        
        try:
            self.schooln = self.category_12.text()
            self.cate = self.sciencelab_6.text()
            self.owner = self.comboBox_11.currentText()
            self.lib = self.library_3.text()
            self.slab = self.sciencelab_5.text()
            self.clab = self.complab_3.text()
            self.kit = self.kitchen_3.text()
            self.staff = self.staffroom_3.text()
            self.admin = self.adminblock_3.text()
            self.dinning = self.dinninghall_3.text()
            self.water = self.reliablesafewater_3.text()
            self.stores = self.stores_3.text()
            self.work = self.workshop_3.text()
            self.play = self.playground_3.text()
            self.garden = self.garden_3.text()
            self.lat = self.latrine_3.text()
            self.hand = self.bachelorsm_5.text()
            self.stance = int(self.stances_3.text())
            self.s1desk = int(self.p1_5.text())
            self.s2desk = int(self.p2_4.text())
            self.s3desk = int(self.p3_4.text())
            self.s4desk = int(self.p4_4.text())
            self.s5desk = int(self.p5_4.text())
            self.s6desk = int(self.p6_4.text())
        except Exception:
            self.EnInteger()

        try:
            sfacilities(self.schooln,self.cate,self.owner,self.lib,self.slab,self.clab,self.kit,self.staff,self.admin,self.dinning,self.water,self.stores,self.work,
                        self.play,self.garden,self.lat,self.stance,self.hand,self.s1desk,self.s2desk,self.s3desk,self.s4desk,self.s5desk,self.s6desk)
            self.saved()

        except Exception:
            self.failed()

    def resetsecfacilities(self):
        self.category_12.setText("")
        self.sciencelab_6.setText("")
        self.library_3.setText("")
        self.sciencelab_5.setText("")
        self.complab_3.setText("")
        self.kitchen_3.setText("")
        self.staffroom_3.setText("")
        self.adminblock_3.setText("")
        self.dinninghall_3.setText("")
        self.reliablesafewater.setText("")
        self.stores_3.setText("")
        self.workshop_3.setText("")
        self.playground_3.setText("")
        self.garden_3.setText("")
        self.latrine_3.setText("")
        self.stances_3.setText("")
        self.bachelorsm_5.setText("")
        self.p1_5.setText("")
        self.p2_4.setText("")
        self.p3_4.setText("")
        self.p4_4.setText("")
        self.p5_4.setText("")
        self.p6_4.setText("")

############################################################ secondary teacher qualification form

    def secqualification(self):    
        self.schooln = self.category_10.text()
        self.cate = self.category_4.text()
        self.owner = self.comboBox_9.currentText()
        try:

            self.s1t = int(self.S1t.text())
            self.S2t = int(self.s2t.text())
            self.s3t = int(self.s3t.text())
            self.s4t = int(self.s4t.text())
            self.s5t = int(self.s5t.text())
            self.s6t = int(self.p6t_2.text())
            self.ml = int(self.licencedm_2.text())
            self.fl = int(self.licencedf_2.text())
            self.cm = int(self.certificatem_2.text())
            self.cf = int(self.certificatef_2.text())
            self.dm = int(self.deplomam_2.text())
            self.df = int(self.deplomaf_2.text())
            self.bm = int(self.bachelorsm_3.text())
            self.bf = int(self.bachelorsf_2.text())
            self.mm = int(self.mastersm_2.text())
            self.mf = int(self.mastersf_2.text())
    
        except Exception:
            self.EnInteger()

        try:
            teachersecqualification(self.schooln,self.cate,self.owner,self.s1t,self.S2t,self.s3t,self.s4t,self.s5t,self.s6t,self.ml,self.fl,
                                    self.cm,self.cf,self.dm,self.df,self.bm,self.bf,self.mm,self.mf)
            self.saved()
        except Exception:
            self.failed()

    def resetsecqualification(self):

        self.category_10.setText("")
        self.category_4.setText("")
        self.S1t.setText("")
##        self.S2t.setText("")
        print('b')
##        self.s3t.setText("")
##        self.s4t.setText("")
##        self.s5t.setText("")
        self.p6t_2.setText("")
        self.licencedm_2.setText("")
        self.licencedf_2.setText("")
        self.certificatem_2.setText("")
        self.certificatef_2.setText("")
        self.deplomam_2.setText("")
        self.deplomaf_2.setText("")
        self.bachelorsm_3.setText("")
        self.bachelorsf_2.setText("")
        self.mastersm_2.setText("")
        self.mastersf_2.setText("")
        
############################################################ secondary school enrollment form

    def secenrollment(self):

        try:

            self.schooln = self.schooln_2.text()
            self.cate = self.category_3.text()
            self.owner = self.comboBox_15.currentText()
            self.s1m = int(self.s1m.text())
            self.s1f = int(self.s1f.text())
            self.s2m = int(self.s2m.text())
            self.s2f = int(self.s2f.text())
            self.s3m = int(self.s3m.text())
            self.s3f = int(self.s3f.text())
            self.s4m = int(self.s4m.text())
            self.s4f = int(self.s4f.text())
            self.s5m = int(self.s5m.text())
            self.s5f = int(self.s5f.text())
            self.s6m = int(self.s6m.text())
            self.s6f = int(self.p6f_2.text())
        except Exception:
            self.EnInteger()

        try:
            insertsecenrollment(self.schooln,self.cate,self.owner,self.s1m,self.s1f,self.s2m,self.s2f,self.s3m,self.s3f,
                                self.s4m,self.s4f,self.s5m,self.s5f,self.s6m,self.s6f)
            self.saved()
        except Exception:
            self.failed()

    def resetensec(self):
        self.schooln_2.setText("")
        self.category_3.setText("")
        self.s1m.setText("")
        self.s1f.setText("")
        self.s2m.setText("")
        self.s2f.setText("")
        self.s3m.setText("")
        self.s3f.setText("")
        self.s4m.setText("")
        self.s4f.setText("")
        self.s5m.setText("")
        self.s5f.setText("")
        self.s6m.setText("")
        self.s6f.setText("")

############################################################ classroom form
         
    def classroomform(self):
        try:
            self.schooln = self.category_8.text()
            self.cat2 = self.p1_3.text()
            self.own = self.comboBox_7.currentText()
            self.p1c = int(self.p1_2.text())
            self.p2c = int(self.p2_2.text())
            self.p3c = int(self.p3_2.text())
            self.p4c = int(self.p4_2.text())
            self.p5c = int(self.p5_2.text())
            self.p6c = int(self.p6_2.text())
            self.p7c = int(self.p7_2.text())
            self.cp = int(self.permanent.text())
            self.ct = int(self.temporary.text())
            self.atf = int(self.atfoundation.text())
            self.atw = int(self.atwindow.text())
            self.wp = int(self.wallpaltw.text())
            self.without = int(self.withoutstructures.text())
        except Exception:
            self.EnInteger()

        try:
            classroom(self.schooln,self.cat2,self.own,self.p1c,self.p2c,self.p3c,self.p4c,self.p5c,self.p6c,self.p7c,self.cp,self.ct,self.atf,self.atw,self.wp,
                      self.without)
            self.saved()
        except Exception:
            self.failed()
            
    def resetclassroom(self):
        self.category_8.setText("")
        self.p1_3.setText("")
        self.p1_2.setText("")
        self.p2_2.setText("")
        self.p3_2.setText("")
        self.p4_2.setText("")
        self.p5_2.setText("")
        self.p6_2.setText("")
        self.p7_2.setText("")
        self.permanent.setText("")
        self.temporary.setText("")
        self.atfoundation.setText("")
        self.atwindow.setText("")
        self.wallpaltw.setText("")
        self.withoutstructures.setText("")
        
############################################################ teacher housing form
    def teacherhousing(self):
        try:
            self.schoolnm = self.category_9.text()
            self.cat3 = self.category_5.text()
            self.owner3 = self.comboBox_8.currentText()

            self.cperm = int(self.permanent_2.text())
            self.ctemp = int(self.temporary_2.text())
            self.atfou = int(self.atfoundation_2.text())
            self.atwin = int(self.atwindow_2.text())
            self.atwall = int(self.wallpaltw_2.text())
        except Exception:
            self.EnInteger()

        try:
            housing(self.schoolnm,self.cat3,self.owner3,self.cperm,self.ctemp,self.atfou,self.atwin,self.atwall)
            self.saved()
        except Exception:
            self.failed()

    def resetteacherhousing(self):
        self.category_9.setText("")
        self.category_5.setText("")
        self.permanent_2.setText("")
        self.temporary_2.setText("")
        self.atfoundation_2.setText("")
        self.atwindow_2.setText("")
        self.wallpaltw_2.setText("")

############################################################ school facilities form

    def facilitiesform(self):
        self.schoolnme = self.category_7.text()
        self.ca = self.sciencelab_2.text()
        self.owner4 = self.comboBox_6.currentText()
        self.lib = self.library.text()
        self.slab = self.sciencelab.text()
        self.clab = self.complab.text()
        self.kit = self.kitchen.text()
        self.stuff = self.staffroom.text()
        self.admin = self.adminblock.text()
        self.dining = self.dinninghall.text()
        self.water = self.reliablesafewater.text()
        self.st = self.stores.text()
        self.ws = self.workshop.text()
        self.pg = self.playground.text()
        self.gd = self.garden.text()
        self.la = self.latrine.text()
        self.bac = self.bachelorsm_2.text()
        self.stan = int(self.stances.text())
        self.p1d = int(self.p1.text())
        self.p2d = int(self.p2.text())
        self.p3d = int(self.p3.text())
        self.p4d = int(self.p4.text())
        self.p5d = int(self.p5.text())
        self.p6d = int(self.p6.text())
        self.p7d = int(self.p7.text())


        try:
            facilities(self.schoolnme,self.ca,self.owner4,self.lib,self.slab,self.clab,self.kit,self.stuff,self.admin,self.dining,self.water,self.st,self.ws,
                       self.pg,self.gd,self.la,self.stan,self.bac,self.p1d,self.p2d,self.p3d,self.p4d,self.p5d,self.p6d,self.p7d)
            self.saved()

        except Exception:
            self.failed()

    def resetfacilities(self):
        self.category_7.setText("")
        self.sciencelab_2.setText("")
        self.library.setText("")
        self.sciencelab.setText("")
        self.complab.setText("")
        self.kitchen.setText("")
        self.staffroom.setText("")
        self.adminblock.setText("")
        self.dinninghall.setText("")
        self.reliablesafewater.setText("")
        self.stores.setText("")
        self.workshop.setText("")
        self.playground.setText("")
        self.garden.setText("")
        self.latrine.setText("")
        self.bachelorsm_2.setText("")
        self.p1.setText("")
        self.p2.setText("")
        self.p3.setText("")
        self.p4.setText("")
        self.p5.setText("")
        self.p6.setText("")
        self.p7.setText("")
        
      
############################################################ Qualification form functions

    def qualification(self):
        try:

            self.schooln = self.category_6.text()
            self.cat2 = self.category_2.text()
            self.owner2 = self.comboBox_5.currentText()
        except Exception:
            self.EnInteger()

        try:
            self.p1tr = int(self.p1t.text())
        except Exception:
            self.EnInteger2("P1 Teachers")
        try:
            self.p2tr = int(self.p2t.text())
        except Exception:
            self.EnInteger2("P2 Teachers")
        try:
            self.p3tr = int(self.p3t.text())
        except Exception:
            self.EnInteger2("P3 Teachers")
        try:
            self.p4tr = int(self.p4t.text())
        except Exception:
            self.EnInteger2("P4 Teachers")
        try:
            self.p5tr = int(self.p5t.text())
        except Exception:
            self.EnInteger2("P5 Teachers")
        try:
            self.p6tr = int(self.p6t.text())
        except Exception:
            self.EnInteger2("P6 Teachers")
        try:
            self.p7tr = int(self.p7t.text())
        except Exception:
            self.EnInteger2("P7 Teachers")
        try:
            self.lm = int(self.licencedm.text())
        except Exception:
            self.EnInteger2("Licensed Male")
        try:
            self.lf = int(self.licencedf.text())
        except Exception:
            self.EnInteger2("Licensed Female")
        try:
            self.catm = int(self.certificatem.text())
        except Exception:
            self.EnInteger2("Certificate Male")
        try:
            self.catf = int(self.certificatef.text())
        except Exception:
            self.EnInteger2("Certificate Female")
        try:
            self.dipm = int(self.deplomam.text())
        except Exception:
            self.EnInteger2("Deploma Male")
        try:
            self.dipf = int(self.deplomaf.text())
        except Exception:
            self.EnInteger2("Deploma Female")
        try:
            self.bacm = int(self.bachelorsm.text())
        except Exception:
            self.EnInteger2("Bachelors Male")
        try:
            self.bacf = int(self.bachelorsf.text())
        except Exception:
            self.EnInteger2("Machelors Female")
        try:
            self.mastm = int(self.mastersm.text())
        except Exception:
            self.EnInteger2("Masters Male")
        try:
            self.mastf = int(self.mastersf.text())
        except Exception:
            self.EnInteger2("Masters Female")

        try:
            teacherqualification(self.schooln,self.cat2,self.owner2,self.p1tr,self.p2tr,self.p3tr,self.p4tr,self.p5tr,self.p6tr,self.p7tr,self.lm,self.lf,
                                 self.catm,self.catf,self.dipm,self.dipf,self.bacm,self.bacf,self.mastm,self.mastf)
            self.saved()
            
        except Exception:
            self.failed()

    def resetqualification(self):
        self.category_6.setText("")
        self.category_2.setText("")
        self.p1t.setText("")
        self.p2t.setText("")
        self.p3t.setText("")
        self.p4t.setText("")
        self.p5t.setText("")
        self.p6t.setText("")
        self.p7t.setText("")
        self.p1t.setText("")
        self.p1t.setText("")
        self.licencedm.setText("")
        self.licencedf.setText("")
        self.certificatem.setText("")
        self.certificatef.setText("")
        self.deplomam.setText("")
        self.deplomaf.setText("")
        self.bachelorsm.setText("")
        self.bachelorsf.setText("")
        self.mastersm.setText("")
        self.mastersf.setText("")             
         
############################################################# enrollment form functions

    def enrollment(self):
        try:
            self.namesh = self.schooln.text()
            self.cat = self.category.text()
            self.owner = self.comboBox.currentText()
        except Exception:
            self.EnInteger()
        try:
            self.m1 = int(self.p1m.text())
        except Exception:
            self.EnInteger2("P1 Male")

        try:
            self.f1 = int(self.p1f.text())
        except Exception:
            self.EnInteger2("P1 Female")
            
        try:
            self.m2 = int(self.p2m.text())
        except Exception:
            self.EnInteger2("P2 Male")           
        try:
            self.f2 = int(self.p2f.text())
        except Exception:
            self.EnInteger2("P2 Female")
            
        try:
            self.m3 = int(self.p3m.text())
        except Exception:
            self.EnInteger2("P3 Male")
        try:   
            self.f3 = int(self.p3f.text())
        except Exception:
            self.EnInteger2("P3 Female")
        try:
            self.m4 = int(self.p4m.text())
        except Exception:
            self.EnInteger2("P4 Male")
        try:
            self.f4 = int(self.p4f.text())
        except Exception:
            self.EnInteger2("P4 Female")
        try:
            self.m5 = int(self.p5m.text())
        except Exception:
            self.EnInteger2("P4 Male")
        try:
            self.f5 = int(self.p5f.text())
        except Exception:
            self.EnInteger2("P5 Female")
        try:
            self.m6 = int(self.p6m.text())
        except Exception:
            self.EnInteger2("P6 Male")
        try:
            self.f6 = int(self.p6f.text())
        except Exception:
            self.EnInteger2("P6 Female")
        try:
            self.m7 = int(self.p7m.text())
        except Exception:
            self.EnInteger2("P7 Male")
        try:
            self.f7 = int(self.p7f.text())
        except Exception:
            self.EnInteger2("P7 Female")

        try:
            insertenrollment(self.namesh,self.cat,self.owner,self.m1,self.f1,self.m2,self.f2,self.m3,self.f3,
                             self.m4,self.f4,self.m5,self.f5,self.m6,self.f6,self.m7,self.f7)
            self.saved()
            
        except Exception:
            self.failed()
            
    def resetenrollment(self):
        self.schooln.setText("")
        self.category.setText("")
        self.p1m.setText("")
        self.p1f.setText("")
        self.p2m.setText("")
        self.p2f.setText("")
        self.p3m.setText("")
        self.p3f.setText("")
        self.p4m.setText("")
        self.p4f.setText("")
        self.p5m.setText("")
        self.p5f.setText("")
        self.p6m.setText("")
        self.p6f.setText("")
        self.p7m.setText("")
        self.p7f.setText("")
                
############################################################# School Entry form functions
    def addschool(self):
        try:
            self.emisno = int(self.emis.text())
            self.schoolname = self.school.text()
            self.county = self.subcounty.text()
            self.parish1 = self.parish.text()
            self.village1 = self.village.text()
            self.type1 = self.comboBox_2.currentText()
            insertschool(self.emisno,self.schoolname,self.county,self.parish1,self.village1,self.type1)
            self.saved()

        except Exception:
            self.failed()
            
    ############# Message Box
    def saved(self):
        
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('SUCCESS')
        mb.setText("SAVED        ")
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_()

    def failed(self):
        
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('FAILED')
        mb.setText("RECORD NOT SAVED")
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_()

    def EnInteger(self):
        
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('Warning')
        mb.setText("Check Values Entered")
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_()
        
    def Enemp(self):
        
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('Warning')
        mb.setText("Check Employess")
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_()

    def EnInteger2(self,name):
        
        mb = QMessageBox()
        mb.setIcon(QMessageBox.Information)
        mb.setWindowTitle('Warning')
        mb.setText("Check %s " % (name))
        mb.setStandardButtons(QMessageBox.Ok)
        mb.exec_()
    

    ############## END    
    def reset(self):
        self.emis.setText("")
        self.school.setText("")
        self.subcounty.setText("")
        self.parish.setText("")
        self.village.setText("")

########################################################### Teacher profile form functions
         
    def addteacher(self):
        self.school = self.school_4.text()
        self.county = self.subcounty_4.text()
        self.name = self.name_3.text()
        self.gender = self.gendercombo_3.currentText()
        self.dob = self.dateEdit.date()
        x = str(self.dob.year())
        y = str(self.dob.month())
        z = str(self.dob.day())
        self.dates = str(y+"/"+z+"/"+x)
        self.hdistrict = self.lineEdit_32.text()
        self.hsubcounty = self.lineEdit_42.text()
        self.hparish = self.lineEdit_43.text()
        self.hvillage = self.lineEdit_44.text()
        self.nok = self.lineEdit_33.text()
        self.qualification = self.lineEdit_34.text()
        self.reg = self.lineEdit_35.text()
        self.title = self.lineEdit_36.text()
        self.confirm = self.lineEdit_37.text()
        self.nin = self.lineEdit_38.text()

        try:
            self.emp = int(self.lineEdit_39.text())

        except Exception:
            self.Enemp()
            
        self.sup = self.lineEdit_40.text()
        self.tin = self.lineEdit_41.text()
        self.marital = self.comboBox_4.currentText()

        try:
            insertteacher(self.emp,self.school,self.county,self.qualification,self.name,self.gender,self.dates,self.marital,self.hdistrict,self.hsubcounty,
                          self.hparish,self.hvillage,self.nok,self.title,self.confirm,self.nin,self.sup,self.tin,self.reg)

            self.saved()

        except Exception:
            self.failed()
        
    def resetteacher(self):
        self.school_4.setText("")
        self.subcounty_4.setText("")
        self.name_3.setText("")
        self.lineEdit_32.setText("")
        self.lineEdit_42.setText("")
        self.lineEdit_43.setText("")
        self.lineEdit_44.setText("")
        self.lineEdit_33.setText("")
        self.lineEdit_34.setText("")
        self.lineEdit_35.setText("")
        self.lineEdit_36.setText("")
        self.lineEdit_37.setText("")
        self.lineEdit_38.setText("")
        self.lineEdit_39.setText("")
        self.lineEdit_40.setText("")
        self.lineEdit_41.setText("")

############################################ TABLE FUNCTIONS AND CONNECTIONS
    def schooltable(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM school"
        result = connection.execute(query)
        self.tableWidget_8.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_8.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_8.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def schooltable2(self):
        connection = sqlite3.connect("Education.db")
        x = "PRIMARY"
        result = connection.execute("SELECT * FROM school WHERE school_type = ?",(x,))
        self.tableWidget_8.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_8.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_8.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def schooltable3(self):
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM school WHERE school_type = ?",("SECONDARY",))
        self.tableWidget_8.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget_8.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_8.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()
        
    def teachertable(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM teacher"
        result = connection.execute(query)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def teachertable2(self):
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM teacher WHERE school_type = ?",("PRIMARY",))
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def teachertable3(self):
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM teacher WHERE school_type = ?",("SECONDARY",))
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()
        
    def enrollmenttable1(self):
        d = datetime.datetime.today()
        dt = d.year
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM enrollment WHERE datestamp = ?",(dt,))
        self.tableWidget_3.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_3.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def enrollmenttable1all(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM enrollment"
        result = connection.execute(query)
        self.tableWidget_3.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_3.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_3.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def qualificationtable(self):
        d = datetime.datetime.today()
        dt = d.year
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM qualifications WHERE datestamp = ?",(dt,))
        self.tableWidget_4.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_4.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_4.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def qualificationtableall(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM qualifications"
        result = connection.execute(query)
        self.tableWidget_4.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_4.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_4.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def facilitiestable(self):
        d = datetime.datetime.today()
        dt = d.year
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM facilities WHERE datestamp = ?",(dt,))
        self.tableWidget_5.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_5.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_5.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def facilitiestableall(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM facilities"
        result = connection.execute(query)
        self.tableWidget_5.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_5.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_5.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def classroomtable(self):
        d = datetime.datetime.today()
        dt = d.year
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM classroom WHERE datestamp = ?",(dt,))
        self.tableWidget_6.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_6.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_6.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def classroomtableall(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM classroom"
        result = connection.execute(query)
        self.tableWidget_6.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_6.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_6.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def housingtable(self):
        d = datetime.datetime.today()
        dt = d.year
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM classroom WHERE datestamp = ?",(dt,))
        self.tableWidget_7.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_7.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_7.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def housingtable2(self):
        d = datetime.datetime.today()
        dt = d.year
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM classroom WHERE datestamp = ? AND school_type = ?",(dt,"PRIMARY"))
        self.tableWidget_7.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_7.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_7.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def housingtable3(self):
        d = datetime.datetime.today()
        dt = d.year
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM classroom WHERE datestamp = ? AND school_type = ?",(dt,"SECONDARY"))
        self.tableWidget_7.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_7.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_7.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()
        
    def housingtableall(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM classroom"
        result = connection.execute(query)
        self.tableWidget_7.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_7.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_7.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

########################################################### SEC TABLE FUNCTIONS

    def secenrollmenttable(self):
        d = datetime.datetime.today()
        dt = d.year
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM secenrollment WHERE datestamp = ?",(dt,))
        self.tableWidget_12.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_12.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_12.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()
        
    def secenrollmenttableall(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM secenrollment"
        result = connection.execute(query)
        self.tableWidget_12.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_12.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_12.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

########################################################### SEC TEACHER QUALIFICATION TABLE

    def secqualificationtable(self):
        d = datetime.datetime.today()
        dt = d.year
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM secqualifications WHERE datestamp = ?",(dt,))
        self.tableWidget_13.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_13.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_13.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()
        
    def secqualificationtableall(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM secqualifications"
        result = connection.execute(query)
        self.tableWidget_13.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_13.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_13.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

######################################################### SEC SCHOOL FACILITIES

    def secfacilitiestable(self):
        d = datetime.datetime.today()
        dt = d.year
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM secfacilities WHERE datestamp = ?",(dt,))
        self.tableWidget_14.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_14.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_14.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()
        
    def secfacilitiestableall(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM secfacilities"
        result = connection.execute(query)
        self.tableWidget_14.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_14.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_14.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

######################################################### SEC CLASSROOM FORM

    def secclassroomtable(self):
        d = datetime.datetime.today()
        dt = d.year
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM secclassroom WHERE datestamp = ?",(dt,))
        self.tableWidget_15.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_15.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_15.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()
        
    def secclassroomtableall(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM secclassroom"
        result = connection.execute(query)
        self.tableWidget_15.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_15.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_15.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

################################################# TEACHERS ON LEAVE
        
    def leavetable(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM leave"
        result = connection.execute(query)
        self.tableWidget_2.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()
        
    def leavetable2(self):
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM leave WHERE school_type = ?",("PRIMARY",))
        self.tableWidget_2.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def leavetable3(self):
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM leave WHERE school_type = ?",("SECONDARY",))
        self.tableWidget_2.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

################################################# TEACHERS ON LEAVE
        
    def retiredtable(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM retired"
        result = connection.execute(query)
        self.tableWidget_9.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_9.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_9.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def retiredtable2(self):
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM retired WHERE school_type = ?",("PRIMARY",))
        self.tableWidget_9.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_9.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_9.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def retiredtable3(self):
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM retired WHERE school_type = ?",("SECONDARY",))
        self.tableWidget_9.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_9.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_9.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

################################################# DECEASED TEACHERS
        
    def deceasedtable(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM deceased"
        result = connection.execute(query)
        self.tableWidget_10.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_10.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_10.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def deceasedtable2(self):
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM deceased WHERE school_type = ?",("PRIMARY",))
        self.tableWidget_10.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_10.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_10.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def deceasedtable3(self):
        connection = sqlite3.connect("Education.db")
        result = connection.execute("SELECT * FROM deceased WHERE school_type = ?",("SECONDARY",))
        self.tableWidget_10.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_10.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_10.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()

    def abscondedtable(self):
        connection = sqlite3.connect("Education.db")
        query = "SELECT * FROM absconded"
        result = connection.execute(query)
        self.tableWidget_11.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget_11.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget_11.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        connection.close()
        
#####################################################################################################################################################################

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LIRA DISTRICT MANAGMENT SYSTEM"))
        self.label_3.setText(_translate("MainWindow", "DISTRICT SUMMARY"))
        self.label_4.setText(_translate("MainWindow", "ENROLLMENT"))
        self.label_5.setText(_translate("MainWindow", "MALE"))
        self.label_6.setText(_translate("MainWindow", "FEMALE"))
        self.label_7.setText(_translate("MainWindow", "TOTAL NUMBER OF CLASSROOMS"))
        self.label_8.setText(_translate("MainWindow", "STUDENT CLASSROOM RATIO"))
        self.label_9.setText(_translate("MainWindow", "LATRINE STANCES"))
        self.label_10.setText(_translate("MainWindow", "NUMBER OF TEACHERS"))
        self.label_11.setText(_translate("MainWindow", "MALE"))
        self.label_12.setText(_translate("MainWindow", "FEMALE"))
        self.label_13.setText(_translate("MainWindow", "TEACHERS BY QUALIFICATION"))
        self.label_14.setText(_translate("MainWindow", "CERTIFICATE"))
        self.label_15.setText(_translate("MainWindow", "BACHELORS"))
        self.label_16.setText(_translate("MainWindow", "MASTERS AND ABOVE "))
        self.label_17.setText(_translate("MainWindow", "TOTAL"))
        self.label_18.setText(_translate("MainWindow", "PUPIL LATRINE STANCE RATIO"))
        self.label_19.setText(_translate("MainWindow", "TOTAL"))
        self.label_20.setText(_translate("MainWindow", "DEPLOMA"))
        self.label_265.setText(_translate("MainWindow", "ENROLLMENT CHART"))
        self.Enterdata.setText(_translate("MainWindow", "ENTER DATA"))
        self.Reports.setText(_translate("MainWindow", "REPORTS"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" color:#ffffff;\">NOTE:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#ffffff;\">The information displayed on this page is a summary of the data stored in the database. it will reset to zero at the end of every year as it waits for the years data to be entered.</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; color:#ffffff;\">Thank you</span></p></body></html>"))
        self.Reports_2.setText(_translate("MainWindow", "TABLES"))
        self.Reports_3.setText(_translate("MainWindow", "SEARCH TEACHER DATABASE"))
        self.Reports_4.setText(_translate("MainWindow", "ADD NEW USER"))
        self.teacherqualificationform.setText(_translate("MainWindow", "TEACHER QUALIFICATION FORM"))
        self.label_21.setText(_translate("MainWindow", "DATA ENTRY FORMS"))
        self.schoolenrollmentform.setText(_translate("MainWindow", "SCHOOL ENROLLMENT FORM"))
        self.addnewteacher.setText(_translate("MainWindow", "ADD NEW TEACHER"))
        self.schoolfacilitiesform.setText(_translate("MainWindow", "SCHOOL FACILITIES FORM"))
        self.addnewschool.setText(_translate("MainWindow", "ADD NEW SCHOOL"))
        self.teacherhousingform.setText(_translate("MainWindow", "TEACHER HOUSING FORM"))
        self.schoolclassroomform.setText(_translate("MainWindow", "SCHOOL CLASSROOM FORM"))
        self.pushButton_8.setText(_translate("MainWindow", "HOME"))
        self.label_47.setText(_translate("MainWindow", "GENERAL FORMS"))
        self.label_48.setText(_translate("MainWindow", "PRIMARY SCHOOL  FORMS"))
        self.pushButton_15.setText(_translate("MainWindow", "SECONDARY ENROLLMENT FORM"))
        self.label_49.setText(_translate("MainWindow", "SECONADRY SCHOOL  FORMS"))
        self.pushButton_30.setText(_translate("MainWindow", "SECONDARY QUALIFICATION FORM"))
        self.pushButton_31.setText(_translate("MainWindow", "SECONDARY FACILITIES FORM"))
        self.schoolclassroomform_2.setText(_translate("MainWindow", "SECONDARY CLASSROOM FORM"))
        self.label_22.setText(_translate("MainWindow", "SCHOOL ENTRY FORM"))
        self.home.setText(_translate("MainWindow", "Home"))
        self.pushButton_4.setText(_translate("MainWindow", "View School Table"))
        self.label_25.setText(_translate("MainWindow", "EMIS NO"))
        self.label_26.setText(_translate("MainWindow", "SCHOOL"))
        self.label_27.setText(_translate("MainWindow", "SUB-COUNTY"))
        self.label_28.setText(_translate("MainWindow", "PARISH "))
        self.label_29.setText(_translate("MainWindow", "VILLAGE"))
        self.save.setText(_translate("MainWindow", "SAVE"))
        self.label_50.setText(_translate("MainWindow", "SCHOOL TYPE"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "PRIMARY"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "SECONDARY"))
        self.pushButton_34.setText(_translate("MainWindow", "SEARCH"))
        self.save_2.setText(_translate("MainWindow", "SAVE AND NEXT"))
        self.pushButton_2.setText(_translate("MainWindow", "Back"))
        self.label_30.setText(_translate("MainWindow", "LIRA DISTRICT LOCAL GOVERNMENT DEPARTMENT TEACHERS PROFILE FORM"))
        self.label_85.setText(_translate("MainWindow", "School"))
        self.label_86.setText(_translate("MainWindow", "Sub-County"))
        self.label_87.setText(_translate("MainWindow", "Name"))
        self.label_88.setText(_translate("MainWindow", "Gender"))
        self.label_89.setText(_translate("MainWindow", "Date Of Birth"))
        self.label_91.setText(_translate("MainWindow", "Home District"))
        self.label_92.setText(_translate("MainWindow", "Next of Kin"))
        self.label_93.setText(_translate("MainWindow", "Qualification"))
        self.label_94.setText(_translate("MainWindow", "Reg. No"))
        self.label_95.setText(_translate("MainWindow", "Title"))
        self.label_96.setText(_translate("MainWindow", "Confirmation status"))
        self.label_97.setText(_translate("MainWindow", "National Identification No (NIN)"))
        self.label_98.setText(_translate("MainWindow", "Employee No"))
        self.label_99.setText(_translate("MainWindow", "Supplier No"))
        self.label_100.setText(_translate("MainWindow", "Tax Identification No (TIN)"))
        self.label_101.setText(_translate("MainWindow", "Marital Status"))
        self.save_4.setText(_translate("MainWindow", "Save"))
        self.gendercombo_3.setItemText(0, _translate("MainWindow", "Male"))
        self.gendercombo_3.setItemText(1, _translate("MainWindow", "Female"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Single"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Married"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Widowed"))
        self.label_102.setText(_translate("MainWindow", "Home Subcounty"))
        self.label_103.setText(_translate("MainWindow", "Home Parish"))
        self.label_104.setText(_translate("MainWindow", "Home Village"))
        self.label_105.setText(_translate("MainWindow", "MM-DD-YY"))
        self.pushButton_110.setText(_translate("MainWindow", "SEARCH"))
        self.save_12.setText(_translate("MainWindow", "Save and Next"))
        self.pushButton_125.setText(_translate("MainWindow", "UPLOAD"))
        self.home_4.setText(_translate("MainWindow", "Home"))
        self.back_3.setText(_translate("MainWindow", "Back"))
        self.viewteachertable_3.setText(_translate("MainWindow", "View Teacher Table"))
        self.home_5.setText(_translate("MainWindow", "Home"))
        self.back_4.setText(_translate("MainWindow", "Back"))
        self.pushButton_35.setText(_translate("MainWindow", "View Enrollment Table"))
        self.label_112.setText(_translate("MainWindow", "Name of School"))
        self.label_115.setText(_translate("MainWindow", "Category"))
        self.label_116.setText(_translate("MainWindow", "Ownership"))
        self.label_117.setText(_translate("MainWindow", "P1 Male"))
        self.label_118.setText(_translate("MainWindow", "P1 Female"))
        self.label_119.setText(_translate("MainWindow", "P2 Male"))
        self.label_120.setText(_translate("MainWindow", "P2 Female"))
        self.label_121.setText(_translate("MainWindow", "P3 Female"))
        self.label_122.setText(_translate("MainWindow", "P3 Male"))
        self.label_123.setText(_translate("MainWindow", "P4 Female"))
        self.label_124.setText(_translate("MainWindow", "P4 Male"))
        self.label_125.setText(_translate("MainWindow", "P5 Female"))
        self.label_126.setText(_translate("MainWindow", "P5 Male"))
        self.label_127.setText(_translate("MainWindow", "P6 Female"))
        self.label_128.setText(_translate("MainWindow", "P6 Male"))
        self.label_129.setText(_translate("MainWindow", "P7 Female"))
        self.label_130.setText(_translate("MainWindow", "P7 Male"))
        self.save_5.setText(_translate("MainWindow", "Save"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Government"))
        self.comboBox.setItemText(1, _translate("MainWindow", "NGO"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Community"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Private"))
        self.save_15.setText(_translate("MainWindow", "Save and Next"))
        self.label_133.setText(_translate("MainWindow", "SECTION A: SCHOOL ENROLLMENT FORM"))
        self.label_146.setText(_translate("MainWindow", "SECTION B: TEACHERS QUALIFICATION FORM"))
        self.home_6.setText(_translate("MainWindow", "Home"))
        self.back_5.setText(_translate("MainWindow", "Back"))
        self.pushButton_36.setText(_translate("MainWindow", "View Qualification Table"))
        self.label_147.setText(_translate("MainWindow", "Name of School"))
        self.label_150.setText(_translate("MainWindow", "Category"))
        self.label_151.setText(_translate("MainWindow", "Ownership"))
        self.label_152.setText(_translate("MainWindow", "P1 Teachers"))
        self.label_153.setText(_translate("MainWindow", "P2 Teachers"))
        self.label_154.setText(_translate("MainWindow", "P3 Teachers"))
        self.label_155.setText(_translate("MainWindow", "P4 Teachers"))
        self.label_156.setText(_translate("MainWindow", "P5 Teachers"))
        self.label_157.setText(_translate("MainWindow", "P6 Teachers"))
        self.label_158.setText(_translate("MainWindow", "P7 Teachers"))
        self.save_6.setText(_translate("MainWindow", "Save"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Government"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "NGO"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "Community"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "Private"))
        self.label_160.setText(_translate("MainWindow", "Licensed M"))
        self.label_161.setText(_translate("MainWindow", "Licenced F"))
        self.label_162.setText(_translate("MainWindow", "Certificate M"))
        self.label_163.setText(_translate("MainWindow", "Certificate F"))
        self.label_164.setText(_translate("MainWindow", "Diploma M"))
        self.label_165.setText(_translate("MainWindow", "Diploma F"))
        self.label_166.setText(_translate("MainWindow", "Bachelors M"))
        self.label_167.setText(_translate("MainWindow", "Bachelors F"))
        self.label_168.setText(_translate("MainWindow", "Masters and above M"))
        self.label_169.setText(_translate("MainWindow", "Masters and above F"))
        self.save_16.setText(_translate("MainWindow", "Save and Next"))
        self.label_176.setText(_translate("MainWindow", "SECTION C: SCHOOL FACILITIES FORM"))
        self.home_7.setText(_translate("MainWindow", "Home"))
        self.back_6.setText(_translate("MainWindow", "Back"))
        self.pushButton_37.setText(_translate("MainWindow", "View Facilities Table"))
        self.label_177.setText(_translate("MainWindow", "Name of School"))
        self.label_180.setText(_translate("MainWindow", "Category"))
        self.label_181.setText(_translate("MainWindow", "Ownership"))
        self.label_182.setText(_translate("MainWindow", "Library"))
        self.label_183.setText(_translate("MainWindow", "Science Laboratory"))
        self.label_184.setText(_translate("MainWindow", "Computer Laboratory"))
        self.label_185.setText(_translate("MainWindow", "Kitchen"))
        self.label_186.setText(_translate("MainWindow", "Stuffroom"))
        self.label_187.setText(_translate("MainWindow", "Administration Block"))
        self.label_188.setText(_translate("MainWindow", "Dining Hall"))
        self.label_189.setText(_translate("MainWindow", "Reliable Safe Water Supply"))
        self.save_7.setText(_translate("MainWindow", "Save"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "Government"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "NGO"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "Community"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "Private"))
        self.label_190.setText(_translate("MainWindow", "Stores"))
        self.label_191.setText(_translate("MainWindow", "Workshop"))
        self.label_192.setText(_translate("MainWindow", "Playground"))
        self.label_193.setText(_translate("MainWindow", "School Garden"))
        self.label_194.setText(_translate("MainWindow", "Latrine/Toilet"))
        self.label_195.setText(_translate("MainWindow", "Number of Stances"))
        self.label_196.setText(_translate("MainWindow", "Handwashing Facility"))
        self.label_197.setText(_translate("MainWindow", "P1 Desks"))
        self.label_198.setText(_translate("MainWindow", "P2 Desks"))
        self.label_199.setText(_translate("MainWindow", "P3 Desk"))
        self.label_200.setText(_translate("MainWindow", "P4 Desk"))
        self.label_201.setText(_translate("MainWindow", "P5 Desk"))
        self.label_202.setText(_translate("MainWindow", "P6 Desk"))
        self.label_203.setText(_translate("MainWindow", "P7 Desk"))
        self.save_17.setText(_translate("MainWindow", "Save and Next"))
        self.label_210.setText(_translate("MainWindow", "SECTION D: SCHOOL CLASSROOM FORM"))
        self.label_211.setText(_translate("MainWindow", "Name of School"))
        self.label_214.setText(_translate("MainWindow", "Category"))
        self.label_215.setText(_translate("MainWindow", "Ownership"))
        self.label_216.setText(_translate("MainWindow", "P1 Classes"))
        self.label_217.setText(_translate("MainWindow", "P2 Classes"))
        self.label_218.setText(_translate("MainWindow", "P3 Classes"))
        self.label_219.setText(_translate("MainWindow", "P4 Classes"))
        self.label_220.setText(_translate("MainWindow", "P5 Classes"))
        self.label_221.setText(_translate("MainWindow", "P6 Classes"))
        self.label_222.setText(_translate("MainWindow", "P7 Classes"))
        self.save_8.setText(_translate("MainWindow", "Save"))
        self.comboBox_7.setItemText(0, _translate("MainWindow", "Government"))
        self.comboBox_7.setItemText(1, _translate("MainWindow", "NGO"))
        self.comboBox_7.setItemText(2, _translate("MainWindow", "Community"))
        self.comboBox_7.setItemText(3, _translate("MainWindow", "Private"))
        self.label_224.setText(_translate("MainWindow", "Complete Permanent"))
        self.label_225.setText(_translate("MainWindow", "Complete Temporary"))
        self.label_226.setText(_translate("MainWindow", "At Foundation"))
        self.label_227.setText(_translate("MainWindow", "At Window Level"))
        self.label_228.setText(_translate("MainWindow", "At Wall plate and obove"))
        self.label_229.setText(_translate("MainWindow", "Number of classes without structures"))
        self.save_18.setText(_translate("MainWindow", "Save and Nexr"))
        self.home_8.setText(_translate("MainWindow", "Home"))
        self.back_7.setText(_translate("MainWindow", "Back"))
        self.pushButton_38.setText(_translate("MainWindow", "View Classroom Table"))
        self.home_9.setText(_translate("MainWindow", "Home"))
        self.back_8.setText(_translate("MainWindow", "Back"))
        self.pushButton_50.setText(_translate("MainWindow", "View Housing Table"))
        self.label_237.setText(_translate("MainWindow", "SECTION E: TEACHER HOUSING FORM"))
        self.label_238.setText(_translate("MainWindow", "Name of School"))
        self.label_241.setText(_translate("MainWindow", "Category"))
        self.label_242.setText(_translate("MainWindow", "Ownership"))
        self.save_9.setText(_translate("MainWindow", "Save"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "Government"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "NGO"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "Community"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "Private"))
        self.label_243.setText(_translate("MainWindow", "Complete Permanent"))
        self.label_244.setText(_translate("MainWindow", "Complete Temporary"))
        self.label_245.setText(_translate("MainWindow", "At Foundation"))
        self.label_246.setText(_translate("MainWindow", "At Window Level"))
        self.label_247.setText(_translate("MainWindow", "At Wall plate and obove"))
        self.save_19.setText(_translate("MainWindow", "Save and Next"))
        self.pushButton_7.setText(_translate("MainWindow", "SCHOOL FACILITIES TABLE"))
        self.pushButton_9.setText(_translate("MainWindow", "TEACHER HOUSING TABLE"))
        self.pushButton_5.setText(_translate("MainWindow", "TEACHER PROFILE TABLE"))
        self.pushButton_6.setText(_translate("MainWindow", "STUDENT ENROLLMENT TABLE"))
        self.pushButton_10.setText(_translate("MainWindow", "CLASSROOM TABLE"))
        self.pushButton_11.setText(_translate("MainWindow", "DECEASED TEACHER TABLE"))
        self.pushButton_3.setText(_translate("MainWindow", "SCHOOL TABLE"))
        self.pushButton_13.setText(_translate("MainWindow", "ABSONDED TEACHER TABLE"))
        self.pushButton.setText(_translate("MainWindow", "Home"))
        self.label_23.setText(_translate("MainWindow", "TABLES HOME"))
        self.pushButton_14.setText(_translate("MainWindow", "TEACHER QUALIFICATION TABLE"))
        self.pushButton_16.setText(_translate("MainWindow", "RETIRED TEACHER TABLE"))
        self.pushButton_17.setText(_translate("MainWindow", "TEACHERS ON LEAVE TABLE"))
        self.label_33.setText(_translate("MainWindow", "General"))
        self.label_34.setText(_translate("MainWindow", "PRIMARY"))
        self.pushButton_12.setText(_translate("MainWindow", "SEC CLASSROMM TABLE"))
        self.pushButton_20.setText(_translate("MainWindow", "SEC STUDENT ENROLLMENT TABLE"))
        self.pushButton_21.setText(_translate("MainWindow", "SEC SCHOOL FACILITIES TABLE"))
        self.pushButton_120.setText(_translate("MainWindow", "SEC TEACHER QUALIFICATION TABLE"))
        self.label_35.setText(_translate("MainWindow", "SECONDARY"))
        self.tableWidget_8.setSortingEnabled(True)
        item = self.tableWidget_8.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Emis No"))
        item = self.tableWidget_8.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School Name"))
        item = self.tableWidget_8.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_8.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_8.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Parish"))
        item = self.tableWidget_8.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Village"))
        self.label_66.setText(_translate("MainWindow", "SCHOOL TABLE"))
        self.pushButton_65.setText(_translate("MainWindow", "HOME"))
        self.pushButton_66.setText(_translate("MainWindow", "BACK"))
        self.pushButton_68.setText(_translate("MainWindow", "PRIMARY"))
        self.pushButton_69.setText(_translate("MainWindow", "SECONDARY"))
        self.label_31.setText(_translate("MainWindow", "Sort By"))
        self.label_24.setText(_translate("MainWindow", "TEACHER PROFILE TABLE"))
        self.pushButton_18.setText(_translate("MainWindow", "HOME"))
        self.pushButton_19.setText(_translate("MainWindow", "BACK"))
        self.pushButton_62.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_71.setText(_translate("MainWindow", "SECONDARY"))
        self.pushButton_73.setText(_translate("MainWindow", "PRIMARY"))
        self.label_32.setText(_translate("MainWindow", "Sort By"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Employee No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Emis No"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Qualification"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Date of Retirment"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Photo"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Marital Status"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Home District"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Home Subcounty"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Home Parish"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Home Village"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Next of Kin"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Confirmation Status"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "title"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "NIN"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "Supplier No"))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "TIN"))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "Date Stamp"))
        self.tableWidget_3.setSortingEnabled(True)
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School Name"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Emis number"))
        item = self.tableWidget_3.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_3.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Village"))
        item = self.tableWidget_3.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Parish"))
        item = self.tableWidget_3.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_3.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget_3.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Ownership"))
        item = self.tableWidget_3.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "P1M"))
        item = self.tableWidget_3.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "P1F"))
        item = self.tableWidget_3.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "P2M"))
        item = self.tableWidget_3.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "P2F"))
        item = self.tableWidget_3.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "P3M"))
        item = self.tableWidget_3.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "P3F"))
        item = self.tableWidget_3.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "P4M"))
        item = self.tableWidget_3.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "P4F"))
        item = self.tableWidget_3.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "P5M"))
        item = self.tableWidget_3.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "P5F"))
        item = self.tableWidget_3.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "P6M"))
        item = self.tableWidget_3.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "P6F"))
        item = self.tableWidget_3.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "P7M"))
        item = self.tableWidget_3.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "P7F"))
        item = self.tableWidget_3.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "M Total"))
        item = self.tableWidget_3.horizontalHeaderItem(24)
        item.setText(_translate("MainWindow", "F total"))
        item = self.tableWidget_3.horizontalHeaderItem(25)
        item.setText(_translate("MainWindow", "Date Stamp"))
        self.pushButton_39.setText(_translate("MainWindow", "HOME"))
        self.pushButton_40.setText(_translate("MainWindow", "BACK"))
        self.pushButton_60.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_61.setText(_translate("MainWindow", "SHOW ALL"))
        self.label_61.setText(_translate("MainWindow", "PRIMARY SCHOOL ENROLLMENT TABLE"))
        self.tableWidget_4.setSortingEnabled(True)
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School Name"))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_4.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Emis No"))
        item = self.tableWidget_4.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Village"))
        item = self.tableWidget_4.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Parish"))
        item = self.tableWidget_4.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_4.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget_4.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Ownership"))
        item = self.tableWidget_4.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "P1 T"))
        item = self.tableWidget_4.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "P2 T"))
        item = self.tableWidget_4.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "P3 T"))
        item = self.tableWidget_4.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "P4 T"))
        item = self.tableWidget_4.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "P5 T"))
        item = self.tableWidget_4.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "P7 T"))
        item = self.tableWidget_4.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "M Licensed"))
        item = self.tableWidget_4.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "F Licensed"))
        item = self.tableWidget_4.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "M Deploma"))
        item = self.tableWidget_4.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "F Deploma"))
        item = self.tableWidget_4.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "M Certificate"))
        item = self.tableWidget_4.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "F Certificate"))
        item = self.tableWidget_4.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "M Bachelors"))
        item = self.tableWidget_4.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "F Bachelors"))
        item = self.tableWidget_4.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "M Masters +"))
        item = self.tableWidget_4.horizontalHeaderItem(24)
        item.setText(_translate("MainWindow", "F Masters +"))
        self.pushButton_41.setText(_translate("MainWindow", "HOME"))
        self.pushButton_42.setText(_translate("MainWindow", "BACK"))
        self.pushButton_58.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_59.setText(_translate("MainWindow", "SHOW ALL"))
        self.label_62.setText(_translate("MainWindow", "PRIMARY TEACHER QUALIFICATION TABLE"))
        self.tableWidget_5.setSortingEnabled(True)
        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School Name"))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Emis No"))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "School type"))
        item = self.tableWidget_5.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Village"))
        item = self.tableWidget_5.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Parish"))
        item = self.tableWidget_5.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_5.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget_5.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Ownership"))
        item = self.tableWidget_5.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Library"))
        item = self.tableWidget_5.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Science Lab"))
        item = self.tableWidget_5.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Computer Lab"))
        item = self.tableWidget_5.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Kitchen"))
        item = self.tableWidget_5.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Adminstration Block"))
        item = self.tableWidget_5.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Dinning Hall"))
        item = self.tableWidget_5.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Safe Water"))
        item = self.tableWidget_5.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Hand Washing Facility"))
        item = self.tableWidget_5.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "P1 Desk"))
        item = self.tableWidget_5.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "P2 Desk"))
        item = self.tableWidget_5.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "P3 Desk"))
        item = self.tableWidget_5.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "P4 Desk"))
        item = self.tableWidget_5.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "P5 Desk"))
        item = self.tableWidget_5.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "P6 Desk"))
        item = self.tableWidget_5.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "Date Stamp"))
        self.pushButton_43.setText(_translate("MainWindow", "HOME"))
        self.pushButton_44.setText(_translate("MainWindow", "BACK"))
        self.pushButton_56.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_57.setText(_translate("MainWindow", "SHOW ALL"))
        self.label_63.setText(_translate("MainWindow", "PRIMARY SCHOOL FACILITIES TABLE"))
        self.tableWidget_6.setSortingEnabled(True)
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School Name"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "school Type"))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Village"))
        item = self.tableWidget_6.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Parish"))
        item = self.tableWidget_6.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_6.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget_6.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Ownership"))
        item = self.tableWidget_6.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "P1 Classroom"))
        item = self.tableWidget_6.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "P2 Classroom"))
        item = self.tableWidget_6.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "P3 Classroom"))
        item = self.tableWidget_6.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "P4 Classroom"))
        item = self.tableWidget_6.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "P5 Classroom"))
        item = self.tableWidget_6.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "P6 Classroom"))
        item = self.tableWidget_6.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "P7 Classroom"))
        item = self.tableWidget_6.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Total Classroom"))
        item = self.tableWidget_6.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Complete Permanent"))
        item = self.tableWidget_6.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "Complete Temporary"))
        item = self.tableWidget_6.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "At Foundation"))
        item = self.tableWidget_6.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "At Window Level"))
        item = self.tableWidget_6.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "Date Stamp"))
        self.pushButton_45.setText(_translate("MainWindow", "HOME"))
        self.pushButton_46.setText(_translate("MainWindow", "BACK"))
        self.pushButton_54.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_55.setText(_translate("MainWindow", "SHOW ALL"))
        self.label_64.setText(_translate("MainWindow", "PRIMARY SCHOOL CLASSROOM TABLE"))
        self.tableWidget_7.setSortingEnabled(True)
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School Name"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "school Type"))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Village"))
        item = self.tableWidget_7.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Parish"))
        item = self.tableWidget_7.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_7.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget_7.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Ownership"))
        item = self.tableWidget_7.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Complete Permanent"))
        item = self.tableWidget_7.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Complete Temporary"))
        item = self.tableWidget_7.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "At Window Level"))
        item = self.tableWidget_7.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Date Stamp"))
        self.pushButton_47.setText(_translate("MainWindow", "HOME"))
        self.pushButton_48.setText(_translate("MainWindow", "BACK"))
        self.pushButton_49.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_53.setText(_translate("MainWindow", "SHOW ALL"))
        self.pushButton_86.setText(_translate("MainWindow", "SECONDARY"))
        self.pushButton_88.setText(_translate("MainWindow", "PRIMARY"))
        self.label_37.setText(_translate("MainWindow", "Sort By"))
        self.label_65.setText(_translate("MainWindow", "TEACHER HOUSING TABLE"))
        self.tableWidget_12.setSortingEnabled(True)
        item = self.tableWidget_12.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_12.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School Name"))
        item = self.tableWidget_12.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Emis No"))
        item = self.tableWidget_12.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_12.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Village"))
        item = self.tableWidget_12.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Parish"))
        item = self.tableWidget_12.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_12.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Ownership"))
        item = self.tableWidget_12.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "S1 M"))
        item = self.tableWidget_12.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "S1 F"))
        item = self.tableWidget_12.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "S2 M"))
        item = self.tableWidget_12.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "S2F"))
        item = self.tableWidget_12.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "S3 F"))
        item = self.tableWidget_12.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "S3F"))
        item = self.tableWidget_12.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "S4 M"))
        item = self.tableWidget_12.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "S4 F"))
        item = self.tableWidget_12.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "S5 M"))
        item = self.tableWidget_12.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "S5 F"))
        item = self.tableWidget_12.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "S6 F"))
        item = self.tableWidget_12.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "M Total"))
        item = self.tableWidget_12.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "F Total"))
        item = self.tableWidget_12.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "Date Stamp"))
        self.pushButton_67.setText(_translate("MainWindow", "HOME"))
        self.pushButton_74.setText(_translate("MainWindow", "BACK"))
        self.pushButton_75.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_76.setText(_translate("MainWindow", "SHOW ALL"))
        self.label_67.setText(_translate("MainWindow", "SECONDARY SCHOOL ENROLLMENT TABLE"))
        self.label_68.setText(_translate("MainWindow", "SECONDARY SCHOOL TEACHER QUALIFICATION TABLE"))
        self.pushButton_77.setText(_translate("MainWindow", "HOME"))
        self.pushButton_78.setText(_translate("MainWindow", "BACK"))
        self.pushButton_79.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_80.setText(_translate("MainWindow", "SHOW ALL"))
        self.tableWidget_13.setSortingEnabled(True)
        item = self.tableWidget_13.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_13.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School Name"))
        item = self.tableWidget_13.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_13.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Emis No"))
        item = self.tableWidget_13.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Village"))
        item = self.tableWidget_13.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Parish"))
        item = self.tableWidget_13.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_13.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget_13.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Ownership"))
        item = self.tableWidget_13.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "S1 Teachers"))
        item = self.tableWidget_13.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "S2 Teachers"))
        item = self.tableWidget_13.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "S3 Teachers"))
        item = self.tableWidget_13.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "S4 Teachers"))
        item = self.tableWidget_13.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "S6 Teachers"))
        item = self.tableWidget_13.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Total"))
        item = self.tableWidget_13.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "M Licensed"))
        item = self.tableWidget_13.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "F Licensed"))
        item = self.tableWidget_13.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "F Certificate"))
        item = self.tableWidget_13.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget_13.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "M Bachelors"))
        item = self.tableWidget_13.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "M Masters and Above"))
        item = self.tableWidget_13.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "F Masters and Above"))
        item = self.tableWidget_13.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "Date Stamp"))
        self.label_69.setText(_translate("MainWindow", "SECONDARY SCHOOL FACILITIES TABLE"))
        self.pushButton_81.setText(_translate("MainWindow", "HOME"))
        self.pushButton_82.setText(_translate("MainWindow", "BACK"))
        self.pushButton_83.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_84.setText(_translate("MainWindow", "SHOW ALL"))
        self.tableWidget_14.setSortingEnabled(True)
        item = self.tableWidget_14.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_14.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School Name"))
        item = self.tableWidget_14.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Emis No"))
        item = self.tableWidget_14.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_14.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Village"))
        item = self.tableWidget_14.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Parish"))
        item = self.tableWidget_14.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_14.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "category"))
        item = self.tableWidget_14.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Ownership"))
        item = self.tableWidget_14.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Library"))
        item = self.tableWidget_14.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Science Lab"))
        item = self.tableWidget_14.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Computer Lab"))
        item = self.tableWidget_14.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Staff Room"))
        item = self.tableWidget_14.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Administration Block"))
        item = self.tableWidget_14.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Dinning Hall"))
        item = self.tableWidget_14.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Safe Water"))
        item = self.tableWidget_14.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Stores"))
        item = self.tableWidget_14.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Playground"))
        item = self.tableWidget_14.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "School Garden"))
        item = self.tableWidget_14.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "Latrine"))
        item = self.tableWidget_14.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "Number of Stances"))
        item = self.tableWidget_14.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "Handwashing Facilities"))
        item = self.tableWidget_14.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "S1 Desk"))
        item = self.tableWidget_14.horizontalHeaderItem(23)
        item.setText(_translate("MainWindow", "S2 Desk"))
        item = self.tableWidget_14.horizontalHeaderItem(24)
        item.setText(_translate("MainWindow", "S3 Desk"))
        item = self.tableWidget_14.horizontalHeaderItem(25)
        item.setText(_translate("MainWindow", "S4 Desk"))
        item = self.tableWidget_14.horizontalHeaderItem(26)
        item.setText(_translate("MainWindow", "S6 Desk"))
        item = self.tableWidget_14.horizontalHeaderItem(27)
        item.setText(_translate("MainWindow", "Date Stamp"))
        self.tableWidget_15.setSortingEnabled(True)
        item = self.tableWidget_15.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_15.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School Name"))
        item = self.tableWidget_15.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Emis No"))
        item = self.tableWidget_15.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_15.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Village"))
        item = self.tableWidget_15.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Parish"))
        item = self.tableWidget_15.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_15.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableWidget_15.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Ownership"))
        item = self.tableWidget_15.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "S1 Classroom"))
        item = self.tableWidget_15.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "S2 Classroom"))
        item = self.tableWidget_15.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "S3 Classroom"))
        item = self.tableWidget_15.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "S4 Classroom"))
        item = self.tableWidget_15.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "S5 Classroom"))
        item = self.tableWidget_15.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "S6 Classroom"))
        item = self.tableWidget_15.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Total Classrooms"))
        item = self.tableWidget_15.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Complete permanent"))
        item = self.tableWidget_15.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Complete Temporary"))
        item = self.tableWidget_15.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "At Window Level"))
        item = self.tableWidget_15.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "At WallPlate and Above"))
        item = self.tableWidget_15.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "Classroom Without Strutures"))
        item = self.tableWidget_15.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "Date Stamp"))
        self.label_70.setText(_translate("MainWindow", "SECONDARY SCHOOL CLASSROOM TABLE"))
        self.pushButton_85.setText(_translate("MainWindow", "HOME"))
        self.pushButton_117.setText(_translate("MainWindow", "BACK"))
        self.pushButton_118.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_119.setText(_translate("MainWindow", "SHOW ALL"))
        self.label_38.setText(_translate("MainWindow", "TEACHER LEAVE TABLE"))
        self.pushButton_22.setText(_translate("MainWindow", "HOME"))
        self.pushButton_23.setText(_translate("MainWindow", "BACK"))
        self.pushButton_64.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_92.setText(_translate("MainWindow", "SECONDARY"))
        self.pushButton_94.setText(_translate("MainWindow", "PRIMARY"))
        self.label_40.setText(_translate("MainWindow", "Sort By"))
        self.tableWidget_2.setSortingEnabled(True)
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Employee No"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "School"))
        item = self.tableWidget_2.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_2.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Details"))
        item = self.tableWidget_2.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Start Date"))
        item = self.tableWidget_2.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "End Date"))
        self.label_41.setText(_translate("MainWindow", "RETIRED TEACHER  TABLE"))
        self.pushButton_24.setText(_translate("MainWindow", "HOME"))
        self.pushButton_25.setText(_translate("MainWindow", "BACK"))
        self.pushButton_95.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_96.setText(_translate("MainWindow", "SECONDARY"))
        self.pushButton_98.setText(_translate("MainWindow", "PRIMARY"))
        self.label_42.setText(_translate("MainWindow", "Sort By"))
        self.tableWidget_9.setSortingEnabled(True)
        item = self.tableWidget_9.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Employee No"))
        item = self.tableWidget_9.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School"))
        item = self.tableWidget_9.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_9.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_9.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Qualification"))
        item = self.tableWidget_9.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Date Of Retirement"))
        item = self.tableWidget_9.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_9.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget_9.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Date Of Birth"))
        item = self.tableWidget_9.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Marital Status"))
        item = self.tableWidget_9.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Home District"))
        item = self.tableWidget_9.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Home Sub County"))
        item = self.tableWidget_9.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Home Parish"))
        item = self.tableWidget_9.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Home Village"))
        item = self.tableWidget_9.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Next Of Kin"))
        item = self.tableWidget_9.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget_9.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Confirmation Status"))
        item = self.tableWidget_9.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "NIN"))
        item = self.tableWidget_9.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "Supplier No"))
        item = self.tableWidget_9.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "Date Stamp"))
        self.label_43.setText(_translate("MainWindow", "DECEASED  TEACHER  TABLE"))
        self.pushButton_26.setText(_translate("MainWindow", "HOME"))
        self.pushButton_27.setText(_translate("MainWindow", "BACK"))
        self.pushButton_99.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_100.setText(_translate("MainWindow", "SECONDARY"))
        self.pushButton_102.setText(_translate("MainWindow", "PRIMARY"))
        self.label_44.setText(_translate("MainWindow", "Sort By"))
        self.tableWidget_10.setSortingEnabled(True)
        item = self.tableWidget_10.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Employee No"))
        item = self.tableWidget_10.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "School"))
        item = self.tableWidget_10.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Emis No"))
        item = self.tableWidget_10.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_10.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_10.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Qualification"))
        item = self.tableWidget_10.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Retirment Date"))
        item = self.tableWidget_10.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Name "))
        item = self.tableWidget_10.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Gender"))
        item = self.tableWidget_10.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "date of Birth"))
        item = self.tableWidget_10.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Marital Status"))
        item = self.tableWidget_10.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Home District"))
        item = self.tableWidget_10.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Home Subcounty"))
        item = self.tableWidget_10.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Next of Kin"))
        item = self.tableWidget_10.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Next Of Kin"))
        item = self.tableWidget_10.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget_10.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Confirmation Status"))
        item = self.tableWidget_10.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "NIN"))
        item = self.tableWidget_10.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "Supplier No"))
        item = self.tableWidget_10.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "TIN"))
        item = self.tableWidget_10.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "Date Of Death"))
        self.label_113.setText(_translate("MainWindow", "Name of School"))
        self.label_131.setText(_translate("MainWindow", "Category"))
        self.label_132.setText(_translate("MainWindow", "Ownership"))
        self.label_134.setText(_translate("MainWindow", "S1 Male"))
        self.label_135.setText(_translate("MainWindow", "S1 Female"))
        self.label_136.setText(_translate("MainWindow", "S2 Male"))
        self.label_137.setText(_translate("MainWindow", "S2 Female"))
        self.label_138.setText(_translate("MainWindow", "S3 Female"))
        self.label_139.setText(_translate("MainWindow", "S3 Male"))
        self.label_140.setText(_translate("MainWindow", "S4 Female"))
        self.label_141.setText(_translate("MainWindow", "S4 Male"))
        self.label_142.setText(_translate("MainWindow", "S5 Female"))
        self.label_143.setText(_translate("MainWindow", "S5 Male"))
        self.label_144.setText(_translate("MainWindow", "S6 Female"))
        self.label_145.setText(_translate("MainWindow", "S6 Male"))
        self.save_10.setText(_translate("MainWindow", "Save"))
        self.comboBox_15.setItemText(0, _translate("MainWindow", "Government"))
        self.comboBox_15.setItemText(1, _translate("MainWindow", "NGO"))
        self.comboBox_15.setItemText(2, _translate("MainWindow", "Community"))
        self.comboBox_15.setItemText(3, _translate("MainWindow", "Private"))
        self.save_23.setText(_translate("MainWindow", "Save nd Next"))
        self.home_10.setText(_translate("MainWindow", "Home"))
        self.back_9.setText(_translate("MainWindow", "Back"))
        self.pushButton_112.setText(_translate("MainWindow", "View Enrollment Table"))
        self.label_159.setText(_translate("MainWindow", "SECTION A: SECONDARY  SCHOOL ENROLLMENT FORM"))
        self.label_148.setText(_translate("MainWindow", "SECTION B: SECONDARY  TEACHERS QUALIFICATION FORM"))
        self.home_11.setText(_translate("MainWindow", "Home"))
        self.back_10.setText(_translate("MainWindow", "Back"))
        self.pushButton_113.setText(_translate("MainWindow", "View Qualification Table"))
        self.label_149.setText(_translate("MainWindow", "Name of School"))
        self.label_170.setText(_translate("MainWindow", "Category"))
        self.label_171.setText(_translate("MainWindow", "Ownership"))
        self.label_172.setText(_translate("MainWindow", "S1 Teachers"))
        self.label_173.setText(_translate("MainWindow", "S2 Teachers"))
        self.label_174.setText(_translate("MainWindow", "S3 Teachers"))
        self.label_175.setText(_translate("MainWindow", "S4 Teachers"))
        self.label_178.setText(_translate("MainWindow", "S5 Teachers"))
        self.label_179.setText(_translate("MainWindow", "S6 Teachers"))
        self.save_11.setText(_translate("MainWindow", "Save"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "Government"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "NGO"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "Community"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "Private"))
        self.label_205.setText(_translate("MainWindow", "Licensed M"))
        self.label_206.setText(_translate("MainWindow", "Licenced F"))
        self.label_207.setText(_translate("MainWindow", "Certificate M"))
        self.label_208.setText(_translate("MainWindow", "Certificate F"))
        self.label_209.setText(_translate("MainWindow", "Diploma M"))
        self.label_212.setText(_translate("MainWindow", "Diploma F"))
        self.label_213.setText(_translate("MainWindow", "Bachelors M"))
        self.label_223.setText(_translate("MainWindow", "Bachelors F"))
        self.label_230.setText(_translate("MainWindow", "Masters and above M"))
        self.label_231.setText(_translate("MainWindow", "Masters and above F"))
        self.save_22.setText(_translate("MainWindow", "Save and Next"))
        self.home_13.setText(_translate("MainWindow", "Home"))
        self.back_12.setText(_translate("MainWindow", "Back"))
        self.pushButton_89.setText(_translate("MainWindow", "View Facilities Table"))
        self.label_204.setText(_translate("MainWindow", "SECTION C: SECONDARY SCHOOL  FACILITIES FORM"))
        self.label_267.setText(_translate("MainWindow", "Name of School"))
        self.label_268.setText(_translate("MainWindow", "Category"))
        self.label_269.setText(_translate("MainWindow", "Ownership"))
        self.label_270.setText(_translate("MainWindow", "Library"))
        self.label_271.setText(_translate("MainWindow", "Science Laboratory"))
        self.label_272.setText(_translate("MainWindow", "Computer Laboratory"))
        self.label_273.setText(_translate("MainWindow", "Kitchen"))
        self.label_274.setText(_translate("MainWindow", "Staffroom"))
        self.label_275.setText(_translate("MainWindow", "Administration Block"))
        self.label_276.setText(_translate("MainWindow", "Dining Hall"))
        self.label_277.setText(_translate("MainWindow", "Reliable Safe Water Supply"))
        self.save_13.setText(_translate("MainWindow", "Save"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "Government"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "NGO"))
        self.comboBox_11.setItemText(2, _translate("MainWindow", "Community"))
        self.comboBox_11.setItemText(3, _translate("MainWindow", "Private"))
        self.label_278.setText(_translate("MainWindow", "Stores"))
        self.label_279.setText(_translate("MainWindow", "Workshop"))
        self.label_280.setText(_translate("MainWindow", "Playground"))
        self.label_281.setText(_translate("MainWindow", "School Garden"))
        self.label_282.setText(_translate("MainWindow", "Latrine/Toilet"))
        self.label_283.setText(_translate("MainWindow", "Number of Stances"))
        self.label_284.setText(_translate("MainWindow", "Handwashing Facility"))
        self.label_285.setText(_translate("MainWindow", "S1 Desk"))
        self.label_286.setText(_translate("MainWindow", "S2 Desk"))
        self.label_287.setText(_translate("MainWindow", "S3  Desk"))
        self.label_288.setText(_translate("MainWindow", "S4 Desk"))
        self.label_289.setText(_translate("MainWindow", "S5 Desk"))
        self.label_290.setText(_translate("MainWindow", "S6 Desk"))
        self.save_21.setText(_translate("MainWindow", "Save and Next"))
        self.home_14.setText(_translate("MainWindow", "Home"))
        self.back_13.setText(_translate("MainWindow", "Back"))
        self.pushButton_90.setText(_translate("MainWindow", "View Classroom Table"))
        self.label_292.setText(_translate("MainWindow", "Name of School"))
        self.label_293.setText(_translate("MainWindow", "Category"))
        self.label_294.setText(_translate("MainWindow", "Ownership"))
        self.label_295.setText(_translate("MainWindow", "S1 Classes"))
        self.label_296.setText(_translate("MainWindow", "S2 Classes"))
        self.label_297.setText(_translate("MainWindow", "S3 Classes"))
        self.label_298.setText(_translate("MainWindow", "S4 Classes"))
        self.label_299.setText(_translate("MainWindow", "S5 Classes"))
        self.label_300.setText(_translate("MainWindow", "S6 Classes"))
        self.save_14.setText(_translate("MainWindow", "Save"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "Government"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "NGO"))
        self.comboBox_12.setItemText(2, _translate("MainWindow", "Community"))
        self.comboBox_12.setItemText(3, _translate("MainWindow", "Private"))
        self.label_302.setText(_translate("MainWindow", "Complete Permanent"))
        self.label_303.setText(_translate("MainWindow", "Complete Temporary"))
        self.label_304.setText(_translate("MainWindow", "At Foundation"))
        self.label_305.setText(_translate("MainWindow", "At Window Level"))
        self.label_306.setText(_translate("MainWindow", "At Wall plate and obove"))
        self.label_307.setText(_translate("MainWindow", "Number of classes without structures"))
        self.save_20.setText(_translate("MainWindow", "Save and Next"))
        self.label_308.setText(_translate("MainWindow", "SECTION D:  SECONDARY SCHOOL CLASSROOM FORM"))
        self.tableWidget_11.setSortingEnabled(True)
        item = self.tableWidget_11.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Employee No"))
        item = self.tableWidget_11.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "school"))
        item = self.tableWidget_11.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Emis No"))
        item = self.tableWidget_11.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "School Type"))
        item = self.tableWidget_11.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Sub County"))
        item = self.tableWidget_11.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Qualification"))
        item = self.tableWidget_11.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Expected Date of Retirement"))
        item = self.tableWidget_11.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tableWidget_11.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Gender "))
        item = self.tableWidget_11.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Date of Birth"))
        item = self.tableWidget_11.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Marital Status"))
        item = self.tableWidget_11.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Home District"))
        item = self.tableWidget_11.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Home Subcounty"))
        item = self.tableWidget_11.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "Home Parish"))
        item = self.tableWidget_11.horizontalHeaderItem(14)
        item.setText(_translate("MainWindow", "Home Village"))
        item = self.tableWidget_11.horizontalHeaderItem(15)
        item.setText(_translate("MainWindow", "Next Of Kin"))
        item = self.tableWidget_11.horizontalHeaderItem(16)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget_11.horizontalHeaderItem(17)
        item.setText(_translate("MainWindow", "Confirmation Status"))
        item = self.tableWidget_11.horizontalHeaderItem(18)
        item.setText(_translate("MainWindow", "NIN"))
        item = self.tableWidget_11.horizontalHeaderItem(19)
        item.setText(_translate("MainWindow", "Supplier No"))
        item = self.tableWidget_11.horizontalHeaderItem(20)
        item.setText(_translate("MainWindow", "TIN"))
        item = self.tableWidget_11.horizontalHeaderItem(21)
        item.setText(_translate("MainWindow", "Reg No"))
        item = self.tableWidget_11.horizontalHeaderItem(22)
        item.setText(_translate("MainWindow", "Date Stamp"))
        self.label_71.setText(_translate("MainWindow", "ABSCONED TEACHER TABLE"))
        self.pushButton_63.setText(_translate("MainWindow", "HOME"))
        self.pushButton_103.setText(_translate("MainWindow", "BACK"))
        self.pushButton_104.setText(_translate("MainWindow", "REFRESH"))
        self.pushButton_28.setText(_translate("MainWindow", "SEARCH"))
        self.label_36.setText(_translate("MainWindow", "Enter teacher\'s Empolyee Number"))
        self.pushButton_29.setText(_translate("MainWindow", "HOME"))
        self.pushButton_32.setText(_translate("MainWindow", "BACK"))
        self.pushButton_121.setText(_translate("MainWindow", "PROFILE FORM"))
        self.pushButton_122.setText(_translate("MainWindow", "PROFILE TABLE"))
        self.label_39.setText(_translate("MainWindow", "TEACHER"))
        self.pushButton_33.setText(_translate("MainWindow", "ABSCONDED"))
        self.pushButton_106.setText(_translate("MainWindow", "DECEASED"))
        self.label_45.setText(_translate("MainWindow", "SEARCH TEACHER DATABASE"))
        self.pushButton_115.setText(_translate("MainWindow", "ON LEAVE"))
        self.pushButton_116.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_249.setText(_translate("MainWindow", "HOME"))
        self.label_507.setText(_translate("MainWindow", "REPORTS"))
        self.label_51.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_52.setText(_translate("MainWindow", "RATIOS"))
        self.label_54.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_56.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_57.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_55.setText(_translate("MainWindow", "PRIMARY"))
        self.label_311.setText(_translate("MainWindow", "SECONDARY"))
        self.label_312.setText(_translate("MainWindow", "PRIMARY"))
        self.label_313.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "District"))
        self.label_58.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_59.setText(_translate("MainWindow", "RATIOS"))
        self.label_60.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_72.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_73.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_314.setText(_translate("MainWindow", "PRIMARY"))
        self.label_315.setText(_translate("MainWindow", "SECONDARY"))
        self.label_316.setText(_translate("MainWindow", "PRIMARY"))
        self.label_317.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "Adekokwok"))
        self.label_613.setText(_translate("MainWindow", "RATIOS"))
        self.label_614.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_615.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_616.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_617.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_318.setText(_translate("MainWindow", "PRIMARY"))
        self.label_319.setText(_translate("MainWindow", "SECONDARY"))
        self.label_320.setText(_translate("MainWindow", "PRIMARY"))
        self.label_321.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_75), _translate("MainWindow", "Adyel"))
        self.label_74.setText(_translate("MainWindow", "RATIOS"))
        self.label_75.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_76.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_77.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_78.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_322.setText(_translate("MainWindow", "PRIMARY"))
        self.label_323.setText(_translate("MainWindow", "SECONDARY"))
        self.label_324.setText(_translate("MainWindow", "PRIMARY"))
        self.label_325.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "Agali"))
        self.label_79.setText(_translate("MainWindow", "RATIOS"))
        self.label_80.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_83.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_84.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_90.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_326.setText(_translate("MainWindow", "PRIMARY"))
        self.label_327.setText(_translate("MainWindow", "SECONDARY"))
        self.label_328.setText(_translate("MainWindow", "PRIMARY"))
        self.label_329.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), _translate("MainWindow", "Agweng"))
        self.label_106.setText(_translate("MainWindow", "RATIOS"))
        self.label_107.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_108.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_109.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_110.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_330.setText(_translate("MainWindow", "PRIMARY"))
        self.label_331.setText(_translate("MainWindow", "SECONDARY"))
        self.label_332.setText(_translate("MainWindow", "PRIMARY"))
        self.label_333.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "Amach"))
        self.label_111.setText(_translate("MainWindow", "RATIOS"))
        self.label_114.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_232.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_233.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_234.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_334.setText(_translate("MainWindow", "PRIMARY"))
        self.label_335.setText(_translate("MainWindow", "SECONDARY"))
        self.label_336.setText(_translate("MainWindow", "PRIMARY"))
        self.label_337.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_9), _translate("MainWindow", "Aromo"))
        self.label_235.setText(_translate("MainWindow", "RATIOS"))
        self.label_236.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_239.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_240.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_248.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_338.setText(_translate("MainWindow", "PRIMARY"))
        self.label_339.setText(_translate("MainWindow", "SECONDARY"))
        self.label_340.setText(_translate("MainWindow", "PRIMARY"))
        self.label_341.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_11), _translate("MainWindow", "Barr"))
        self.label_249.setText(_translate("MainWindow", "RATIOS"))
        self.label_250.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_251.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_252.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_253.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_342.setText(_translate("MainWindow", "PRIMARY"))
        self.label_343.setText(_translate("MainWindow", "SECONDARY"))
        self.label_344.setText(_translate("MainWindow", "PRIMARY"))
        self.label_345.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("MainWindow", "Lira"))
        self.label_254.setText(_translate("MainWindow", "RATIOS"))
        self.label_255.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_256.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_257.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_258.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_346.setText(_translate("MainWindow", "PRIMARY"))
        self.label_347.setText(_translate("MainWindow", "SECONDARY"))
        self.label_348.setText(_translate("MainWindow", "PRIMARY"))
        self.label_349.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_10), _translate("MainWindow", "Ngetta"))
        self.label_259.setText(_translate("MainWindow", "RATIOS"))
        self.label_260.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_261.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_262.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_263.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_350.setText(_translate("MainWindow", "PRIMARY"))
        self.label_351.setText(_translate("MainWindow", "SECONDARY"))
        self.label_352.setText(_translate("MainWindow", "PRIMARY"))
        self.label_353.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_13), _translate("MainWindow", "Ogur"))
        self.label_618.setText(_translate("MainWindow", "RATIOS"))
        self.label_619.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_620.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_621.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_622.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_354.setText(_translate("MainWindow", "PRIMARY"))
        self.label_355.setText(_translate("MainWindow", "SECONDARY"))
        self.label_356.setText(_translate("MainWindow", "PRIMARY"))
        self.label_357.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_76), _translate("MainWindow", "Ojwina"))
        self.label_623.setText(_translate("MainWindow", "RATIOS"))
        self.label_624.setText(_translate("MainWindow", "ENROLLMENT GRAPH"))
        self.label_625.setText(_translate("MainWindow", "ENROLLMENT SUMMARY"))
        self.label_626.setText(_translate("MainWindow", "TEACHER QUALIFICATION PIE CHART"))
        self.label_627.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_358.setText(_translate("MainWindow", "PRIMARY"))
        self.label_359.setText(_translate("MainWindow", "SECONDARY"))
        self.label_360.setText(_translate("MainWindow", "PRIMARY"))
        self.label_361.setText(_translate("MainWindow", "SECONDARY"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_77), _translate("MainWindow", "Railways"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Subcounty"))
        self.label_264.setText(_translate("MainWindow", "SEARCH PARISH"))
        self.pushButton_124.setText(_translate("MainWindow", "SEARCH"))
        self.label_266.setText(_translate("MainWindow", "ENROLLMENT"))
        self.label_291.setText(_translate("MainWindow", "RATIOS"))
        self.label_301.setText(_translate("MainWindow", "TEACHER QUALIFICATION"))
        self.label_309.setText(_translate("MainWindow", "ENROLLMENT GRAPHS"))
        self.label_310.setText(_translate("MainWindow", "TEACHER QUALIFICATION GRAPHS"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Parish"))
        self.label_81.setText(_translate("MainWindow", "SEARCH SCHOOL"))
        self.label_82.setText(_translate("MainWindow", "Enter EMIS Number"))
        self.pushButton_51.setText(_translate("MainWindow", "Pri Enrollment"))
        self.pushButton_91.setText(_translate("MainWindow", "Sec Enrollment"))
        self.pushButton_107.setText(_translate("MainWindow", "Pri Facilities"))
        self.pushButton_109.setText(_translate("MainWindow", "Sec Facilities"))
        self.pushButton_111.setText(_translate("MainWindow", "Pri Qualification"))
        self.pushButton_114.setText(_translate("MainWindow", "Sec Qualification"))
        self.pushButton_123.setText(_translate("MainWindow", "Teacher Housing"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "School"))
        self.label_46.setText(_translate("MainWindow", "LEAVE FORM"))
        self.label_53.setText(_translate("MainWindow", "Employee Number"))
        self.label_508.setText(_translate("MainWindow", "Details of Leave"))
        self.label_509.setText(_translate("MainWindow", "Start Date"))
        self.label_510.setText(_translate("MainWindow", "End Date"))
        self.pushButton_52.setText(_translate("MainWindow", "Save"))
        self.pushButton_108.setText(_translate("MainWindow", "Exit Without Save"))
        self.label_364.setText(_translate("MainWindow", "First Name"))
        self.label_365.setText(_translate("MainWindow", "Last  Name"))
        self.label_366.setText(_translate("MainWindow", "User Name"))
        self.label_367.setText(_translate("MainWindow", "Password"))
        self.label_368.setText(_translate("MainWindow", "Password"))
        self.label_369.setText(_translate("MainWindow", "User Name"))
        self.label_362.setText(_translate("MainWindow", "NEW USER"))
        self.label_363.setText(_translate("MainWindow", "REFERENCES\' DETAILS"))
        self.pushButton_70.setText(_translate("MainWindow", "signup"))
        self.pushButton_72.setText(_translate("MainWindow", "Home"))
        self.menuImport_Data.setTitle(_translate("MainWindow", "Import Data"))
        self.menuExport_data.setTitle(_translate("MainWindow", "Export data"))
        self.menuUpdate.setTitle(_translate("MainWindow", "Update"))
        self.actionImport_Data.setText(_translate("MainWindow", "Import Data"))
        self.actionExport_Data.setText(_translate("MainWindow", "Export Data"))
        self.actionPrint.setText(_translate("MainWindow", "Print"))
        self.actionTutorial.setText(_translate("MainWindow", "Tutorial"))
        self.actionImport_School.setText(_translate("MainWindow", "Import School"))
        self.actionImport_Teacher.setText(_translate("MainWindow", "Import Teacher"))
        self.actionImport_School_Enrollment.setText(_translate("MainWindow", "Import Primary School Enrollment"))
        self.actionImport_school_Facilities.setText(_translate("MainWindow", "Import Primary School Facilities"))
        self.actionImport_school_Classroom.setText(_translate("MainWindow", "Import Primary School Classroom"))
        self.actionImport_All.setText(_translate("MainWindow", "Import All"))
        self.actionImport_Secondary_School_Enrollment.setText(_translate("MainWindow", "Import Secondary School Enrollment"))
        self.actionImport_Secondary_School_Facilities.setText(_translate("MainWindow", "Import Secondary School Facilities"))
        self.actionImport_Secondary_School_Classrooms.setText(_translate("MainWindow", "Import Secondary School Classrooms"))
        self.actionImport_Teacher_Housing.setText(_translate("MainWindow", "Import Teacher Housing"))
        self.actionGet_Update.setText(_translate("MainWindow", "Get Update"))
        self.actionExport_All_Date.setText(_translate("MainWindow", "Export All Date"))
        self.actionCheck_for_Updates.setText(_translate("MainWindow", "Check for Updates"))

from mplwidget import MplWidget

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:

        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

c.close()
conn.close()

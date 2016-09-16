import getpass
import imaplib
import getpass
import email
import datetime

def process_mailbox(M):
    rv, data = M.search(None, "ALL") #get all emails
    if rv != 'OK':
        print "No Messages ever"
        return
    #for iterat_var in sequence:
    #print data[0]
    
    #number applications
    appnum=0
    
    for num in data[0].split(): 
        #split based on space delimiter, returns list of substrings for
        #each element of array, returned messages
        rv, data = M.fetch(num,'(RFC822)')#body of emails?
        if rv != 'OK':
            print"Error getting message", num
            return
        
        msg=email.message_from_string(data[0][1])
        print 'Message %s: %s' % (num, msg['Subject'])
        print 'Raw Date:', msg['Date']
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple))
            datestr = local_date.strftime("%d_%b_%Y_%H_%M_%S")
            print "Local date:", datestr
            msg_subject = msg['Subject']
            msg_from = msg['From']
            if msg_from != 'apache@physwww.physics.mcmaster.ca (Apache)':
                continue
            
        #check if from apache
        
        #get data portion of subject
        subsplitlist=msg_subject.split(':',1)
        subsplitlist=subsplitlist[1]
        
        #extract different data values of subject
        itemslist=subsplitlist.split(',',2)
               
        prefname =itemslist[0]
        lastname =itemslist[1]
        appid =itemslist[2]
        
        #Body details
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = unicode(part.get_payload(decode=True), errors='ignore')
                file_name = lastname + "_" + prefname + "_" + datestr + ".txt"
                output_file = open(file_name, 'w')
                #output_file.write(body.decode('utf-8').replace(u'\u2018',"'").replace(u'\u2019',"'").replace(u'\xe9',"e"))
                output_file.write(body)
                output_file.close()
                appnum=appnum+1
            else:
                continue




M=imaplib.IMAP4_SSL('imap.gmail.com')

#login
try:
    M.login('apply.ccuwip.mcmaster@gmail.com',getpass.getpass())
except imaplib.IMAP4.error:
    print "LOGIN FAIL"
    exit()

rv, data = M. select("INBOX")
if rv == 'OK':
    print "Processing mailbox\n"
    process_mailbox(M)#do stuff with emails
    M.close()
    M.logout()

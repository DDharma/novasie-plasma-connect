from routes import app,request,cross_origin
from modules.connection import sql_connection
from modules.OtpSend import optSender
from random import randint

def tokenKey():
    """[Returning the token key]

    Returns:
        [int]: [key]
    """
    return randint(0000,9999)

@app.route("/")
@cross_origin()
def hello():
    return "hello koshish"

#Routes to return all the data from the table with post request having data like { "CITY":"DEHRADUN"}
@app.route("/allDonarDetails",methods=["POST"])
@cross_origin()
def allDonarDetails():
    """[Function which return all the data form table]

    Returns:
        [JSON]: [Objects of the donar lists ]
    """
    #Caling function to connecting database
    mydb = sql_connection()
    #print("-----------------------------------")

    try:
        if request.method == "POST":
            date_json_data  = request.get_json()
            city = date_json_data["CITY"]
        

            mycursor = mydb.cursor()
            cityQuery = "SELECT * FROM ProjectPlasma_plasmatable WHERE CITY = %s"

            cityData = (city,) 
            mycursor.execute(cityQuery,cityData)
            donarData = mycursor.fetchall()
            mycursor.close()
            mydb.close()
        
            returnData = {
                "data":donarData
            }
            return returnData

    except Exception as e:
        return str(e)

#Routes to return all the data from the table with post request having data like { "MOBNO":"9529875997"}
@app.route("/allDonarDetailsMob",methods=["POST"])
@cross_origin()
def allDonarDetailsMob():
    """[Function which return all the data form table with mobile no]

    Returns:
        [JSON]: [Objects of single donar ]
    """
    #Caling function to connecting database
    mydb = sql_connection()
    #print("-----------------------------------")

    try:
        if request.method == "POST":
            date_json_data  = request.get_json()
            city = date_json_data["MOBNO"]
    
            mycursor = mydb.cursor()
            cityQuery = "SELECT * FROM ProjectPlasma_plasmatable WHERE MOBNO = {}".format(city)

            mycursor.execute(cityQuery)
            donarData = mycursor.fetchall()
            mycursor.close()
            mydb.close()
        
            returnData = {
                "data":donarData
            }
            return returnData

    except Exception as e:
        return str(e)

#Routes to check either number available in data base or not
@app.route("/checkNumber",methods=["POST"])
@cross_origin()
def checkNumber():
    """[Function to check MOb no exitis or not]

    Returns:
        [type]: [description]
    """
    
    #Caling function to connecting database
    mydb = sql_connection()
    #print("-----------------------------------")
    try:
        if request.method == "POST":
            date_json_data  = request.get_json()
            mob = date_json_data["MOBNO"]
            print(mob)
            mycursor = mydb.cursor()
            countNumber = "SELECT COUNT(MOBNO) FROM ProjectPlasma_plasmatable WHERE MOBNO ={}".format(mob)
            print(1)
            #mobNum = (mob,) 
            mycursor.execute(countNumber)
            print(2)

            mob_check = {}
            print(3)
            for i in mycursor: 
                mob_check["return"] = i[0]
            mycursor.close()
            mydb.close()
            if mob_check["return"] == 0:
                returnData = {
                "status":0
            }
            else:
                returnData = {
                    "status":1
                }
            return returnData

    except Exception as e:
        return str(e)

#Routes to send OTP to user
@app.route("/otpSend",methods=["POST"])
@cross_origin()
def otpSend():
    """[Request for OTP]

    Returns:
        [JSON]: [OTP, MOBILE NO WITH MSZ]
    """
    try:
        if request.method == "POST":
            date_json_data  = request.get_json()
            mob = date_json_data["MOBNO"]

        return optSender(mob)
    except Exception as e:
        return str(e)


#Routes to return all the data from the table with post request having data like { "MOBNO":"9529875997"}
@app.route("/key",methods=["POST"])
@cross_origin()
def key():
    """[Function which return key form table for the perticular mobile no]

    Returns:
        [JSON]: [Objects of key ]
    """
    #Caling function to connecting database
    mydb = sql_connection()
    #print("-----------------------------------")

    try:
        if request.method == "POST":
            date_json_data  = request.get_json()
            city = date_json_data["MOBNO"]
    
            mycursor = mydb.cursor()
            cityQuery = "SELECT STATUS FROM ProjectPlasma_plasmatable WHERE MOBNO = {}".format(city)

            mycursor.execute(cityQuery)
            keyData = mycursor.fetchall()
            mycursor.close()
            mydb.close()
        
            returnData = {
                "data":keyData[0][0]
            }
            return returnData

    except Exception as e:
        return str(e)


#Routes to send the data to server for signUp
@app.route("/signup",methods=["POST"])
@cross_origin()
def signup():

    #Caling function to connecting database
    mydb = sql_connection()
    #print("-----------------------------------")
    try:
        if request.method == "POST":
            date_json_data  = request.get_json()

            name     = date_json_data["NAME"]
            mob      = date_json_data["MOBNO"]
            password = date_json_data["PASSWORD"]
            Key = tokenKey()

            print(mob,name,password,Key)
            mycursor = mydb.cursor()
            print("runnig",0)
            sendDataQuery = "INSERT INTO ProjectPlasma_plasmatable (MOBNO,NAME,PASSWORD,STATUS) VALUES ({},'{}','{}',{})".format(mob,name,password,Key)    
            print("runnig",1)  
            mycursor.execute(sendDataQuery)
            print("runnig",2)

            returnData = {
                "key":Key
            }
            mydb.commit()
            mycursor.close()
            mydb.close()
            return returnData

    except Exception as e:
        return str(e)
    
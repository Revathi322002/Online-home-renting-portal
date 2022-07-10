class rent:
    def home():
        city=input("which area you want: \n1:kodambakkam \n2:anna nagar \n3.goripalayam \n")
        if city=="1":
            informations=["locality:kodambakkam","area:chennai","square_feet:798","type:2BHK","rent:rs.6000/month","owner_id=1"]
            for i in informations:
                print(i)
        elif city=="2":
            informations=["locality:anna nagar","area:chennai","square_feet:1200","type:3BHK","rent:rs.15000/month","owner_id=2"]
            for i in informations:
                print(i)
        elif city=="3":
            informations=["locality:goripalayam","area:madurai","square_feet:560","type:1BHK","rent:rs.5500/month","owner_id=2"]
            for i in informations:
                print(i)
class tenate:
    def user_available():
        options = input("1:view houses  \n2:request  \n3:log out \n")
        if options == "1":
            informations = rent
            content = informations.home()
        elif options == "2":
            print("which area do you prefer: ")
            informations = rent
            content = informations.home()
        elif options == "3":
            print("THANK YOU! for your vist, you are logged out successfully")

class owner:
    def owner_request():
        options=input("1:Can create a request to post  \n2:Remove their house for rental \n")
        if options == "1":
            informations = rent
            content = informations.home()
        elif options == "2":
            print("nO houses are available, all are booked")

class user_details:
    def details():
        informations = input("chose users details: \n1:1st user \n2:2nd user \n3:3rd user  \n")
        if informations == "1":
            informations = ["User Id:1", "Name:Lucifer", "Email:lucifer@gmail.com", "Mobile:9876543210", "Aadhaar:123412341234"]
            for i in informations:
                print(i)
        elif informations == "2":
            informations = ["User Id:2", "Name:Peter Parker", "Email:perterparker@gmail.com", "Mobile:1234567890", "Aadhaar:567856785678"]
            for i in informations:
                print(i)
        elif informations == "3":
            informations = ["User Id:3", "Name:Tony Stark", "Email:tonystark@gmail.com", "Mobile:1234509876", "Aadhaar:345634563456"]
            for i in informations:
                print(i)

class approver:
    def approver_request():
        options=input("choose the options: \n1:Can view all the User details \n2:Decline the request \n")
        if options =="1":
            informations_ = user_details
            content = informations_.details()
        elif options == "2":
            print("your request is declined")

if __name__ == "__main__":
    print("WELCOME TO HOME RENTAL PORTAL! \n HOW CAN I HELP YOU!")
    user = input("1:Tenant \n2:Owner \n3:Approver \n")
    if user == "1":
        option = tenate
        object = option.user_available()
    elif user == "2":
        option = owner
        object = option.owner_request()
    elif user == "3":
        option = approver
        object = option.approver_request()

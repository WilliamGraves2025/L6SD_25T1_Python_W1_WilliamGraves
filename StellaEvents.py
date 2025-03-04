import os
os.system('cls')

Vendors = []

# Find a vendor in the list

class FindVendor:
    def __init__(self):
        pass

    def FindVendor(self):
        MatchingVendors = []
        VendorName = ""
        VendorAddress = ""
        VendorPhone = ""
        print("Enter Vendor Name: ")
        VendorName = input()
        print("Enter Vendor Address: ")
        VendorAddress = input()
        print("Enter Vendor Phone: ")
        VendorPhone = int(input())
        
        for Vendor in Vendors:
            if (VendorName == "" or Vendor[0] == VendorName) and (VendorAddress == "" or Vendor[1] == VendorAddress) or (VendorPhone == "" or Vendor[2] == VendorPhone):
                MatchingVendors.append(Vendor)
        return MatchingVendors

# Add vendor to the list

class AddVendor(FindVendor):
    def __init__(self):
        pass
    
    def AddVendor(self):
        print("Enter Vendor Name: ")
        VendorName = input()
        print("Enter Vendor Address: ")
        VendorAddress = input()
        print("Enter Vendor Phone: ")
        VendorPhone = input()
        Vendor = [VendorName, VendorAddress, VendorPhone]
        Vendors.append(Vendor)
        print("Vendor added successfully!")

# Remove vendor from the list

class RemoveVendor(FindVendor):
    def __init__(self):
        pass
    
    def RemoveVendor(self):
        MatchingVendors = self.FindVendor()
        if len(MatchingVendors) == 0:
            print("No results")
            return
        elif len(MatchingVendors) == 1:
            print(MatchingVendors)
            Vendors.remove(MatchingVendors[0])
            print("Vendor removed successfully!")
        else:
            print("More than one result was found")
            return
            
# Update vendor details

class UpdateVendor(FindVendor):
    def __init__(self):
        pass

    def UpdateVendor(self):
        MatchingVendors = self.FindVendor()
        if len(MatchingVendors) == 0:
            print("No results")
            return
        elif len(MatchingVendors) == 1:
            print(MatchingVendors)
            MatchingVendor = Vendors.index(MatchingVendor[0])
            print("What would you like to change?")
            print("1: Vendor Name")
            print("2: Vendor Address")
            print("3: Vendor Phone")
            Change = int(input())
            if Change == 1:
                print("Enter new name")
                NewName = input()
                Vendors[MatchingVendor][0] = NewName
                print("Vendor name updated successfully!")
                print(Vendors[MatchingVendor])
                return
            elif Change == 2:
                print("Enter new address")
                NewAddress = input()
                Vendors[MatchingVendor][1] = NewAddress
                print("Vendor address updated successfully!")
                print(Vendors[MatchingVendor])
                return
            elif Change == 3:
                print("Enter new phone")
                NewPhone = input()
                Vendors[MatchingVendor][2] = NewPhone
                print("Vendor phone updated successfully!")
                print(Vendors[MatchingVendor])
                return
            else:
                print("Invalid number")
                return

        else:
            print("More than one result was found")
            return

# View all vendors in the list

class ViewAllVendors:
    def __init__(self):
        pass

    def ViewAllVendors(self):
        MatchingVendors = []
        VendorName = ""
        VendorAddress = ""
        VendorPhone = ""
        
        for Vendor in Vendors:
            if (VendorName == "" or Vendor[0] == VendorName) and (VendorAddress == "" or Vendor[1] == VendorAddress) or (VendorPhone == "" or Vendor[2] == VendorAddress):
                MatchingVendors.append(Vendor)
        return MatchingVendors


# Run the main menu

def MainMenu():
    while True:   
        print("Welcome to the vendor database")
        print("What would you like to do?")
        print("1: Find Vendor")
        print("2: Add Vendor")
        print("3: Update Vendor")
        print("4: Remove Vendor")
        print("5: View All Vendors")
        Action = int(input())
        if Action == 1:
            FindVendorClass = FindVendor()
            Result = FindVendorClass.FindVendor()
            print(Result)
        elif Action == 2:
            AddVendorClass = AddVendor()
            AddVendorClass.AddVendor()
        elif Action == 3:
            UpdateVendorClass = UpdateVendor()
            UpdateVendorClass.UpdateVendor()
        elif Action == 4:
            RemoveVendorClass = RemoveVendor()
            RemoveVendorClass.RemoveVendor()
        elif Action == 5:
            ViewAllVendorsClass = ViewAllVendors()
            Result = ViewAllVendorsClass.ViewAllVendors()
            print(Result)
        else:
            print("Invalid number")
            
        os.system('pause')
        os.system('cls')
MainMenu()
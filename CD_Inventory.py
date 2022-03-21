#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Ziqi Yan, 2022-Mar-20, implement assignmen 08
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []

class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:

    """

    def __init__(self, id, title, artist):
        self.cd_id = id
        self.cd_title = title
        self.cd_artist = artist


# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    @staticmethod
    def load_inventory(file_name):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        tables = [] # this clears existing data and allows to load data from file
        objFile = open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = CD(int(data[0]), data[1], data[2])
            tables.append(dicRow)
        objFile.close()
        return tables

    @staticmethod
    def save_inventory(file_name, lst_Inventory):
        
        objFile = open(file_name, 'w')
        for cd in lst_Inventory:
            lstValues = [cd.cd_id, cd.cd_title, cd.cd_artist]
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()

# -- PRESENTATION (Input/Output) -- #
class IO:
    """Processes data to and from file:

    properties:

    methods:
        show_menu(): -> None
        get_choice(): -> String
        dis_data(lst_Inventory): -> None
        add_cd(lst_Inventory): -> None
    """

    @staticmethod
    def show_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def get_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def dis_data(lst_Inventory):
        """Displays current inventory table


        Args:
            table (list of cd object): list of cd objects that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for cd in lst_Inventory:
            print('{}\t{} (by:{})'.format(*[cd.cd_id, cd.cd_title, cd.cd_artist]))
        print('======================================')
    # TODO add code to get CD data from user
    @staticmethod
    def add_cd(lst_Inventory):
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        lst_Inventory.append(CD(int(strID), strTitle, stArtist))

# -- Main Body of Script -- #
# TODO Add Code to the main body
# Load data from file into a list of CD objects on script start
lstOfCDObjects = FileIO.load_inventory(strFileName)

# Display menu to user
    # show user current inventory
    # let user add data to the inventory
    # let user save inventory to file
    # let user load inventory from file
    # let user exit program

while True:
    # 2.1 Display Menu to user and get choice
    IO.show_menu()
    strChoice = IO.get_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('reloading...')
        try:
            lstOfCDObjects = FileIO.load_inventory(strFileName) 
        except:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
        IO.dis_data(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.3 process add a CD
    elif strChoice == 'a':
        IO.add_cd(lstOfCDObjects)
        continue  # start loop back at top.
    # 3.4 process display current inventory
    elif strChoice == 'i':
        IO.dis_data(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.dis_data(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            try:
                FileIO.save_inventory(strFileName,lstOfCDObjects)
            except:
                input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')
"""
    HomeLogic is rhe class that handles the logic for the home page.
"""
from tkinter import filedialog
from logic.cloud import CloudSetup, Filestack

class HomeLogic:
    """
        This class handles the logic behind the Home fram (after successfull authentication).
    """
    def __init__(self, userObj):
        """
            This is the constructor of the HomeLogic class.
            - userObj: the user object, which contains the user details
        """
        self.userObj = userObj
        self.cloudSetObj = CloudSetup(userObj["cloud_provider"], userObj["cloud_provider_api_key"])
        # Create File handler object for the cloud provider
        if userObj["cloud_provider"] == "filestack":
            self.filehandler = Filestack()


    def launch_file_explorer(self) -> None:
        """
            This method launches the file explorer of the system.
            Opens the file dialog to select the file.
        """
        file = filedialog.askopenfilename(initialdir="/", filetypes=[("Text file", "*.txt"), ("PDF file", "*.pdf"),  ("Docx file", "*.docx"), ("Image file", "*.png *jpg")], title="Select a File to Upload")
        
        if file:
            """
                If the file is selected, upload it to the cloud by calling the upload_file method.
            """
            self.upload_file(file)


    def upload_file(self, file):
        """
            This method uploads the file to the cloud.
            - file: the file to be uploaded
        """
        filelink = self.filehandler.upload_file(file)
        print(filelink.upload_response)


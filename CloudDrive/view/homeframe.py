import os
from dotenv import load_dotenv
import tkinter as tk
import customtkinter as ctk
from PIL import Image
load_dotenv(".env")

class HomeFrame():
    """
        This class defines the Home frame. Home frame is the frame 
        shown to the user after successfull authentication. 
        How this frame looks?
        - It has a sidebar on the left side of the frame,
        which contains the user details and the cloud provider details,
        And has the upload button.
        - It has a main content area in the middle of the frame (covers 80% of the frame),
        which contains the files and folders of the user.
        - parent: the parent of the frame
    """
    def __init__(self, parent, prev, userObj):
        self.remove_frame(prev)
        self.parent = parent
        self.frame = prev
        self.userObj = userObj
        self.frame.grid(row=0, column=0)
        self.frame.pack_propagate(False)
        self.frame.tkraise()
        self.build()


    def build(self):
        """
            build() method builds the Home frame.
        """
        self.frame.configure(fg_color="#023e8a", corner_radius=0)
        self.build_sidebar()
        self.build_main_content()


    def build_sidebar(self):
        """
            build_sidebar() method builds the sidebar of the Home frame.
            This sidebar contains the My Account tab and Upload button.
        """
        # Left Sidebar
        self.left_sidebar = ctk.CTkFrame(self.frame,
            width=int(os.getenv("DEFAULT_APP_WIDTH"))*0.2,
            height=int(os.getenv("DEFAULT_APP_HEIGHT")),
            fg_color="#023e8a",
            corner_radius=0
        )

        # Left Sidebar Content
        # My Account
        self.my_account = ctk.CTkFrame(self.left_sidebar,
            width=int(os.getenv("DEFAULT_APP_WIDTH"))*0.18,
            height=int(os.getenv("DEFAULT_APP_HEIGHT"))*0.1,
            fg_color="#023e8a",
            corner_radius=10
        )
        self.my_account.pack_propagate(False)
        self.my_account.pack(side=tk.BOTTOM, pady=10)
        self.my_account.tkraise()

        # App Title Logo
        cloud_img = ctk.CTkImage(Image.open(os.getenv("CLOUD_ICON")), size=(45, 45))
        ctk.CTkButton(master=self.frame,
            image=cloud_img,
            fg_color="transparent",
            hover=False,
            text=os.getenv("APP_TITLE"),
            font=(os.getenv("DEFAULT_FONT"), int(os.getenv("HEADING_FONT2_SIZE"), 12)),
            text_color=os.getenv("PRIMARY_COLOR_MED")
        ).pack(pady=60, side=tk.TOP, padx=10)

        # My Account Label
        user_icon_img = ctk.CTkImage(Image.open(os.getenv("USER_ICON")), size=(30, 30))
        ctk.CTkButton(self.my_account,
            text="My Account",
            image=user_icon_img,
            text_color="white",
            fg_color="#023e8a",
            hover_color="#023e8a",
            font=(os.getenv("DEFAULT_FONT"), int(os.getenv("HEADING_FONT6_SIZE"))),
            command=lambda: ()
        ).pack(padx=10)

        self.left_sidebar.pack_propagate(False)
        self.left_sidebar.pack(side=tk.LEFT, pady=10, padx=10)
        self.left_sidebar.tkraise()


    def build_main_content(self):
        """
            build_main_content() method builds the main content of the Home frame.
            This main content contains the uploaded files and folders of the user.
        """
        # Main Content
        self.main_content = ctk.CTkFrame(self.frame,
            width=int(os.getenv("DEFAULT_APP_WIDTH"))*0.8,
            height=int(os.getenv("DEFAULT_APP_HEIGHT")),
            fg_color="#f7fcfe",
            corner_radius=25
        )
        self.main_content.pack_propagate(False)
        self.main_content.pack(side=tk.RIGHT, pady=10, padx=10)
        self.main_content.tkraise()


    def remove_frame(self, frame):
        """
            remove_frame() method removes the current frame
        """
        for widget in frame.winfo_children():
            widget.destroy()

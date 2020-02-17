# VRIMS
This is a Video Video Rental Inventory System project in Python.
The goal of the project is to design and implement a simple inventory control system for a video rental store.
The following are the various classes that are to be implemented.

#1. Video
  Member variables
      a. Steing videoName
      b. boolean checkout
      c. int rating
  Member functions
      a. String getName();
      b. Checkout();
      c. Return();
      d. receiveRating(int rating);
      e. boolean getCheckout();
  Costructor
      a. Video(String Name)
#2. Video Store
  Member Variables
      a. Video[]store'
  Member functions
      a. addVideo(String name);
      b. doCheckout(String name);
      c. doReturn(String name);
      d. receiveRating(String name, int Rating);
      e. listInventory()'
#3. VideoLauncher
   Contains the main method to test the program 

#Sample Output
--------------- Main Menu -------------------
|    1. Add Video                   |        
|    2. Checkout Video              |        
|    3. Return video                |        
|    4. Receive Rating              |        
|    5. List Inventory              |        
|    6. Exit                        |        
---------------------------------------------
Enter Your Choice!
1
Enter ID : 5
Enter video name : Python Tutorial
Enter video rating : 8
Enter quantity : 4
Enter Video Status (T/F)T

--------------- Main Menu -------------------
|    1. Add Video                   |        
|    2. Checkout Video              |        
|    3. Return video                |        
|    4. Receive Rating              |        
|    5. List Inventory              |        
|    6. Exit                        |        
---------------------------------------------
Enter Your Choice!
2
Enter the video name to checkout : Python Tutorial
Name :  Python Tutorial 
 Checkout :  T
 Rating :  8
 
 --------------- Main Menu -------------------
|    1. Add Video                   |
|    2. Checkout Video              |
|    3. Return video                |
|    4. Receive Rating              |
|    5. List Inventory              |
|    6. Exit                        |
---------------------------------------------
Enter Your Choice!
3
Enter the name of the video you want to return : Calpol
Video Calpol returned successfully

--------------- Main Menu -------------------
|    1. Add Video                   |
|    2. Checkout Video              |
|    3. Return video                |
|    4. Receive Rating              |
|    5. List Inventory              |
|    6. Exit                        |
---------------------------------------------
Enter Your Choice!
4
Enter the name of the video you want to receive rating : Calpol
---------------------------------------------
|1.To update Name                           |
---------------------------------------------
|2.To update Rating                         |
---------------------------------------------
2
Enter the new rating : 8
Rating  8 has been mapped to the video  Calpol

--------------- Main Menu -------------------
|    1. Add Video                   |
|    2. Checkout Video              |
|    3. Return video                |
|    4. Receive Rating              |
|    5. List Inventory              |
|    6. Exit                        |
---------------------------------------------
Enter Your Choice!
5
ID :  1   Name :  Allegra  Rating :  9   Checkout :  T
ID :  2   Name :  Crocin   Rating :  5   Checkout :  F
ID :  3   Name :  Uprise   Rating :  5   Checkout :  T
ID :  4   Name :  Calpol   Rating :  8   Checkout :  T
ID :  5   Name :  Python Tutorial Rating :  8 Checkout :  F
ID :  6   Name :  Dp       Rating :  5   Checkout :  F
 
--------------- Main Menu -------------------
|    1. Add Video                   |
|    2. Checkout Video              |
|    3. Return video                |
|    4. Receive Rating              |
|    5. List Inventory              |
|    6. Exit                        |
---------------------------------------------
Enter Your Choice!
6
----Thank you for using Video Rental Inventory Management----

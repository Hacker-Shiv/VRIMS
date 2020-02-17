import video_store
import sys
menu_choice=0
while(menu_choice!=6):
        print('--------------- Main Menu -------------------')
        print("|    1. Add Video                   |")
        print('|    2. Checkout Video              |')
        print('|    3. Return video                |')
        print('|    4. Receive Rating              |')
        print('|    5. List Inventory              |')
        print('|    6. Exit                        |')
        print('---------------------------------------------')
        m_menu_choice=int(input("Enter Your Choice!\n"))
        if(m_menu_choice==1):
            video_store.add_vid()
        elif(m_menu_choice==2):
            video_store.search_vid()
        elif(m_menu_choice==3):
            video_store.update_vid()
        elif(m_menu_choice==4):
            video_store.update_vid()
        elif m_menu_choice==5:
            video_store.list_all()
        elif m_menu_choice==6:
            print("----Thank you for using Video Rental Inventory Management----")
            break
        else:
            print("Invalid Input! Try Again!\n")    
sys.exit()

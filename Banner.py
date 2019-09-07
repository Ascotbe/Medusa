import random
Version = '0.15'
Blog="""https://ascotbe.github.io"""
banner_1='''
 m    m            #                               mmmm                      
 ##  ##  mmm    mmm#  m   m   mmm    mmm          #"   "  mmm    mmm   m mm  
 # ## # #"  #  #" "#  #   #  #   "  "   #         "#mmm  #"  "  "   #  #"  # 
 # "" # #""""  #   #  #   #   """m  m"""#             "# #      m"""#  #   # 
 #    # "#mm"  "#m##  "mm"#  "mmm"  "mm"#         "mmm#" "#mm"  "mm"#  #   # 
                                                                                                       
                        Blog  {}  |  V {}                                                                                                                                                                        
'''
banner_2 = '''
       __  __          _                   ____                  
      |  \/  | ___  __| |_   _ ___  __ _  / ___|  ___ __ _ _ __  
      | |\/| |/ _ \/ _` | | | / __|/ _` | \___ \ / __/ _` | '_ \ 
      | |  | |  __/ (_| | |_| \__ \ (_| |  ___) | (_| (_| | | | |
      |_|  |_|\___|\__,_|\__,_|___/\__,_| |____/ \___\__,_|_| |_|

             Blog  {}  |  V {}


'''
banner_3 ="""                                                                                                                                                                                                   
                                                                                                                                                                     
"""
banner_4="""                                                                                                                                                                                                                                                                                                                                                                                                     

"""
banner_5="""

"""
banner_6="""

"""
banner_7="""

"""
banner_8="""

"""
banner_9="""

"""
banner_10="""

"""
def RandomBanner():
    Randoms=random.randint(0,10)
    if(Randoms==1):
        print(banner_1.format(Blog,Version))
    elif(Randoms==2):
        print(banner_2.format(Blog,Version))
    # elif (Randoms == 3):
    #     print(banner_3.format(Blog, Version))
    # elif (Randoms == 4):
    #     print(banner_4.format(Blog, Version))
    # elif (Randoms == 5):
    #     print(banner_5.format(Blog, Version))
    # elif (Randoms == 6):
    #     print(banner_6.format(Blog, Version))
    # elif (Randoms == 7):
    #     print(banner_7.format(Blog, Version))
    # elif (Randoms == 8):
    #     print(banner_8.format(Blog, Version))
    # elif (Randoms == 9):
    #     print(banner_9.format(Blog, Version))
    # elif (Randoms == 10):
    #     print(banner_10.format(Blog, Version))
    else:
        print(banner_2.format(Blog,Version))


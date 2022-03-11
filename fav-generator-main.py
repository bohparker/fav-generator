# favicon generator
"""
asks user for favicon img names and inserts them into
favicon link tags in html
"""
import favi

def main():
    print('Favicon Generator')
    print()

    # create the css file
    file = open('favs.html', 'w')
    
    # get the 4 favicon file names and paths
    shortcut = input('Enter image path and name for shortcut image: ')
    icon = input('Enter image path and name for icon image: ')
    apple_icon = input('Enter image and path name for apple icon: ')
    android_icon = input('Enter image and path name for android icon: ')

    # create the html tags containing images
    favi.ins_shortcut(shortcut,file)
    favi.ins_icon(icon,file)
    favi.ins_apple_icon(apple_icon,file)
    favi.ins_android_icon(android_icon,file)

    # close the file
    file.close()

main()

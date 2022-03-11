def ins_shortcut(shortcut,file):
    file.write(
    '<link rel="shortcut icon" href="' + shortcut + '">' + '\n'
        )

def ins_icon(icon,file):
    file.write(
    '<link rel="icon" type="image/png" sizes="32x32" href="' + icon + '">' + '\n'
        )

def ins_apple_icon(apple_icon,file):
    file.write(
    '<link rel="apple-touch-icon" sizes="180x180" href="' + apple_icon + '">' + '\n'
        )

def ins_android_icon(android_icon,file):
    file.write(
        '<link rel="icon" sizes="192x192" href="' + android_icon + '">' + '\n'
        )

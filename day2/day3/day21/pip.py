import termcolor

termcolor.cprint('Hello world', 
    'magenta',
    attrs = ['reverse']
)




text = '{0}+{1}={2}'.format(10,10,10+10)

termcolor.cprint(text, 'red', attrs = ['bold'])
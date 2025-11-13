import devops_module as dev
import sys as sy

number=sy.argv[0]

path=sy.argv[1]

dev.update_image(number,path)

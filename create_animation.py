#! /usr/bin/env python
import argparse
from os import system
import uuid
parser = argparse.ArgumentParser()                                               


parser.add_argument("--files", "-f", type=str, required=True, nargs='*')
parser.add_argument("--output", "-o", type=str, required=True)
parser.add_argument("--create_script", "-c", type=str, nargs='?', const = "./convert.sh")

args = parser.parse_args()
files = args.files
output = args.output
workdir = "/tmp/{}/".format(uuid.uuid4().hex)
index = 1

if (args.create_script):
	script_file = open(args.create_script, "wb")


def command(cmd):
	if (args.create_script):
		script_file.write(cmd + "\n")
	else:
		system(cmd)
		print(cmd)

def file_form_index(index):
	return workdir + "{}.jpg".format(index) 

command("mkdir  -p {}".format(workdir))
for file in sorted(files):
	new_file = file_form_index(index)
	cmd = "cp {} {}".format(file, new_file)
	command(cmd)
	cmd = "mogrify -resize 640x480 {}".format(new_file)
	command(cmd)
	index+=1

for file in sorted(files, reverse=True):
	new_file = file_form_index(index)
	cmd = "cp {} {}".format(file, new_file)
	command(cmd)
	cmd = "mogrify -resize 640x480 {}".format(new_file)
	command(cmd)
	index+=1


convert_input =  " ".join([file_form_index(i) for i in range(1, index)])
convert_cmd = "convert -delay 10 -loop 0 {} {}".format(convert_input, output)
command(convert_cmd)

command("rm -r {}".format(workdir))

if (args.create_script):
	script_file.close()
# path_to_anim = "/home/alex/Pictures/100D3000/anim2"
# from os import listdir, system
# from os.path import isfile, join
# onlyfiles = [f for f in listdir(path_to_anim) if isfile(join(path_to_anim, f))]
# reverse_files = sorted(onlyfiles, reverse=True)
# for i in range(len(onlyfiles)):
# 	print (onlyfiles[i], reverse_files[i])
# system("mkdir {}".format(path_to_anim + "/sorted"))
# index = 1
# for x in onlyfiles:
# 	command = "cp {} {}".format(path_to_anim+"/" +x, path_to_anim + "/sorted/" + str(index)+".JPG")
# 	print(command)
# 	system(command)
# 	index +=1

# for x in reverse_files	:
# 	command = "cp {} {}".format(path_to_anim+"/" +x, path_to_anim + "/sorted/" + str(index)+".JPG")
# 	print(command)
# 	system(command)
# 	index +=1

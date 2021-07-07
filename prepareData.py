#!/usr/bin/env python3
import os
import cv2

import argparse
import configparser
import re
import sys

import requests


def prepare(save_dir,img_dir,filename):
	#from pyocclient import owncloud
	IMG_SIZE = 70
	img_array = cv2.imread(os.path.join(img_dir,filename), cv2.IMREAD_GRAYSCALE)
	new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
	#return new_array.reshape(-1,IMG_SIZE,IMG_SIZE,-1)
	cv2.imwrite(os.path.join(save_dir,"processed.jpeg"),new_array)




def main():
	# Parse command line arguments
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument("-c", "--config", help="configuration filename")
    arguments = argument_parser.parse_args()
    config_filename = arguments.config

    # Parse configuration
    config_parser = configparser.ConfigParser()
    config_parser.read(config_filename)
    try:
        username = config_parser.get("Connection", "username")
        password = config_parser.get("Connection", "password")
        hostname = config_parser.get("Connection", "hostname")
    except configparser.Error:
        sys.stderr.write('Missing configuration in "{}".\n'.format(config_filename))
        return FAILURE

    

if __name__ == '__main__':
	#oc = owncloud.Client('192.168.1.13', verify_certs=False,debug=True)
	#print(oc.__dict__.keys())
	#oc.login('admin', 'raspberry')
	#print(oc.list('/imageDatasetRaw'))
	prepare('./save/','./','img1.jpeg')



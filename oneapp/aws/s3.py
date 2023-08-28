# import boto3
# import re


# patternm=re.compile(r'^aws')
# #print (dir(boto3))
# #print (dir(boto3.session))
# accesskeyid=boto3.Session().get_credentials().access_key
# secreaccess=boto3.Session().get_credentials().secret_key
# client = boto3.client(
#     's3',
#     aws_access_key_id=accesskeyid,
#     aws_secret_access_key=secreaccess,
#     region_name="ap-south-1"
# )
# completebucket_names=[]
# #print (dir(client))
# lisbukcets_all=client.list_buckets()
# #print (lisbukcets_all)
# '''print (lisbukcets_all.keys())'''
# '''print (lisbukcets_all['Buckets'])'''
# count_of_bukc=len(lisbukcets_all['Buckets'])
# print ("Below are the List of buckets availale in account")
# for j in range(0,count_of_bukc,1):
#     #print (lisbukcets_all['Buckets'][j]['Name'])
#     completebucket_names.append(lisbukcets_all['Buckets'][j]['Name'])
# print (completebucket_names)
# userinput_bucket=input("Enter the uniq-name to create new bucket:\n")
# if (userinput_bucket.strip() in completebucket_names):
#     print ("Bucket {0} is already present in account".format(userinput_bucket))

# else:
#     print ("Bukcet {0} is not present in account".format(userinput_bucket))
#     userinput_conf=input("Enter yes to create bucket\n")
#     if (userinput_conf.strip() == "yes"):
#         buckcreation_full=[]
#         print ("User confirmed to create bukcet{0}".format(userinput_bucket))
#         client.create_bucket(Bucket='{0}'.format(userinput_bucket),CreateBucketConfiguration={'LocationConstraint':'ap-south-1'})
#         lisbukcets_all_postcreation = client.list_buckets()
#         print (lisbukcets_all_postcreation['Buckets'])
#         len_buc_cou=len(lisbukcets_all_postcreation['Buckets'])
#         for chek_buk in range(0,len_buc_cou,1):
#             #print (lisbukcets_all_postcreation['Buckets'][chek_buk])
#             buckcreation_full.append(lisbukcets_all_postcreation['Buckets'][chek_buk]['Name'])

#         if (userinput_bucket.strip() in buckcreation_full ):
#             print ("Bucket {0} has been created successfully post user confirmation".format(userinput_bucket))

#         else:
#             print ("Bucket {0} not created successfully".format(userinput_bucket))
#     upload_objec = input("Enter \n'1' to upload object\n\n'2' to download :")
#     bucke_ope=input("Enter the Bukcetname\n")
#     if (upload_objec == "1"):
#             path_file=input("Enter the path of file (eg:D:\foldername-aaa\filename.txt-bb.txt)\n")
#             keyname=input("Enter the s3bucket filename (eg:filename.txt-bb.txt)\n")
#             client.upload_file(path_file,bucke_ope,keyname)
#             objets_list=client.list_objects(Bucket=bucke_ope)
#             print (objets_list)
#             print (objets_list.keys())
#             print (objets_list['Contents'])
#             print ("Below  content is Object name  ")
#             for  obj_ra in range(0,len(objets_list['Contents']),1):
#                 keyname_ui=objets_list['Contents'][obj_ra]['Key']
#                 size_ui=objets_list['Contents'][obj_ra]['Size']
#                 print ("{0}".format(keyname_ui))
#     elif (upload_objec == "2"):
#         path_to_download=input("Enter the localpath to download the file\n")
#         s3bucket_filename=input("Enter the filename of s3 bucket\n")
#         fullfilepath="{0}\{1}".format(path_to_download,s3bucket_filename)
#         print ("DOWNLOAD S3 Bucket file {0} to Local path {1}".format(s3bucket_filename,fullfilepath))
#         with open(fullfilepath,'wb') as data:
#             client.download_fileobj(bucke_ope,s3bucket_filename,data)




#     else:
#         print ("User Not conformed to create bucket {0}".format(userinput_bucket))

# #!/usr/bin/python
# import boto3
# ec2_call_region=boto3.client('ec2')
# def regioncollection():
#     global regionlist#!/usr/bin/python
# import boto3
# ec2_call_region=boto3.client('ec2')
# def regioncollection():
#     global regionlist
#     regionlist=[]
#     region_collections=ec2_call_region.describe_regions()
#     for regid in range(0,len(region_collections['Regions']),1):
#         if region_collections['Regions'][regid]['RegionName'].strip() not in  regionlist:
#             regionlist.append(region_collections['Regions'][regid]['RegionName'].strip())
#     print( "Below are Regions available in aws account \n\n\n {0}".format("\n".join(regionlist)))

# regioncollection()



# regionname_input=input("Enter the Region name required from above list\n")

# ec2_call=boto3.client('ec2','{0}'.format(regionname_input))

# def collectingkeypairs():
#     keypair_collection=[]
#     keypaircollection=ec2_call.describe_key_pairs()
#     for keypaircoll in range(0,len(keypaircollection['KeyPairs']),1):
#         if keypaircollection['KeyPairs'][keypaircoll]['KeyName'] not in keypair_collection:
#             keypair_collection.append(keypaircollection['KeyPairs'][keypaircoll]['KeyName'])
#     print( "Below are the Key pair collection in the region {0}\n\n\n{1}".format(regionname_input.strip(),"\n".join(keypair_collection))        )


# collectingkeypairs()
# #print( dir(ec2_call))
# #print( dir(ec2_call.run_instances()))

# aws_key_pair=input("Enter the key pair from above list\n")
# print (aws_key_pair)

# def collecting_security_groups():
#     global security_group_list
#     global security_group_collection
#     security_group_list=[]
#     security_group_collection=ec2_call.describe_security_groups()
#     for sec in range(0,len(security_group_collection['SecurityGroups']),1):
#         if security_group_collection['SecurityGroups'][sec]['GroupName'] not in security_group_list:
#             security_group_list.append(security_group_collection['SecurityGroups'][sec]['GroupName'])
# #    print( "\nBelow are the Security group available in the region  {0}\n\n{1}".format(regionname_input.strip(),"\n".join(security_group_list))        )


# collecting_security_groups()




# def collecting_subnet_details():
#     global subnet_list
#     global subnet_collections
#     subnet_list=[]

#     subnet_collections=ec2_call.describe_subnets()
#     for subran in range(0,len(subnet_collections['Subnets']),1):
#         if  subnet_collections['Subnets'][subran]['SubnetId'] not in subnet_list:
#             subnet_list.append(subnet_collections['Subnets'][subran]['SubnetId'])
# #    print( "\n Below are the Subnets available in the region {0}\n\n{1}".format(regionname_input.strip(),"\n".join(subnet_list)))



# collecting_subnet_details()


# count_instances_required=input("Enter the count of instances required\n")
# print( "Below are the Regions available in aws account\n\n{0}\n".format("\n".join(regionlist)))
# regionselect=input("Enter Any one region name where you want to create instances\n")
# print( regionselect)

# print( "Below are Subnets available available in  the region {0}\n\n{1}".format(regionselect.strip(),"\n".join(subnet_list)))

# subnetselect=input("Enter Any one subnet name from above list which will be used to create EC2 instance\n\n")

# print( subnetselect)

# def selected_subnet_details():
#     global vpcid_selected
#     for selesubn in range(0,len(subnet_collections['Subnets']),1):
#         if(subnet_collections['Subnets'][selesubn]['SubnetId'] == str(subnetselect.strip())):
#             print( "Below are the details of Subnet {0} in region {1}\n\n".format(subnetselect.strip(),regionselect.strip()))
#             print( "PublicIp_on_launch: {0}".format( subnet_collections['Subnets'][selesubn]['MapPublicIpOnLaunch']))
#             print( "Vpc_id: {0}".format(subnet_collections['Subnets'][selesubn]['VpcId']))
#             vpcid_selected="{0}".format(subnet_collections['Subnets'][selesubn]['VpcId'])
#             print( "Available_IP_adress_count: {0}".format(subnet_collections['Subnets'][selesubn]['AvailableIpAddressCount']))
#             print( "CIDR_Block_range: {0}".format(subnet_collections['Subnets'][selesubn]['CidrBlock']))
#             print( "Subnet_state: {0}".format(subnet_collections['Subnets'][selesubn]['State']))
#             print( "Availability_zone: {0}\n\n".format(subnet_collections['Subnets'][selesubn]['AvailabilityZone']))

# selected_subnet_details()

# #print( "Below are the Security Group details available in the region {0}\n\n{1}".format(regionselect.strip(),"\n".join(security_group_list)))

# #selectsecuritygrp=raw_input("Enter the Security group from above list which will be used to create EC2 instance\n\n")

# def security_group_collection_collect():
#     security_group_under_vpcids=[]
# #    print( security_group_collection['SecurityGroups'])
#     for secran in range(0,len(security_group_collection['SecurityGroups']),1):
#         if (security_group_collection['SecurityGroups'][secran]['VpcId'] == str(vpcid_selected)):
#             if security_group_collection['SecurityGroups'][secran]['GroupName'] not in security_group_under_vpcids:
#                 security_group_under_vpcids.append(security_group_collection['SecurityGroups'][secran]['GroupName'])
#     if(len(security_group_under_vpcids)>0):
#         print( "Below are the security Groups available  under Vpcid {0}\n\n{1}".format(vpcid_selected,"\n".join(security_group_under_vpcids)))


# security_group_collection_collect()


# selectsecuritygrp=input("Enter the Security group from above list which will be used to create EC2 instance\n\n")
# print( selectsecuritygrp)

# def Collecting_details_selected_security_group():
#     global selectsecuritygrp
#     Inbound_port=[]
#     Outbound_port=[]
#     for selecsg_range in range(0,len(security_group_collection['SecurityGroups']),1):
#         if (str(security_group_collection['SecurityGroups'][selecsg_range]['GroupName']) == str(selectsecuritygrp)):
#             print( security_group_collection['SecurityGroups'][selecsg_range]['GroupName'])
#             print( "\n\nBelow are the Details of security group {0}\n\n".format(selectsecuritygrp.strip()))
#             #print( security_group_collection['SecurityGroups'][selecsg_range])
#             print( "Security_Group_id: {0}".format(security_group_collection['SecurityGroups'][selecsg_range]['GroupId']))
#             selectsecuritygrp="{0}".format(security_group_collection['SecurityGroups'][selecsg_range]['GroupId'])
#             print( "Vpc_id: {0}".format(security_group_collection['SecurityGroups'][selecsg_range]['VpcId']))
#             for inbound in range(0,len(security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions']),1):
#                 if security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions'][inbound]['ToPort'] not in Inbound_port:
#                     Inbound_port.append(security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions'][inbound]['ToPort'])
#             for oubound in range(0,len(security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions']),1):
#                 if security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions'][oubound]['FromPort'] not in Outbound_port:
#                     Outbound_port.append(security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions'][oubound]['FromPort'])
#             print( "Inbound_Port details: {0}".format(Inbound_port))
#             print( "Outbound_Port_details: {0}".format(Outbound_port))





# Collecting_details_selected_security_group()




# instance_type=input("Enter the Instance type\n")
# ami_id=input("Enter the ami id\n")


# #def creating_instances():
# #    instance_creation=ec2_call.run_instances(ImageId="ami-0c6615d1e95c98aca",InstanceType="{0}".format(instance_type.strip()),KeyName="{0}".format('nov15'),MaxCount=int(count_instances_required),MinCount=int(1),SecurityGroupIds=[selectsecuritygrp],SubnetId="{0}".format(subnetselect.strip()),NetworkInterfaces=[
# #    {
# #        'DeviceIndex': 0,
# #        'SubnetId' : subnetselect.strip(),
# #        'Groups': [selectsecuritygrp],
# #        ]
# #        'AssociatePublicIpAddress': True
# #    })
# #    print( instance_creation)


# #creating_instances()

# #kj=ec2_call.run_instances(InstanceType=str(instance_type.strip()),
# #                         MaxCount=int(count_instances_required),
# #                         MinCount=int(count_instances_required),
# #                         ImageId="ami-0c6615d1e95c98aca")

# #print( kj)

# ec2_call_create=boto3.resource('ec2',region_name='{0}'.format(regionname_input))

# def creating_instances():
#     global instance_creation
#     instance_creation=ec2_call_create.create_instances(ImageId="{0}".format(ami_id),InstanceType="{0}".format(instance_type.strip()),KeyName="{0}".format(aws_key_pair),MaxCount=int(count_instances_required),MinCount=int(1),NetworkInterfaces=[
#     {
#         'DeviceIndex': 0,
#         'SubnetId' : subnetselect.strip(),
#         'Groups': [selectsecuritygrp],

#         'AssociatePublicIpAddress': True
#     }])
# #    print( dir(instance_creation))
# #    instance_creation.reload()

#     for instanceid in instance_creation:
#         print( instanceid.id)
#         instanceid.wait_until_running()




# creating_instances()



# def Fetching_details_instances():
#     for insdeta in instance_creation:
#         instance_id_de=insdeta.id
#         desinsta=ec2_call.describe_instances(InstanceIds=[instance_id_de])
#         print( "\n\nBelow are the details of Newly created instance id {0}\n\n".format(instance_id_de))
#         print( "Public_DNS_NAME: {0}".format(desinsta['Reservations'][0]['Instances'][0]['PublicDnsName']))
#         print( "State of instance: {0}".format(desinsta['Reservations'][0]['Instances'][0]['State']['Name']))
#         print( "Public_IP_Adress: {0}".format(desinsta['Reservations'][0]['Instances'][0]['PublicIpAddress']))
#         print( "Vpc_id: {0}".format(desinsta['Reservations'][0]['Instances'][0]['VpcId'] ))
#         print( "Cpu_core_details: {0}".format(desinsta['Reservations'][0]['Instances'][0]['CpuOptions']['CoreCount']))
#         print( "Image-id_of_instance: {0}".format(desinsta['Reservations'][0]['Instances'][0]['ImageId']))
#         print( "Private_IP_Adress: {0}".format(desinsta['Reservations'][0]['Instances'][0]['PrivateIpAddress']))
#         print( "Keypairname: {0}".format(desinsta['Reservations'][0]['Instances'][0]['KeyName']))
#         print( "Security_groups: {0}".format(desinsta['Reservations'][0]['Instances'][0]['SecurityGroups']))
#         print( "Subnet_id: {0}".format(desinsta['Reservations'][0]['Instances'][0]['SubnetId']))
#         print( "root_device_name: {0}".format(desinsta['Reservations'][0]['Instances'][0]['RootDeviceName']))
#         print( "root_device_type: {0}".format(desinsta['Reservations'][0]['Instances'][0]['RootDeviceType']))
#         print( "\n\n===============End of details of instance id {0}======================================\n\n".format(instance_id_de))



# Fetching_details_instances()
# '''regionlist=[]
# region_collections=ec2_call_region.describe_regions()
# for regid in range(0,len(region_collections['Regions']),1):
#     if region_collections['Regions'][regid]['RegionName'].strip() not in  regionlist:
#       regionlist.append(region_collections['Regions'][regid]['RegionName'].strip())
#     print( "Below are Regions available in aws account \n\n\n {0}".format("\n".join(regionlist)))

# regioncollection()



# regionname_input=input("Enter the Region name required from above list\n")

# ec2_call=boto3.client('ec2','{0}'.format(regionname_input))

# def collectingkeypairs():
#     keypair_collection=[]
#     keypaircollection=ec2_call.describe_key_pairs()
#     for keypaircoll in range(0,len(keypaircollection['KeyPairs']),1):
#         if keypaircollection['KeyPairs'][keypaircoll]['KeyName'] not in keypair_collection:
#             keypair_collection.append(keypaircollection['KeyPairs'][keypaircoll]['KeyName'])
#     print( "Below are the Key pair collection in the region {0}\n\n\n{1}".format(regionname_input.strip(),"\n".join(keypair_collection))        )


# collectingkeypairs()
# #print( dir(ec2_call))
# #print( dir(ec2_call.run_instances()))

# aws_key_pair=input("Enter the key pair from above list\n")
# print (aws_key_pair)

# def collecting_security_groups():
#     global security_group_list
#     global security_group_collection
#     security_group_list=[]
#     security_group_collection=ec2_call.describe_security_groups()
#     for sec in range(0,len(security_group_collection['SecurityGroups']),1):
#         if security_group_collection['SecurityGroups'][sec]['GroupName'] not in security_group_list:
#             security_group_list.append(security_group_collection['SecurityGroups'][sec]['GroupName'])
# #    print( "\nBelow are the Security group available in the region  {0}\n\n{1}".format(regionname_input.strip(),"\n".join(security_group_list))        )


# collecting_security_groups()




# def collecting_subnet_details():
#     global subnet_list
#     global subnet_collections
#     subnet_list=[]

#     subnet_collections=ec2_call.describe_subnets()
#     for subran in range(0,len(subnet_collections['Subnets']),1):
#         if  subnet_collections['Subnets'][subran]['SubnetId'] not in subnet_list:
#             subnet_list.append(subnet_collections['Subnets'][subran]['SubnetId'])
# #    print( "\n Below are the Subnets available in the region {0}\n\n{1}".format(regionname_input.strip(),"\n".join(subnet_list)))



# collecting_subnet_details()


# count_instances_required=input("Enter the count of instances required\n")
# print( "Below are the Regions available in aws account\n\n{0}\n".format("\n".join(regionlist)))
# regionselect=input("Enter Any one region name where you want to create instances\n")
# print( regionselect)

# print( "Below are Subnets available available in  the region {0}\n\n{1}".format(regionselect.strip(),"\n".join(subnet_list)))

# subnetselect=input("Enter Any one subnet name from above list which will be used to create EC2 instance\n\n")

# print( subnetselect)

# def selected_subnet_details():
#     global vpcid_selected
#     for selesubn in range(0,len(subnet_collections['Subnets']),1):
#         if(subnet_collections['Subnets'][selesubn]['SubnetId'] == str(subnetselect.strip())):
#             print( "Below are the details of Subnet {0} in region {1}\n\n".format(subnetselect.strip(),regionselect.strip()))
#             print( "PublicIp_on_launch: {0}".format( subnet_collections['Subnets'][selesubn]['MapPublicIpOnLaunch']))
#             print( "Vpc_id: {0}".format(subnet_collections['Subnets'][selesubn]['VpcId']))
#             vpcid_selected="{0}".format(subnet_collections['Subnets'][selesubn]['VpcId'])
#             print( "Available_IP_adress_count: {0}".format(subnet_collections['Subnets'][selesubn]['AvailableIpAddressCount']))
#             print( "CIDR_Block_range: {0}".format(subnet_collections['Subnets'][selesubn]['CidrBlock']))
#             print( "Subnet_state: {0}".format(subnet_collections['Subnets'][selesubn]['State']))
#             print( "Availability_zone: {0}\n\n".format(subnet_collections['Subnets'][selesubn]['AvailabilityZone']))

# selected_subnet_details()

# #print( "Below are the Security Group details available in the region {0}\n\n{1}".format(regionselect.strip(),"\n".join(security_group_list)))

# #selectsecuritygrp=raw_input("Enter the Security group from above list which will be used to create EC2 instance\n\n")

# def security_group_collection_collect():
#     security_group_under_vpcids=[]
# #    print( security_group_collection['SecurityGroups'])
#     for secran in range(0,len(security_group_collection['SecurityGroups']),1):
#         if (security_group_collection['SecurityGroups'][secran]['VpcId'] == str(vpcid_selected)):
#             if security_group_collection['SecurityGroups'][secran]['GroupName'] not in security_group_under_vpcids:
#                 security_group_under_vpcids.append(security_group_collection['SecurityGroups'][secran]['GroupName'])
#     if(len(security_group_under_vpcids)>0):
#         print( "Below are the security Groups available  under Vpcid {0}\n\n{1}".format(vpcid_selected,"\n".join(security_group_under_vpcids)))


# security_group_collection_collect()


# selectsecuritygrp=input("Enter the Security group from above list which will be used to create EC2 instance\n\n")
# print( selectsecuritygrp)

# def Collecting_details_selected_security_group():
#     global selectsecuritygrp
#     Inbound_port=[]
#     Outbound_port=[]
#     for selecsg_range in range(0,len(security_group_collection['SecurityGroups']),1):
#         if (str(security_group_collection['SecurityGroups'][selecsg_range]['GroupName']) == str(selectsecuritygrp)):
#             print( security_group_collection['SecurityGroups'][selecsg_range]['GroupName'])
#             print( "\n\nBelow are the Details of security group {0}\n\n".format(selectsecuritygrp.strip()))
#             #print( security_group_collection['SecurityGroups'][selecsg_range])
#             print( "Security_Group_id: {0}".format(security_group_collection['SecurityGroups'][selecsg_range]['GroupId']))
#             selectsecuritygrp="{0}".format(security_group_collection['SecurityGroups'][selecsg_range]['GroupId'])
#             print( "Vpc_id: {0}".format(security_group_collection['SecurityGroups'][selecsg_range]['VpcId']))
#             for inbound in range(0,len(security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions']),1):
#                 if security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions'][inbound]['ToPort'] not in Inbound_port:
#                     Inbound_port.append(security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions'][inbound]['ToPort'])
#             for oubound in range(0,len(security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions']),1):
#                 if security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions'][oubound]['FromPort'] not in Outbound_port:
#                     Outbound_port.append(security_group_collection['SecurityGroups'][selecsg_range]['IpPermissions'][oubound]['FromPort'])
#             print( "Inbound_Port details: {0}".format(Inbound_port))
#             print( "Outbound_Port_details: {0}".format(Outbound_port))





# Collecting_details_selected_security_group()




# instance_type=input("Enter the Instance type\n")
# ami_id=input("Enter the ami id\n")


# #def creating_instances():
# #    instance_creation=ec2_call.run_instances(ImageId="ami-0c6615d1e95c98aca",InstanceType="{0}".format(instance_type.strip()),KeyName="{0}".format('nov15'),MaxCount=int(count_instances_required),MinCount=int(1),SecurityGroupIds=[selectsecuritygrp],SubnetId="{0}".format(subnetselect.strip()),NetworkInterfaces=[
# #    {
# #        'DeviceIndex': 0,
# #        'SubnetId' : subnetselect.strip(),
# #        'Groups': [selectsecuritygrp],
# #        ]
# #        'AssociatePublicIpAddress': True
# #    })
# #    print( instance_creation)


# #creating_instances()

# #kj=ec2_call.run_instances(InstanceType=str(instance_type.strip()),
# #                         MaxCount=int(count_instances_required),
# #                         MinCount=int(count_instances_required),
# #                         ImageId="ami-0c6615d1e95c98aca")

# #print( kj)

# ec2_call_create=boto3.resource('ec2',region_name='{0}'.format(regionname_input))

# def creating_instances():
#     global instance_creation
#     instance_creation=ec2_call_create.create_instances(ImageId="{0}".format(ami_id),InstanceType="{0}".format(instance_type.strip()),KeyName="{0}".format(aws_key_pair),MaxCount=int(count_instances_required),MinCount=int(1),NetworkInterfaces=[
#     {
#         'DeviceIndex': 0,
#         'SubnetId' : subnetselect.strip(),
#         'Groups': [selectsecuritygrp],

#         'AssociatePublicIpAddress': True
#     }])
# #    print( dir(instance_creation))
# #    instance_creation.reload()

#     for instanceid in instance_creation:
#         print( instanceid.id)
#         instanceid.wait_until_running()




# creating_instances()



# def Fetching_details_instances():
#     for insdeta in instance_creation:
#         instance_id_de=insdeta.id
#         desinsta=ec2_call.describe_instances(InstanceIds=[instance_id_de])
#         print( "\n\nBelow are the details of Newly created instance id {0}\n\n".format(instance_id_de))
#         print( "Public_DNS_NAME: {0}".format(desinsta['Reservations'][0]['Instances'][0]['PublicDnsName']))
#         print( "State of instance: {0}".format(desinsta['Reservations'][0]['Instances'][0]['State']['Name']))
#         print( "Public_IP_Adress: {0}".format(desinsta['Reservations'][0]['Instances'][0]['PublicIpAddress']))
#         print( "Vpc_id: {0}".format(desinsta['Reservations'][0]['Instances'][0]['VpcId'] ))
#         print( "Cpu_core_details: {0}".format(desinsta['Reservations'][0]['Instances'][0]['CpuOptions']['CoreCount']))
#         print( "Image-id_of_instance: {0}".format(desinsta['Reservations'][0]['Instances'][0]['ImageId']))
#         print( "Private_IP_Adress: {0}".format(desinsta['Reservations'][0]['Instances'][0]['PrivateIpAddress']))
#         print( "Keypairname: {0}".format(desinsta['Reservations'][0]['Instances'][0]['KeyName']))
#         print( "Security_groups: {0}".format(desinsta['Reservations'][0]['Instances'][0]['SecurityGroups']))
#         print( "Subnet_id: {0}".format(desinsta['Reservations'][0]['Instances'][0]['SubnetId']))
#         print( "root_device_name: {0}".format(desinsta['Reservations'][0]['Instances'][0]['RootDeviceName']))
#         print( "root_device_type: {0}".format(desinsta['Reservations'][0]['Instances'][0]['RootDeviceType']))
#         print( "\n\n===============End of details of instance id {0}======================================\n\n".format(instance_id_de))



# Fetching_details_instances()'''

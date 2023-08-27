# import boto3
# import time


# def get_user_input(prompt):
#     return input(prompt).strip()

# def create_vpc(vpc_cidr_block):
#     ec2 = boto3.client('ec2')

#     vpc_creation = ec2.create_vpc(CidrBlock=vpc_cidr_block)
#     vpc_id = vpc_creation['Vpc']['VpcId']

#     # Wait for the VPC to become available
#     while True:
#         checking_vpcstate = ec2.describe_vpcs(VpcIds=[vpc_id])
#         if checking_vpcstate['Vpcs'][0]['State'] == 'available':
#             break
#         time.sleep(2)

#     return vpc_id
# def create_subnet(vpc_id, subnet_cidr_block):
#     ec2 = boto3.client('ec2')

#     subnet_cret = ec2.create_subnet(VpcId=vpc_id, CidrBlock=subnet_cidr_block)
#     subnet_id = subnet_cret['Subnet']['SubnetId']

#     ec2.modify_subnet_attribute(SubnetId=subnet_id, MapPublicIpOnLaunch={'Value': True})

#     return subnet_id
# def create_internet_gateway():
#     ec2 = boto3.client('ec2')

#     create_igw = ec2.create_internet_gateway()
#     igw_id = create_igw['InternetGateway']['InternetGatewayId']

#     return igw_id

# def attach_internet_gateway_to_vpc(vpc_id, igw_id):
#     ec2 = boto3.client('ec2')

#     ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)

# def create_route_table(vpc_id, igw_id):
#     ec2 = boto3.client('ec2')

#     route_tablecreation= ec2.create_route_table(VpcId=vpc_id)
#     route_table_id = route_tablecreation['RouteTable']['RouteTableId']

#     # Create a route to the internet gateway
#     ec2.create_route(
#         RouteTableId=route_table_id,
#         DestinationCidrBlock='0.0.0.0/0',
#         GatewayId=igw_id
#     )

#     return route_table_id

# def associate_route_table(route_table_id, subnet_id):
#     ec2 = boto3.client('ec2')

#     ec2.associate_route_table(RouteTableId=route_table_id, SubnetId=subnet_id)

# def regioncollection():
#     ec2_call_region = boto3.client('ec2')
#     global regionlist
#     regionlist = []
#     region_collections = ec2_call_region.describe_regions()
#     for regid in range(0, len(region_collections['Regions']), 1):
#         if region_collections['Regions'][regid]['RegionName'].strip() not in regionlist:
#             regionlist.append(region_collections['Regions'][regid]['RegionName'].strip())
#     print("Below are Regions available in AWS account:\n{0}".format("\n".join(regionlist)))

# def main():
#     try:
#         regioncollection()
#         regionname_input = input("Enter the Region name to create VPC in the required Region from the above list: ")
#         vpc_cidr_block = get_user_input("Enter VPC CIDR block : ")

#         boto3.setup_default_session(region_name=regionname_input)

#         vpc_id = create_vpc(vpc_cidr_block)
#         subnet_cidr_block = get_user_input("Enter Subnet CIDR block : ")
#         subnet_id = create_subnet(vpc_id, subnet_cidr_block)

#         igw_id = create_internet_gateway()
#         attach_internet_gateway_to_vpc(vpc_id, igw_id)

#         route_table_id = create_route_table(vpc_id, igw_id)
#         if not route_table_id:
#             print("Route table creation failed.")
#             return

#         # Associate the route table with the subnet
#         associate_route_table(route_table_id, subnet_id)

#         # Print the state of each resource
#         ec2 = boto3.client('ec2')
#         vpc_state = ec2.describe_vpcs(VpcIds=[vpc_id])['Vpcs'][0].get('State', 'N/A')
#         subnet_state = ec2.describe_subnets(SubnetIds=[subnet_id])['Subnets'][0].get('State', 'N/A')
#         igw_state = ec2.describe_internet_gateways(InternetGatewayIds=[igw_id])['InternetGateways'][0]['Attachments'][0].get('State', 'N/A')
#         route_table_state = ec2.describe_route_tables(RouteTableIds=[route_table_id])['RouteTables'][0]['Associations'][0].get('State', 'N/A')


#         print("created vpc id: {0} and vpc state :{1}".format(vpc_id,vpc_state))

#         print("created subnet id :{0} and subnet state :{1}".format(subnet_id,subnet_state))
#         print("created internet gateway id: {0} and state: {1}".format(igw_id,igw_state))
#         print(f"created Route Table ID: {route_table_id}, State: {route_table_state}")
#         print("created route table id :{0} and state :{1}".format(route_table_id,route_table_state))
#     except Exception as e:
#         print("An error occurred: ", str(e))

# if __name__ == "__main__":
#     main()
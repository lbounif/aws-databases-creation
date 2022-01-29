import boto3
conn = boto3.client('rds', aws_access_key_id='**********',
                     aws_secret_access_key='**********',
                     region_name='eu-west-1')

response = conn.create_db_instance(
        AllocatedStorage=10,
        DBName="test",
        DBInstanceIdentifier="my-first-rds-instance",
        DBInstanceClass="db.t2.micro",
        Engine="mysql",
        MasterUsername="root",
        MasterUserPassword="pass1234",
        Port=3306,
        VpcSecurityGroupIds=["**********"],
    
    )

print (response)
# sg-08c496340fefd1d12
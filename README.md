<p align="center">
  <a href="https://dev.to/vumdao">
    <img alt="Multi threading in lambda function" src="https://dev-to-uploads.s3.amazonaws.com/i/8w206lcs798a2mfit9tb.png" width="500" />
  </a>
</p>
<h3 align="center">
  <b>Here's a simple multi-threaded program in lambda function.</b>
</h3>


## What’s In This Document 
- [Create lambda function using chalice](#-Create-lambda-function-using-chalice)
- [Run test](#-Run-test)
- [Check result](#-Check-result)

#

### 🚀 **[Create lambda function using chalice](#-Create-lambda-function-using-chalice)**
- Source code
```
from chalice import Chalice
import threading
import time
from datetime import datetime


app = Chalice(app_name='multithread-test')
app.debug = True


def run_thread(msg):
    app.log.debug(f"Call {msg} and sleep, timestamp {datetime.now()}")
    time.sleep(5)


@app.lambda_function(name='multithread-test')
def handler(event, context):
    thread_list = list()
    for i in range(0, 5):
        msg = f'thread-{i}'
        thread = threading.Thread(target=run_thread, args=(msg,))
        thread_list.append(thread)
        thread.start()

    for t in thread_list:
        t.join()

    return "Done!"
```
- Create AWS chalice new project
```
⚡ $ chalice new-project multithread-test
```
- Deploy function
```
⚡ $ chalice deploy 
Creating deployment package.
Creating IAM role: multithread-test-dev
Creating lambda function: multithread-test-dev-multithread-test
Resources deployed:
  - Lambda ARN: arn:aws:lambda:ap-northeast-2:1111111111111:function:multithread-test-dev-multithread-test
```

### 🚀 **[Run test](#-Run-test)**
- Invoke lambda function using aws-cli
```
⚡ $ aws lambda invoke --function-name multithread-test-dev-multithread-test --region ap-northeast-2 outfile 
{
    "StatusCode": 200,
    "ExecutedVersion": "$LATEST"
}
```

### 🚀 [Check result](#-Check-result)
![Alt Text](https://dev-to-uploads.s3.amazonaws.com/i/evb0w86gjnfaoa8w4nuq.png)

**Read More**
- [Pelican-resume with docker-compose and AWS + CDK](https://dev.to/vumdao/pelican-resume-with-docker-compose-and-aws-cdk-33e5)
- [Using Helm Install Botkube Integrate With Slack On EKS](https://dev.to/vumdao/using-helm-install-botkube-integrate-with-slack-on-eks-gmn)
- [Ansible AWS EC2 Dynamic Inventory Plugin](https://dev.to/vumdao/ansible-aws-ec2-dynamic-inventory-plugin-3bme)
- [How To List All Enabled Regions Within An AWS account](https://dev.to/vumdao/list-all-enabled-regions-within-an-aws-account-4oo7)
- [Using AWS KMS In AWS Lambda](https://dev.to/vumdao/using-aws-kms-in-aws-lambda-2jm2)
- [Create AWS Backup Plan](https://dev.to/vumdao/create-aws-backup-plan-a0f)
- [Techniques For Writing Least Privilege IAM Policies](https://dev.to/vumdao/techniques-for-writing-least-privilege-iam-policies-4fc7)
- [EKS Persistent Storage With EFS Amazon Service](https://dev.to/vumdao/eks-persistent-storage-with-efs-amazon-service-14ei)
- [Create k8s Cronjob To Schedule Delete Expired Files](https://dev.to/vumdao/create-k8s-cronjob-to-schedule-delete-expired-files-1i41)
- [Amazon ECR - Lifecycle Policy Rules](https://dev.to/vumdao/amazon-ecr-lifecycle-policy-rules-1l59)
- [Connect Postgres Database Using Lambda Function](https://dev.to/vumdao/connect-postgres-database-using-lambda-function-1mca)
- [Using SourceIp in ALB Listener Rule](https://dev.to/vumdao/using-sourceip-in-alb-listener-rule-377b)
- [Amazon Simple Systems Manager (SSM)](https://dev.to/vumdao/amazon-simple-systems-manager-ssm-2pb0)
- [Invalidation AWS CDN Using Boto3](https://dev.to/vumdao/invalidation-aws-cdn-using-boto3-2k9g)
- [Create AWS Lambda Function Triggered By S3 Notification Event](https://dev.to/vumdao/create-aws-lambda-function-triggered-by-s3-notification-event-9p0)
- [CI/CD Of Invalidation AWS CDN Using Gitlab Pipeline](https://dev.to/vumdao/ci-cd-of-invalidation-aws-cdn-using-gitlab-pipeline-34op)
- [Create CodeDeploy](https://dev.to/vumdao/create-codedeploy-4425)
- [Gitlab Pipeline With AWS Codedeploy](https://dev.to/vumdao/gitlab-pipeline-with-aws-codedeploy-30cl)
- [Create AWS-CDK image container](https://dev.to/vumdao/create-aws-cdk-image-container-43ei)
- [Deploy Python Lambda Functions With Container Image](https://dev.to/vumdao/deploy-python-lambda-functions-with-container-image-5hgj)
- [Custom CloudWatch Events](https://dev.to/vumdao/custom-cloudwatch-events-4j3j)
- [How To Get Lastest Image Version in AWS ECR](https://dev.to/vumdao/how-to-get-lastest-image-version-in-aws-ecr-4op2)
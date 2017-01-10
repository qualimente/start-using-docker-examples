# Overview #

Demonstrate the use of aws-cli packaged as a replacement for a local installation.

# Demo #

Export AWS credential &amp; region configuration as environment variables:

```
export AWS_ACCESS_KEY_ID="<id>"
export AWS_SECRET_ACCESS_KEY="<key>"
export AWS_DEFAULT_REGION="<region>"
```

Export a shell alias for `aws`:

```
alias aws='docker run --rm -it -e "AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}" -e "AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}" -e "AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}" -v "$(pwd):/work" qualimente/aws-cli'
```

The aws-cli image's entrypoint command is `aws`, so you may use the image as a drop-in replacement on your system, e.g. to list the account's EC2 instances:

```
aws ec2 describe-instances
```

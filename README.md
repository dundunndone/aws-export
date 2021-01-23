# AWS Actions Export

`aws-actions-export.py` 
- Exports list of AWS actions, resources, and condition keys per service. Import HTML file into Excel for additional filtering.

### Benefits 

These scripts provide a number of benefits to help reduce security risks within IAM policies.

 - Find supported **Resources** per Action.
 - List documented Actions dependent on `iam:PassRole`. (76 so far)

Not all actions will be listed. Results are subject to updates made by AWS to the [Service Authorization Reference](https://docs.aws.amazon.com/service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.html) docs.


# AWS CLI Export

`cli-export.py` 
 - Exports list of all AWS CLI vervion 2 actions per service. 
 - Additional work can be done to pull supported switches.

 
## Pre-reqs

- Run `pip3 install -r requirements.txt` to install `bs4` and `requests`

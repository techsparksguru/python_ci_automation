#!/bin/bash

# Jenkins Configurations Directory
echo $JENKINS_HOME

BACKUP_DATE=('date +"%d-%m-%Y"')

# Backup jenkins job configurations
cp -R $JENKINS_HOME/jobs Backups/jobs

# List the files copied
ls Backups
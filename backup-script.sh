#!/bin/bash

# Jenkins Configurations Directory
echo $JENKINS_HOME

# Backup jenkins job configurations
cp -R $JENKINS_HOME/jobs Backups

# List the files copied
ls Backups
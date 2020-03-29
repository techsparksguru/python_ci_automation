#!/bin/bash

# Jenkins Configurations Directory
echo $JENKINS_HOME

# Backup general configurations, job configurations, and user content
cp -R $JENKINS_HOME/jobs Backups/jobs

# List the files copied
ls Backups

#!/bin/bash

# Jenkins Configurations Directory
echo $JENKINS_HOME

BACKUP_DATE=('date +"%d-%m-%Y"')

# Backup general configurations, job configurations, and user content
cp $JENKINS_HOME/*.xml Backups
cp -R $JENKINS_HOME/users Backups/users
cp -R $JENKINS_HOME/userContent Backups/userContent
cp -R $JENKINS_HOME/nodes Backups/nodes
ls Backups

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa

git add --all
git commit -m "Automated Jenkins commit - ${BACKUP_DATE}"
git push origin jenkins_backup
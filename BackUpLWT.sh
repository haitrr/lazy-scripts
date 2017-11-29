!/bin/bash
# Backup script for linux use crontab to schedule
#sudo crontab -e : 30 22 * * * <Path to this file>
now_date=$(date '+%d-%h-%Y')
wget -O ../lwtBackup/$now_date.sql.gz "http://localhost/lwt/backup_restore.php?backup=1"


# Backup script for windows need to use the batch file to call
$url = 'http://localhost/lwt/backup_restore.php?backup=1'
$path = Split-Path -Parent -Path $MyInvocation.MyCommand.Definition;
Write-output $path;
$date = get-date -format "M-d-yyyy"
$extension = '.sql.gz'
$path = $path +'/'+ $date + $extension
(New-Object system.net.webclient).downloadFile($url, $path)
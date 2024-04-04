#!/bin/sh

# Get machine name
machine_name=`defaults read /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName`
echo "Machine name:\t\t" $machine_name

# Get host name
host_name=`hostname`
echo "Host name:\t\t" $host_name

# Get macOS version
os_version=`sw_vers | grep ProductVersion | awk '{print $2}'`
echo "macOS:\t\t\t" $os_version

# Get IP address
ip_address=`ifconfig en0 | grep "inet " | awk '{print $2}'`
echo "IP:\t\t\t" $ip_address

# Get python version
python_version=`python3 --version | awk '{print $2}'`
echo "Python:\t\t\t" $python_version

# Get git version
git_version=`git --version | awk '{print $3}'`
echo "git:\t\t\t" $git_version

# Get Command-line Tools for XCode version
cltools_version=`pkgutil --pkg-info=com.apple.pkg.CLTools_Executables | grep version | awk '{printf "%4.1f",$2}'`
echo "Command-Line Tools:\t" $cltools_version

# softwareupdate -l
#sudo softwareupdate -i (update_pkg_name)

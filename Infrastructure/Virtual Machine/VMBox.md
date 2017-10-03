#VM Box

How to share folders:

https://www.reddit.com/r/linuxmint/comments/2glbhf/moving_files_from_mint_vm_to_windows_host/

Devices - > Shared Folders Settings
Click Add new Shared Folder
Select a folder you want to share from the host.
Select Auto-mount
Click OK
Reboot the linux guest OS.
Once the virtual linux comes back up, you should see your shared folder in /media/sf_foldername
If you have not installed the guest additions, it may not work. That is also under the devices menu.


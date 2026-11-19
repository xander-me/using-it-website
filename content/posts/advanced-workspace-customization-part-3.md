---
title: "Advanced Workspace Customization (Part 3)"
description: ""
pubDate: "2024-11-01 20:54:56"
updatedDate: "2025-11-28 15:52:44"
slug: "advanced-workspace-customization-part-3"
draft: true
categories:
  - "osdcloud"
  - "powershell"
tags:
wordpress_id: "368"
original_url: "https://using-it.dk/advanced-workspace-customization-part-3/"
---

In this part, we’ll dive deeper into the Workspace customization options that allow you to add specific drivers, create custom deployment scripts, and integrate essential applications or configurations.

**1. Adding Drivers to the Workspace**

Adding drivers to your Workspace ensures that the deployed OS is compatible with specific hardware, a crucial step for environments with multiple device types.

**Injecting Drivers Automatically**

OSDCloud can automatically download and inject drivers for popular manufacturers like Dell, HP, and Lenovo:

`Edit-OSDCloudWinPE -CloudDriver Dell,HP,Lenovo`

This command will pull the latest drivers from each specified vendor, injecting them into the WinPE image within your Workspace.

**Manually Adding Drivers**

For specific or less common devices, you may need to download drivers manually and place them in the Drivers folder:

1. **Download drivers** from the manufacturer’s website.

2. **Place them in the Workspace:** Copy the driver files into the C:\OSDCloud\Drivers folder.

**Tip:** Always keep drivers organized by device type to simplify future updates and management.

**2. Adding Custom Scripts to Automate Deployment Tasks**

Scripts can automate a variety of tasks during the deployment process, from setting up software to configuring Windows settings.

**Running a Custom Script During Deployment**

1. **Place your script in the Workspace**: Save your script (e.g., setup.ps1) to the Scripts folder within your Workspace directory.

2. **Include the Script in WinPE:**

`Edit-OSDCloudWinPE -WebPSScript "https://yourdomain.com/path/to/setup.ps1"`

This command pulls in your PowerShell script from the specified URL, so it runs automatically during deployment.

**Example Script: Install Applications Post-Deployment**

Here’s a sample PowerShell script (install-apps.ps1) to install applications after deployment:

*# install-apps.ps1*

*# Install Google Chrome*

Start-Process msiexec.exe -ArgumentList '/i chrome_installer.msi /qn' -Wait

*# Install Visual Studio Code*

Invoke-WebRequest -Uri "https://update.code.visualstudio.com/latest/win32-x64-user/stable" -OutFile "VSCodeSetup.exe"

Start-Process "VSCodeSetup.exe" -ArgumentList "/verysilent" -Wait

*# Install Microsoft Teams*

Invoke-WebRequest -Uri "https://go.microsoft.com/fwlink/?linkid=869428" -OutFile "TeamsSetup.exe"

Start-Process "TeamsSetup.exe" -ArgumentList "/silent" -Wait

Place install-apps.ps1 in your Scripts folder, and add it to WinPE using the Edit-OSDCloudWinPE command. This script will automatically install the specified apps post-deployment.

**3. Applying Branding and Visual Customizations**

Branding your deployment environment creates a cohesive look and can provide a professional touch, especially for client-facing deployments.

**Setting a Custom Wallpaper**

To add a custom wallpaper to the WinPE environment:

Edit-OSDCloudWinPE -Wallpaper "C:\Path\To\Wallpaper.jpg"

This image will appear in the background during the WinPE boot, offering a branded experience right from the start.

**Customizing the Lock Screen (Post-Deployment)**

You can also apply branding to the Windows lock screen with a post-deployment script:

1. **Create a Lock Screen Script (****set-lockscreen.ps1****):**

*# Set the lock screen image*

$lockScreenPath = "C:\Path\To\LockScreen.jpg"

New-Item -Path "C:\Windows\Web\Screen" -ItemType Directory -Force

Copy-Item -Path $lockScreenPath -Destination "C:\Windows\Web\Screen\lockscreen.jpg" -Force

Set-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\PersonalizationCSP" -Name "LockScreenImagePath" -Value "C:\Windows\Web\Screen\lockscreen.jpg"

2. **Add this script to your Workspace’s ****Scripts**** folder** and execute it post-deployment as part of your customization process.

**Creating Bootable Media**

Once your Workspace is fully customized, it’s time to create bootable media for deploying the operating system. You have two main options: a **USB drive** for physical devices or an **ISO file** for virtual environments.

**1. Creating a Bootable USB Drive**

1. **Insert a USB Drive** into your computer.

2. **Create the Bootable USB:**

New-OSDCloudUSB -WorkspacePath C:\OSDCloud

This command will format the USB drive and copy all necessary files from your Workspace, creating a ready-to-use bootable deployment drive.

**2. Creating a Bootable ISO File**

1. **Run the ISO Creation Command:**

New-OSDCloudISO -WorkspacePath C:\OSDCloud

This will create an ISO file from your Workspace, which you can then mount or use for virtual machines.

**Tip:** ISO files are ideal for testing in virtual environments, making it easy to test your deployment before rolling out to physical devices.

**Running the Deployment**

With your bootable media prepared, you’re ready to deploy the OS using OSDCloud.

**1. Boot the Target Device**

• Insert the USB drive (or mount the ISO in a virtual machine).

• Configure the device’s BIOS to boot from the USB or ISO.

**2. Starting the Deployment**

**Using the OSDCloud GUI**

If configured, the OSDCloud GUI will launch automatically upon boot:

1. **Select Deployment Options**: Choose your Windows version, language, edition, and any other preferences.

2. **Start the Deployment**: Click “Start” to begin.

**Starting Deployment via PowerShell Commands**

For automated deployments without the GUI, use:

Start-OSDCloud -OSVersion "Windows 11" -OSBuild 22H2 -OSEdition Enterprise -OSLanguage en-US -OSActivation Volume -ZTI -Restart

*This command performs a Zero Touch Installation (ZTI) of Windows 11 Enterprise, activating with a volume license and restarting the machine upon completion.*

**Note:** Adjust the parameters as necessary to match your deployment requirements.

**Wrapping Up: OSDCloud’s Flexible Deployment Model**

At this point, you’ve gone from setting up your Template to deploying a fully customized Windows OS. Here’s a quick recap of the process:

1. **Create a Template**: Set language and locale standards.

2. **Set Up a Workspace**: Add specific drivers, scripts, and branding.

3. **Create Bootable Media**: Generate a USB or ISO for deployment.

4. **Deploy**: Use OSDCloud’s flexible options (GUI or PowerShell) to roll out your OS.

With OSDCloud’s modular structure and extensive customization options, you’re equipped to handle any deployment scenario with ease. Next steps might include exploring **advanced scripting** for even more automation, integrating with **Windows Autopilot**, or using **Azure AD** for modern device management. Stay tuned for the next post!